import unittest
from app import get_log_filepaths, build_summary

# test method to build summary
class SummaryTestCase(unittest.TestCase):
    def test_build_summary(self):
        projects_worked = build_summary()
        self.assertTrue(type(projects_worked) is list, "projects_worked is not a list")
        # assert that projects worked is not an empty list
        for project in projects_worked:
            self.assertTrue(type(project) is dict, project, "project in projects_worked is not a dict")
            self.assertTrue(type(project)["project_name"] is str, "project_name in project is not a str")
            self.assertTrue(type(project)["work_days_total"] is int, "work_days in project is not an int")
            self.assertTrue(type(project)["work_sessions_total"] is int, "work_sessions in project is not an int")
            self.assertTrue(type(project)["work_hours_total"] is int, "work_hours in project is not an int")

class LogPathsTestCase(unittest.TestCase):

    # test method to collect log filepaths

    def test_get_log_paths(self):
        log_folder_filepath = "./test-logs"
        log_filepaths = get_log_filepaths(log_folder_filepath)
        self.assertTrue(type(log_filepaths) is list, "There is no list of log filepaths")
        # assert list is not empty

        for log_filepath in log_filepaths:
            self.assertTrue(type(log_filepath) is str)

    # test method for checking log filepaths for proper file path format

class LogTestCase(unittest.TestCase):
    def test_(self):

    # test method for collecting save entries from each file

    # test method for checking save entry format

    # test method to make sure each save entry makes chronological sense (compared to the file metadata)

    # test method to be able to count work sessions based on time gaps between saves

    # test method to calculate time worked / day / project

    # test method to calculate time worked / month / project

    # test method to calculate time worked / project (all time)

    # test method to calculate days worked / week

    # test method to calculate days worked / month

    # test method to calculate days worked (all time)

    # test method to calculate time worked (all time)

    # test method to make a heatmap

    # test method to calculate work sessions length based on first and last save

    # test method to calculate time worked / day

    # test method to calculate time worked / month

if __name__ == '__main__':
    unittest.main()
