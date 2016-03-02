import os

from notebook.utils import url_path_join as ujoin
from nbgrader.apps import FormgradeApp
from traitlets.config import Config


def load_jupyter_server_extension(nbapp):
    """Load the nbserver"""

    c = Config()
    c.FormgradeApp.authenticator_class = 'nbgrader.auth.NotebookAuth'
    c.BaseAuth.connect_ip = nbapp.ip
    c.BaseAuth.connect_port = nbapp.port
    c.BaseAuth.url_prefix = '/formgrader'
    c.NotebookAuth.notebook_address = nbapp.ip
    c.NotebookAuth.notebook_port = nbapp.port
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
        print(handler[0])
        handlers.append(tuple(handler))
    webapp.add_handlers(".*$", handlers)

    # update settings
    settings = formgrader.tornado_settings.copy()
    settings.update(webapp.settings)
    webapp.settings = settings
