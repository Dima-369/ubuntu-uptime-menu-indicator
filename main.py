import gi

from utils import *

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk, GLib
from gi.repository import AppIndicator3

today_hour_limit = 5

# to avoid setting the warning icon several times
reached_limit_for_today = False


class ShowLoggedTimeForToday:
    def __init__(self):
        self.ind = AppIndicator3.Indicator.new(
            "today-pc-time",
            default_icon,
            AppIndicator3.IndicatorCategory.APPLICATION_STATUS)

        self.ind.set_ordering_index(0)
        self.ind.set_status(AppIndicator3.IndicatorStatus.ACTIVE)

        self.menu = Gtk.Menu()
        item_quit = Gtk.MenuItem('Quit')
        item_quit.connect('activate', quit)
        self.menu.append(item_quit)
        self.menu.show_all()
        self.ind.set_menu(self.menu)

        self.update_label()
        GLib.timeout_add_seconds(60, self.handler_timeout)

    def handler_timeout(self):
        self.update_label()
        # return True so that we get called again
        return True

    def update_label(self):
        global reached_limit_for_today
        hours = set_label_text(self.ind)
        if not reached_limit_for_today:
            if hours >= today_hour_limit:
                self.ind.set_icon(warning_icon)
                reached_limit_for_today = True
        update_time_file()

    @staticmethod
    def quit():
        Gtk.main_quit()

    @staticmethod
    def main():
        Gtk.main()


if __name__ == "__main__":
    setup_variables_from_time_file()
    ind = ShowLoggedTimeForToday()
    ind.main()
