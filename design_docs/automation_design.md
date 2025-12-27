# Automating Daily Script Execution with Cron

## 1. Overview

This document outlines the approach to automate the execution of the main Python script at 09:00 Pacific Time (PT) every day using a `cron` job. `cron` is a time-based job scheduler in Unix-like computer operating systems. It enables users to schedule jobs (commands or shell scripts) to run periodically at certain times or dates.

The `cron` job will execute a shell command that:
1.  Navigates to the project directory.
2.  Activates the Python virtual environment.
3.  Executes the main Python script.
4.  Redirects the script's output (both stdout and stderr) to a log file for monitoring and debugging.

## 2. Implementation Steps

To implement this automation, follow these steps:

### Step 1: Determine the Full Paths

First, you need to identify the absolute paths to your project directory and the Python interpreter within your virtual environment.

*   **Project Directory:** You can find this by navigating to your project folder and running the `pwd` command. For this project, it is `/home/paul/lithrop_ledger`.
*   **Python Interpreter:** The full path to the Python interpreter in your virtual environment is `/home/paul/lithrop_ledger/LL_env/bin/python`.
*   **Main Script:** The full path to the main script is `/home/paul/lithrop_ledger/main.py`.

### Step 2: Convert 09:00 PT to Your System's Timezone

`cron` uses the system's local timezone. You need to convert 09:00 PT to the timezone your server is running in. Let's assume your server is running on UTC. 09:00 PT is 17:00 UTC (during daylight saving) or 16:00 UTC (during standard time). You should configure the cron job to run at the correct UTC time. For this example, we will use 17:00 UTC, which corresponds to 09:00 PDT.

### Step 3: Edit the Crontab

The `crontab` is the file that contains the schedule of cron entries to be run. You can edit it by running the following command in your terminal:

```bash
crontab -e
```

This will open the crontab file in your default text editor.

### Step 4: Add the Cron Job

Add the following line to the end of your crontab file. This line schedules the execution of the `main.py` script.

```cron
0 17 * * * /home/paul/lithrop_ledger/LL_env/bin/python /home/paul/lithrop_ledger/main.py >> /home/paul/lithrop_ledger/logs/cron.log 2>&1
```

### Cron Job Breakdown:

*   `0 17 * * *`: This is the schedule. It means the job will run at minute 0 of hour 17 (5 PM UTC), every day, every month, and every day of the week.
*   `/home/paul/lithrop_ledger/LL_env/bin/python`: This is the absolute path to the Python interpreter in the virtual environment. Using the absolute path ensures the correct interpreter is used and the script has access to all its dependencies.
*   `/home/paul/lithrop_ledger/main.py`: This is the absolute path to the script you want to run.
*   `>> /home/paul/lithrop_ledger/logs/cron.log 2>&1`: This part handles logging.
    *   `>> /home/paul/lithrop_ledger/logs/cron.log`: This redirects the standard output (stdout) of the script and appends it to a log file named `cron.log` inside the `logs` directory.
    *   `2>&1`: This redirects the standard error (stderr) to the same place as the standard output, so both normal output and error messages will be captured in the log file.

### Step 5: Save and Exit

Save the crontab file and exit the editor. Your `cron` job is now scheduled. You can verify that it has been added by running `crontab -l`.

By following these steps, your script will run automatically every day at the specified time, and you will have a log file to check its execution status.
