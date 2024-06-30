# Resolve Time Tracker

## Introduction
This project is designed to help you track the time you spend on DaVinci Resolve video projects. It includes functionalities such as collecting log entries, validating entry formats, counting work sessions, and calculating total time worked on projects.

## Problem
I have no idea how much time I am spending on DaVinci Resolve video projects, so I can't understand my level of productivity or how much to charge clients.

## Solution
A computer checks your resolve log files and shows you a breakdown per project, per day, per month, etc., of time spent on each project.

## User Journey
### Stories
- As a user, I can give my log file folder so that the app can analyze it.
- As a user, I can read a breakdown of time spent so that I can learn about my effort.
- As a user, I can read a heatmap graph including total days spent editing so that I can learn about my consistency.

## Notes
- Users should backup log files themselves.
- Things to learn: Python syntax brush up, Python tests (including which tests to make to ensure no problems).
- I must understand how to write the tests and the basic structure of the app (which files, methods, arguments, etc.) before I start talking to LLMs. I don't want advice or any extra information until I have a footing. I need to know what I want before I ask for help from someone who doesn't understand reality like I do.
- I would like to continue learning unit tests so I can really understand how to make tests for all the use cases I need and understand what things are, the lines of code I don't know what they do.

## Installation
To install the necessary dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage
To use the functionalities provided by this project, you can import the necessary functions from the `app` module. For example:
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

## Comparison of Aider, Cursor, and GitHub Copilot

### Aider
- **Purpose**: Aider is a local tool designed to assist developers by providing code suggestions and automating repetitive tasks.
- **Data Privacy**: Aider runs locally on your machine, ensuring that your codebase and sensitive information remain secure. Only the necessary context for generating responses is sent to OpenAI's servers.
- **Integration**: Aider integrates with your local development environment and can be used with various editors and IDEs.
- **Customization**: Highly customizable to fit specific workflows and coding standards.

### Cursor
- **Purpose**: Cursor is a code editor with built-in AI capabilities to assist with code completion, refactoring, and other development tasks.
- **Data Privacy**: Cursor processes data locally and may also send some data to external servers for AI processing, depending on the configuration.
- **Integration**: Cursor is a standalone code editor, so it does not require integration with other editors or IDEs.
- **Customization**: Offers various plugins and extensions to enhance functionality.

### GitHub Copilot
- **Purpose**: GitHub Copilot is an AI-powered code completion tool that provides real-time code suggestions and helps with writing code faster.
- **Data Privacy**: GitHub Copilot sends code snippets and context to GitHub's servers for processing, which may raise privacy concerns for some users.
- **Integration**: Seamlessly integrates with popular code editors like Visual Studio Code, JetBrains IDEs, and Neovim.
- **Customization**: Limited customization options compared to Aider and Cursor, but it offers a wide range of language support and intelligent code suggestions.

### Summary
- **Aider**: Best for developers who prioritize data privacy and want a highly customizable local tool.
- **Cursor**: Ideal for those who prefer an all-in-one code editor with built-in AI capabilities.
- **GitHub Copilot**: Suitable for developers looking for seamless integration with popular editors and real-time code suggestions.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
