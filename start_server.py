import sys
import threading
import time
from app import app

def run_server():
    try:
        print("Starting Flask server...")
        app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
    except Exception as e:
        print(f"Error starting server: {e}")

if __name__ == '__main__':
    print("Flask app starting on http://127.0.0.1:5000")
    print("Press Ctrl+C to stop")
    
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
    
    time.sleep(2)
    print("Server should be running now. Check http://127.0.0.1:5000")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down server...")
        sys.exit(0)