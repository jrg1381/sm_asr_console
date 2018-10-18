# encoding: utf-8
import npyscreen


class ErrorPopup(npyscreen.MessagePopup):
    def __init__(self, *args, **keywords):
        self.message_text = ["foo", "bar"]
        super(ErrorPopup, self).__init__(*args, **keywords)

    def create(self):
        self.add(npyscreen.MultiLineEdit, name="Error", editable=False, max_height=20, values=self.message_text)

    def on_ok(self):
        self.parentApp.setNextForm(None)