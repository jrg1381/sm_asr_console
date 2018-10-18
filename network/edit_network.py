# encoding: utf-8
import npyscreen
import curses
from error_handler import error_handler
from swagger_client import ManagementApi


class NetworkSubMenuList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(NetworkSubMenuList, self).__init__(*args, **keywords)
        # Map from the text on screen to the name of the sub-form
        self.form_index = { 
            "Use DHCP" : "NETWORK/DHCP",
            "Configure static IP": "NETWORK/STATIC_IP",
            "Network tools": "NETWORK/TOOLS",
            }
        self.values = list(self.form_index.keys())
            
    def actionHighlighted(self, act_on_this, key_press):
        self.parent.parentApp.switchForm(self.form_index[act_on_this])  

class NetworkDhcp(npyscreen.ActionPopup):
    @error_handler("doom")
    def enable_dhcp(self):
        self.parentApp.management_api.set_dhcp()

    def create(self):
        self.add(npyscreen.MultiLine, values=["Choose OK to enable DHCP networking.", "The system will restart."], editable=False)

    def on_ok(self):
        self.enable_dhcp()
        self.parentApp.switchFormPrevious()

    def on_cancel(self):
        self.parentApp.switchFormPrevious()

class _BaseNetworkForm(npyscreen.ActionFormV2):
    def h_refresh(self):
        pass

    def create(self):
        self.management_api = self.parentApp.management_api
        self.licensing_api = self.parentApp.licensing_api
        self.add_handlers({curses.KEY_F5: self.h_refresh})

    def on_ok(self):
        self.parentApp.switchFormPrevious()

    def on_cancel(self):
        self.parentApp.switchFormPrevious()  


class EditNetwork(_BaseNetworkForm):
    def create(self):
        super().create()
        self.wg_network_options = self.add(NetworkSubMenuList, rely=1)

class NetworkStatic(_BaseNetworkForm):
    def create(self):
        self.value = None
        self.wg_max_workers = self.add(npyscreen.TitleText, width=80, name="network", value="foo")
    
    def on_ok(self):
        print(self.wg_max_workers.value)
        super().on_ok()

class NetworkTools(_BaseNetworkForm):
    def create(self):
        self.wg_max_workers = self.add(npyscreen.TitleText, width=80, name="network", value="foo")
