from datetime import datetime, time, timedelta
import glob
import os
import re

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

                        # TODO:
                        # Make a txt file at the application support directory
                        txt_file_path = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/resolve-time-log.txt"
                        if not os.path.exists(txt_file_path):
                            with open(txt_file_path, 'w') as txt_file:
                                txt_file.write(line)
                        else:
                            with open(txt_file_path, 'r') as txt_file:
                                if line not in txt_file.read():
                                    with open(txt_file_path, 'a') as txt_file_append:
                                        txt_file_append.write(line)

        except FileNotFoundError:
            print(f"The file {log_file_path} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # return save_entries, a list of sorted dicts [{'timestamp':'...', 'project_title':'...'},{'...'}]

    return sorted(save_entries, key=lambda entry: datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S,%f'))

def collect_monthly_save_entries(all_entries):
    months_worked = {}
    # go through each entry
    for entry in all_entries:
        # get ref to mm_yyyy (ex:06_2024) unless it's a duplicate
        mm_yyyy = f"{datetime.strftime(datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S,%f'), '%m_%Y')}"
        # add key:value pair with key as 'mm/yyyy', and value as an empty list, if that month isn't already there
        if mm_yyyy not in months_worked:
            months_worked[mm_yyyy] = []
        # append current save entry to save_entries list pertaining to the month
        # print(months_worked)
        months_worked[mm_yyyy].append(entry)

    return months_worked
    # example :{'04/2024':[save entries], '05/2024':[save entries], '06/2024':[save entries]}

def save_entries_info(save_entries): # returns dict of total and per project summaries for: all time, per month
    """
    Function to get number of work sessions, total hours, hours per project from save entries.
    """

    # if there are no save entries, return an empty summary

    if not save_entries:
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

    for entry in save_entries:

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
