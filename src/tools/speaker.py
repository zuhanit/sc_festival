from eudplib import *

const sb = StringBuffer()

function globalText(*args) {
    for i in range(0, 5)
        sb.print(args)
}