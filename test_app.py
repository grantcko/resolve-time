import unittest
from app import get_log_filepaths, build_summary, collect_save_entries, validate_entry_format, count_work_sessions, calculate_time_per_day, calculate_time_per_month, calculate_total_time, calculate_days_per_week, calculate_days_per_month, calculate_total_days, make_heatmap, calculate_session_lengths

# test method to build summary
class SummaryTestCase(unittest.TestCase):
    def test_build_summary(self):
        projects_worked = build_summary()
        self.assertTrue(type(projects_worked) is list, "projects_worked is not a list")
        # assert that projects worked is not an empty list
        self.assertTrue(len(projects_worked) > 0, "projects_worked list is empty")
        for project in projects_worked:
            self.assertTrue(type(project) is dict, "project in projects_worked is not a dict")
            self.assertTrue(type(project["project_name"]) is str, "project_name in project is not a str")
            self.assertTrue(type(project["work_days_total"]) is int, "work_days in project is not an int")
            self.assertTrue(type(project["work_sessions_total"]) is int, "work_sessions in project is not an int")
            self.assertTrue(type(project["work_hours_total"]) is int, "work_hours in project is not an int")

class LogPathsTestCase(unittest.TestCase):

    # test method to collect log filepaths
    def test_get_log_paths(self):
        log_folder_filepath = "./test-logs"
        log_filepaths = get_log_filepaths(log_folder_filepath)
        self.assertTrue(type(log_filepaths) is list, "log_filepaths is not a list")
        self.assertTrue(len(log_filepaths) > 0, "log_filepaths list is empty")
        for log_filepath in log_filepaths:
            self.assertTrue(type(log_filepath) is str, "log_filepath is not a string")

class LogTestCase(unittest.TestCase):
    
    def setUp(self):
        # Setup code to initialize necessary variables or state
        self.log_file_path = '/mnt/data/davinci_resolve.log'
    
    def test_collect_save_entries(self):
        log_entries = collect_save_entries(self.log_file_path)
        self.assertTrue(type(log_entries) is list, "log_entries is not a list")
        self.assertTrue(len(log_entries) > 0, "log_entries list is empty")
        for entry in log_entries:
            self.assertTrue(type(entry) is dict, "Entry is not a dict")
            self.assertIn('timestamp', entry, "Entry does not have a timestamp")
            self.assertIn('message', entry, "Entry does not have a message")

    def test_save_entry_format(self):
        log_entries = collect_save_entries(self.log_file_path)
        for entry in log_entries:
            self.assertTrue(validate_entry_format(entry), "Entry format is invalid")

    def test_chronological_order(self):
        log_entries = collect_save_entries(self.log_file_path)
        timestamps = [entry['timestamp'] for entry in log_entries]
        self.assertTrue(timestamps == sorted(timestamps), "Entries are not in chronological order")
        self.assertFalse(timestamps == sorted(timestamps, reverse=True), "Entries are not in chronological order")

    def test_work_sessions_count(self):
        log_entries = collect_save_entries(self.log_file_path)
        session_count = count_work_sessions(log_entries)
        self.assertTrue(type(session_count) is int, "Session count is not an integer")
        self.assertTrue(session_count > 0, "Session count should be greater than 0")

    def test_time_worked_all_time(self):
        log_entries = collect_save_entries(self.log_file_path)
        total_time = calculate_total_time(log_entries)
        self.assertTrue(type(total_time) is int, "Total time is not an integer")
        self.assertTrue(total_time > 0, "Total time should be greater than 0")

    def test_session_length(self):
        log_entries = collect_save_entries(self.log_file_path)
        session_lengths = calculate_session_lengths(log_entries)
        self.assertTrue(type(session_lengths) is list, "Session lengths is not a list")
        self.assertTrue(len(session_lengths) > 0, "Session lengths list is empty")
        for length in session_lengths:
            self.assertTrue(type(length) is int, "Session length is not an integer")

if __name__ == '__main__':
    unittest.main()
