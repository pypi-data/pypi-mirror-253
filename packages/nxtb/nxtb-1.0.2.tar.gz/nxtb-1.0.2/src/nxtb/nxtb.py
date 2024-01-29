# SPDX-FileCopyrightText: 2024 S60W79 <ernetnakisuml@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-only

import requests
import json
from . import nxbot
from . import timestamps

apikey = "rXXqTgQZUPZ89lzB"
loginkey = ""


def state(nr=0):
    if nr == 0:
        nr = input("")
    url = "https://api.nextbike.net/api/getBikeState.json"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    data = {"apikey": apikey, "loginkey": loginkey, "bike": nr, "show_errors": 1}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.text
    raise Exception("Api rejected: " + json.loads(response.text)["error"]["message"])


def zones(domain):
    url = "https://api.nextbike.net/api/getFlexzones.json"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    data = {"api_key": apikey, "domain": domain, "show_errors": 1}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.text
    raise Exception("Api rejected: " + json.loads(response.text)["error"]["message"])


def pause(nr=0):
    if nr == 0:
        nr = input("")
    url = "https://api.nextbike.net/api/rentalBreak.json"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    data = {"apikey": apikey, "bike": int(nr), "loginkey": loginkey, "show_errors": 1}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.text
    raise Exception("Api rejected: " + json.loads(response.text)["error"]["message"])


def openlock(nr=0):
    if nr == 0:
        nr = input("")
    url = "https://api.nextbike.net/api/openLock.json"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    data = {"apikey": apikey, "bike": int(nr), "loginkey": loginkey, "show_errors": 1}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.text
    raise Exception("Api rejected: " + json.loads(response.text)["error"]["message"])


