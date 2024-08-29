@echo off
REM Check if Python is installed
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python is not installed. Please install Python before running this script.
    pause
    exit /b
)

REM Install the required packages
echo Installing required packages...
pip install -r requirements.txt

echo Installation complete.
pause
