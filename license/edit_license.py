# encoding: utf-8
import sys
import re
import curses
import npyscreen
from swagger_client.models import ManagementLicenseCode
from error_handler import error_handler

API_ERROR_TEXT="API error (licensing api)"

class LicenseSubMenuList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(LicenseSubMenuList, self).__init__(*args, **keywords)
        # Map from the text on screen to the name of the sub-form
        self.form_index = { 
            "Apply license" : "LICENSE/APPLY",
            "Return license": "LICENSE/RETURN",
            "Go offline": "LICENSE/OFFLINE",
            "Configure proxy settings": "LICENSE/PROXY"
            }
        self.values = list(self.form_index.keys())
            
    def actionHighlighted(self, act_on_this, key_press):
        self.parent.parentApp.switchForm(self.form_index[act_on_this])  

class LicenseField(npyscreen.TitleText):
    def __init__(self, *args, **keywords):
        super(LicenseField, self).__init__(*args, **keywords)

    def when_value_edited(self):
        if not re.match(r"\d+$", self.value):
            self.value = re.sub(r'\D', "", self.value)

    def safe_to_exit(self):
        sys.exit(0)
        if len(str(self.value)) > 20:
            return False
        return True

class _BaseLicenseForm(npyscreen.ActionFormV2):
    @error_handler(title=API_ERROR_TEXT)
    def _fetch_license_details(self):
        retval = []
        # Maximum widths of keys and values
        max_key = 0
        max_val = 0
        license = self.licensing_api.get_license()
        for k, v in license.to_dict().items():
            max_key = max(max_key, len(str(k)))
            max_val = max(max_val, len(str(v)))
        for k, v in license.to_dict().items():
            retval.append(("{:<"+ str(max_key + 1) + "}{}").format(k, v))
        return retval

    def h_refresh(self, data):
        self.wg_license_status.values = self._fetch_license_details()
        self.display()

    def create(self):
        self.management_api = self.parentApp.management_api
        self.licensing_api = self.parentApp.licensing_api
        self.add_handlers({curses.KEY_F5: self.h_refresh})
        self.wg_license_status = self.add(npyscreen.MultiLine, name="License status", editable=False)

    def beforeEditing(self):
        self.wg_license_status.values = self._fetch_license_details()

    def on_ok(self):
        self.parentApp.switchFormPrevious()

    def on_cancel(self):
        self.parentApp.switchFormPrevious()     

class EditLicense(_BaseLicenseForm):
    def create(self):
        super().create()
        self.wg_license_options = self.add(LicenseSubMenuList, rely=17)

class ReturnLicense(npyscreen.ActionPopup):
    @error_handler(API_ERROR_TEXT)
    def return_license(self):
        self.parentApp.licensing_api.remove_license()

    def create(self):
        self.add(npyscreen.MultiLine, values=["Choose OK to return the license."], editable=False)

    def on_ok(self):
        self.return_license()
        self.parentApp.switchFormPrevious()

    def on_cancel(self):
        self.parentApp.switchFormPrevious()

class LicenseProxy(_BaseLicenseForm):
    def create(self):
        super().create()
        self.wg_text = self.add(npyscreen.TitleFixedText, rely=17, value="Configure license proxy")

class LicenseOffline(npyscreen.ActionPopup):
    @error_handler(API_ERROR_TEXT)
    def configure_offline_mode(self):
        # create request
        self.parentApp.licensing_api.set_offline()

    def create(self):
        self.add(npyscreen.MultiLine, values=["Choose OK to change offline licensing mode."], editable=False)
        self.wg_offline_option = self.add(npyscreen.CheckBox, name="Offline", values=("Offline",), rely=5)

    def beforeEditing(self):
        pass
        # Get the current state to populate the checkbox

    def on_ok(self):
        self.configure_offline_mode()
        self.parentApp.switchFormPrevious()

    def on_cancel(self):
        self.parentApp.switchFormPrevious()

class ApplyLicense(_BaseLicenseForm):
    @error_handler(title=API_ERROR_TEXT)   
    def _apply_license(self):
        request = ManagementLicenseCode(
            username=self.wg_username.value,
            email_address=self.wg_email.value,
            company_name=self.wg_company.value,
            license=self.wg_license_code.value)
        response = self.licensing_api.update_license(request)

    def create(self):
        super().create()
        self.wg_license_code = self.add(LicenseField, rely=17, name="License code")
        self.wg_username = self.add(npyscreen.TitleText, rely=19, name="User name")
        self.wg_email = self.add(npyscreen.TitleText, rely=20, name="Email address")
        self.wg_company = self.add(npyscreen.TitleText, rely=21, name="Company")

    def on_ok(self):
        self._apply_license()
        super().on_ok()