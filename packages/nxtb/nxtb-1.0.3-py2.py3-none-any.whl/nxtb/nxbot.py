# SPDX-FileCopyrightText: 2024 S60W79 <ernetnakisuml@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-only

import time
import nxtb
import json
from . import timestamps


class catcher:
    def __init__(self, place, amt=1, start="0", end="0", typus=0):
        self.placeId = place
        self.succeded = 0
        self.amount = amt
        self.typus = 0
        self.start = 0
        self.end = 0
        self.start = timestamps.getTime(start)
        self.end = timestamps.getTime(end)

    def getOffer(self):
        getPlace = nxtb.placeinfo(self.placeId)
        return json.loads(getPlace)["place"]["bikes_available_to_book"]

    def book(self, amount):
        start = self.start
        if self.start < int(time.time()):
            start = int(time.time())
        try:
            out = nxtb.book(self.placeId, start, self.end, amount, self.typus)
            self.succeded += 1
            return out
        except:
            pass

    def advancedCheck(self):
        # should be triggered, when script seems to completely succeded. If the booking is somehow canceled, the self.succeded number is synronized.
        try:
            # booksum is the new succeded number
            booksum = 0
            for booking in json.loads(nxtb.bookings())["items"]:
                if booking["state_id"] == 5 and booking["place_id"] == self.placeId:
                    # increase if state is ready at set place
                    booksum += 1
            return booksum
        except:
            print("Warning, connection error!")
            return self.succeded

    def check(self):
        # check maximum offer and amount of mounted bikes. book maximal&wanted for the booking
        amt = min(self.getOffer(), self.amount - self.succeded)
        if self.start > time.time():
            # not yet startetd
            return False
        if amt == 0:
            time.sleep(30)
            self.succeded = self.advancedCheck()
            return False
        else:
            self.book(amt)
            return True

    def loop(self):
        while True:
            if self.end < time.time():
                print(self.succeded, "\t of \t", self.amount, "\tbikes catched")
                raise Exception("Catching Job ended")
                break
            if self.check():
                print("----------------\nJob (partly) succeded!\n----------------")
            time.sleep(10)
