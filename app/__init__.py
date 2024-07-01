from datetime import datetime, time, timedelta
import glob
import os
import re

import sys

def get_log_filepaths(log_folder_filepath):

    """
    Function to get all log file paths in the given directory.
    """

    # Define the pattern for the log files
    log_filepath_pattern = f'{log_folder_filepath}/davinci_resolve.log*'

    # Collect all matching file paths
    log_file_paths = glob.glob(log_filepath_pattern)

    # Return the list of log file paths
    return log_file_paths

def build_summary(info):
    """
    Function to build a summary of projects worked on.
    """
    # TODO:

    return ""

def collect_save_entries(log_filepaths):
    """
    Function to collect log entries from a file.

    Args:
    log_file_path (str): Path to the log file.

    Returns:
    list: A list of dictionaries containing 'datetime' and 'project_name' from the log entries.
    """
    save_entries = []

    # Regular expression to match the log line

    log_pattern = re.compile(r"^\S+\s+\|\s+SyManager\.ProjectManager\s+\|\s+INFO\s+\|\s+(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})\s+\|\s+Start saving project (?P<project_title>.+)$")

    # collect timestamp and project title into into a save entry dict, into save entries list (for each filepath)

    for log_file_path in log_filepaths:
        try:
            with open(log_file_path, 'r') as log_file:
                for line in log_file:
                    match = log_pattern.match(line)
                    if match:
                        save_entry = {
                            'timestamp': match.group('timestamp'),
                            'project_title': match.group('project_title')
                        }
                        save_entries.append(save_entry)
        except FileNotFoundError:
            print(f"The file {log_file_path} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # return save entries, a list of dicts [{'timestamp':'...', 'project_title':'...'},{'...'}]
    
    # sort list save_entries based on the datetime pertaining to the timestamp value

    return sorted(save_entries, key=lambda entry: datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S,%f'))

def save_entries_info(save_entries):
    """
    Function to get number of work sessions, total hours, hours per project from save entries.
    """
    if not save_entries:
        return 0

    session_count = 1
    work_hours = timedelta(microseconds=0)
    compare_timestamp = None
    project_work_hours = {}
    
    current_project = None
    current_project_hours = timedelta(microseconds=0)

    for entry in save_entries:
        timestamp = datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S,%f')

        if compare_timestamp is None:
            compare_timestamp = timestamp
            continue

        time_difference_min = (timestamp - compare_timestamp).total_seconds() / 60.0

        if time_difference_min > 10:

            # IF AN EDIT SESSION ENDED

            session_count += 1
            compare_timestamp = timestamp
        else:

            # IF AN EDIT SESSION CONTINUED

            difference = timestamp - compare_timestamp
            work_hours += difference
            current_project_hours += difference
            compare_timestamp = timestamp

            # if current_project != project of the entry currently being iterated
                # add into project_work_hours - current_project:current hours
                # reset current project hours to 0 and 
                # set current project to project of the entry currently being iterated

    return {
        'session_count': session_count,
        'work_hours': work_hours.total_seconds()/60/60,
        'project_work_hours': project_work_hours
    }

# COMMAND LINE LOGIC

if len(sys.argv) < 2:
    print("Usage: python app/__init__.py <log_folder_filepath>")
    sys.exit(1)

log_folder_filepath = sys.argv[1]
log_filepaths = get_log_filepaths(log_folder_filepath)
save_entries = collect_save_entries(log_filepaths)
info = save_entries_info(save_entries)
print(info)
summary = build_summary(info)
print(summary)
