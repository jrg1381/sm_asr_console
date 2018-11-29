# encoding: utf-8
""" Main menu options """

import npyscreen


class MainMenuList(npyscreen.MultiLineAction):
    """ Maps from names on screen to (form) classes to show """
    def __init__(self, *args, **keywords):
        super(MainMenuList, self).__init__(*args, **keywords)
        # Map from the text on screen to the name of the sub-form
        self.form_index = {
            "License": "LICENSE",
            "Workers": "WORKERS",
            "Networking": "NETWORK",
            "Services": "SERVICES",
            "Reboot": "MAIN/REBOOT",
            "Shutdown": "MAIN/SHUTDOWN",
            "Tools": "DIAGNOSTICS"
            }
        self.values = list(self.form_index.keys())

    def actionHighlighted(self, act_on_this, key_press):
        self.parent.parentApp.switchForm(self.form_index[act_on_this])
