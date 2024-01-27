# importing the Necessary Modules and Library
import http.server
import socketserver
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import webbrowser
# Set the port you want the server to run on
port = 8080
# Get the current directory where the script is located
web_directory = os.getcwd()
# Create a simple HTTP server
handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", port), handler)
# Flag to track if the server is running
server_running = False
def start_server():
    global server_running
    if not server_running:
        print(f"Serving on http://127.0.0.1:{port}")
        # Open the default web browser
        webbrowser.open(f"http://127.0.0.1:{port}")
        # Start the server
        httpd.serve_forever()
        server_running = True
# Define a custom event handler to watch for changes in the directory
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f'Reloading due to change in: {event.src_path}')
        # If the server is running, shut it down
        if server_running:
            httpd.shutdown()
            httpd.server_close()
        # Recreate and start the server
        start_server()
# Start the server
start_server()
# Define an observer to watch for file changes
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path=web_directory, recursive=True)
observer.start()
try:
    observer.join()  # Join the observer thread
except KeyboardInterrupt:
    print("Shutting down server")
    observer.stop()
except:
    print("Error occurred")
    observer.stop()
