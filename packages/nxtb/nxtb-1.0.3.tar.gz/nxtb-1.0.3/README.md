<!--
SPDX-FileCopyrightText: 2024 S60W79 <ernetnakisuml@gmail.com>

SPDX-License-Identifier: GPL-3.0-only
-->

# Nextbike Command Line Interface

CLI for accessing the Nextbike Api, powered by python, based on json feedback

This code is licensed under the GPL v3 license.

## Usage

```
python cli.py MODUS --option1 value --option2 ...
```

For example:

```
python cli.py rent --nr 123456 --loginkey ###############
```

### Generic help

```
python cli.py -h
```
or

```
python cli.py --help
```

## Global Flags

* --loginkey

Session password. Could be obtained by the login modus.

* --apikey

Allways optional, apikey if man want it to set manually. If not set, use the standart apikey.

## Modi

### account

Gives Details about the given account.
**--loginkey required!**

### book

Books/Reserves a specific amount of bikes, in a specific timewindow, at a specific place. Note that you have to enter the place id, also when you want to book a single bike.
Also the starting point of the timewindow might not work correctly, depending on the Nextbike System you are using then. If you need that, use the fix *catch*.

#### Options

* **place**
    * place id, required, if not set, input/pipe requested
* start
    * start of the timewindow, set like HH:MM, HH:MM/dd-mm-yyyy, or the unix timestamp in seconds.
* end
    * end of the timewindow, set like HH:MM, HH:MM/dd-mm-yyyy, or the unix timestamp in seconds.
* amount
    * amount of bikes to be booked
* typus
    * bike type of the bike(s) to be booked
* **--loginkey required!**

#### Examples

Booth commands will book you a bike at Berlin, Alexanderplatz. For the first one you would have to know the place id, for the second one only the  name of the station.

```
python cli.py book --place 3165072 --loginkey ################
python cli.py cities --city 362 --searchplace Alexanderplatz | jq .[0].uid | python cli.py book --loginkey ################

```

### bookings

List of all bookings.
**--loginkey required!**

### cancel

Cancel a currently running booking by its Id.

**--loginkey required!**


### catch
nr
Bookings for empty stations or booking starting in the future, fix for booking:

After started, the script will wait untill at the given station is a bike available when the start time is reached. The booking will be called again if the booking has been canceled.

* **place**
    * place id, required, if not set, input/pipe requested
* start
    * start of the timewindow, set like HH:MM, HH:MM/dd-mm-yyyy, or the unix timestamp in seconds.
* end
    * end of the timewindow, set like HH:MM, HH:MM/dd-mm-yyyy, or the unix timestamp in seconds.
* amount
    * amount of bikes to be booked
* typus
    * bike type of the bike(s) to be booked
* **--loginkey required!**


### cities

Returns if no city specified, a list of all cities.
If one City specified, there is a list off all places/single bikes, which could be searched.

#### Options

* city
    * id of the city (three digits)
* searchplace
    * Search term for a place

#### Example

How to find berlin Alexander platz. First find the domain and then search for Alexanderplatz.

```
python cli.py cities |  jq '.countries.[] | select(.name=="nextbike Berlin") | .cities[0].uid'
python cli.py cities --city 362 --searchplace Alexanderplatz
```

### current

List of all currently running rentals.
**--loginkey required!**


### history

List of the rental history.
**--loginkey required!**

### login

Generates a loginkey, depending on the mobilephone number or username and the PIN.
The Loginkey is only valid with the apikey used with login.

#### Options

* mobile
    * mobilephone number with country prefix (e.g. 49#####), but without the leading 0
* username
    * could be used instead of mobile
* **PIN**
    * 6 digits pin, sent by SMS after register or PIN change.

### logout

Invalidates the current loginkey.
**--loginkey required!**

### openlock

Opens the lock, in case the lock is currently closed.
The rental of the bike has to run, to trigger this function.

#### Options

* nr, required, if not set, input/pipe requested
    * bikenumber of the bike to be unlocked

**--loginkey required!**

### pause

Activates parking mode for specific bike. When activated, the bike **won't** be returned when the lock is closed but swtitch into pause mode.

#### Optionspython cli.py zones --domain bn | jq .geojson.nodeValue > bn.gejson

* **nr**
    * bikenumber of the bike to be paused, required, if not set, input/pipe requested

**--loginkey required!**

### placeinfo

Returns some details about the given place

#### Options

* place, required, if not set, input/pipe requested
    * place id
**--loginkey required!**

### readRfid

Returns a list of all rfid uids set for the account

**--loginkey required!**

### rent

Starts a rental of a given bike

#### Options

* **nr**
    * number of a bike to be rented, required, if not set, input/pipe requested
* paused
    * start the rental if set directly in pause mode (binary flag)
* resume
    * force the resume of the last rental, so that the rental time will be summed. **Attention** if set, this might cause long rental times.
* nresume
    * Prevent resume, so that the rental time won't be sumed

    **--loginkey required!**

### returnbike

Manual return bike. This is only needed, if the bike is locked but the rental is still running. Normally, the bike will return after closing the lock.

#### Options

* **nr**
    * number of the bike to be returned, required, if not set, input/pipe requested
* place
    * place id where the bike is returned
* lat
    * latitude where the bike is returned
* lng
    * longtitude where the bike is returned
* comment
    * comment of the rental in written form
* rating
    * number 0-5, 0 is the worst, 5 is the best
* fee
    * Accept the automatic service fee for return bike outside of official place and flexzone (binary flag)
* force
    * If set skip some checks and force return.

### setRfid

Sets a uid for the account, so that you can rent bikes with rfid chips.

**warning**: this method is unsafe, because the chips can be spoofed. Also if the chip gets lost, you can't lock them by yourself.

You have to repeat the uid after executing the command

#### options

* uid
    * uid, given as an integer
* nr1
    * number written on the card, to distinguish between rfid cards
* nr2

* 2nd number written on the card, just like nr1

### state

Status of a given bike

#### Options

* nr
    * bikenumber of the bike to be checked, required, if not set, input/pipe requested

### zones

get geojson of the service zones. Mostly zones without additional payments are coloured blue, zones with additional payments are coloured pink. But that may differ. Many cities do not have any zones but only stations. You can find out the domains with the cties function.

#### Options

* domain
    * if set, only load the geojson of the given city domain (e.g.)


#### Example

Get the zones in Berlin and safe them in a file. You can open them with programms like gnome-maps or marble

```
python cli.py zones --domain bn | jq .geojson.nodeValue > berlin.geojson
gnome-maps berlin.geojson

```


