# -*- coding: utf-8 -*-
#
# File: checkinout.py
#
# Copyright (c) nexiles GmbH
#

__author__ = """Stefan Eletzhofer <se@nexiles.de>"""
__docformat__ = 'plaintext'

import os
import sys
import logging
import zipfile
import contextlib
import webbrowser
import json
import tempfile
from tabulate import tabulate

from nexiles.tools.api import get_resource

from nexiles.tools.api import utils
from nexiles.tools.api import query
from nexiles.tools.api import content
from nexiles.tools.api import document
from nexiles.tools.api import checkinout
from nexiles.tools.api import validators
from nexiles.tools.api import version
from nexiles.tools.api.zip import unzip

logger = logging.getLogger("nexiles.tools.api")

__all__ = []


class Application(object):
    """
    A Application
    """

    def __init__(self, api, name, base_dir=None, **options):
        self.api = api
        self.name = name
        self.options = options
        self._base_dir = base_dir or name

    @property
    def document_name(self):
        return "nexiles." + self.name + ".app"

    @property
    def base_dir(self):
        return self._base_dir

    @property
    def build_dir(self):
        return os.path.join(self.base_dir, "build")

    @property
    def zip_file_name(self):
        return "{0}-app.zip".format(self.name)

    @contextlib.contextmanager
    def app_directory(self):
        cwd = os.getcwd()
        os.chdir(self.base_dir)
        yield self.base_dir
        os.chdir(cwd)

    def create_directory_structure(self):
        """create_directory_structure() -> None

        Create the default directory structure for an application.
        """
        # create the application base directory and the build directory
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
        if not os.path.exists(self.build_dir):
            os.makedirs(self.build_dir)

    def query_one(self, name=None, resource_type=None):
        if resource_type is None:
            resource_type = "documents"
        if name is None:
            name = self.document_name
        return query.query_one(self.api, type=resource_type, name=self.document_name)

    def get_latest_iteration(self):
        return self.query_one(name=self.document_name)

    def build(self):
        raise NotImplementedError()

    def pack(self):
        """pack() -> string

        Pack application to a zip file.

        :returns: path to zip file relative to the application folder
        """
        path = os.path.join("build", self.zip_file_name)
        with self.app_directory():
            with zipfile.ZipFile(path, "w") as zf:
                for root, dirs, files in os.walk("."):
                    logger.debug("processing dir: {0}".format(root))
                    if "build" in dirs:
                        dirs.remove("build")

                    for f in files:
                        logger.debug("adding file: {0}".format(f))
                        zf.write(os.path.join(root, f))
        return path

    def upload(self):
        """upload() -> None

        Upload the current zip file to the server.
        """
        # check out the app
        # upload new primary content
        # check in the app
        raise NotImplementedError()

    def unpack(self):
        """unpack() -> None

        Unpack application archive.
        """
        # download the template app
        # unzip the files into the source directory
        with self.app_directory():
            unzip(self.zip_file_name)

    def _get_content(self, oid):
        # XXX: hacky, but so we don't have to make a new request object with
        # authentication options
        session = self.api._store.get("session")

        resource = get_resource(self.api, "documents")
        contents = content.list_content(resource, oid=oid, role="PRIMARY")

        if not contents:
            return None

        data = contents.pop()
        download_url = data.get("url")

        # request download
        response = session.get(download_url)
        return dict(
            content=response.content,
            url=response.url,
            content_type=response.headers.get("content-type"),
            content_length=response.headers.get("content-length"),
            status_code=response.status_code,
        )

    def initmeta(self):
        metadatafile = os.path.join(self.base_dir, "app-meta.json")

        # init metadata
        metadata = json.loads(file(metadatafile).read())
        metadata["description"] = "Start " + self.name
        metadata["version"] = "0.1.0"
        metadata["name"] = self.name

        # create a temporary file where we write our changes into
        # rename to metadatafile afterwards
        with tempfile.NamedTemporaryFile(
                'w', dir=os.path.dirname(metadatafile), delete=False) as tf:
            tf.write(json.dumps(metadata, indent=4))
            tempname = tf.name
        os.rename(tempname, metadatafile)

        return metadata

    def download(self, document_name=None, dest=None):
        """download(document_name) -> string

        Download zip file of app to the build directory.

        If `document_name` is not given, the app's document name is used.

        If `dest` is not given, the dwnloaded file is put in the app's build
        directory using the apps's `zip_file_name`.

        :param document_name:  The name of the document to download.
        :param dest:           The destination directory
        :returns:              Path to the downloaded file
        """
        if document_name is None:
            document_name = self.document_name

        if dest is None:
            dest = os.path.join(self.build_dir, self.zip_file_name)

        if not os.path.exists(os.path.dirname(dest)):
            raise RuntimeError("Destination dir '{0}' does not exist".format(dest))

        app_doc = self.query_one(document_name)
        if app_doc is None:
            msg = "App not found: {0}".format(document_name)
            logger.error(msg)
            raise RuntimeError(msg)

        app_oid = app_doc["oid"]

        data = self._get_content(app_oid)
        if data is None:
            raise RuntimeError("No content items found: for {0} @ {1}".format(document_name, app_oid))

        with open(dest, "wb") as f:
            f.write(data["content"])

        return dest


