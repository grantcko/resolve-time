from datetime import datetime, time, timedelta
import glob
import os
import re
import subprocess
import threading
import pyautogui

def get_log_filepaths(log_folder_filepath):

    """
    Function to get all log file paths in the given directory.

    returns a list of strings
    """

    # Define the pattern for the log files
    log_filepath_pattern = f'{log_folder_filepath}/davinci_resolve.log*'

    # Collect all matching file paths
    log_filepaths = glob.glob(log_filepath_pattern)

    # print(log_filepaths)

    # Return the list of log file paths
    return log_filepaths

def build_summary(info, monthly_info):
    """
    Function to build a summary of projects worked on.
    """

    project_summaries = []
    for project, hours in info['project_work_hours'].items():
        project_summaries.append(f"  \"{project}\" {hours:.2f} hours")

    total_summary = (
        f"\n      [ALL-TIME]\n      ----------\n"
        f"  sessions : {info['session_count']}\n"
        f"  time : {info['work_hours']:.2f} hours\n"
        f"  -\n" + "\n".join(project_summaries) + "\n"
    )

    # TODO: print monthly info (monthly_info should be a dict with dicts (keys, mmyyyy:)
    # iterate over monthly info and print each month name , year, total sessions , total hours

    monthly_summary = []
    months = monthly_info.keys()
    for month in months:
        month_project_summaries = []
        for project, hours in monthly_info[month]['project_work_hours'].items():
            month_project_summaries.append(f"  \"{project}\" {hours:.2f} hours")

        monthly_summary.append(
            f"      [{month}]\n      ---------\n"
            f"  sessions : {monthly_info[month]['session_count']}\n"
            f"  time : {monthly_info[month]['work_hours']:.2f} hours\n"
            f"  -\n" + "\n".join(month_project_summaries)
        )

    # get ref to the total summary
    summary = f"{total_summary}"

    # add each month's summary to that
    for month_summary in monthly_summary:
        summary = f"  {summary}\n{month_summary}\n"

    #

    return summary

