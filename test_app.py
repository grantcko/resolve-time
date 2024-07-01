import pytest
from app import get_log_filepaths, build_summary, collect_save_entries, save_entries_info

# test method to build summary
class TestSummaryFunction:

    def setup_method(self):
        # Setup code to initialize necessary variables or state
        self.log_folder_filepath = './test_logs'
        self.save_entries = collect_save_entries(self.log_folder_filepath)

    def test_build_summary(self):
        info = save_entries_info(self.save_entries)
        assert type(build_summary(info)) is str

class TestLogPaths:

    # test funciton to collect log filepaths

    def test_get_log_filepaths_function(self):
        log_folder_filepath = "./test_logs"
        log_filepaths = get_log_filepaths(log_folder_filepath)
        assert type(log_filepaths) is list, "log_filepaths is not a list"
        assert len(log_filepaths) > 0, "log_filepaths list is empty"
        for log_filepath in log_filepaths:
            assert type(log_filepath) is str, "log_filepath is not a string"

class TestLog:

    # get references to first log's filepath and save entries from that filepath

    def setup_method(self):
        # Setup code to initialize necessary variables or state
        self.log_filepaths = get_log_filepaths('./test_logs')
        self.save_entries = collect_save_entries(self.log_filepaths)

    # test if save entries are actually collected and stored correctly

    def test_save_entries(self):
        assert type(self.save_entries) is list, "self.save_entries is not a list"
        assert len(self.save_entries) > 0, "self.save_entries should be greater than 0"
        assert len(self.save_entries) == 886, "self.save_entries should have 886 entries"
        for entry in self.save_entries:
            assert type(entry) is dict, "Entry is not a dict"
            assert 'timestamp' in entry, "Entry does not have a timestamp"
            assert 'project_title' in entry, "Entry does not have a project_title"

    # test if timestamps are in chronological order

    def test_timestamps_chronological_order(self):
        timestamps = [entry['timestamp'] for entry in self.save_entries]
        assert len(timestamps) > 0, "timestamps should be greater than 0"
        assert timestamps == sorted(timestamps), "Entries are not in chronological order"
        assert not timestamps == sorted(timestamps, reverse=True), "Entries are not in chronological order"

class TestSaveEntriesInfoFunction:

    # get references

    def setup_method(self):
        # Setup code to initialize necessary variables or state
        self.log_folder_filepath = './test_logs'
        self.save_entries = collect_save_entries(self.log_folder_filepath)

    # test if save_entries_info method returns work sessions count

    def test_work_sessions_count(self):
        session_count = save_entries_info(self.save_entries)['session_count']
        assert type(session_count) is int, "Session count is not an integer"
        assert session_count > 0, "Session count should be greater than 0"
        assert session_count == 2, "Session count should be 275"

    # test if save_entries_info method returns work hours

    def test_work_hours(self):
        work_hours = save_entries_info(self.save_entries)['work_hours']
        assert type(work_hours) is float, "Work hours is not an float"
        assert work_hours > 0, "Work hours should be greater than 0"
        assert work_hours == 2.3089347222222227, "Work hours should be 2.3089347222222227"        

    # test if save_entries_info method returns project hours

    def test_project_hours(self):
        project_hours = save_entries_info(self.save_entries)['project_work_hours']
        assert type(project_hours) is dict, "project_work_hours is not an dict"
