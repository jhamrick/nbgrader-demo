import os

from nbgrader.apps import FormgradeApp
from nbgrader.auth import BaseAuth
from notebook.utils import url_path_join as ujoin
from traitlets import Unicode
from traitlets.config import Config


def _jupyter_server_extension_paths():
    return [
        dict(module="formgrade_extension")
    ]


class NotebookAuth(BaseAuth):
    """Notebook server authenticator."""

    notebook_base_url = Unicode(config=True, help="Base URL of the notebook server.")
    def _notebook_base_url_default(self):
        return '/'

    notebook_url_prefix = Unicode(None, config=True, allow_none=True, help="""
        Relative path of the formgrader with respect to the notebook's base
        directory.  No trailing slash. i.e. "Documents" or "Documents/notebooks". """)
    def _notebook_url_prefix_changed(self, name, old, new):
        self.notebook_url_prefix = new.strip('/')

    remap_url = Unicode(config=True, help="""Suffix appened to
        `NotebookAuth.notebook_base_url` to form the full URL to the formgrade
        server.  By default this is '/formgrader'.""")
    def _remap_url_default(self):
        return '/formgrader'
    def _remap_url_changed(self, name, old, new):
        self.remap_url = new.rstrip('/')

    def __init__(self, *args, **kwargs):
        super(NotebookAuth, self).__init__(*args, **kwargs)
        self._base_url = self.notebook_base_url.rstrip('/') + self.remap_url

    def add_remap_url_prefix(self, url):
        if url == '/':
            return self.remap_url + '/?'
        else:
            if not url.startswith('/'):
                return self.remap_url + '/' + url
            else:
                return self.remap_url + url

    def transform_handler(self, handler):
        new_handler = list(handler)

        # transform the handler url
        url = self.add_remap_url_prefix(handler[0])
        new_handler[0] = url

        # transform any urls in the arguments
        if len(handler) > 2:
            new_args = handler[2].copy()
            if 'url' in new_args:
                new_args['url'] = self.add_remap_url_prefix(new_args['url'])
            new_handler[2] = new_args

        return tuple(new_handler)

    def notebook_server_exists(self):
        return True

    def get_notebook_url(self, relative_path):
        """Gets the notebook's url."""
        if self.notebook_url_prefix is not None:
            relative_path = self.notebook_url_prefix + '/' + relative_path
        return "{}/notebooks/{}".format(self.notebook_base_url.rstrip('/'), relative_path)


def load_jupyter_server_extension(nbapp):
    """Load the nbserver"""

    c = Config()
    c.FormgradeApp.authenticator_class = NotebookAuth
    c.BaseAuth.connect_ip = nbapp.ip
    c.BaseAuth.connect_port = nbapp.port
    c.BaseAuth.url_prefix = '/formgrader'
    c.NotebookAuth.notebook_base_url = nbapp.base_url
    c.NotebookAuth.notebook_url_prefix = "instructor"
    c.NbGrader.log_level = nbapp.log_level
    c.NbGrader.course_directory = os.path.join(os.getcwd(), "instructor")

    formgrader = FormgradeApp(parent=nbapp)
    formgrader.update_config(c)
    super(FormgradeApp, formgrader).initialize([])
    formgrader.init_tornado_settings()
    formgrader.init_handlers()

    # update handlers
    webapp = nbapp.web_app
    base_url = webapp.settings["base_url"]
    handlers = []
    for handler in formgrader.handlers:
        handler = list(handler)
        handler[0] = ujoin(base_url, handler[0])
        handlers.append(tuple(handler))
    webapp.add_handlers(".*$", handlers)

    # update settings
    formgrader.tornado_settings['nbgrader_mathjax_url'] = webapp.settings['mathjax_url']
    formgrader.tornado_settings['log_function'] = webapp.settings['log_function']
    webapp.settings.update(formgrader.tornado_settings)
