# Import exernal modules

from datetime import datetime
import glob
import os
import pytest
import sys
import subprocess
import time

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
sys.path.append(os.path.abspath('tests'))
import vary_defs

#### Definitions

log_filepaths = get_log_filepaths("tests/test_logs")
home_path = os.environ["HOME"]
masterlog_file = vary_defs.masterlog()

# Medium accuracy entry processing - aka by save entries

save_entries = collect_entries(log_filepaths, masterlog_file, accuracy="medium")
save_entries_info = entries_info(save_entries)
save_entries_monthly = sort_monthly(save_entries)
save_entries_monthly_info = get_entries_monthly_info(save_entries_monthly)

medium = {
    "entries": save_entries,
    "entries_info": save_entries_info,
    "entries_monthly": save_entries_monthly,
    "monthly_info": save_entries_monthly_info,
}

# High accuracy - aka by seconds

sec_entries = collect_entries(log_filepaths, masterlog_file, accuracy="high")
sec_entries_info = entries_info(sec_entries)
sec_entries_monthly = sort_monthly(sec_entries)
sec_entries_monthly_info = get_entries_monthly_info(sec_entries_monthly)

high = {
    "entries": sec_entries,
    "entries_info": sec_entries_info,
    "entries_monthly": sec_entries_monthly,
    "monthly_info": sec_entries_monthly_info,
}


class TestSummaries:

    def test_build_summary(self):
        summary = build_summary(medium["entries_info"], medium["monthly_info"])

        # Check that the summary includes correct project names

        # Check that the summary includes correct hours

        # Check that the summary includes correct dates

        # Check that the summary includes correct session count and work hours

    def test_build_summary_exact(self): #TODO:
        summary = build_summary(high["entries_info"], medium["monthly_info"])
        # assert that summary includes correct project names
        # assert that summary includes correct hours
        # assert that summary includes correct dates
        # assert that summary includes correct heatmap
        # assert that summary includes today summary

class TestLogPathsFunction:

    # test funciton to collect log filepaths

    def test_get_log_filepaths_function(self):
        assert type(log_filepaths) is list, "log_filepaths is not a list"
        assert len(log_filepaths) > 0, "log_filepaths list is empty"
        for log_filepath in log_filepaths:
            assert type(log_filepath) is str, "log_filepath is not a string"

class TestCollectedSaveEntries:

    # test if save entries are actually collected and stored correctly

    # set up a fixture to define which entries are being tested (save entries)
    @pytest.fixture
    def entries(self):
        return medium["entries"]

    def test_entries(self, entries):
        assert type(entries) is list, "entries is not a list"
        assert len(entries) > 0, "entries should be greater than 0"
        assert len(entries) == 886, "entries should have 886 entries"
        for entry in entries:
            assert type(entry) is dict, "Entry is not a dict"
            assert 'timestamp' in entry, "Entry does not have a timestamp"
            assert 'project_title' in entry, "Entry does not have a project_title"

    # test if timestamps are in chronological order
    def test_timestamps_chronological_order(self, entries):
        timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S,%f') for entry in entries]
        assert len(timestamps) > 0, "timestamps should be greater than 0"
        assert timestamps == sorted(timestamps), "Entries are not in chronological order"
        assert not timestamps == sorted(timestamps, reverse=True), "Entries are not in chronological order"

class TestCollectedSecEntries:

    # test if save entries are actually collected and stored correctly

    # set up a fixture to define which entries are being tested (save entries)
    @pytest.fixture
    def entries(self):
        return high["entries"]

    def test_entries(self, entries):
        assert type(entries) is list, "entries is not a list"
        assert len(entries) > 0, "entries should be greater than 0"
        assert len(entries) == 1000, "entries should have ??? entries" #TODO
        for entry in entries:
            assert type(entry) is dict, "Entry is not a dict"
            assert 'timestamp' in entry, "Entry does not have a timestamp"
            assert 'project_title' in entry, "Entry does not have a project_title"

    # test if timestamps are in chronological order
    def test_timestamps_chronological_order(self, entries):
        timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S,%f') for entry in entries]
        assert len(timestamps) > 0, "timestamps should be greater than 0"
        assert timestamps == sorted(timestamps), "Entries are not in chronological order"
        assert not timestamps == sorted(timestamps, reverse=True), "Entries are not in chronological order"

class TestSaveEntriesInfo:

    # test info generated from save entries

    # set up a fixture to define which info is being tested (save entries info)
    @pytest.fixture
    def info(self):
        return medium["entries_info"]

    def test_work_sessions_count(self, info):
        session_count = info['session_count']
        assert type(session_count) is int, "Session count is not an integer"
        assert session_count > 0, "Session count should be greater than 0"
        assert session_count == 100, "Session count should be ???" #TODO

    # test if entries_info method returns work hours

    def test_work_hours(self, info):
        work_hours = info['work_hours']
        assert type(work_hours) is float, "Work hours is not an float"
        assert work_hours > 0, "Work hours should be greater than 0"
        assert work_hours == 8.469408611111112, "Work hours should be ???" #TODO

    def test_project_work_hours(self, info):
        project_hours = info['project_work_hours']
        assert type(project_hours) is dict, "project_work_hours is not a dict"
        assert len(project_hours) > 0, "project_work_hours should not be an empty dict"
        for project, hours in project_hours.items():
            assert type(hours) is float, f"Work hours for project {project} is not a float"
            assert hours > 0, f"Work hours for project {project} should be greater than 0"

