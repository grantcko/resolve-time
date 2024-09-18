#!/bin/zsh

# Rename masterlog_blank.txt to masterlog.txt
mv tests/masterlog_blank.txt tests/masterlog.txt

# Run pytest
pytest
