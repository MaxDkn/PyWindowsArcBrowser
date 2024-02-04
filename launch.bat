@echo off
set REQUIREMENTS_FILE=requirements.txt

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [Error]: You need to install the Python interpreter !
    pause
    exit
)

for /f %%i in (%REQUIREMENTS_FILE%) do (
    
    python -c "import %%i" >nul 2>&1
    if %errorlevel% neq 0 (
        pip install %%i
        
        
        ) else ( echo %%i)
    ) 

::echo Installing modules from the requirements.txt file

::python -m pip install --upgrade pip

::python -m pip install -r requirements.txt

::echo Install completed.
cd programs
start pythonw main.py