def collect_entries(log_filepaths, masterlog, accuracy="medium"):
    """
    Function to collect log entries from serveral files and store them in the master log

    Args:
    log_filepath (list): list of log file paths (strings)
    masterlog: the master log file
    accuracy: how many log entries are collected, the resolution.

    Returns:
    list: A list of dictionaries containing 'datetime' and 'project_name' from the log entries.
    """
    entries = []

    # Regular expression to match the log line

    log_pattern = re.compile(r"^\S+\s+\|\s+SyManager\.ProjectManager\s+\|\s+INFO\s+\|\s+(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})\s+\|\s+Start saving project (?P<project_title>.+)$")

    # log_pattern = re.compile(r".*")

    # collect timestamp and project title into into a save entry dict, into save entries list (for each filepath)
    # and save any new entries to a txt file to the computer

    for log_filepath in log_filepaths:
        # print(log_filepath)
        try:
            with open(log_filepath, 'r') as log_file:
                num = 1 #
                for line in log_file:
                    # print(line)
                    match = log_pattern.match(line)
                    if match:
                        #
                        # print("Match" + str(num) + f" : {match.group(0)}")
                        num += 1
                        #
                        entry = {
                            'timestamp': match.group('timestamp'),
                            'project_title': match.group('project_title')
                        }
                        entries.append(entry)

                        # Make a txt file at the application support directory
                        txt_filepath = masterlog
                        if not os.path.exists(txt_filepath):
                            with open(txt_filepath, 'w') as txt_file:
                                txt_file.write(line)
                        else:
                            with open(txt_filepath, 'r') as txt_file:
                                if line not in txt_file.read():
                                    with open(txt_filepath, 'a') as txt_file_append:
                                        txt_file_append.write(line)

        except FileNotFoundError:
            print(f"The file {log_filepath} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # return entries, a list of sorted dicts [{'timestamp':'...', 'project_title':'...'},{'...'}]
    all_collected_entries = sorted(entries, key=lambda entry: datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S,%f'))
    # print(all_collected_entries)
    return all_collected_entries

def sort_monthly(entries):
    months_worked = {}
    # go through each entry
    for entry in entries:
        # get ref to mm_yyyy (ex:06_2024) unless it's a duplicate
        mm_yyyy = f"{datetime.strftime(datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S,%f'), '%m_%Y')}"
        # add key:value pair with key as 'mm/yyyy', and value as an empty list, if that month isn't already there
        if mm_yyyy not in months_worked:
            months_worked[mm_yyyy] = []
        # append current save entry to entries list pertaining to the month
        # print(months_worked)
        months_worked[mm_yyyy].append(entry)

    return months_worked
    # example :{'04/2024':[save entries], '05/2024':[save entries], '06/2024':[save entries]}

def entries_info(entries):# returns dict of total and per project summaries for: all time, per month
    """
    Function to get number of work sessions, total hours, hours per project from save entries.
    """

    # if there are no save entries, return an empty summary

    if not entries:
        return {
             'session_count': 0,
             'work_hours': 0.0,
             'project_work_hours': {}
            }

    ## get starting references for: ##
    # session count, work hours, current-1 timestamp (to compare with current)

    session_count = 1
    work_hours = timedelta(microseconds=0)
    compare_timestamp = None

    ## get starting references for: ##
    # work summaries per project, current project, current project's hours

    project_work_hours = {}
    current_project = None
    current_project_hours = timedelta(microseconds=0)

    # iterate over each save entry and collect session count and work hours for all time and per project

    # print(entries)
    for entry in entries:
        ## VARIABLES ##

        # current entry's timestamp
        timestamp = datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S,%f')
        # if we are on the first entry, set the compare timestamp, continue to next entry
        if compare_timestamp is None:
            compare_timestamp = timestamp
            continue
        # difference between the current timestamp and the last one
        time_difference_min = (timestamp - compare_timestamp).total_seconds() / 60.0

        # IF: AN EDIT SESSION ENDED -> count one more session and set the compare timestamp
        # ELSE: IF AN EDIT SESSION CONTINUED -> increase work_hours and session count, set project stats if end of project

        if time_difference_min > 15:
            session_count += 1
            compare_timestamp = timestamp
        else:
            difference = timestamp - compare_timestamp
            work_hours += difference
            current_project_hours += difference
            compare_timestamp = timestamp

            if current_project != entry['project_title']:
                if current_project is not None:
                    project_work_hours[current_project] = project_work_hours.get(current_project, 0) + current_project_hours.total_seconds() / 3600
                current_project = entry['project_title']
                current_project_hours = timedelta(microseconds=0)

    if current_project is not None:
        project_work_hours[current_project] = project_work_hours.get(current_project, 0) + current_project_hours.total_seconds() / 3600

    return {
        'session_count': session_count,
        'work_hours': work_hours.total_seconds()/60/60,
        'project_work_hours': project_work_hours
    }

def auto_gen_logs(current_datetime, home_path):
    # Run resolve's CaptureLogs app
    subprocess.run(['open', '/Library/Application Support/Blackmagic Design/DaVinci Resolve/CaptureLogs.app'])

    # Exit out of CaptureLogs - Wait a second and press "enter" using pyautogui
    pyautogui.PAUSE = 1.0
    pyautogui.press('enter')
    pyautogui.press('enter')

def process_logs(home_path, current_datetime, txt_filepath, zip_file_pattern, accuracy="medium"):
    """
    Function to unzip the newly generated log file, save new log entries into master log, and collect info. RETURNS all the info, along with the zip filepath for deletion
    """
    # Unzip that zip file with a margin of error in the filename (up to the minute in the timestamp)
    # Use a glob pattern to find the file
    matching_files = glob.glob(zip_file_pattern)

    if matching_files:
        zip_filepath = matching_files[0]
        subprocess.run(['open', zip_filepath])
    else:
        print("No matching log file found.")

    # Get reference to the unzipped folder containing log files
    log_folder_filepath = f"{home_path}/Desktop/Library/Application Support/Blackmagic Design/DaVinci Resolve/logs"

    threading.Event().wait(3)

    log_filepaths = get_log_filepaths(log_folder_filepath)  # get reference to log_filepaths, a list of filepaths

    # Add our new resolve time log to log_filepaths, at the end of the list
    log_filepaths.append(txt_filepath)

    entries = collect_entries(log_filepaths, txt_filepath)
    info = entries_info(entries)
    # collect monthly save entries and get save entries info from each month, build summary from info and monthly info
    monthly_entries = sort_monthly(entries)
    months = monthly_entries.keys()
    monthly_info = {}
    for month in months:
        if month not in monthly_info:
            monthly_info[month] = entries_info(monthly_entries[month])

    return {
        "info":info,
        "monthly_info":monthly_info,
        "zip_filepath":zip_filepath,
    }

def get_entries_monthly_info(entries_monthly):
    """
    Function to get info from each month's log entries.
    Returns a dictionary containing each month's info (also a dict)
    """
    entries_months = entries_monthly.keys()
    entries_monthly_info = {}
    for month in entries_months:
        if month not in entries_monthly_info:
            entries_monthly_info[month] = entries_info(entries_monthly[month])
    return entries_monthly_info
