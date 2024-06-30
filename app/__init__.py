import os
import re
from datetime import datetime

def get_log_filepaths(log_folder_filepath):
    # TODO:

    """
    Function to get all log file paths in the given directory.
    """

    # collect all the folder's filepaths where they match a specific format
    # filepath is "test-logs/davinci_resolve.log" or "test-logs/davinci_resolve.log.[int]"

    log_file_paths = []
    log_file_paths.append()

    # check to see if each one is a log file and kick it out if not

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
