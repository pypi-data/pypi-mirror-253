# SPDX-FileCopyrightText: 2024 S60W79 <ernetnakisuml@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-only

from datetime import datetime
import time


def parseTime(inp):
    return time.mktime(datetime.strptime(inp, "%H:%M/%d-%m-%Y").timetuple())


def getTime(inp="0"):
    if isinstance(inp, int):
        return inp
    if inp == "0":
        return int(time.time())
    if "/" in inp:
        return int(parseTime(inp))
    if ":" in inp:
        return int(parseTime(str(inp) + "/" + datetime.today().strftime("%d-%m-%Y")))
    if "/" not in inp and ":" not in inp:
        return int(inp)
    return int(inp)