class TestSecEntriesInfo:
    # test info generated from save entries

    # set up a fixture to define which info is being tested (save entries info)
    @pytest.fixture
    def info(self):
        return high["entries_info"]

    def test_work_sessions_count(self, info):
        session_count = info['session_count']
        assert type(session_count) is int, "Session count is not an integer"
        assert session_count > 0, "Session count should be greater than 0"
        assert session_count == 100, "Session count should be ???" #TODO

    # test if entries_info method returns work hours

    def test_work_hours(self, info):
        work_hours = info['work_hours']
        assert type(work_hours) is float, "Work hours is not an float"
        assert work_hours > 0, "Work hours should be greater than 0"
        assert work_hours == 8.469408611111112, "Work hours should be ???" #TODO

    def test_project_work_hours(self, info):
        project_hours = info['project_work_hours']
        assert type(project_hours) is dict, "project_work_hours is not a dict"
        assert len(project_hours) > 0, "project_work_hours should not be an empty dict"
        for project, hours in project_hours.items():
            assert type(hours) is float, f"Work hours for project {project} is not a float"
            assert hours > 0, f"Work hours for project {project} should be greater than 0"

class TestAutoLogGeneration:
    def test_auto_gen_logs_function(self):
        # Get a reference to the date and time
        current_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")
        # get reference to $HOME environmental variable
        # Genereate the log files
        auto_gen_logs(current_datetime, home_path)
        # Define desired path for log files to end up
        path = os.path.join(os.path.expanduser("~"), "Desktop")
        # Collect all the log file filepaths in that folder
        log_files = [f for f in os.listdir(path) if f.startswith("DaVinci-Resolve-logs-")]

        assert len(log_files) > 0, "No log files found on the desktop."

        # Check if any of the log files were created in the last few minutes
        recent_file_found = False
        for log_file in log_files:
            file_path = os.path.join(path, log_file)
            creation_time = os.path.getctime(file_path)
            if (datetime.now() - datetime.fromtimestamp(creation_time)).total_seconds() < 300:  # 5 minutes
                recent_file_found = True
                break

        assert recent_file_found, "No RENCENT log file found on the desktop."

        time.sleep(1.0)
        # Remove the generated zip file
        subprocess.run(['rm', '-rf', glob.glob(f"{home_path}/Desktop/DaVinci-Resolve-logs-{current_datetime[:11]}*.tgz")[0]])
        # log_files = [f for f in os.listdir(path) if f.startswith("DaVinci-Resolve-logs-")]
        # assert len(log_files) == 0, "log files found on the desktop."

@pytest.fixture
def log_files_setup_teardown():
    # Setup: Generate log files
    current_datetime = datetime.strptime("20240917-185013", "%Y%m%d-%H%M%S")
    zip_file_pattern = f"{home_path}/Desktop/DaVinci-Resolve-logs-{current_datetime[:11]}*.tgz"
    auto_gen_logs(current_datetime, home_path)

    yield current_datetime, zip_file_pattern

    # Teardown: Remove generated files
    subprocess.run(['rm', '-rf', glob.glob(zip_file_pattern)[0]])
    subprocess.run(['rm', '-rf', f"{home_path}/Desktop/Library"])

class TestLogProcessing:
    def test_process_logs_function_mid(self, log_files_setup_teardown):
        current_datetime, zip_file_pattern = log_files_setup_teardown
        processed = process_logs(home_path, current_datetime, masterlog_file, zip_file_pattern, accuracy="medium")

        # testing info...
        assert isinstance(processed["info"], dict), "processed info should be a dictionary"
        assert len(processed["info"]) > 0, "info should not be empty"
        assert processed["info"] == "whatever", "monthly info should be ???"
        # testing monthly info...
        assert isinstance(processed["monthly_info"], dict), "processed monthly_info should be a dictionary"
        assert len(processed["monthly_info"]) > 0, "Monthly info should not be empty"
        assert processed["monthly_info"] == "whatever", "monthly info should be ???"
        # testing zip filepath...
        assert isinstance(processed["zip_filepath"], str), "Zip filepath should be a string"

    def test_process_logs_function_high(self, log_files_setup_teardown):
        current_datetime, zip_file_pattern = log_files_setup_teardown
        processed = process_logs(home_path, current_datetime, masterlog_file, zip_file_pattern, accuracy="high")

        # testing info...
        assert isinstance(processed["info"], dict), "processed info should be a dictionary"
        assert len(processed["info"]) > 0, "info should not be empty"
        assert processed["info"] == "whatever", "monthly info should be ???"
        # testing monthly info...
        assert isinstance(processed["monthly_info"], dict), "processed monthly_info should be a dictionary"
        assert len(processed["monthly_info"]) > 0, "Monthly info should not be empty"
        # testing zip filepath
        assert isinstance(processed["zip_filepath"], str), "Zip filepath should be a string"
        assert processed["monthly_info"] == "whatever", "monthly info should be ???"
