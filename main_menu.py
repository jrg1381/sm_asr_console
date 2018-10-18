# encoding: utf-8
import sys
import datetime
import asyncio
import curses
import npyscreen
from error_handler import error_handler
from main_menu_list import MainMenuList
from widgets.net_interfaces_widget import NetInterfacesWidget
from swagger_client import ApiClient, Configuration, ManagementApi, LicensingApi
from swagger_client.rest import ApiException

APP_NAME = "Realtime ASR"


class MainMenu(npyscreen.ActionFormV2):
    def __init__(self, *args, **kwargs):
        super(MainMenu, self).__init__(*args, **kwargs)
        self.ping_message = "?????"
        self.last_successful_ping = None

    @error_handler("API exception")
    def populate_status(self):
        self.status_bar.entry_widget.values = ["????",]

        version = self.management_api.about()
        license = self.licensing_api.get_license()
        free_space = self.management_api.get_free_storage()

        self.status_bar.entry_widget.values = [
            "{:<16}{}".format("Version", version.version),
            "{:<16}{}".format("License status", license.status),
            "{:<16}{}".format("License code", license.license_code),
            "{:<16}{}".format("Licensed", license.licensed)
        ]
        for entry in free_space.items:
            self.status_bar.entry_widget.values.append(
            "{:<16}{} -> {}".format("Disk free ", entry.path, entry.bytes)
            )

    @staticmethod
    def call_in_background(target, *, loop=None, executor=None):
        """Schedules and starts target callable as a background task

        If not given, *loop* defaults to the current thread's event loop
        If not given, *executor* defaults to the loop's default executor

        Returns the scheduled task.
        """
        if loop is None:
            loop = asyncio.get_event_loop()
        if callable(target):
            return loop.run_in_executor(executor, target)
        raise TypeError("target must be a callable, not {!r}".format(type(target)))

    def set_ping_message(self):
        try:
            if self.last_successful_ping:
                since_last_ping = (datetime.datetime.utcnow() - self.last_successful_ping).total_seconds()
                self.ping_message += "."
                if since_last_ping < 10:
                    return
            self.management_api.about()
            self.ping_message = "API responding"
            self.last_successful_ping = datetime.datetime.utcnow()
        except:
            if self.last_successful_ping:
                since_good_ping = (datetime.datetime.utcnow() - self.last_successful_ping).total_seconds()
                self.ping_message = "API not responding for {}s".format(int(since_good_ping))
            else:
                self.ping_message("No responses from API since start")

    def update_safe_status(self):
        now_utc = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).replace(microsecond=0).isoformat()
        self.call_in_background(self.set_ping_message)

        self.system_status_bar.entry_widget.values = [
            "{:<15}: {}".format("System time (UTC)", now_utc),
            self.ping_message
            ]
        self.network_status_bar.entry_widget.update()
        self.system_status_bar.entry_widget.update()

    def h_refresh(self, data):
        self.populate_status()
        self.display()
        self.wg_options.update()

    def create(self):
        self.management_api = self.parentApp.management_api
        self.licensing_api = self.parentApp.licensing_api

        self.add_handlers({curses.KEY_F5: self.h_refresh})

        centred_title = "{:^78}".format(APP_NAME)
        self.title = self.add(npyscreen.FixedText, name=APP_NAME, value=centred_title, editable=False, relx=1, rely=1, width=80)
        self.wg_options = self.add(MainMenuList, name="main_menu", max_width=12, rely=2)
        self.system_status_bar = self.add(npyscreen.BoxTitle, name="System status", editable=False, rely=2, relx=14, max_height=4)
        self.network_status_bar = self.add(NetInterfacesWidget, name="Network status", editable=False, rely=6, relx=14, max_height=8)
        self.status_bar = self.add(npyscreen.BoxTitle, name="ASR status", editable=False, relx=14, rely=14, max_height=8)
        self.nextrely += 1

    def beforeEditing(self):
        self.populate_status()

    def on_ok(self):
        sys.exit(0)

    def on_cancel(self):
        sys.exit(0)

    def while_waiting(self):
        self.update_safe_status()

class Reboot(npyscreen.ActionPopup):
    @error_handler("API Error (management_api)")
    def reboot(self):
        # if remote host, use api, if localhost, use real system function
        self.parentApp.management_api.hard_reboot()

    def create(self):
        self.add(npyscreen.MultiLine, values=["Choose OK to reboot the system."], editable=False)

    def on_ok(self):
        self.reboot()
        self.parentApp.switchFormPrevious()

    def on_cancel(self):
        self.parentApp.switchFormPrevious()

class Shutdown(npyscreen.ActionPopup):
    @error_handler("API Error (management_api)")
    def shutdown(self):
        self.parentApp.management_api.hard_shutdown()

    def create(self):
        self.add(npyscreen.MultiLine, values=["Choose OK to shut down the system."], editable=False)

    def on_ok(self):
        self.shutdown()
        self.parentApp.switchFormPrevious()

    def on_cancel(self):
        self.parentApp.switchFormPrevious()