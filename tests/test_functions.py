# Import exernal modules

from datetime import datetime
import os
import pytest
import sys

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

log_filepaths = get_log_filepaths("tests/test_logs")

# Medium accuracy entry processing - aka by save entries

save_entries = collect_entries(log_filepaths, accuracy="medium")
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

sec_entries = collect_entries(log_filepaths, accuracy="high")
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

    def test_build_summary(self): #TODO:
        return
        # assert that summary includes correct project names
        # assert that summary includes correct hours
        # assert that summary includes correct dates
        # assert that summary includes correct heatmap
        # assert that summary includes today summary

    def test_build_summary_exact(self): #TODO:
        return
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
        # assert that file on the desktop created in the last few minutes starting with "DaVinci-Resolve-logs-" exists

class TestLogProcessing:
    def test_process_logs_function(self): #TODO:
        return
