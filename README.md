# Resolve Time Tracker

## Introduction
Resolve Time Tracker is a tool designed to help you monitor the time spent on DaVinci Resolve video projects. It provides functionalities such as collecting log entries, validating entry formats, counting work sessions, and calculating the total time worked on projects.

## Problem Statement
Tracking the time spent on DaVinci Resolve video projects is challenging, making it difficult to understand productivity levels or determine appropriate client charges.

## Solution
Resolve Time Tracker analyzes your DaVinci Resolve log files and provides a detailed breakdown of time spent on each project, per day, per month, etc.

## User Stories
- **As a user,** I can provide my log file folder for analysis.
- **As a user,** I can view a breakdown of time spent on projects to understand my effort.
- **As a user,** I can view a heatmap graph showing total days spent editing to understand my consistency.

## Notes
- Users should back up log files themselves.
- Key learning areas: Python syntax, Python tests, and understanding the basic structure of the app.
- Focus on learning unit tests to cover all use cases and understand unfamiliar lines of code.

## Installation
To install the necessary dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage
To use the functionalities provided by this project, import the necessary functions from the `app` module. For example:
```python
from app import get_log_filepaths, collect_save_entries, validate_entry_format, count_work_sessions, calculate_total_time, calculate_time_per_project

log_file_path = 'test_logs/davinci_resolve.log'
save_entries = collect_save_entries(log_file_path)
```

## Running Tests
To run the tests, use:
```bash
pytest
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
