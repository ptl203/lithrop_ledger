# Automating Daily Script Execution with Cron

## 1. Overview

This document outlines the approach to automate the execution of the main Python script at 09:00 Pacific Time (PT) every day using a `cron` job. `cron` is a time-based job scheduler in Unix-like computer operating systems. It enables users to schedule jobs (commands or shell scripts) to run periodically at certain times or dates.

The `cron` job will execute a shell script that:
1.  Navigates to the project directory.
2.  Activates the Python virtual environment.
3.  Executes the main Python script.
4.  Redirects the script's output (both stdout and stderr) to a log file for monitoring and debugging.

## 2. Implementation Steps

To implement this automation, follow these steps:

### Step 1: Create an Execution Script

A best practice for `cron` jobs is to execute a single, simple shell script that handles the setup and execution of your program. This makes the `cron` entry cleaner and easier to manage.

Create a file named `run_newsletter.sh` in the root of your `lithrop-ledger` project with the following content:

**`run_newsletter.sh`**
```bash
#!/bin/bash

# Get the absolute path of the script
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)

# Navigate to the project directory
cd "$SCRIPT_DIR"

# Activate the virtual environment
source LL_env/bin/activate

# Run the main script and log the output
python3 main.py >> "$SCRIPT_DIR/logs/cron.log" 2>&1
```

**Make the script executable:**
```bash
chmod +x run_newsletter.sh
```

This script is robust because it automatically determines the project's location, making it portable.

### Step 2: Convert 09:00 PT to Your System's Timezone

`cron` uses the system's local timezone. You need to convert 09:00 PT to the timezone your server is running in. For this example, we will assume your Raspberry Pi is set to **UTC**. 09:00 AM PT (during Pacific Daylight Time, UTC-7) is **16:00 UTC**.

You can check your system's timezone with `timedatectl`.

### Step 3: Edit the Crontab

The `crontab` is the file that contains the schedule of cron entries. Edit it by running:

```bash
crontab -e
```

### Step 4: Add the Cron Job

Add the following line to the end of your crontab file. This schedules the execution of the `run_newsletter.sh` script.

**Important:** You must use the **absolute path** to the `run_newsletter.sh` script. You can find it by navigating to your project directory and running `pwd`. For example, if your project is in `/home/pi/lithrop-ledger`, the path would be `/home/pi/lithrop-ledger/run_newsletter.sh`.

```cron
# Run the Lithrop Ledger newsletter script daily at 9:00 AM PT (16:00 UTC)
0 16 * * * /path/to/your/lithrop-ledger/run_newsletter.sh
```

**Replace `/path/to/your/lithrop-ledger/` with the actual absolute path to your project folder.**

### Cron Job Breakdown:

*   `0 16 * * *`: Runs the job at minute 0 of hour 16 (4:00 PM UTC), every day.
*   `/path/to/your/lithrop-ledger/run_newsletter.sh`: The absolute path to the execution script. The logging is now handled *inside* this script.

### Step 5: Save and Exit

Save the crontab file and exit the editor. Your `cron` job is now scheduled. You can verify it by running `crontab -l`.
