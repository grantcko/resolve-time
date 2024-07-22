#!/usr/bin/env python3

import sys
import subprocess
import time
import pyautogui
from datetime import datetime
from functions import *

# COMMAND LINE LOGIC

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


## TODO:

# Get a reference to txt file filepath
txt_file_path = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/resolve-time-log.txt"

# Run resolve's CaptureLogs app
subprocess.run(['open', '/Library/Application Support/Blackmagic Design/DaVinci Resolve/CaptureLogs.app'])

# Get a reference to the date and time
current_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")

# Wait a second and press "enter" using pyautogui
pyautogui.PAUSE = 1.0
pyautogui.press('enter')
pyautogui.press('enter')

# Get a reference to the title of the generated zip file using the date and time
zip_file_name = f"DaVinci-Resolve-logs-{current_datetime}.tgz"
zip_file_path = f"/Users/granthall/Desktop/{zip_file_name}"

# Unzip that zip file
subprocess.run(['open', zip_file_path])

# Get reference to the unzipped folder containing log files
log_folder_filepath = "/Users/granthall/Desktop/Library/Application Support/Blackmagic Design/DaVinci Resolve/logs"

log_filepaths = get_log_filepaths(log_folder_filepath)  # (keep this) get reference to log_filepaths, a list of filepaths

# Add our new resolve time log to log_filepaths, at the end of the list
log_filepaths.append(txt_file_path)
summarize(log_filepaths) # summarize
