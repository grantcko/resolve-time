#!/usr/bin/env python3

import sys
import subprocess
import threading
import pyautogui
from datetime import datetime
from functions import *
import glob
import os

def summarize(log_filepaths):
    save_entries = collect_save_entries(log_filepaths)
    info = save_entries_info(save_entries)
    # collect monthly save entries and get save entries info from each month, build summary from info and monthly info
    monthly_save_entries = collect_monthly_save_entries(save_entries)
    months = monthly_save_entries.keys()
    monthly_info = {}
    for month in months:
        if month not in monthly_info:
            monthly_info[month] = save_entries_info(monthly_save_entries[month])
    summary = build_summary(info, monthly_info)
    print(summary)

# COMMAND LINE

# Get a reference to txt file filepath
txt_file_path = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/resolve-time-log.txt"

# Get a reference to the date and time
current_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")

# Run resolve's CaptureLogs app
subprocess.run(['open', '/Library/Application Support/Blackmagic Design/DaVinci Resolve/CaptureLogs.app'])

# get reference to $HOME environmental variable
home_path = os.environ["HOME"]

# Exit out of CaptureLogs - Wait a second and press "enter" using pyautogui
pyautogui.PAUSE = 1.0
pyautogui.press('enter')
pyautogui.press('enter')

# Get a reference to the title of the generated zip file using the date and time
zip_file_name = f"DaVinci-Resolve-logs-{current_datetime}.tgz"
zip_file_path = f"{home_path}/Desktop/{zip_file_name}"

# Unzip that zip file with a margin of error in the filename (up to the minute in the timestamp)
# Use a glob pattern to find the file
zip_file_pattern = f"{home_path}/Desktop/DaVinci-Resolve-logs-{current_datetime[:11]}*.tgz"
matching_files = glob.glob(zip_file_pattern)

if matching_files:
    zip_file_path = matching_files[0]
    subprocess.run(['open', zip_file_path])
else:
    print("No matching log file found.")

# Get reference to the unzipped folder containing log files
log_folder_filepath = f"{home_path}/Desktop/Library/Application Support/Blackmagic Design/DaVinci Resolve/logs"
# print("log_folder_filepath : " + log_folder_filepath)

threading.Event().wait(3)

log_filepaths = get_log_filepaths(log_folder_filepath)  # get reference to log_filepaths, a list of filepaths

print(log_filepaths)
# Add our new resolve time log to log_filepaths, at the end of the list
log_filepaths.append(txt_file_path)
print(log_filepaths)
summarize(log_filepaths) # summarize

# Wait 3 seconds. Not using sleep() because of iteraction with datetime
threading.Event().wait(3)

# # Remove the generated zip file
subprocess.run(['rm', '-rf', zip_file_path])

# # Remove the unzipped log folder
subprocess.run(['rm', '-rf', f"{home_path}/Desktop/Library"])