######################################################################
######################################################################
######################################################################

def command_create(api, args):
    if not args.dir:
        args.dir = args.name

    api = sensing_service_url(api, args)
    static_dir = os.path.join(args.dir, "static")
    app = Application(api, args.name, base_dir=static_dir)

    if os.path.exists(app.base_dir) and not args.clobber:
        print("Directory ({0}) already exists.  Use '--clobber' to overwrite.".format(app.base_dir))
        sys.exit(1)

    # create local app folder if needed
    if not os.path.exists(app.build_dir):
        print("creating app directory structure.")
        app.create_directory_structure()

    # download template zip file
    template_app = Application(api, args.template)
    path = os.path.join(app.build_dir, app.zip_file_name)
    path = template_app.download(dest=path)
    print("downloaded template to: {0}".format(path))

    # unpack it
    app.unpack()
    print("unpacked files to{0}".format(args.dir))

    metadata = app.initmeta()
    print("-------------------------------------------")
    print("App name: " + metadata["name"])
    print("App description: " + metadata["description"])
    print("App version: " + metadata["version"])


def command_download(api, args):
    app = Application(api, args.name, base_dir=args.dest_dir)
    if os.path.exists(app.base_dir) and not args.clobber:
        print("Directory ({0}) exists.  Use '--clobber' to overwrite.".format(app.base_dir))
        sys.exit(1)

    # create local app folder if needed
    if not os.path.exists(app.build_dir):
        app.create_directory_structure()

    # download zip file
    path = app.download(document_name=app.document_name)

    # unpack it
    app.unpack()
    print("downloaded file: {0}".format(path))


def command_pack(api, args):
    app = Application(api, args.name, base_dir=args.source_dir)
    if not os.path.exists(app.base_dir):
        print("app folder not found.")
        sys.exit(1)

    # create local app folder if needed
    if not os.path.exists(app.build_dir):
        app.create_directory_structure()

    # create zip file
    path = app.pack()

    print("packed application: {0}".format(path))


def command_upload(api, args):
    app = Application(api, args.name, base_dir=args.source_dir)
    resource = get_resource(api, "documents")
    if not os.path.exists(app.base_dir):
        print("app folder not found.")
        sys.exit(1)

    zip_file_path = os.path.join(app.build_dir, app.zip_file_name)

    latest = app.get_latest_iteration()
    if latest is None:
        # create the document
        # doc = document.create(resource, args.number or app.document_name,
        doc = document.create(resource, args.number,
                              app.document_name, args.container,
                              description=args.description,
                              folder=args.folder,
                              content=content.create_content_info("PRIMARY", zip_file_path)
                              )

        print("created: {0}".format(utils.object_pretty_print(doc)))
    else:
        oid = latest["oid"]
        doc = utils.get_object(resource, oid)
        print("Latest iteration: {0} state: {1}".format(doc.item["version"], doc.item["state"]))

        # check out the app
        print(" checking out ...")
        doc_co = checkinout.checkout(resource, oid, "nxtools app upload")

        # delete old primary content and upload new primary content
        print(" uploading ...")
        content.delete_content(resource, doc_co["oid"], "PRIMARY", app.zip_file_name, iterate=False)
        content.upload_content(resource, doc_co["oid"], "PRIMARY", zip_file_path, iterate=False)

        # check in the app
        print(" checking in ...")
        doc_ci = checkinout.checkin(resource, doc_co["oid"], "nxtools app upload")

        doc = utils.get_object(resource, doc_ci["oid"])
        print("New iteration: {0} state: {1}".format(doc.item["version"], doc.item["state"]))


def command_open(api, args):
    """ open the app
    """
    app = query.query_one(api, type="apps", name=args.name)
    if app is None:
        print("Application not found.")
        sys.exit(2)

    url = app["app_url"]
    if args.startpage:
        url = url.replace("index.html", args.startpage)

    print("opening ", url)
    webbrowser.open(url)


def print_results(results, headers):
    print(tabulate([{h: r[h] for h in headers } for r in results] , headers="keys", tablefmt="simple"))


