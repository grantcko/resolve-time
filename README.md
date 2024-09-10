# resolve-time

## Status: work in progress

# Known issues:
- if you change the project name, it will be logged as a different project
- tests not running and the tests suck.
- weird calulation error between total hours worked and the sole project worked that month (should be same)
- if this app isn't run often, then some logs are lost and you get incorrect data with no way of seeing what days you missed
- application only calculates from saves, might be inaccurate, better data is with the rest of the log entries because they are not dependent on users saving settings and practicies

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
This project is licensed under the MIT License.

## misc notes:
- make sure my tests are ok, code is commented, readmes are good, code is refactored
- i want there to be a start date for save information displayed
- users encouraged to backup resolve-time-log file
- need to figure out how to use this script when the functions are seperated
- i think autosave must be turned on
- i would like to test this app vs hand timing vs timeapp
- research command line python app frameworks + pytest and importing files

- i want logs saved to be run every time resolve opens
- let user know if the auto start setting is off, they might have incorrect data.

- let user know they might have incorrect data if a resolve-time-log file is already present upon installation.
  - in that case. it might be good to create a new log file and seperate the two when displaying - maybe give an option to select archived time logs
  - if there are different logs files then each log file should have a created and last updated information at least to the date

- i want options to customise timeout time
- dont have any other folders on your desktop
- idea from git-hours
- can't do anything untill it's done
- need to allow accessability controls
- advantage is that you don't need the app running all the time to use it
- in the future i want this to be a part of davinci or at least have it auto run upon davinci booting up
- i want the program to automatically force quit the capture logs application
- for mac only
- i want to make decisions on what to do based on problems, features, research, sharing
