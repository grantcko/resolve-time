import re
import sys

def extract_timestamps(filepath, prj_name):

  """
  Search for and return the timestamps of the provided prj in the log file.
  """

  # Define the regex pattern to match the timestamp
  pattern = re.compile(f'.*\\| INFO  \\| (.*) \\| Start saving project {prj_name}')

  count = 0
  try:
      with open(filepath, 'r') as file:
          for line in file:
              match = pattern.match(line)
              if match:
                  print(match.group(1))
                  count += 1
  except FileNotFoundError:
      print(f"File not found: {filepath}")
  except Exception as e:
      print(f"An error occurred: {e}")
  print("---")
  print(f"Total matches: {count}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: timestamp_extractor.tmp <filepath> <project name>")
    else:
        extract_timestamps(sys.argv[1], sys.argv[2])
