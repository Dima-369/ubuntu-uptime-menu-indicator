import os
import subprocess
import time


def get_os_distributor_id():
    return subprocess.check_output("lsb_release -s --id", shell=True) \
        .decode("utf-8").strip()


os_distributor_id = get_os_distributor_id()


def get_default_icon():
    if os_distributor_id == "elementary":
        return os.path.dirname(__file__) + "/transparent.png"
    else:
        return "account_logged_in"


def get_warning_icon():
    if os_distributor_id == "elementary":
        # 'clock-alert' icon with more padding from
        # https://materialdesignicons.com/
        return os.path.dirname(__file__) + "/alert.png"
    else:
        return "ubuntuone-client-error"


# Apparently, an icon has to be set, so we can use a 1x1px transparent icon
# for Elementary OS which is barely noticeable and a check mark icon for Ubuntu
default_icon = get_default_icon()
warning_icon = get_warning_icon()

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