def returnbike(
    nr=0, place=0, lat=1000, lng=1000, comment="", rating=5, fee=False, force=False
):
    if nr == 0:
        nr = input("")
    url = "https://api.nextbike.net/api/return.json"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    advanced = {}
    if place != 0:
        advanced = {"place": place}
    else:
        if lat != 1000:
            advanced = {"lat": lat, "lng": lng}
    data = {
        **{
            "api_key": apikey,
            "bike": nr,
            "loginkey": loginkey,
            "comment": comment,
            "rating": rating,
            "fee": fee,
            "force": force,
            "show_errors": 1,
        },
        **advanced,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.text
    raise Exception("Api rejected: " + json.loads(response.text)["error"]["message"])


def cancel(bookingId=0):
    if bookingId == 0:
        bookingId = input("")
    url = "https://api.nextbike.net/api/cancelBooking.json"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    data = {
        "api_key": apikey,
        "booking_id": bookingId,
        "loginkey": loginkey,
        "show_errors": 1,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.text
    raise Exception("Api rejected: " + json.loads(response.text)["error"]["message"])


def placeinfo(place=0):
    if place == 0:
        place = input("")
    url = "https://api.nextbike.net/api/getPlaceDetails.json"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    data = {"apikey": apikey, "loginkey": loginkey, "place": place, "show_errors": 1}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.text
    raise Exception("Api rejected: " + json.loads(response.text)["error"]["message"])


def current():
    url = "https://api.nextbike.net/api/getOpenRentals.json"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    data = {"apikey": apikey, "loginkey": loginkey, "show_errors": 1}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.text
    raise Exception("Api rejected: " + json.loads(response.text)["error"]["message"])


def history():
    url = "https://api.nextbike.net/api/rentals.json"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    data = {"apikey": apikey, "loginkey": loginkey, "show_errors": 1}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.text
    raise Exception("Api rejected: " + json.loads(response.text)["error"]["message"])


def bookings():
    url = "https://api.nextbike.net/api/bookings.json"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    data = {"apikey": apikey, "loginkey": loginkey, "show_errors": 1}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.text
    raise Exception("Api rejected: " + json.loads(response.text)["error"]["message"])


def cities(city="", searchplace=""):
    appendix = "&list_cities=1"
    if city != "":
        appendix = "&city=" + city
    url = (
        "https://maps.nextbike.net/maps/nextbike-official.json?include_domains=de,ue,ug,um,ur,bh"
        + appendix
    )
    response = requests.get(url)
    if response.status_code == 200:
        if searchplace == "":
            return response.text
        else:
            matching = []
            for place in json.loads(response.text)["countries"][0]["cities"][0][
                "places"
            ]:
                if searchplace.lower() in place["name"].lower():
                    matching.append(place)
            return json.dumps(matching)
    raise Exception("Api rejected: " + json.loads(response.text)["error"]["message"])


def book(place=0, start="0", end="0", amount=1, typus="0"):
    if place == 0:
        place = input("")
    start = timestamps.getTime(start)
    end = timestamps.getTime(end)
    url = "https://api.nextbike.net/api/booking.json"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    if start == 0:
        if typus == "0":
            data = {
                "apikey": apikey,
                "loginkey": loginkey,
                "place": place,
                "end_time": end,
                "num_bikes": amount,
                "show_errors": 1,
            }
        else:
            data = {
                "apikey": apikey,
                "loginkey": loginkey,
                "place": place,
                "end_time": end,
                "biketypes": {typus: amount},
                "show_errors": 1,
            }
    else:
        data = {
            "apikey": apikey,
            "loginkey": loginkey,
            "place": place,
            "start_time": start,
            "end_time": end,
            "num_bikes": amount,
            "show_errors": 1,
        }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.text
    raise Exception("Api rejected: " + json.loads(response.text)["error"]["message"])


def account():
    url = "https://api.nextbike.net/api/getUserDetails.json"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    data = {"apikey": apikey, "loginkey": loginkey, "show_errors": 1}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.text
    raise Exception("Api rejected: " + json.loads(response.text)["error"]["message"])


def readRfid():
    url = "https://api.nextbike.net/api/getCustomerRfids.json"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    data = {"apikey": apikey, "loginkey": loginkey, "show_errors": 1}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.text
    raise Exception("Api rejected: " + json.loads(response.text)["error"]["message"])


def setRfid(uid, nr1="", nr2=""):
    if int(input("repeat UID:")) != int(uid):
        # prevent connecting wrong uid.
        raise Exception("Canceled: UIDs do not match!")
    url = "https://api.nextbike.net/api/setCustomerRfid.json"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    data = {
        "apikey": apikey,
        "loginkey": loginkey,
        "rfid": int(uid),
        "uid": int(uid),
        "rfid_uid": int(uid),
        "type": "girocard",
        "expiry_date": 1694954785,
        "card_number1": nr1,
        "card_number2": nr2,
        "show_errors": 1,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.text
    raise Exception("Api rejected: " + json.loads(response.text)["error"]["message"])


def login(mobile="", username="", pin=0):
    if pin == 0:
        pin = input("PIN:")
    url = "https://api.nextbike.net/api/login.json"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    if mobile != "":
        data = {"apikey": apikey, "mobile": mobile, "pin": pin, "show_errors": 1}
    else:
        if username != "":
            data = {
                "apikey": apikey,
                "username": username,
                "pin": int(pin),
                "show_errors": 1,
            }
        else:
            raise Exception("Either mobile phone number or username have to be given!")
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(
            "Api rejected: " + json.loads(response.text)["error"]["message"]
        )
    raise Exception("Api rejected: " + json.loads(response.text)["error"]["message"])


def logout():
    url = "https://api.nextbike.net/api/logout.json"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    data = {"apikey": apikey, "loginkey": loginkey, "show_errors": 1}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.text
    raise Exception("Api rejected: " + json.loads(response.text)["error"]["message"])


def rent(nr=0, paused=False, resume=False, nresume=False):
    if nr == 0:
        nr = input("")
    url = "https://api.nextbike.net/api/rent.json"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    data = {
        "loginkey": loginkey,
        "apikey": apikey,
        "bike": nr,
        "start_paused": paused,
        "resume": resume,
        "nresume": nresume,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.text
    raise Exception("Api rejected: " + json.loads(response.text)["error"]["message"])


def catch(place=0, amount=1, start="0", end="0", typus=0):
    if place == 0:
        place = input("")
    catching = nxbot.catcher(place, amount, start, end, typus)
    catching.loop()
