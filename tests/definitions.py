# Import external modules

from datetime import datetime, time, timedelta
import glob
import os
import pytest
import sys
import subprocess
import time
import csv

# Import internal modules

sys.path.append(os.path.abspath('src'))
from resolvetime.functions import get_log_filepaths
from resolvetime.functions import build_summary
from resolvetime.functions import collect_entries
from resolvetime.functions import sort_monthly
from resolvetime.functions import entries_info
from resolvetime.functions import auto_gen_logs
from resolvetime.functions import process_logs
from resolvetime.functions import get_entries_monthly_info

#### Definitions

log_filepaths = get_log_filepaths("tests/test_logs/sep-b_2024")
log_filepaths_missing = get_log_filepaths("tests/test_logs/apr-jun_2024")
log_filepaths_overlap = get_log_filepaths("tests/test_logs/sep-a_2024")
home_path = os.environ["HOME"]
masterlog_file_blank = "tests/masterlog_blank.txt"
masterlog_file_missing = "tests/masterlog_missing.txt"
masterlog_file_overlap = "tests/masterlog_overlap.txt"
test_current_datetime = "20240917-185013"
test_zip_file_pattern = f"tests/zipped-logs/DaVinci-Resolve-logs-{test_current_datetime[:11]}*.tgz"
test_log_folder_filepath="tests/zipped-logs/Library/Application Support/Blackmagic Design/DaVinci Resolve/logs"

## CALCULATED STATS

# Calculated stats from blank master run

with open('tests/calculated_stats/blankmstr_medac.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)[1:]  # Skip the first column for headers
    data = {row[0]: {header: int(value) if value.isdigit() else str(value) for header, value in zip(headers, row[1:])} for row in reader}

    bkmr_total_entries = data['total']['entry-count-sep-b']
    bkmr_day_count = data['total']['days-count']
    bkmr_month_count = data['total']['months-count']
    # bkmr_dates_worked = [f"09_{(data['total']['dates-worked-sep'])}_2024"]
    bkmr_dates_worked = [f"09_{day}_2024" for day in str(data['total']['dates-worked-sep']).split()]

# Calculated stats from missing entries master run

with open('tests/calculated_stats/missingmstr_medac.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)[1:]  # Skip the first column for headers
    data = {row[0]: {header: int(value) if value.isdigit() else str(value) for header, value in zip(headers, row[1:])} for row in reader}

    msmr_total_entries = data['total']['entry-count-total']
    msmr_day_count = data['total']['days-count']
    msmr_month_count = data['total']['months-count']
    # bkmr_dates_worked = [f"09_{(data['total']['dates-worked-sep'])}_2024"]
    msmr_dates_worked = [f"09_{day}_2024" for day in str(data['total']['dates-worked-sep']).split()]

# calculated stats from overlap entries master run

with open('tests/calculated_stats/overlapmstr_medac.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)[1:]  # Skip the first column for headers
    data = {row[0]: {header: int(value) if value.isdigit() else str(value) for header, value in zip(headers, row[1:])} for row in reader}

    opmr_total_entries = data['total']['entry-count-sep-b']
    opmr_day_count = data['total']['days-count']
    opmr_month_count = data['total']['months-count']
    # bkmr_dates_worked = [f"09_{(data['total']['dates-worked-sep'])}_2024"]
    bkmr_dates_worked = [f"09_{day}_2024" for day in str(data['total']['dates-worked-sep']).split()]

## INFO FROM LOGS BEING IMPORTED

# Blank Master

save_entries = collect_entries(log_filepaths, masterlog_file_blank, accuracy="medium")
save_entries_info = entries_info(save_entries)
save_entries_monthly = sort_monthly(save_entries)
save_entries_monthly_info = get_entries_monthly_info(save_entries_monthly)

bkmr_mediumac = {
    "entries": save_entries,
    "entries_info": save_entries_info,
    "entries_monthly": save_entries_monthly,
    "monthly_info": save_entries_monthly_info,
}

# Missing Master

save_entries = collect_entries(log_filepaths, masterlog_file_missing, accuracy="medium")
save_entries_info = entries_info(save_entries)
save_entries_monthly = sort_monthly(save_entries)
save_entries_monthly_info = get_entries_monthly_info(save_entries_monthly)

msmr_mediumac = {
    "entries": save_entries,
    "entries_info": save_entries_info,
    "entries_monthly": save_entries_monthly,
    "monthly_info": save_entries_monthly_info,
}

# Overlapping Master

save_entries = collect_entries(log_filepaths, masterlog_file_overlap, accuracy="medium")
save_entries_info = entries_info(save_entries)
save_entries_monthly = sort_monthly(save_entries)
save_entries_monthly_info = get_entries_monthly_info(save_entries_monthly)

opmr_mediumac = {
    "entries": save_entries,
    "entries_info": save_entries_info,
    "entries_monthly": save_entries_monthly,
    "monthly_info": save_entries_monthly_info,
}
