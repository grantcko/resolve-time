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
    """
    # TODO:

    # get reference to empty list for collecting save entries
    # read log file at given file path
    # for every line that includes "Started saving project *" append dictionary to save entry list with:
        # datetime: date time str that matches this format "2024-06-25 10:11:22,128"
        # project_name: project name on that same line, listed right after "Started saving project"
    # collect the dates and the project titles in a dict
        # example:
    # append to the list

    return []

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
