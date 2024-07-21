#!/usr/bin/env python3

import sys
from functions import *
from hello import hello

# COMMAND LINE LOGIC

if len(sys.argv) < 2:
    print("Usage: resolve-time <log_folder_filepath>")
    sys.exit(1)

log_folder_filepath = sys.argv[1]
log_filepaths = get_log_filepaths(log_folder_filepath)
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
