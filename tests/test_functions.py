# Import exernal modules

from datetime import datetime
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

# calculated stats from test logs
with open('tests/calculated_stats/blankmstr_medac.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)
    blankmstr_total_entries = int(rows[9][1])  # Row 10, column 2 (0-indexed)

# Medium accuracy entry processing - aka by save entries

save_entries = collect_entries(log_filepaths, masterlog_file_blank, accuracy="medium")
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

sec_entries = collect_entries(log_filepaths, masterlog_file_blank, accuracy="high")
sec_entries_info = entries_info(sec_entries)
sec_entries_monthly = sort_monthly(sec_entries)
sec_entries_monthly_info = get_entries_monthly_info(sec_entries_monthly)

high = {
    "entries": sec_entries,
    "entries_info": sec_entries_info,
    "entries_monthly": sec_entries_monthly,
    "monthly_info": sec_entries_monthly_info,
}

@pytest.fixture
def summary_setup_teardown():
    yield
    # reset master logs to their initial state
    with open(masterlog_file_blank, 'w') as masterlog_file:
        masterlog_file.truncate(0)
    with open(masterlog_file_missing, 'w') as masterlog_file:
        masterlog_file.truncate(0)
    collect_entries(log_filepaths_missing, masterlog_file_missing, accuracy="medium")
    with open(masterlog_file_overlap, 'w') as masterlog_file:
        masterlog_file.truncate(0)
    collect_entries(log_filepaths_overlap, masterlog_file_overlap, accuracy="medium")
    # Remove the unzipped log folder
    subprocess.run(['rm', '-rf', "tests/zipped-logs/Library*"])

class TestSummariesMediumAccuracy:#
    def test_with_blank_masterlog(self, summary_setup_teardown):
        processed = process_logs(home_path, test_current_datetime, masterlog_file_blank, test_zip_file_pattern, log_folder_filepath=test_log_folder_filepath, accuracy="medium")
        summary = build_summary(processed["info"], processed["monthly_info"])
        assert summary == "TODO", f"summary should be ???"

        # assert that summary includes correct project names
        # assert that summary includes correct hours
        # assert that summary includes correct dates
        # assert that summary includes correct heatmap
        # assert that summary includes today summary
        # assert that summary includes correct session count and work hours

    def test_with_missing_entries_masterlog(self, summary_setup_teardown):
        processed = process_logs(home_path, test_current_datetime, masterlog_file_missing, test_zip_file_pattern, log_folder_filepath=test_log_folder_filepath, accuracy="medium")
        summary = build_summary(processed["info"], processed["monthly_info"])
        assert summary == "TODO", f"summary should be ???"
        # assert that summary includes correct project names
        # assert that summary includes correct hours
        # assert that summary includes correct dates
        # assert that summary includes correct heatmap
        # assert that summary includes today summary
        # assert that summary includes correct session count and work hours

    def test_with_overlapping_masterlog(self, summary_setup_teardown):
        processed = process_logs(home_path, test_current_datetime, masterlog_file_overlap, test_zip_file_pattern, log_folder_filepath=test_log_folder_filepath, accuracy="medium")
        summary = build_summary(processed["info"], processed["monthly_info"])
        assert summary == "TODO", f"summary should be ???"
        # assert that summary includes correct project names
        # assert that summary includes correct hours
        # assert that summary includes correct dates
        # assert that summary includes correct heatmap
        # assert that summary includes today summary
        # assert that summary includes correct session count and work hours


@pytest.fixture
def summary_setup_teardown():
    yield
    # reset master logs to their initial state
    with open(masterlog_file_blank, 'w') as masterlog_file:
        masterlog_file.truncate(0)
    with open(masterlog_file_missing, 'w') as masterlog_file:
        masterlog_file.truncate(0)
    collect_entries(log_filepaths_missing, masterlog_file_missing, accuracy="high")
    with open(masterlog_file_overlap, 'w') as masterlog_file:
        masterlog_file.truncate(0)
    collect_entries(log_filepaths_overlap, masterlog_file_overlap, accuracy="high")
    # Remove the unzipped log folder
    subprocess.run(['rm', '-rf', "tests/zipped-logs/Library"])

# class TestSummariesHighAccuracy:
#     def test_with_blank_masterlog(self):
#         summary = build_summary(high["entries_info"], high["monthly_info"])
#         assert summary == "TODO", f"summary should be ???"
#         # assert that summary includes correct project names
#         # assert that summary includes correct hours
#         # assert that summary includes correct dates
#         # assert that summary includes correct heatmap
#         # assert that summary includes today summary
#         # assert that summary includes correct session count and work hours

#     def test_with_missing_entries_masterlog(self):
#         summary = build_summary(high["entries_info"], high["monthly_info"])
#         assert summary == "TODO", f"summary should be ???"
#         # assert that summary includes correct project names
#         # assert that summary includes correct hours
#         # assert that summary includes correct dates
#         # assert that summary includes correct heatmap
#         # assert that summary includes today summary
#         # assert that summary includes correct session count and work hours

#     def test_with_overlapping_masterlog(self):
#         summary = build_summary(high["entries_info"], high["monthly_info"])
#         assert summary == "TODO", f"summary should be ???"
#         # assert that summary includes correct project names
#         # assert that summary includes correct hours
#         # assert that summary includes correct dates
#         # assert that summary includes correct heatmap
#         # assert that summary includes today summary
#         # assert that summary includes correct session count and work hours

class TestLogPathsFunction:

    # test funciton to collect log filepaths

    def test_get_log_filepaths_function(self):
        assert type(log_filepaths) is list, "log_filepaths is not a list"
        assert len(log_filepaths) > 0, "log_filepaths list is empty"
        for log_filepath in log_filepaths:
            assert type(log_filepath) is str, "log_filepath is not a string"

class TestCollectedMediumAcEntries:#

    # test if save entries are actually collected and stored correctly

    # set up a fixture to define which entries are being tested (save entries)
    @pytest.fixture
    def entries(self):
        return medium["entries"]

    def test_entries(self, entries):
        assert type(entries) is list, "entries is not a list"
        assert len(entries) > 0, "entries should be greater than 0"
        assert len(entries) == blankmstr_total_entries, f"entries should have {blankmstr_total_entries} entries"
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

# class TestCollectedHighAcEntries:#

#     # test if save entries are actually collected and stored correctly

#     # set up a fixture to define which entries are being tested (save entries)
#     @pytest.fixture
#     def entries(self):
#         return high["entries"]

#     def test_entries(self, entries):
#         assert type(entries) is list, "entries is not a list"
#         assert len(entries) > 0, "entries should be greater than 0"
#         assert len(entries) == 1000, "entries should have ??? entries" #TODO
#         for entry in entries:
#             assert type(entry) is dict, "Entry is not a dict"
#             assert 'timestamp' in entry, "Entry does not have a timestamp"
#             assert 'project_title' in entry, "Entry does not have a project_title"

#     # test if timestamps are in chronological order
#     def test_timestamps_chronological_order(self, entries):
#         timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S,%f') for entry in entries]
#         assert len(timestamps) > 0, "timestamps should be greater than 0"
#         assert timestamps == sorted(timestamps), "Entries are not in chronological order"
#         assert not timestamps == sorted(timestamps, reverse=True), "Entries are not in chronological order"

class TestMediumAcStats:#

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

# class TestHighAcStats:#
#     # test info generated from save entries

#     # set up a fixture to define which info is being tested (save entries info)
#     @pytest.fixture
#     def info(self):
#         return high["entries_info"]

#     def test_work_sessions_count(self, info):
#         session_count = info['session_count']
#         assert type(session_count) is int, "Session count is not an integer"
#         assert session_count > 0, "Session count should be greater than 0"
#         assert session_count == 100, "Session count should be ???" #TODO

#     # test if entries_info method returns work hours

#     def test_work_hours(self, info):
#         work_hours = info['work_hours']
#         assert type(work_hours) is float, "Work hours is not an float"
#         assert work_hours > 0, "Work hours should be greater than 0"
#         assert work_hours == 8.469408611111112, "Work hours should be ???" #TODO

#     def test_project_work_hours(self, info):
#         project_hours = info['project_work_hours']
#         assert type(project_hours) is dict, "project_work_hours is not a dict"
#         assert len(project_hours) > 0, "project_work_hours should not be an empty dict"
#         for project, hours in project_hours.items():
#             assert type(hours) is float, f"Work hours for project {project} is not a float"
#             assert hours > 0, f"Work hours for project {project} should be greater than 0"

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
    yield
    # clear masterlog file
    # with open(masterlog_file_blank, 'w') as masterlog_file:
    #     masterlog_file.truncate(0)
    subprocess.run(['rm', '-rf', "tests/zipped-logs/Library"])

class TestLogProcessing:#
    def test_process_logs_function_mediumac(self, log_files_setup_teardown):
        processed = process_logs(home_path, test_current_datetime, masterlog_file_blank, test_zip_file_pattern, accuracy="medium")

        # testing info...
        assert isinstance(processed["info"], dict), "processed info should be a dictionary"
        assert len(processed["info"]) > 0, "info should not be empty"
        assert processed["info"] == "TODO", "monthly info should be ???"
        # testing monthly info...
        assert isinstance(processed["monthly_info"], dict), "processed monthly_info should be a dictionary"
        assert len(processed["monthly_info"]) > 0, "Monthly info should not be empty"
        assert processed["monthly_info"] == "TODO", "monthly info should be ???"
        # testing zip filepath...
        assert isinstance(processed["zip_filepath"], str), "Zip filepath should be a string"

    def test_process_logs_function_highac(self, log_files_setup_teardown):
        processed = process_logs(home_path, test_current_datetime, masterlog_file_blank, test_zip_file_pattern, accuracy="high")

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
