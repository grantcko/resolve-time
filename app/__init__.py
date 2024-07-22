#!/usr/bin/env python3

import sys
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


if len(sys.argv) < 2:

    # make a txt file at the application support directory (/Library/Application Support/Blackmagic Design/DaVinci Resolve/resolve-time-log.txt)
    # get a reference to that txt file filepath (resolve_time_log)

    # run resolve's CaptureLogs app (/Library/Application Support/Blackmagic Design/DaVinci Resolve/CaptureLogs.app)
    # wait a second and press "enter" - use pyautogui
    # get a reference to the resolve generated zip file containing the log files (on the desktop)
    # get a reference to the date and time (used for the filename generated)

    # get a reference to the title of the generated zip file using the date and time (format: "DaVinci-Resolve-logs-20240721-170737")
    # unzip that zip file
    # get reference to unzipped folder containing log files (/Users/granthall/Desktop/Library/Application Support/Blackmagic Design/DaVinci Resolve/logs)

    log_filepaths = get_log_filepaths(log_folder_filepath) # (keep this) get reference to log_filepaths, a list of filepaths
        # sidenote: this function (get_log_filepaths) will write any new save entries to the new resolve time log

    # add our new resolve_time_log to log_filepaths
    # and summarize

# log_folder_filepath = # filepath from log app
summarize(log_filepaths)
