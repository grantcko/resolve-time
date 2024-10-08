from definitions import *
## GETTING THE LOGS

class TestAutoLogGeneration:
    def test_auto_gen_logs_function(self):
        # Get a reference to the date and time
        current_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")
        # get reference to $HOME environmental variable
        # Genereate the log files
        auto_gen_logs(current_datetime, home_path)
        # Define desired path for log files to end up
        path = os.path.join(os.path.expanduser("~"), "Desktop")
        # Collect all the log file filepaths in that folder
        log_files = [f for f in os.listdir(path) if f.startswith("DaVinci-Resolve-logs-")]

        assert len(log_files) > 0, "No log files found on the desktop."

        # Check if any of the log files were created in the last few minutes
        recent_file_found = False
        for log_file in log_files:
            file_path = os.path.join(path, log_file)
            creation_time = os.path.getctime(file_path)
            if (datetime.now() - datetime.fromtimestamp(creation_time)).total_seconds() < 300:  # 5 minutes
                recent_file_found = True
                break

        assert recent_file_found, "No RENCENT log file found on the desktop."

        time.sleep(1.0)
        # Remove the generated zip file
        subprocess.run(['rm', '-rf', glob.glob(f"{home_path}/Desktop/DaVinci-Resolve-logs-{current_datetime[:11]}*.tgz")[0]])
        # log_files = [f for f in os.listdir(path) if f.startswith("DaVinci-Resolve-logs-")]
        # assert len(log_files) == 0, "log files found on the desktop."

class TestLogPathsFunction:

    # test funciton to collect log filepaths
    def test_get_log_filepaths_function(self):
        assert type(log_filepaths) is list, "log_filepaths is not a list"
        assert len(log_filepaths) > 0, "log_filepaths list is empty"
        for log_filepath in log_filepaths:
            assert type(log_filepath) is str, "log_filepath is not a string"

## COLLECTED ENTRIES

@pytest.fixture
def test_entries_setup_teardown():
    # define which entries are being tested (save entries)
    entries = collect_entries(log_filepaths, masterlog_file_missing, accuracy="medium")
    yield entries
    with open(masterlog_file_missing, 'w') as masterlog_file:
        masterlog_file.truncate(0)
    collect_entries(log_filepaths_missing, masterlog_file_missing, accuracy="medium")


class TestCollectedMediumAcEntries:
    # test if save entries are actually collected and stored correctly
    def test_entries(self, test_entries_setup_teardown):
        entries = test_entries_setup_teardown
        assert type(entries) is list, "entries is not a list"
        assert len(entries) > 0, "entries should be greater than 0"
        # using bkmr stats because it conveniently has only data on sepb which this test case deals with
        assert len(entries) == bkmr_total_entries, f"entries should have {bkmr_total_entries} entries"
        for entry in entries:
            assert type(entry) is dict, "Entry is not a dict"
            assert 'timestamp' in entry, "Entry does not have a timestamp"
            assert 'project_title' in entry, "Entry does not have a project_title"

    # test if timestamps are in chronological order
    def test_timestamps_chronological_order(self, test_entries_setup_teardown):
        entries = test_entries_setup_teardown
        timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S,%f') for entry in entries]
        assert len(timestamps) > 0, "timestamps should be greater than 0"
        assert timestamps == sorted(timestamps), "Entries are not in chronological order"
        assert not timestamps == sorted(timestamps, reverse=True), "Entries are not in chronological order"

############ MISSING MASTER LOG MISSING ENTRIES

## PROCESSED STATS

# set up a fixture to define which info is being tested
@pytest.fixture
def info_setup():
    info = msmr_mediumac["entries_info"]
    yield info

class TestProcessedStats:
    # test info generated from entries

    def test_day_count(self, info_setup):
        info = info_setup
        day_count = info['day_count']
        assert day_count == msmr_day_count, f"Amount of days worked should be {msmr_day_count}"

    # TODO: test for day count per project

    def test_month_count(self, info_setup):
        info = info_setup
        month_count = info['month_count']
        assert month_count == msmr_month_count, f"Amount of months worked should be {msmr_month_count}"

    # TODO: test for month count per project

    def test_dates_worked(self, info_setup):
        info = info_setup
        dates_worked = info['dates_worked']
        assert type(dates_worked) is list, f"dates_worked should be a list"
        assert dates_worked == msmr_dates_worked, "dates_worked should be the same as collected stats"

    # TODO:

    # def test_work_sessions_count(self, info):
    #     session_count = info['session_count']
    #     assert type(session_count) is int, "Session count is not an integer"
    #     assert session_count > 0, "Session count should be greater than 0"
    #     assert session_count == msmr_session_count, "Session count should be msmr_session_count"

    # def test_work_hours(self, info):
    #     work_hours = info['work_hours']
    #     assert type(work_hours) is float, "Work hours is not an float"
    #     assert work_hours > 0, "Work hours should be greater than 0"
    #     assert work_hours == 0, "Work hours should be ???"

    # def test_project_work_hours(self, info):
    #     project_hours = info['project_work_hours']
    #     assert type(project_hours) is dict, "project_work_hours is not a dict"
    #     assert len(project_hours) > 0, "project_work_hours should not be an empty dict"
    #     for project, hours in project_hours.items():
    #         assert type(hours) is float, f"Work hours for project {project} is not a float"
    #         assert hours > 0, f"Work hours for project {project} should be greater than 0"

