@echo off

rem Print software information
echo ===============================================
echo      Author: SukarnaJana
echo      Version: 12.8.4
echo      LastUpdate: 09/04/2024
echo      Software Name: CanGii
echo ===============================================
echo.

rem Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b
)

rem Check if requirements.txt file exists
if not exist requirements.txt (
    echo requirements.txt file not found. Creating a sample file...
    echo.>requirements.txt
    echo ExampleLibrary==1.0.0>>requirements.txt
)

rem Install libraries from requirements.txt
echo Installing required libraries...
pip install -r requirements.txt

rem Check if installation was successful
if %errorlevel% neq 0 (
    echo An error occurred during library installation.
    pause
)

pause
