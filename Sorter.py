# this is still a work in progress, just an idea i had to automatically sort files

from watchdog.observer import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json

trackedFolder = ""
folderDest = ""
yourName = ""

class FileHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)

folder_to_track = '/Users/" + yourName+ "/Desktop/' + trackedFolder
folder_destination = '/Users/" + yourName + "/Desktop/' + folderDest
event_handler = FileHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

