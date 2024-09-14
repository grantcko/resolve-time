#!/usr/bin/env python3

import sys
import subprocess
import typer
from datetime import datetime
import threading
from . import functions
import glob
import os

#### REFERENCES ####

app = typer.Typer()

# Get a reference to txt file filepath
txt_filepath = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/resolve-time-log.txt"

# Get a reference to the date and time
current_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")

# get reference to $HOME environmental variable
home_path = os.environ["HOME"]

@app.command()
def run_all():
    #### GET LOG FILES, PROCESS, PRINT SUMMARY ####

    # TODO: create an option for auto or manual log file generation then define the filepath that gets passed to process the logs accordingly

    # auto generate the log files
    app.command()(functions.auto_gen_logs(current_datetime, home_path))

    auto_zip_filepath = f"{home_path}/Desktop/DaVinci-Resolve-logs-{current_datetime[:11]}*.tgz"

    processed_info = app.command()(functions.process_logs(home_path, current_datetime, txt_filepath, auto_zip_filepath))

    summary = app.command()(functions.build_summary(processed_info["info"], processed_info["monthly_info"]))

    print(summary)

    #### REMOVE LOG FILES ####

    # Wait 3 seconds. Not using sleep() because of iteraction with datetime
    threading.Event().wait(3)

    # Remove the generated zip file
    subprocess.run(['rm', '-rf', processed_info["zip_filepath"]])

    # Remove the unzipped log folder
    subprocess.run(['rm', '-rf', f"{home_path}/Desktop/Library"])

if __name__ == "__main__":
    app()
