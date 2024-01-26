#Message on change fetches data from a website, and notifies the user when the data has changed.
#Copyright (C) 2024  Rūdolfs Driķis
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

import requests
import argparse
import time
from playsound import playsound
import webbrowser


def main(url='', delay=10, change_sound='change.mp3', open_page=False):
    comparison_data = requests.get(url).text
    while True:
        latest_obtained_data = requests.get(url).text
        if latest_obtained_data == comparison_data:
            print('Nothing has changed')
        else:
            break

        time.sleep(delay)

    print("Something has changed!")
    if open_page:
        webbrowser.open(url)
    playsound(change_sound)
