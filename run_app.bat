@echo off
echo Starting Indian Labor Law Compliance System...
echo.
echo Testing application components...
python test_app.py
echo.
echo Starting web server...
echo Open your browser to: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python app.py