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

import argparse
import message_on_change.fetch_logic


parser = argparse.ArgumentParser(
    prog="Comparator",
    description="compares a downloaded version of a webpage, to the hosted one on a specified URL at a given interval, to signal to you when a change has been made."
)
parser.add_argument('URL')
parser.add_argument('-d', '--delay', nargs=1)
parser.add_argument('-o', '--open-after', dest='open_after', required=False, action='store_true')
args = parser.parse_args()

if args.delay is not None:
    delay = args.delay
else:
    delay = 10

if args.open_after is not None:
    open_after = True
else:
    print('open after')
    open_after = False

message_on_change.fetch_logic.main(
    url=args.URL,
    delay=delay,
    open_page=open_after
)