"""
SConnectForm.py

Form to connect to slack
"""

import npyscreen


class SConnectForm(npyscreen.Form):
    def create(self):
        self.name = "Login to Slack"
        # cs = self.add(npyscreen.BoxBasic, name="Connect to Slack")
        self.add(npyscreen.TitleText, name="Login:")
        self.add(npyscreen.TitlePassword, name="Password:")
        self.how_exited_handers[
            npyscreen.wgwidget.EXITED_ESCAPE] = self.exit

    def exit(self):
        self.parentApp.setNextForm(None)
        self.editing = False
