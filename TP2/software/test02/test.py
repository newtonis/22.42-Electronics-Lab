from kivy import Config

Config.set('graphics', 'multisamples', '0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import *
from kivy.properties import *
from kivy.uix.label import *
from kivy.uix.button import *
from kivy.uix.listview import *
from kivy.uix.anchorlayout import *
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.listview import ListView


from math import *

import numpy as np

Builder.load_file("test.kv")

wait_time_scale = np.linspace(0.001, 1, 10000)
points_scale = np.linspace(10, 100, 100)
freq_scale = np.logspace(0, 6.3, 1000)


def get_rel_pos(rel, arr):
    if rel == 1:
        return arr[-1]
    return arr[int(rel*len(arr))]


def round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(abs(x))))-1)


def convert_seconds(value):
    value = round_sig(value, 1)
    if value < 0.1:
        return "%3d ms" % (value*1000)
    else:
        return "%.2f s" % value


def convert_freq(value):
    value = round_sig(value,1)
    if value < 1000:
        return "%3d Hz" % value
    if value < 1000 * (10**3):
        return "%.1f KHz" % (value/1000.0)
    return "%.1f MHz" % (value/float(10**6))


class SelectionItemA(BoxLayout):
    label_text = StringProperty("Default value")
    value_text = StringProperty("0.1")
    value = NumericProperty(0.5)

    def __init__(self, **kwargs):
        super(SelectionItemA, self).__init__(**kwargs)

    def begin(self, title):
        self.ids.Title.text = title

    def touch_action(self):
        self.update_action()

    def update_action(self):
        pass

    def set_value_text(self, text):
        self.value_text = text

    def set_text(self, text):
        self.label_text = text

    def get_value(self):
        return self.value


class WaitTimeMenu(SelectionItemA):

    def __init__(self, **kwargs):
        super(WaitTimeMenu, self).__init__(**kwargs)
        self.set_text("Wait time")
        self.update_action()

    def update_action(self):
        value = get_rel_pos(self.get_value(), wait_time_scale)
        self.set_value_text(convert_seconds(value))


class PointsMenu(SelectionItemA):
    def __init__(self, **kwargs):
        super(PointsMenu, self).__init__(**kwargs)
        self.set_text("Points")
        self.update_action()

    def update_action(self):
        value = get_rel_pos(self.get_value(), points_scale)
        self.set_value_text("%d" % value)


class EndFreqMenu(SelectionItemA):
    def __init__(self, **kwargs):
        super(EndFreqMenu, self).__init__(**kwargs)
        self.set_text("End freq.")
        self.update_action()

    def update_action(self):
        value = get_rel_pos(self.get_value(), freq_scale)
        self.set_value_text(convert_freq(value))


class StartFreqMenu(SelectionItemA):
    def __init__(self, **kwargs):
        super(StartFreqMenu, self).__init__(**kwargs)
        self.set_text("Start freq.")
        self.update_action()

    def update_action(self):
        value = get_rel_pos(self.get_value(), freq_scale)
        self.set_value_text(convert_freq(value))


class StartButton(Button):
    screenmanager = ObjectProperty()
    press_action = None

    def set_press_action(self, action):
        self.press_action = action

    def release_action(self):
        if self.press_action:
            self.press_action()


class MyItemButton(ListItemButton):
    pass


class SelectProperty(BoxLayout):
    title_text = StringProperty("Default value")
    items = ListProperty()

    def set_title(self, text):
        self.title_text = text


class SelectOsc(SelectProperty):

    def __init__(self, **kwargs):
        super(SelectOsc, self).__init__(**kwargs)
        self.set_title("Osc")
        self.items = ["osc 1", "osc 2"]


class SelectGen(SelectProperty):
    def __init__(self, **kwargs):
        super(SelectGen,self).__init__(**kwargs)
        self.set_title("Gen")
        self.items = ["gen 1", "gen 2", "gen 3"]


class ContinueMenu(BoxLayout):
    start_action = None
    back_action = None

    def start(self):
        if self.start_action:
            self.start_action()

    def back(self):
        if self.back_action:
            self.back_action()


class ContainerBox(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)
        self.ids.StartButton.set_press_action(self.go_next_menu)

    def go_next_menu(self):
        self.manager.current = 'screen2'


class BodeMenu(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super(BodeMenu, self).__init__(**kwargs)
        self.ids.ContinueMenu.start_action = self.start
        self.ids.ContinueMenu.back_action = self.back

    def on_enter(self, *args):
        pass

    def start(self):
        self.manager.current = 'screen3'

    def back(self):
        self.manager.current = 'screen1'


class MeasMenu(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super(MeasMenu, self).__init__(**kwargs)


class MainApp(App):

    def build(self):
        my_screenmanager = ScreenManager()

        container_box = ContainerBox(name='screen1')
        bode_menu = BodeMenu(name='screen2')
        meas_menu = MeasMenu(name='screen3')

        my_screenmanager.add_widget(container_box)
        my_screenmanager.add_widget(bode_menu)
        my_screenmanager.add_widget(meas_menu)

        return my_screenmanager


if __name__ == '__main__':
    MainApp().run()
