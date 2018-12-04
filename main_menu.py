# encoding: utf-8

""" Main menu """
import sys
import os
import datetime
import asyncio
import curses
import npyscreen
from error_handler import error_handler
from main_menu_list import MainMenuList
from widgets.net_interfaces_widget import NetInterfacesWidget

APP_NAME = "{} ASR".format(os.environ.get("APP_NAME", "Speechmatics"))

# pylint:  disable=too-many-ancestors
# pylint:  disable=too-many-instance-attributes


class MainMenu(npyscreen.ActionFormV2):
    """ Main menu form """
    def __init__(self, *args, **kwargs):
        super(MainMenu, self).__init__(*args, **kwargs)
        self.ping_message = "?????"
        self.last_successful_ping = None

    @error_handler("API exception")
    def populate_status(self):
        """ Fill in the status widget """
        self.status_bar.entry_widget.values = ["????", ]

        version = self.management_api.about()
        sm_license = self.licensing_api.get_license()
        free_space = self.management_api.get_free_storage()

        self.status_bar.entry_widget.values = [
            "{:<16}{}".format("Version", version.version),
            "{:<16}{}".format("License status", sm_license.status),
            "{:<16}{}".format("License code", sm_license.license_code),
            "{:<16}{}".format("Licensed", sm_license.licensed)
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
        """ Ping the API and set the ping message describing the result """
        try:
            if self.last_successful_ping:
                since_last_ping = (datetime.datetime.utcnow() - self.last_successful_ping).total_seconds()
                self.ping_message += "."
                if since_last_ping < 10:
                    return
            self.management_api.about()
            self.ping_message = "API responding"
            self.last_successful_ping = datetime.datetime.utcnow()
        except Exception:  # pylint: disable=broad-except
            if self.last_successful_ping:
                since_good_ping = (datetime.datetime.utcnow() - self.last_successful_ping).total_seconds()
                self.ping_message = "API not responding for {}s".format(int(since_good_ping))
            else:
                self.ping_message("No responses from API since start")

    def update_safe_status(self):
        """
        Update those parts of the status which don't depend on the remote end working.
        Because we know these operations can be done safely without throwing up an error,
        they can be done repeatedly in a loop.
        """
        now_utc = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).replace(microsecond=0).isoformat()
        self.call_in_background(self.set_ping_message)

        self.system_status_bar.entry_widget.values = [
            "{:<15}: {}".format("System time (UTC)", now_utc),
            self.ping_message
            ]
        self.network_status_bar.entry_widget.update()
        self.system_status_bar.entry_widget.update()

    def h_refresh(self, data):  # pylint: disable=unused-argument
        """
        Refresh the main menu display.
        Try to avoid calling this too often as the npyscreen docs warn against it.
        """
        self.populate_status()
        self.display()
        self.wg_options.update()

    def create(self):
        """
        Create the main menu, initialize the swagger clients
        """
        # The member is added dynamically
        columns = curses.COLS  # pylint: disable=no-member
        self.management_api = self.parentApp.management_api
        self.licensing_api = self.parentApp.licensing_api

        self.add_handlers({curses.KEY_F5: self.h_refresh})

        centred_title = ("{:^" + str(columns) + "}").format(APP_NAME)
        self.title = self.add(npyscreen.FixedText, name=APP_NAME, value=centred_title, editable=False, relx=1, rely=1,
                              width=int(columns))
        self.wg_options = self.add(MainMenuList, name="main_menu", max_width=12, rely=2)
        self.system_status_bar = self.add(npyscreen.BoxTitle, name="System status", editable=False, rely=2, relx=14,
                                          max_height=4)
        self.network_status_bar = self.add(NetInterfacesWidget, name="Network status", editable=False, rely=6, relx=14,
                                           max_height=8)
        self.status_bar = self.add(npyscreen.BoxTitle, name="ASR status", editable=False, relx=14, rely=14,
                                   max_height=8)
        self.nextrely += 1

    def beforeEditing(self):  # pylint: disable=invalid-name
        """ Called after the screen is created but before editing is allowed """
        self.populate_status()

    def on_ok(self):
        """ Quit app on OK """
        sys.exit(0)

    def on_cancel(self):
        """ Quit app on cancel (TODO: remove cancel button from main screen only) """
        sys.exit(0)

    def while_waiting(self):
        """ Run on a timer to update the status """
        self.update_safe_status()


class Reboot(npyscreen.ActionPopup):
    """ Pop-up menu defining the reboot confirmation screen """
    @error_handler("API Error (management_api)")
    def reboot(self):
        """
        If remote host, use api, if localhost, use real system function (TODO)
        """
        self.parentApp.management_api.hard_reboot()

    def create(self):
        """ Initialize the popup """
        self.add(npyscreen.MultiLine, values=["Choose OK to reboot the system."], editable=False)

    def on_ok(self):
        """ OK selected, reboot the system """
        self.reboot()
        self.parentApp.switchFormPrevious()

    def on_cancel(self):
        """ Cancel selected, return to previous form """
        self.parentApp.switchFormPrevious()


class Shutdown(npyscreen.ActionPopup):
    """ Popup menu defining the shutdown confirmation screen """
    @error_handler("API Error (management_api)")
    def shutdown(self):
        """
        Shutdown the system using the API or the local shutdown command
        """
        self.parentApp.management_api.hard_shutdown()

    def create(self):
        self.add(npyscreen.MultiLine, values=["Choose OK to shut down the system."], editable=False)

    def on_ok(self):
        self.shutdown()
        self.parentApp.switchFormPrevious()

    def on_cancel(self):
        self.parentApp.switchFormPrevious()
