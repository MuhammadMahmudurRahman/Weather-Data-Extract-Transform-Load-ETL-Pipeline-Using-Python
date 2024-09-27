@echo off
set LOGFILE="C:\Rumon\DS23EC\8. Python\Kunskapskontroll 2\Muhammad_Kunskapskontroll_2\scheduler_test.log"
set PYTHON_LOGFILE="C:\Rumon\DS23EC\8. Python\Kunskapskontroll 2\Muhammad_Kunskapskontroll_2\weather_update.log"
set PYTHON_SCRIPT="C:\Rumon\DS23EC\8. Python\Kunskapskontroll 2\Muhammad_Kunskapskontroll_2\weather_update.py"

echo [%date% %time%] Running the scheduled Python script >> %LOGFILE%
start /b "" cmd /c "python %PYTHON_SCRIPT% >> %PYTHON_LOGFILE% 2>&1"

if %errorlevel% neq 0 (
    echo [%date% %time%] Error occurred while running the Python script >> %LOGFILE%
) else (
    echo [%date% %time%] Finished running the scheduled Python script >> %LOGFILE%
)
