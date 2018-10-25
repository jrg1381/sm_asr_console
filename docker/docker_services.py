# encoding: utf-8
import npyscreen
import curses
from error_handler import error_handler

log_entries = []

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

    def create(self):
        super().create()
        self.add_handlers({'q': self.parentApp.switchFormPrevious})
        self.wStatus2.value = "'q' to quit. 'l' to search in text."

    def beforeEditing(self):
        self.wMain.values = log_entries
        self.wMain.display()

class DockerServiceList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(DockerServiceList, self).__init__(*args, **keywords)

    @error_handler("Management API")
    def actionHighlighted(self, act_on_this, key_press):
        global log_entries
        service_name = act_on_this.split()[0]
        logs = self.parent.parentApp.management_api.get_logs(service_name, count=-1)
        log_entries = logs.log_lines.split('\n')
        self.parent.parentApp.switchForm("SERVICES/LOGVIEWER")

class DockerServices(npyscreen.ActionFormV2):
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