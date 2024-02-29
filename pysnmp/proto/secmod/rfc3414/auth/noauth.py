#
# This file is part of pysnmp software.
#
# Copyright (c) 2005-2019, Ilya Etingof <etingof@gmail.com>
#
# Copyright (c) 2023-2024, LeXtudio Inc. <support@lextudio.com>
#
# License: https://www.pysnmp.com/pysnmp/license.html
#
from pysnmp.proto.secmod.rfc3414.auth import base
from pysnmp.proto import errind, error


class NoAuth(base.AbstractAuthenticationService):
    serviceID = (1, 3, 6, 1, 6, 3, 10, 1, 1, 1)  # usmNoAuthProtocol

    def hashPassphrase(self, authKey):
        return

    def localizeKey(self, authKey, snmpEngineID):
        return

    @property
    def digestLength(self):
        return 0

    # 7.2.4.2
    def authenticateOutgoingMsg(self, authKey, wholeMsg):
        return wholeMsg

    def authenticateIncomingMsg(self, authKey, authParameters, wholeMsg):
        return
