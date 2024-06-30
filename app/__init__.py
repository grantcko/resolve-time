from datetime import datetime
import glob
import os
import re

def get_log_filepaths(log_folder_filepath):

    """
    Function to get all log file paths in the given directory.
    """

    # Define the pattern for the log files
    log_filepath_pattern = "test_logs/davinci_resolve.log*"

    # Collect all matching file paths
    log_file_paths = glob.glob(log_filepath_pattern)

    # Return the list of log file paths
    return log_file_paths

def build_summary(work_sessions, total_time):
    """
    Function to build a summary of projects worked on.
    """
    # TODO:
    return []

def collect_save_entries(log_file_path):
    """
    Function to collect log entries from a file.
    
    Args:
    log_file_path (str): Path to the log file.
    
    Returns:
    list: A list of dictionaries containing 'datetime' and 'project_name' from the log entries.
    """
    save_entries = []

    # Regular expression to match the log line
    log_pattern = re.compile(r"^\S+\s+\|\s+SyManager\.ProjectManager\s+\|\s+INFO\s+\|\s+(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})\s+\|\s+Start saving project (?P<project_name>.+)$")
    
    try:
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                match = log_pattern.match(line)
                if match:
                    save_entry = {
                        'timestamp': match.group('timestamp'),
                        'project_name': match.group('project_name')
                    }
                    save_entries.append(save_entry)
    except FileNotFoundError:
        print(f"The file {log_file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return save_entries

def validate_entry_format(save_entry):
    """
    Function to validate the format of a save entry.
    """
    # TODO:
    return False

def count_work_sessions(save_entries):
    """
    Function to count the number of work sessions from save entries.
    """
    # TODO:
    return 0

def calculate_total_time(save_entries):
    """
    Function to calculate total time worked from save entries.
    """
    # TODO:
    return 0

def calculate_time_per_project(save_entries, project_name):
    """
    Funtion to calculate time worked per project from save entries.
    """
    # Place holder for actual logic
    return 0.0
