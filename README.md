# Python3 script to log and display today's uptime

For Elementary OS and Ubuntu.

Displays today's uptime with Gtk's AppIndicator3 library and displays a warning icon once a certain amount of hours (by default 5) are exceeded.

## Notes

* Use the `ubuntu` branch if you want to use it there. It uses different icons because the 1px transparent icon shifts the menu bar noticeably while it is barely visible on Elementary OS
* Because of many crash reasons in my `last` log, every 60 seconds using `GLib.timeout_add_seconds(60, self.handler_timeout)` a variable is incremented and written to the `total_today_time` file to track the uptime
  * This also means that the script has to be kept running to log the uptime and very likely does not work for laptops
* If you want to adjust the limit, change `today_hour_limit` in `main.py`

## Screenshots

![](https://github.com/Gira-X/elementary-os-uptime-indicator/raw/elementaryos/screenshots/1.png)
![](https://github.com/Gira-X/elementary-os-uptime-indicator/raw/elementaryos/screenshots/2.png)
