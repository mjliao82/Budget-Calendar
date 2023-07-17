# run_app.py
import subprocess
import time
import webbrowser

def start_server():
    # Start the server as a subprocess
    process = subprocess.Popen(["python", "app.py"], stdout=subprocess.PIPE)

    # Wait a moment for server to start
    time.sleep(2)

    # Open a web browser pointing to the Flask app
    webbrowser.open("http://127.0.0.1:5000/")

    return process

if __name__ == "__main__":
    process = start_server()
    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Kill the subprocess when the script is stopped
        process.kill()
