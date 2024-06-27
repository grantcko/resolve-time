import unittest
from app import get_file_path

# there must be a prompt to get the log files location
# dict includes filepath and all the log files

class TestSetLogFolder(unittest.TestCase):
    def test_get_file_path(self):
        filepath = "./test-logs"
        logs = get_file_path(filepath)
        self.assertTrue(type(logs) is list)
        for log in logs:
            self.assertTrue(type(log) is str)


# app must trigger calculations when proper format is inputed through terminal

# app must get all the log files

# must be named davinci_resolve.log.[int]

# if each file has save entries, the entries must fit a particular format

# each save entry must make chronological sense (compared to the file metadata)

# app must be able to identify individual work sessions based on time gaps between saves

# app must calculate work sessions length based on first and last save

# app must calculate time worked / da

# app must calculate time worked / month

# app must calculate time worked / day / project

# app must calculate time worked / month / project

# app must calculate time worked / project (all time)

# app must calculate days worked / week

# app must calculate days worked / month

# app must calculate days worked (all time)

# app must calculate time worked (all time)

# app must show all calculations

# app must make a heatmap


if __name__ == '__main__':
    unittest.main()
