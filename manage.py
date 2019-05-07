#!/usr/bin/env python
import os
import sys
#..
'''
import threading
from property.RestAPI import RestAPI
def callThread():
    RestAPI().begin()

list_lock = threading.Lock()

t = threading.Thread(target=RestAPI().begin())
t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
t.start()
#threading.start_new_thread(callThread, ())
#..
'''
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "modernBusiness.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
