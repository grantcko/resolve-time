#!/bin/zsh

print "STARTTESTS"
mv tests/masterlog_blank.txt tests/masterlog.txt
pytest
mv tests/masterlog.txt tests/masterlog_blank.txt
mv tests/masterlog_missing.txt tests/masterlog.txt
pytest
mv tests/masterlog.txt tests/masterlog_missing.txt
mv tests/masterlog_overlap.txt tests/masterlog.txt
pytest
mv tests/masterlog.txt tests/masterlog_overlap.txt
print "ENDTESTS"
