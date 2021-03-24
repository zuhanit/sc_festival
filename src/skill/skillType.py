from eudplib import *
from eudplib.core.eudfunc.consttype import createEncoder
from eudplib.core.rawtrigger.strenc import _EncodeAny
import re

skillTypeDict = {
    "q": 0,
    "w": 1,
    "e": 2,
}

def skilltype(txt):
    txt = unProxy(txt)
    try:
        return skillTypeDict[txt]
    except KeyError:
        for s, i in skillTypeDict.items():
            if re.search(txt, s) is not None:
                return i
        raise KeyError

def EncodeType(txt, issueError=True):
    return _EncodeAny("TrgType", skilltype, skillTypeDict, txt, issueError)

TrgType = createEncoder(EncodeType)