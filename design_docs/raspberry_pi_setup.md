# Raspberry Pi Automated Newsletter Setup

This document outlines the recommended Raspberry Pi models for running the Lithrop Ledger application and provides a detailed guide for setting it up for automated daily execution.

## 1. Analysis of Raspberry Pi Models

This document outlines the recommended Raspberry Pi models for running the Lithrop Ledger application and provides a detailed guide for setting it up for automated daily execution.

### Recommended Models

For the task of running a daily Python script that fetches news from an API and sends an email, the resource requirements are minimal. The primary considerations are cost, power consumption, and network connectivity.

| Feature | Raspberry Pi Zero | Raspberry Pi Zero 2 W | Raspberry Pi 4 |
| :--- | :--- | :--- | :--- |
| **Price** | ~$5 | ~$15 | ~$35+ |
| **CPU** | 1GHz single-core | 1GHz quad-core 64-bit Arm Cortex-A53 | 1.5GHz quad-core 64-bit Arm Cortex-A72 |
| **RAM** | 512MB | 512MB | 1GB, 2GB, 4GB, or 8GB |
| **Connectivity** | - | Wi-Fi, Bluetooth | Wi-Fi, Bluetooth, Gigabit Ethernet |
| **Power** | ~1W | ~1.5W | ~3.5W |
| **Suitability** | **Viable.** The cheapest option, but the lack of built-in Wi-Fi requires extra setup. | **Recommended.** The ideal balance of low cost, low power, and sufficient performance with built-in Wi-Fi. | **Overkill, but future-proof.** Provides significant overhead for future enhancements. |

**Conclusion:** The **Raspberry Pi Zero 2 W** is the most cost-effective and energy-efficient choice for this project. The Raspberry Pi Zero is a cheaper alternative if you are willing to set up Wi-Fi manually, and the Raspberry Pi 4 is a suitable, albeit more expensive, option that offers more flexibility for future projects.

This guide will focus on setting up the project on a **Raspberry Pi Zero**.

## 2. Setup and Automation

This guide assumes you have a Raspberry Pi with Raspberry Pi OS (or a similar Debian-based Linux distribution) installed and have access to the command line.

### Step 1: Initial Setup & Dependencies

1.  **Update the System:**
    ```bash
    sudo apt-get update && sudo apt-get upgrade -y
    ```
2.  **Install Python and Pip:**
    ```bash
    sudo apt-get install python3 python3-pip python3-venv -y
    ```
3.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/lithrop-ledger.git
    cd lithrop-ledger
    ```
4.  **Set up the Python Virtual Environment:**
    ```bash
    python3 -m venv LL_env
    source LL_env/bin/activate
    pip install -r requirements.txt
    ```

### Step 2: Configure Environment Variables

Create a `.env` file in the project's root directory with the necessary credentials:
```
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
EMAIL_APP_PASSWORD="YOUR_EMAIL_APP_PASSWORD"
SMTP_USERNAME="your.email@gmail.com"
RECIPIENT_EMAIL="recipient.email@example.com"
TEST_MODE=False
```

### Step 3: Create an Execution Script

To simplify the `cron` job, create a shell script to run the Python script within its virtual environment.

**`run_newsletter.sh`**
```bash
#!/bin/bash
# Navigate to the project directory
cd /home/pi/lithrop-ledger 
# Activate the virtual environment
source LL_env/bin/activate
# Run the main script
python3 main.py
```
Make the script executable:
```bash
chmod +x run_newsletter.sh
```
Place this script in the root of the `lithrop-ledger` directory.

### Step 4: Schedule the Daily `cron` Job

`cron` is a time-based job scheduler in Unix-like operating systems. We will use it to run the `run_newsletter.sh` script automatically every day.

1.  **Open the Crontab Editor:**
    ```bash
    crontab -e
    ```
    If it's your first time, you may be asked to choose an editor. Select your preferred one (e.g., `nano`).

2.  **Add the Cron Job:**
    Add the following line to the end of the file to schedule the script to run at 7:00 AM every day:
    ```
    0 7 * * * /home/pi/lithrop-ledger/run_newsletter.sh >> /home/pi/lithrop-ledger/logs/cron.log 2>&1
    ```

    *   `0 7 * * *`: This specifies the time. The format is `(minute) (hour) (day of month) (month) (day of week)`. `0 7 * * *` means at 0 minutes past the 7th hour, every day.
    *   `/home/pi/lithrop-ledger/run_newsletter.sh`: The absolute path to the execution script.
    *   `>> /home/pi/lithrop-ledger/logs/cron.log 2>&1`: This redirects the script's output (both `stdout` and `stderr`) to a log file. This is useful for debugging.

3.  **Save and Exit:**
    *   If using `nano`, press `Ctrl+X`, then `Y`, then `Enter`.

The setup is now complete. The Raspberry Pi will automatically run the newsletter script every day at 7:00 AM.
