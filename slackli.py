#!/usr/bni/env python
# encoding: utf-8

import npyscreen
from SConnectForm import SConnectForm


class Slackli(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", SConnectForm())


def main():
    slackli = Slackli()
    slackli.run()


if __name__ == "__main__":
    main()
