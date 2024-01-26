import json
import sys
import math

import inputimeout


def get_input(timeout):
    try:
        message = inputimeout.inputimeout("", timeout)
    except:
        message = None

    return message


def log(msg):
    sys.stdout.write(str(msg) + "\n")
    sys.stdout.flush()


def progress_string(adict):
    return "pyramid progress - %s" % json.dumps(adict)


def log_progress(adict):
    log(progress_string(adict))


def print_final(adict):
    log_progress({"progress": 1.0})
    log("pyramid job complete - %s" % json.dumps(adict))


def find_invalid_value(anobject, location_path):
    if isinstance(anobject, list):
        for i, element in enumerate(anobject):
            if isinstance(element, float) and not math.isfinite(element):
                return location_path + [i]
            elif isinstance(element, (list, dict)):
                path = find_invalid_value(element, location_path + [i])

                if path:
                    return path
    elif isinstance(anobject, dict):
        for key in anobject:
            element = anobject[key]
            if isinstance(element, float) and not math.isfinite(element):
                return location_path + [key]
            elif isinstance(element, (list, dict)):
                path = find_invalid_value(element, location_path + [key])

                if path:
                    return path

    return None
