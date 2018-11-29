#!/usr/bin/env python
# encoding: utf-8

""" Main application class. Entrypoint is here. """

import os
import npyscreen
from license.edit_license import (
    EditLicense,
    ApplyLicense,
    ReturnLicense,
    LicenseProxy,
    LicenseOffline)
from workers.edit_workers import EditWorkers
from network.edit_network import EditNetwork, NetworkDhcp, NetworkStatic
from docker.docker_services import DockerServices, LogViewer
from diagnostics.diagnostics import DiagnosticsForm
from error_popup import ErrorPopup
from main_menu import MainMenu, Shutdown, Reboot

from swagger_client import ApiClient, Configuration, ManagementApi, LicensingApi


class ApplianceControlApp(npyscreen.NPSAppManaged):
    """ Class to initialize the application and invisibly create the forms """
    def __init__(self, *args, **keywords):
        super(ApplianceControlApp, self).__init__(*args, **keywords)
        api_client_config = Configuration()
        api_client_config.host = os.environ.get("TEST_HOST", "localhost") + ":8080"
        api_client_config.logger_file = "/tmp/api.log"
        api_client = ApiClient(configuration=api_client_config)
        self.management_api = ManagementApi(api_client)
        self.licensing_api = LicensingApi(api_client)

        self.keypress_timeout_default = 25
        self.appliance_type = "RT"

    def onStart(self):
        self.addFormClass("ERROR", ErrorPopup)

        self.addForm('MAIN', MainMenu)

        self.addForm('MAIN/REBOOT', Reboot)
        self.addForm('MAIN/SHUTDOWN', Shutdown)

        self.addForm('WORKERS', EditWorkers)

        self.addForm('LICENSE', EditLicense)
        self.addForm('LICENSE/APPLY', ApplyLicense)
        self.addForm('LICENSE/RETURN', ReturnLicense)
        self.addForm('LICENSE/PROXY', LicenseProxy)
        self.addForm('LICENSE/OFFLINE', LicenseOffline)

        self.addForm('NETWORK', EditNetwork)
        self.addForm('NETWORK/DHCP', NetworkDhcp)
        self.addForm('NETWORK/STATIC_IP', NetworkStatic)

        self.addForm('SERVICES', DockerServices)
        self.addFormClass('SERVICES/LOGVIEWER', LogViewer)

        self.addForm('DIAGNOSTICS', DiagnosticsForm)


if __name__ == "__main__":
    APP = ApplianceControlApp()
    APP.run()
