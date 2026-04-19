@echo off
setlocal

cd /d "%~dp0"

if exist "%~dp0.venv\Scripts\python.exe" (
    "%~dp0.venv\Scripts\python.exe" "%~dp0password_generator_app.py"
    goto :eof
)

py -3 "%~dp0password_generator_app.py" >nul 2>&1
if %errorlevel%==0 (
    py -3 "%~dp0password_generator_app.py"
) else (
    python "%~dp0password_generator_app.py"
)

endlocal
