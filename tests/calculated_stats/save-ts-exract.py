import re
import sys

def extract_timestamps(filepath):



  # Define the regex pattern to match the timestamp
  pattern = re.compile('.*\\| INFO  \\| (.*) \\| Start saving project -CHOP-')

  try:
      with open(filepath, 'r') as file:
          for line in file:
              match = pattern.match(line)
              if match:
                  print(match.group(1))
  except FileNotFoundError:
      print(f"File not found: {filepath}")
  except Exception as e:
      print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: timestamp_extractor.tmp <filepath>")
    else:
        extract_timestamps(sys.argv[1])
