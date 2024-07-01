import pytest
import os
from datetime import datetime
from app import get_log_filepaths, build_summary, collect_save_entries, save_entries_info

# get references to log filepaths and save entries

log_filepaths = get_log_filepaths("./test_logs")
save_entries = collect_save_entries(log_filepaths)

class TestSummaryFunction:

    def test_build_summary(self):
        info = save_entries_info(save_entries)
        assert type(build_summary(info)) is str

class TestLogPaths:

    # test funciton to collect log filepaths

    def test_get_log_filepaths_function(self):
        assert type(log_filepaths) is list, "log_filepaths is not a list"
        assert len(log_filepaths) > 0, "log_filepaths list is empty"
        for log_filepath in log_filepaths:
            assert type(log_filepath) is str, "log_filepath is not a string"

class TestLog:

    # test if save entries are actually collected and stored correctly

    def test_save_entries(self):
        assert type(save_entries) is list, "save_entries is not a list"
        assert len(save_entries) > 0, "save_entries should be greater than 0"
        assert len(save_entries) == 886, "save_entries should have 886 entries"
        for entry in save_entries:
            assert type(entry) is dict, "Entry is not a dict"
            assert 'timestamp' in entry, "Entry does not have a timestamp"
            assert 'project_title' in entry, "Entry does not have a project_title"

    # test if timestamps are in chronological order

    def test_timestamps_chronological_order(self):
        timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S,%f') for entry in save_entries]
        # print(timestamps)
        # print("--------------------------------")
        # print(sorted(timestamps))
        assert len(timestamps) > 0, "timestamps should be greater than 0"
        assert timestamps == sorted(timestamps), "Entries are not in chronological order"
        assert not timestamps == sorted(timestamps, reverse=True), "Entries are not in chronological order"

class TestSaveEntriesInfoFunction:

    # test if save_entries_info method returns work sessions count

    def test_work_sessions_count(self):
        info = save_entries_info(save_entries)
        session_count = info['session_count']
        assert type(session_count) is int, "Session count is not an integer"
        assert session_count > 0, "Session count should be greater than 0"
        # TODO: assert session_count == , "Session count should be "

    # test if save_entries_info method returns work hours

    def test_work_hours(self):
        info = save_entries_info(save_entries)
        work_hours = info['work_hours']
        assert type(work_hours) is float, "Work hours is not an float"
        assert work_hours > 0, "Work hours should be greater than 0"
        assert work_hours == 8.469408611111112, "Work hours should be 8.469408611111112"        

    # test if save_entries_info method returns project hours

    def test_project_hours(self): # AIDER
        project_hours = save_entries_info(save_entries)['project_hours']
        assert type(project_hours) is dict, "project hours is not an dict"
        assert len(project_hours) == 1, "project_hours should have just 1 key value pair"
        # go over each project saved in project_hours (each key value pair)
            # make sure that the project hours are int and greater than 0
            
    # test if save_entries_info method returns project hours

    def test_project_hours(self):
        info = save_entries_info(save_entries)
        project_hours = info['project_work_hours']
        assert type(project_hours) is dict, "project_work_hours is not a dict"

