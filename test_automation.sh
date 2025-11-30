#!/bin/bash

# --- Configuration ---
# Set the path to your project directory
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
# Set the path to your main Python script
MAIN_SCRIPT="main.py"
# Set the path for the log file
LOG_FILE="${PROJECT_DIR}/logs/test_automation.log"
# Set the Python executable path
PYTHON_EXEC="python3"

# Ensure the logs directory exists
mkdir -p "${PROJECT_DIR}/logs"

echo "--- Starting Lithrop Ledger Automation Test ---" | tee -a "${LOG_FILE}"
echo "Test initiated at: $(date)" | tee -a "${LOG_FILE}"
echo "Project directory: ${PROJECT_DIR}" | tee -a "${LOG_FILE}"

# Navigate to the project directory
cd "${PROJECT_DIR}" || { echo "Error: Could not change to project directory ${PROJECT_DIR}" | tee -a "${LOG_FILE}"; exit 1; }

# Activate the virtual environment
source "${PROJECT_DIR}/LL_env/bin/activate" || { echo "Error: Could not activate virtual environment" | tee -a "${LOG_FILE}"; exit 1; }

# Execute the main Python script
echo "Executing Python script: ${PYTHON_EXEC} ${MAIN_SCRIPT}" | tee -a "${LOG_FILE}"
"${PYTHON_EXEC}" "${MAIN_SCRIPT}" >> "${LOG_FILE}" 2>&1
SCRIPT_EXIT_CODE=$?

if [ ${SCRIPT_EXIT_CODE} -eq 0 ]; then
    echo "Python script executed successfully." | tee -a "${LOG_FILE}"
    echo "Check your recipient email for the newsletter." | tee -a "${LOG_FILE}"
else
    echo "Error: Python script failed with exit code ${SCRIPT_EXIT_CODE}." | tee -a "${LOG_FILE}"
    echo "Review ${LOG_FILE} for details." | tee -a "${LOG_FILE}"
fi

echo "Test finished at: $(date)" | tee -a "${LOG_FILE}"
echo "--- Lithrop Ledger Automation Test Complete ---" | tee -a "${LOG_FILE}"

exit ${SCRIPT_EXIT_CODE}
