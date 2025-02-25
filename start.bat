@echo Off

echo Checking environment setup...
:: Check if .env file exists, create if not found
if not exist .env (
    echo GEMINI_API_KEY=your_api_key_here > .env
    echo Created .env file.
) else (
    echo .env file exists.
)


:: Activate virtual environment
call venv\Scripts\activate
echo Virtual environment activated.

:: Install dependencies from requirements.txt
if exist requirements.txt (
    echo Installing dependencies from requirements.txt...
    pip install -r requirements.txt
    echo Dependencies installed.
) else (
    echo No requirements.txt file found, Creating a requirements file...
    echo requests > requirements.txt
    echo python-dotenv >> requirements.txt
    echo pymysql >> requirements.txt
    echo requirements.txt created.
    type requirements.txt
    echo Installing dependencies from requirements.txt...
    pip install -r requirements.txt
    echo Dependencies installed.
)

:: Start the application
echo Starting Teleco AI bot...
python app.py

:: Pause to keep the console open
pause