def command_list(api, args):
    resource = get_resource(api, "apps")

    query = {
        "limit": args.limit
    }

    if hasattr(args, "name"):
        query["name"] = args.name

    if hasattr(args, "number"):
        query["number"] = args.number

    if hasattr(args, "state"):
        query["state"] = args.state

    if hasattr(args, "latest_iteration"):
        if args.latest_iteration is False:
            query["latest_iteration"] = "no"
        if args.latest_iteration is True:
            query["latest_iteration"] = "yes"

    if hasattr(args, "latest_released"):
        if args.latest_released is False:
            query["latest_released"] = "no"
        else:
            query["latest_released"] = "yes"

    logger.debug("query: {0}".format(query))

    results = utils.query(resource, **query)
    columns = {"name": 35, "oid": 30, "state": 12, "version": 34}

    # Tableoutput of results
    headers = "name oid number version state app_url".split()
    print_results(results, headers)


def add_commands(subparsers, defaults):
    """ add subparser commandline args
    """

    def common_args(subparser, clobber=True):
        subparser.add_argument("--name",
                               required=True,
                               help="the name of the app")
        if clobber:  # args needed fow rw access
            subparser.add_argument("--clobber",
                                   required=False,
                                   default=False,
                                   action="store_true",
                                   help="overwrite files")
            subparser.add_argument("--no-clobber",
                                   required=False,
                                   action="store_false",
                                   help="don't overwrite files")
        return subparser

    def create_upload_args(subparser):
        subparser.add_argument("--number",
                               required=False,
                               dest="number",
                               type=str,
                               help="the number")
        subparser.add_argument("--container-name",
                               required=False,
                               default=defaults.app_container_name,
                               dest="container",
                               type=str,
                               help="the name of the container (Product,"
                                    " Library) for the document")
        subparser.add_argument("--folder-path",
                               required=False,
                               default=defaults.app_folder_path,
                               dest="folder",
                               type=str,
                               help="the folder path in the container to"
                                    " store the document")
        subparser.add_argument("--description",
                               required=False,
                               dest="description",
                               type=str,
                               help="the description")
        return subparser

    ###########################################################################
    subparser = subparsers.add_parser("app-create")
    common_args(subparser)
    create_upload_args(subparser)
    subparser.add_argument("--dir",
                           required=False,
                           dest="dir",
                           type=str,
                           help="use this to override the default destination directory, which is the app name.")
    subparser.add_argument("--template",
                           default=defaults.app_template_name,
                           help="the template to use")
    subparser.add_argument("--source-dir",
                           required=False,
                           default=defaults.app_source_dir,
                           dest="source_dir",
                           type=str,
                           help="the source dir of the app.")
    subparser.set_defaults(command=command_create)

    ###########################################################################
    subparser = subparsers.add_parser("app-upload")
    common_args(subparser,
                clobber=False)
    create_upload_args(subparser)
    subparser.add_argument("--source-dir",
                           required=False,
                           default=defaults.app_source_dir,
                           dest="source_dir",
                           type=str,
                           help="the source dir of the app.")
    subparser.set_defaults(command=command_upload)

    ###########################################################################
    subparser = subparsers.add_parser("app-download")
    common_args(subparser)
    subparser.add_argument("--dest-dir",
                           required=False,
                           default=defaults.app_source_dir,
                           dest="dest_dir",
                           type=str,
                           help="the download destination directory. Defaults"
                                " to '{0}'. A subfolder 'build' will be"
                                " automatically added to your"
                                " destination.".format(defaults.app_source_dir))
    subparser.set_defaults(command=command_download)

    ###########################################################################
    subparser = subparsers.add_parser("app-pack")
    common_args(subparser)
    subparser.add_argument("--source-dir",
                           required=False,
                           default=defaults.app_source_dir,
                           dest="source_dir",
                           type=str,
                           help="the source dir of the app.")
    subparser.set_defaults(command=command_pack)

    ###########################################################################
    subparser = subparsers.add_parser("app-open")
    common_args(subparser,
                clobber=False)
    subparser.add_argument("--start-page",
                           required=False,
                           default=defaults.app_start_page,
                           dest="startpage",
                           type=str,
                           help="the start page to use")
    subparser.set_defaults(command=command_open)

    ###########################################################################
    subparser = subparsers.add_parser("app-list")
    subparser.add_argument("--number",
                           required=False,
                           dest="number",
                           type=str,
                           help="the number")
    subparser.add_argument("--limit",
                           dest="limit",
                           default=100,
                           type=int,
                           help="limit the size of the app-list")
    subparser.add_argument("--state",
                           dest="state",
                           type=str,
                           help="list apps with a certain state (\"INWORK\",\"RELEASED\",...)")
    subparser.add_argument("--latest-iteration",
                           dest="latest_iteration",
                           type=validators.is_bool,
                           help="list only the latest iteration of the apps (True or False)")
    subparser.add_argument("--latest-released",
                           dest="latest_released",
                           action="store_true",
                           help="list the latest, released apps only")
    subparser.set_defaults(command=command_list)
