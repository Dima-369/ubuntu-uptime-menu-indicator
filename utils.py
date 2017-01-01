import os
import time

# Apparently, an icon has to be set so we can use a 1x1px transparent icon
# which is barely noticeable to hide the icon and only display the text
default_icon = os.path.dirname(__file__) + "/transparent.png"
# clock-alert icon with more padding from https://materialdesignicons.com/
warning_icon = os.path.dirname(__file__) + "/alert.png"

time_file = os.path.dirname(__file__) + "/total_today_time"

total_minutes = 0


def get_current_date():
    return time.strftime("%Y-%m-%d")


def write_to_time_file():
    with open(time_file, 'w') as wf:
        wf.write(str(total_minutes) + " " + get_current_date())


def min_to_human_readable(m):
    hours, minutes = divmod(m, 60)
    return "{:02}:{:02}".format(hours, minutes)


def setup_variables_from_time_file():
    global total_minutes
    if os.path.isfile(time_file):
        with open(time_file) as f:
            lines = f.read().replace('\n', '').split(' ')
            total_minutes = int(lines[0])
            old_date = lines[1]
        if old_date != get_current_date():
            total_minutes = 0
    else:
        total_minutes = 0
        write_to_time_file()


def set_label_text(label):
    """Returns the hours from the total_minutes so it can be checked if the
    limit was exceeded"""
    hours, minutes = divmod(total_minutes, 60)
    text = "{:02}:{:02}".format(hours, minutes)
    label.set_label(text, text)
    return hours


def update_time_file():
    global total_minutes
    total_minutes += 1
    with open(time_file) as f:
        lines = f.read().replace('\n', '').split(' ')
        old_date = lines[1]
    if old_date != get_current_date():
        total_minutes = 0
    write_to_time_file()
