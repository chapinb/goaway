__author__ = 'cbryce'
__license__ = ''
__date__ = ''
__version__ = ''

"""
goaway - A simple script that tells you to get up and do something away from the computer
Copyright (C) 2015  Chapin Bryce

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import time
import easygui
import schedule

"""
Save your eyes

Every 15 minutes you should look away from your computer for a minute
- look at something roughly 20 or more feet away for a minute or 2
"""


def save_your_eyes():
    DURATION = 60  # Seconds

    now = time.time()
    easygui.msgbox(msg="Your eyes need a break, look at least 20ft away for a minute!", ok_button="Is it done yet?")
    while time.time()-now < DURATION:
        easygui.msgbox(msg="Not done yet! keep looking away! \n\nYou have " + str(time.time() - now - DURATION) +
                           " seconds remaining", ok_button="check again")

"""
Save your back

Every 45 minutes stand up, move around for two minutes
- Go to the bathroom, get a drink, etc. just try to move a little
"""


def save_your_back():
    DURATION = 120  # Seconds

    now = time.time()
    easygui.msgbox(msg="Your back need a break, go stand up and do somehting for 2 minutes!", ok_button="Is it done "
                                                                                                       "yet?")
    while time.time() - now < DURATION:
        easygui.msgbox(msg="Not done yet! keep looking away! \n\nYou have " + str(time.time() - now - DURATION) +
                           " seconds remaining", ok_button="check again")


if __name__ == '__main__':

    EYE_INTERVAL = 15
    BACK_INTERVAL = 48

    schedule.every(EYE_INTERVAL).minutes.do(save_your_eyes)
    schedule.every(BACK_INTERVAL).minutes.do(save_your_back)

    while True:
        schedule.run_pending()
        time.sleep(1)