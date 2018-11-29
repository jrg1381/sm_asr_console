# encoding: utf-8
""" A very simple popup to display an error message """
import npyscreen

# pylint:  disable=too-many-ancestors


class ErrorPopup(npyscreen.MessagePopup):
    """ Simple error popup for network errors and so on """
    def __init__(self, *args, **keywords):
        self.message_text = ["foo", "bar"]
        super(ErrorPopup, self).__init__(*args, **keywords)

    def create(self):
        """ Create the widget """
        self.add(npyscreen.MultiLineEdit, name="Error", editable=False, max_height=20, values=self.message_text)

    def on_ok(self):
        """ On OK, re-show the parent app's current form"""
        # This magic is in the docs somewhere
        self.parentApp.setNextForm(None)