@pytest.fixture
def log_files_setup_teardown():
    processed = process_logs(
        home_path,
        test_current_datetime,
        masterlog_file_missing,
        test_zip_file_pattern,
        log_folder_filepath=test_log_folder_filepath,
        accuracy="medium"
        )
    yield processed
    # clear masterlog file
    with open(masterlog_file_missing, 'w') as masterlog_file:
        masterlog_file.truncate(0)
    subprocess.run(['rm', '-rf', "tests/zipped-logs/Library"])

class TestLogProcessing:
    def test_processed_info(self, log_files_setup_teardown):
        # testing info...
        processed = log_files_setup_teardown
        assert isinstance(processed["info"], dict), "processed info should be a dictionary"
        assert len(processed["info"]) > 0, "info should not be empty"
        assert processed["info"]["total_entries"] == msmr_total_entries, f"There should be {msmr_total_entries} entries, total"
        assert processed["info"]["day_count"] == msmr_day_count, f"There should be {msmr_day_count} days, total"

    def test_processed_monthly_info(self, log_files_setup_teardown):
        # testing monthly info...
        processed = log_files_setup_teardown
        assert isinstance(processed["monthly_info"], dict), "processed monthly_info should be a dictionary"
        assert len(processed["monthly_info"]) > 0, "Monthly info should not be empty"
        assert "09_2024" in processed["monthly_info"], "09_2024 should be a key in monthly_info"
        assert "10_2024" not in processed["monthly_info"], "10_2024 should not be a key in monthly_info"
        assert processed["monthly_info"]["09_2024"]["total_entries"] == msmr_total_entries, f"There should be {msmr_total_entries} entries, in Sept"

    def test_zip_filepath(self, log_files_setup_teardown):
        # testing zip filepath...
        processed = log_files_setup_teardown
        assert isinstance(processed["zip_filepath"], str), "Zip filepath should be a string"

## SUMMARIES, AKA THE FRONT END

@pytest.fixture
def summary_setup_teardown():
    yield
    # reset master logs to their initial state
    with open(masterlog_file_missing, 'w') as masterlog_file:
        masterlog_file.truncate(0)
    with open(masterlog_file_missing, 'w') as masterlog_file:
        masterlog_file.truncate(0)
    collect_entries(log_filepaths_missing, masterlog_file_missing, accuracy="medium")
    with open(masterlog_file_overlap, 'w') as masterlog_file:
        masterlog_file.truncate(0)
    collect_entries(log_filepaths_overlap, masterlog_file_overlap, accuracy="medium")
    # Remove the unzipped log folder
    subprocess.run(['rm', '-rf', "tests/zipped-logs/Library*"])

class TestSummaries:#
    def test_summary(self, summary_setup_teardown):
        # test the summary that is displayed in the terminal for all the correct info
        processed = process_logs(
            home_path,
            test_current_datetime,
            masterlog_file_missing,
            test_zip_file_pattern,
            log_folder_filepath=test_log_folder_filepath,
            accuracy="medium"
            )
        summary = build_summary(processed["info"], processed["monthly_info"])
        assert isinstance(summary, str), f"Summary should be a string"
        assert str(msmr_total_entries) in summary, f"Summary should include the total entries: {msmr_total_entries}"
        assert str(msmr_day_count) in summary, f"Summary should include the day count: {msmr_day_count}"
        assert str(msmr_month_count) in summary, f"Summary should include the month count: {msmr_month_count}"
        #

        # TODO:
        # assert that summary includes today summary
        # assert that summary includes correct heatmap
        # assert that summary includes correct project names
        # assert that summary includes correct hours
        # assert that summary includes correct dates worked
        # assert that summary includes correct day count
        # assert that summary includes correct month count
        # assert that summary includes correct session count

# Final teardown (make sure no leftover folder, files, data)
@pytest.fixture
def summary_setup_teardown():
    yield
    # reset master logs to their initial state
    with open(masterlog_file_blank, 'w') as masterlog_file:
        masterlog_file.truncate(0)
    with open(masterlog_file_missing, 'w') as masterlog_file:
        masterlog_file.truncate(0)
    collect_entries(log_filepaths_missing, masterlog_file_missing, accuracy="high")
    with open(masterlog_file_overlap, 'w') as masterlog_file:
        masterlog_file.truncate(0)
    collect_entries(log_filepaths_overlap, masterlog_file_overlap, accuracy="high")
    # Remove the unzipped log folder
    subprocess.run(['rm', '-rf', "tests/zipped-logs/Library"])
