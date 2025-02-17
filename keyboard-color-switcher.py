#!/usr/bin/python3

# Imports
import gi
import sys

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_border_width(100)

        #### HeaderBar Define
        self.headerbar = Gtk.HeaderBar()
        self.set_titlebar(self.headerbar)
        self.headerbar.set_show_close_button(True)
        self.headerbar.props.title = "Keyboard Color Switcher"

        ### Hiding the About button until it's coded in.
        self.button = Gtk.Button()
        icon = Gio.ThemedIcon(name="open-menu-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        self.button.add(image)
        self.headerbar.pack_end(self.button)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.add(vbox)

        ### Label Definement
        self.aboutlabel = Gtk.Label()
        self.aboutlabel.set_text("GTK tool for changing keyboard region colors")
        self.aboutcenterlabel = Gtk.Label()
        self.aboutcenterlabel.set_text("supported models: oryp2-ess, oryp4, oryp5, serw11")
#       self.centerlabel.set_halign()

        ### Button Definement
        self.leftbutton = Gtk.ColorButton()
        self.leftlabel = Gtk.Label("Left")
        self.leftbutton.set_halign(Gtk.Align.CENTER)
        self.leftbutton.set_valign(Gtk.Align.CENTER)
        self.leftbutton.set_size_request(75, 50)

        self.centerbutton = Gtk.ColorButton()
        self.centerlabel = Gtk.Label("Center")
        self.centerbutton.set_halign(Gtk.Align.CENTER)
        self.centerbutton.set_valign(Gtk.Align.CENTER)
        self.centerbutton.set_size_request(75, 50)

        self.rightbutton = Gtk.ColorButton()
        self.rightlabel = Gtk.Label("Right")
        self.rightbutton.set_halign(Gtk.Align.CENTER)
        self.rightbutton.set_valign(Gtk.Align.CENTER)
        self.rightbutton.set_size_request(75, 50)

        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(6)
        self.grid.set_halign(Gtk.Align.CENTER)
        self.grid.set_valign(Gtk.Align.CENTER)

        ### Connect Signal handlers
        self.leftbutton.connect("clicked", self.on_button_clicked)
        self.leftbutton.connect("color-set", self.on_color_activated, "left")

        self.centerbutton.connect("clicked", self.on_button_clicked)
        self.centerbutton.connect("color-set", self.on_color_activated, "center")

        self.rightbutton.connect("clicked", self.on_button_clicked)
        self.rightbutton.connect("color-set", self.on_color_activated, "right")

        ### Grid Setup
        self.grid.attach(self.leftlabel, 0, 2, 1, 1)
        self.grid.attach(self.leftbutton, 0, 1, 1, 1)
        self.grid.attach(self.centerlabel, 1, 2, 1, 1)
        self.grid.attach(self.centerbutton, 1, 1, 1, 1)
        self.grid.attach(self.rightlabel, 2, 2, 1, 1)
        self.grid.attach(self.rightbutton, 2, 1, 1, 1)

        vbox.pack_start(self.aboutlabel, True, True, 0)
        vbox.pack_start(self.aboutcenterlabel, True, True, 0)
        vbox.pack_start(self.grid, True, True, 0)

        ### Color Grab
    def on_color_activated(self, widget, region):
        print(region)
        color = widget.get_rgba()
        red = "{0:0{1}X}".format(int(color.red*255),2)
        green = "{0:0{1}X}".format(int(color.green*255),2)
        blue = "{0:0{1}X}".format(int(color.blue*255),2)
        color_string = red + green + blue
        print(color_string)

        if region == "left":
            try:
                with open('/sys/class/leds/system76::kbd_backlight/color_left', 'w') as f_left:
                    f_left.write(color_string)
            except:
                print("Failed to set color")

        if region == "center":
            try:
                with open('/sys/class/leds/system76::kbd_backlight/color_center', 'w') as f_center:
                    f_center.write(color_string)
            except:
                print("Failed to set color")

        if region == "right":
            try:
                with open('/sys/class/leds/system76::kbd_backlight/color_right', 'w') as f_right:
                    f_right.write(color_string)
            except:
                print("Failed to set color")

    def on_button_clicked(self, widget):
        win.show_all()

class AboutWindow(Gtk.AboutDialog):

    def __init__(self):
        Gtk.AboutDialog.__init__(self)
        self.set_border_width(100)

        self.aboutdialog = Gtk.AboutDialog()
        self.aboutdialog.set_destroy_with_parent(True)
        self.aboutdialog.set_version("0.2")

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
