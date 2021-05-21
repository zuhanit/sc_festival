from datetime import datetime
from eudplib import *


def OnInit():
    chkt = GetChkTokenized()
    buildTime = GetStringIndex(str(datetime.now()))
    SPRP = bytearray(chkt.getsection("SPRP"))
    SPRP[2:4] = i2b2(buildTime)
    chkt.setsection("SPRP", SPRP)