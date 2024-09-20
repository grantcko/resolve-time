# resolve-time (🧑‍💻work in progress🧑‍💻)
A tool designed to help you monitor time spent in DaVinci Resolve.

## Todo:
- ☑ Tests
- ☑ Make it so that the program is executable like any other CLI
- ☑ Complete V1
- ☐ Rewrite tests
- ☐ Hand time and collect filled logs for comparison
- ☐ Organize backend
- ☐ Implement different accuracy collection option
- ☐ Front end V2
- ☐ Implement auto generate logs option

## Known issues:
- if you change the project name, it will be logged as a different project
- tests not running and the tests suck.
- weird calulation error between total hours worked and the sole project worked that month (should be same)
- if this app isn't run often, then some logs are lost and you get incorrect data with no way of seeing what days you missed
- application only calculates from saves, might be inaccurate, better data is with the rest of the log entries because they are not dependent on users saving settings and practicies

## Installation

1. start virtual environment
2. install with pipx

## Problem Statement
Tracking the time spent on DaVinci Resolve video projects is challenging, making it difficult to understand productivity levels or determine appropriate client charges.

## Solution
Resolve Time Tracker analyzes your DaVinci Resolve log files and provides a detailed breakdown of time spent on each project, per day, per month, etc.

## User Stories
<!-- - **As a user,** I can provide my log file folder for analysis. -->
- **As a user,** I can view a breakdown of time spent on Davnici Resolve projects to understand my effort. (all time and per month (total + per project))
<!-- - **As a user,** I can view a heatmap graph showing total days spent editing to understand my consistency. -->

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
-  i want to make decisions on what to do based on problems, features, research, sharing
- i wanna make it so that the user can pass an option to save space by only running calculations based on save entries. that way i don't have to delete the beautiful code i wrote and there is increased functionality for free. otherwise, i think i'm gonna make it so that the app simply backs up and saves the fucking save entries properly, maybe into a postgress database or a mysql database or something to be extra efficient or just into a fucking csv
anki stats influences the summary of this project
ok so i need to rework the logic and write the test-logs to create a simple model including all the different variations of log entries. one thing to note is that resolve only saves the project name on the saves right? Well I think it might be safe to assume that all the entries inbetween or before at least, belong to that project. I would need to figure out if log entries are saved when one switches projects so i can be extra accurate on what entries belong to each project
- 🤙
- so i need to rethink the flow of logic in my functions. I think i want to just really change collect_monthly_save_entries() and save_entries_info() to just "entries" not "save entries". Then in the process_logs() logic, I will pass, to info generation, either second to second entries, aka exact or just save entries. How will i know? Well process_logs() will have an argument required that defines wether exact or space saving is required. I think by default exact is probably going to be way fucking better, because it will be hard to determine someone's stats based on individual saving/autosaving practices.
- so with this new flow, i need to just make another collect_save_entries() function, called collect_exact_entries(), meaning that it collects the relevant info from the first entry in a group of entries written in the same second. This will probably cut the file size into a fraction of the original logs, relative to how much time is covered. This also only removes marginal (subsecond) amounts of accuracy, and in some cases, entries are written in the same milisecond, so there is litterally no need to save every single entry. That is only if you cared about time tracking.
- 🤙
- how do the logs on resolve work? well I'm glad you asked. Basically, information from the log files are generated via an apple script app. I think what is happening below the surface there is some sort of processing of data from the davinci resolve database or something. there are 6 log files generated with log entries for each of the things that happen in davinci resolve. They have various piece of info and are all timestamped to the milisecond. The entries created upon project saves in particular have info about the project that is currently being edited. The file are numbered 0-5 (sorta). 0 contains the latest info and 5 contains the oldest info. Each entry is sorted from top to bottom of the file in chonological order. Oldest entries gets kicked out first. Only the last ~12mb worth of entries saved.
i have gotta fill master logs back up and figure out how to clear their contents again after I do it to em...
then i gotta calculate out all the fucking test log bullshit like all the stats then put those into the tests
every test will operate based on sep-b_2024 logs for simplicity sake. And everything is also calculated using a blank existing masterlog except for the summaries where different existing masterlogs are used. that will really be the only place to test for missing known missing data.
- at some point i have gotta make sure that I have everything documented properly if I want people to work on this with me so...
- and i have partially gotta explain the blank, missing, and overlap in the tests
