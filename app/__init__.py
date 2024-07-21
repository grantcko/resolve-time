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

    # set log_folder_filepath = "/Applications/DaVinci Resolve/save-logs"
    # run resolve's log app and get filepath to logs
    # get reference to log_filepaths
    log_filepaths = get_log_filepaths(log_folder_filepath)
    # add "/Applications/DaVinci Resolve/save-logs" to log filepaths at the end
    # and summarize

# log_folder_filepath = # filepath from log app
summarize(log_filepaths)
