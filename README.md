# resolve-time

## Status: work in progress

# Known issues:
- resolve only saves 12mb worth of log files and will delete the oldest logs
- weird calulation error between total hours worked and the sole project worked that month (should be same)
- if you change the project name, it will be logged as a different project


## Introduction
resolve-time is a tool designed to help you monitor the time spent on DaVinci Resolve video projects

## Problem Statement
Tracking the time spent on DaVinci Resolve video projects is challenging, making it difficult to understand productivity levels or determine appropriate client charges.

## Solution
Resolve Time Tracker analyzes your DaVinci Resolve log files and provides a detailed breakdown of time spent on each project, per day, per month, etc.

## User Stories
<!-- - **As a user,** I can provide my log file folder for analysis. -->
- **As a user,** I can view a breakdown of time spent on Davnici Resolve projects to understand my effort. (all time and per month (total + per project))
<!-- - **As a user,** I can view a heatmap graph showing total days spent editing to understand my consistency. -->

## Installation

1. Navigate to project directory
2. Run:
```
cp app/__init__.py /usr/local/bin/resolve-time
```

## Usage

## Problem Statement
Tracking the time spent on DaVinci Resolve video projects is challenging, making it difficult to understand productivity levels or determine appropriate client charges.

## Running Tests
To run the tests, use:
```bash
pytest
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

notes:
- i want options to customise timeout time
- i want to impement a feature that saves logs in a new file in the application folder or application support, or some other folder. Then it really only has to collect the save lines in the files and write them to a new file. then i want the option to change that folder as well
- research: programatically running applications (/Library/Application Support/Blackmagic Design/DaVinci Resolve/CaptureLogs.app), unzipping files,
- doc for subproccess.call, .extract() and .extractall()
- dont have any other folders on your desktop
- users encouraged to backup resolve-time-log file
- idea from git-hours
