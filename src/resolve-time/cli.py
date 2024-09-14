#!/usr/bin/env python3

import sys
import typer
from datetime import datetime
from functions import *
import glob
import os

#### REFERENCES ####

# Get a reference to txt file filepath
txt_filepath = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/resolve-time-log.txt"

# Get a reference to the date and time
current_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")

# get reference to $HOME environmental variable
home_path = os.environ["HOME"]

#### GET LOG FILES, PROCESS, PRINT SUMMARY ####

# TODO: create an option for auto or manual log file generation then define the filepath that gets passed to process the logs accordingly

# auto generate the log files
auto_gen_logs(current_datetime, home_path)

auto_zip_filepath = f"{home_path}/Desktop/DaVinci-Resolve-logs-{current_datetime[:11]}*.tgz"

processed_info = process_logs(home_path, current_datetime, txt_filepath, auto_zip_filepath)

summary = build_summary(processed_info["info"], processed_info["monthly_info"])

print(summary)

#### REMOVE LOG FILES ####

# Wait 3 seconds. Not using sleep() because of iteraction with datetime
threading.Event().wait(3)

# Remove the generated zip file
subprocess.run(['rm', '-rf', processed_info["zip_filepath"]])

# Remove the unzipped log folder
subprocess.run(['rm', '-rf', f"{home_path}/Desktop/Library"])
