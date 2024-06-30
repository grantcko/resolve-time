import pytest
from app import get_log_filepaths, build_summary, collect_save_entries, validate_entry_format, count_work_sessions, calculate_total_time, calculate_time_per_project

# test method to build summary
class TestSummary:

    def setup_method(self):
        # Setup code to initialize necessary variables or state
        self.log_file_path = 'test_logs/davinci_resolve.log'
        self.save_entries = collect_save_entries(self.log_file_path)

    def test_build_summary(self):
        work_sessions = count_work_sessions(self.save_entries)
        total_time = calculate_total_time(self.save_entries)
        projects_worked = build_summary(work_sessions, total_time)

        assert type(projects_worked) is list, "projects_worked is not a list"
        assert len(projects_worked) > 0, "projects_worked list is empty"

        for project in projects_worked:
            assert type(project) is dict, "project in projects_worked is not a dict"
            assert type(project["project_name"]) is str, "project_name in project is not a str"
            assert type(project["work_days_total"]) is int, "work_days in project is not an int"
            assert type(project["work_sessions_total"]) is int, "work_sessions in project is not an int"
            assert type(project["work_hours_total"]) is int, "work_hours in project is not an int"

class TestLogPaths:

    # test method to collect log filepaths
    def test_get_log_paths_function(self):
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
        self.log_file_path = 'test_logs/davinci_resolve.log'
        self.save_entries = collect_save_entries(self.log_file_path)
        self.example_project_name = "treehouse-doc_1"

    # test if save entries are actually collected and stored correctly

    def test_save_entries(self):
        assert type(self.save_entries) is list, "self.save_entries is not a list"
        assert len(self.save_entries) > 0, "self.save_entries list is empty"
        for entry in self.save_entries:
            assert type(entry) is dict, "Entry is not a dict"
            assert 'timestamp' in entry, "Entry does not have a timestamp"
            assert 'project_title' in entry, "Entry does not have a project_title"

    # test function to ensure the proper formatting of the save entries

    def test_validate_entry_format_function(self):
        assert len(self.save_entries) > 0, "self.save_entries list is empty"
        for entry in self.save_entries:
            assert not validate_entry_format("onExecutor | INFO  | 2024"), "Entry format is invalid"
            assert isinstance(validate_entry_format(entry), bool), "Entry format is not boolean"
            assert validate_entry_format(entry), "Entry format is invalid"
            assert not validate_entry_format("Start saving project treehouse-doc_1"), "Entry format is invalid, missing date"
            assert not validate_entry_format("2024-04-10 20:35:07,604"), "Entry format is invalid missing title"

    # test if timestamps are in chronological order

    def test_timestamps_chronological_order(self):
        timestamps = [entry['timestamp'] for entry in self.save_entries]
        assert len(timestamps) > 0, "timestamps should be greater than 0"
        assert timestamps == sorted(timestamps), "Entries are not in chronological order"
        assert not timestamps == sorted(timestamps, reverse=True), "Entries are not in chronological order"

    # test function to count total number of work sessions

    def test_count_work_sessions_fuction(self):
        session_count = count_work_sessions(self.save_entries)
        assert type(session_count) is int, "Session count is not an integer"
        assert session_count > 0, "Session count should be greater than 0"

    # test function to calculate the total time spent across all projects

    def test_calculate_total_time_function(self):
        total_time = calculate_total_time(self.save_entries)
        assert type(total_time) is int, "Total time is not an integer"
        assert total_time > 0, "Total time should be greater than 0"

    # test function to calculate time spent per project

    def test_calculate_time_per_project_function(self):
        project_name = self.example_project_name
        total_time = calculate_time_per_project(self.save_entries, project_name)
        assert isinstance(total_time, float), "calculate_time_per_project does not return a float"
        assert total_time > 0, "total time should be larger than 0"


