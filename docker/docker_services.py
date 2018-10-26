# encoding: utf-8
import npyscreen
import curses
from error_handler import error_handler

current_service = None

class LogViewerActionController(npyscreen.ActionControllerSimple):
    def create(self):
        self.add_action(r'^:q', self.quit, False)
    
    def quit(self, command_line, widget_proxy, live):
        self.parent.parentApp.switchFormPrevious()

class LogViewer(npyscreen.FormMuttActiveTraditional):
    ACTION_CONTROLLER = LogViewerActionController
    FORM_NAME = "LogViewer"

    def __init__(self, *args, **kwargs):
        super(LogViewer, self).__init__(*args, **kwargs)

    @error_handler("Management API")
    def h_refresh(self, data):
        logs = self.parentApp.management_api.get_logs(current_service, count=-1)
        log_entries = logs.log_lines.split('\n')
        self.wMain.values = log_entries
        self.wMain.display()

    def create(self):
        super().create()
        self.add_handlers({curses.KEY_F5: self.h_refresh})
        self.add_handlers({'q': self.parentApp.switchFormPrevious})
        self.wStatus2.value = "'q' to quit. 'l' to search in text."

    def beforeEditing(self):
        self.h_refresh(None)

class DockerServiceList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(DockerServiceList, self).__init__(*args, **keywords)

    @error_handler("Management API")
    def actionHighlighted(self, act_on_this, key_press):
        global current_service
        current_service = act_on_this.split()[0]
        self.parent.parentApp.switchForm("SERVICES/LOGVIEWER")

class DockerServices(npyscreen.ActionFormV2):
    @error_handler("Management API")
    def fetch_services(self):
        services = self.management_api.get_services()
        rows = []
        for s in services.service_status:
            rows.append("{:<60}{:>8}".format(s.service, s.status))
        self.wg_service_list.values = rows

    def h_refresh(self, data):
        self.fetch_services()

    def create(self):
        self.management_api = self.parentApp.management_api
        self.licensing_api = self.parentApp.licensing_api
        self.add_handlers({curses.KEY_F5: self.h_refresh})
        self.add_handlers({'q': self.parentApp.switchFormPrevious})
        self.wg_service_list = self.add(DockerServiceList)

    def beforeEditing(self):
        self.fetch_services()

    def on_ok(self):
        self.parentApp.switchFormPrevious()

    def on_cancel(self):
        self.parentApp.switchFormPrevious()  
