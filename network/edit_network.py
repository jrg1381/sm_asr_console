# encoding: utf-8
import npyscreen
import curses
from error_handler import error_handler
from swagger_client import ManagementApi
from swagger_client.models import ManagementIpAddressInfo


class NetworkSubMenuList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(NetworkSubMenuList, self).__init__(*args, **keywords)
        # Map from the text on screen to the name of the sub-form
        self.form_index = { 
            "Use DHCP" : "NETWORK/DHCP",
            "Configure static IP": "NETWORK/STATIC_IP",
            }
        self.values = list(self.form_index.keys())
            
    def actionHighlighted(self, act_on_this, key_press):
        self.parent.parentApp.switchForm(self.form_index[act_on_this])  

class NetworkDhcp(npyscreen.ActionPopup):
    @error_handler("Management API")
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

class NetworkStatic(npyscreen.ActionPopup):
    @error_handler("Management API")
    def _change_network(self):
        request = ManagementIpAddressInfo(
            nameservers=self.wg_nameservers.value.split(' '),
            netmask=self.wg_netmask.value,
            gateway=self.wg_gateway.value,
            address=self.wg_ip_address.value)
        response = self.parentApp.management_api.set_manual_ip_address(request)

    def create(self):
        super().create()
        self.wg_nameservers = self.add(npyscreen.TitleText, rely=1, name="Nameservers (space separated)")
        self.wg_netmask = self.add(npyscreen.TitleText, rely=3, name="Netmask (e.g. 255.255.255.0)")
        self.wg_gateway = self.add(npyscreen.TitleText, rely=5, name="Gateway (e.g. 192.168.1.1)")
        self.wg_ip_address = self.add(npyscreen.TitleText, rely=7, name="IP address (e.g. 192.168.1.40)")

    def on_ok(self):
        self._change_network()
        self.parentApp.switchFormPrevious()

    def on_cancel(self):
        self.parentApp.switchFormPrevious()
