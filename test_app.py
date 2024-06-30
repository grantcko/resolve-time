import unittest
from app import get_log_filepaths, build_summary, collect_save_entries, validate_entry_format, count_work_sessions, calculate_total_time, calculate_time_per_project

# test method to build summary
class SummaryTestCase(unittest.TestCase):

    def setUp(self):
        # Setup code to initialize necessary variables or state
        self.log_file_path = 'test-logs/davinci_resolve.log'
        self.save_entries = collect_save_entries(self.log_file_path)

    def test_build_summary(self):
        work_sessions = count_work_sessions(self.save_entries)
        total_time = calculate_total_time(self.save_entries)
        projects_worked = build_summary(work_sessions, total_time)

        self.assertTrue(type(projects_worked) is list, "projects_worked is not a list")
        self.assertTrue(len(projects_worked) > 0, "projects_worked list is empty")

        for project in projects_worked:
            self.assertTrue(type(project) is dict, "project in projects_worked is not a dict")
            self.assertTrue(type(project["project_name"]) is str, "project_name in project is not a str")
            self.assertTrue(type(project["work_days_total"]) is int, "work_days in project is not an int")
            self.assertTrue(type(project["work_sessions_total"]) is int, "work_sessions in project is not an int")
            self.assertTrue(type(project["work_hours_total"]) is int, "work_hours in project is not an int")

class LogPathsTestCase(unittest.TestCase):

    # test method to collect log filepaths
    def test_get_log_paths_function(self):
        log_folder_filepath = "./test-logs"
        log_filepaths = get_log_filepaths(log_folder_filepath)
        self.assertTrue(type(log_filepaths) is list, "log_filepaths is not a list")
        self.assertTrue(len(log_filepaths) > 0, "log_filepaths list is empty")
        for log_filepath in log_filepaths:
            self.assertTrue(type(log_filepath) is str, "log_filepath is not a string")

class LogTestCase(unittest.TestCase):

    # get references to first log's filepath and save entries from that filepath

    def setUp(self):
        # Setup code to initialize necessary variables or state
        self.log_file_path = 'test-logs/davinci_resolve.log'
        self.save_entries = collect_save_entries(self.log_file_path)
        self.example_project_name = "treehouse-doc_1"

    # test if save entries are actually collected and stored correctly

    def test_save_entries(self):
        self.assertTrue(type(self.save_entries) is list, "self.save_entries is not a list")
        self.assertTrue(len(self.save_entries) > 0, "self.save_entries list is empty")
        for entry in self.save_entries:
            self.assertTrue(type(entry) is dict, "Entry is not a dict")
            self.assertIn('timestamp', entry, "Entry does not have a timestamp")
            self.assertIn('project_title', entry, "Entry does not have a project_title")

    # test function to ensure the proper formatting of the save entries

    def test_validate_entry_format_function(self):
        self.assertTrue(len(self.save_entries) > 0, "self.save_entries list is empty")
        for entry in self.save_entries:
            self.assertFalse(validate_entry_format("onExecutor | INFO  | 2024"), "Entry format is invalid")
            self.assertIsInstance(validate_entry_format(entry), bool, "Entry format is not boolean")
            self.assertTrue(validate_entry_format(entry), "Entry format is invalid")
            self.assertFalse(validate_entry_format("Start saving project treehouse-doc_1"), "Entry format is invalid, missing date")
            self.assertFalse(validate_entry_format("2024-04-10 20:35:07,604"), "Entry format is invalid missing title")

    # test if timestamps are in chronological order

    def test_timestamps_chronological_order(self):
        timestamps = [entry['timestamp'] for entry in self.save_entries]
        self.assertTrue(len(timestamps) > 0, "timestamps should be greater than 0")
        self.assertTrue(timestamps == sorted(timestamps), "Entries are not in chronological order")
        self.assertFalse(timestamps == sorted(timestamps, reverse=True), "Entries are not in chronological order")

    # test function to count total number of work sessions

    def test_count_work_sessions_fuction(self):
        session_count = count_work_sessions(self.save_entries)
        self.assertTrue(type(session_count) is int, "Session count is not an integer")
        self.assertTrue(session_count > 0, "Session count should be greater than 0")

    # test function to calculate the total time spent across all projects

    def test_calculate_total_time_function(self):
        total_time = calculate_total_time(self.save_entries)
        self.assertTrue(type(total_time) is int, "Total time is not an integer")
        self.assertTrue(total_time > 0, "Total time should be greater than 0")

    # test function to calculate time spent per project

    def test_calculate_time_per_project_function(self):
        project_name = self.example_project_name
        total_time = calculate_time_per_project(self.save_entries, project_name)
        self.assertIsInstance(total_time, float, "calculate_time_per_project does not return a float")
        self.assertTrue(total_time > 0, "total time should be larger than 0")

if __name__ == '__main__':
    unittest.main()
