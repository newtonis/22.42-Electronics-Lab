from kivy.uix.boxlayout import *
from kivy.properties import *
from kivy.uix.button import *
from kivy.uix.switch import *
from kivy.uix.togglebutton import *
from kivy.uix.screenmanager import Screen
from auxiliar import *
from config import *



rm = visa.ResourceManager()


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

    def get_corrected_value(self):
        return round_sig(get_rel_pos(self.get_value(), wait_time_scale), 2)


class VInputMenu(SelectionItemA):
    def __init__(self, **kwargs):
        super(SelectionItemA, self).__init__(**kwargs)
        self.set_text("Input Volt.")
        self.update_action()

    def update_action(self):
        value = get_rel_pos(self.get_value(), voltage_scale)
        self.set_value_text(convert_voltage(value))

    def get_corrected_value(self):
        return round_sig(get_rel_pos(self.get_value(), voltage_scale), 2)


class PointsMenu(SelectionItemA):
    def __init__(self, **kwargs):
        super(PointsMenu, self).__init__(**kwargs)
        self.set_text("Points")
        self.update_action()

    def update_action(self):
        value = get_rel_pos(self.get_value(), points_scale)
        self.set_value_text("%d" % value)

    def get_corrected_value(self):
        return round_sig(get_rel_pos(self.get_value(), points_scale), 2)


class EndFreqMenu(SelectionItemA):
    def __init__(self, **kwargs):
        super(EndFreqMenu, self).__init__(**kwargs)
        self.set_text("End freq.")
        self.update_action()

    def update_action(self):
        value = get_rel_pos(self.get_value(), freq_scale)
        self.set_value_text(convert_freq(value))

    def get_corrected_value(self):
        return round_sig(get_rel_pos(self.get_value(), freq_scale) ,2)


class StartFreqMenu(SelectionItemA):
    def __init__(self, **kwargs):
        super(StartFreqMenu, self).__init__(**kwargs)
        self.set_text("Start freq.")
        self.update_action()

    def update_action(self):
        value = get_rel_pos(self.get_value(), freq_scale)
        self.set_value_text(convert_freq(value))

    def get_corrected_value(self):
        return round_sig(get_rel_pos(self.get_value(), freq_scale) ,2)


class ResistorMenu(SelectionItemA):
    def __init__(self, **kwargs):
        super(ResistorMenu, self).__init__(**kwargs)
        self.set_text("R value")
        self.update_action()
        self.value = 0

    def update_action(self):
        value = get_rel_pos(self.get_value(), res_scale)
        value = int(value)
        self.set_value_text(convert_res(value))

    def get_corrected_value(self):
        return int( get_rel_pos(self.get_value(), res_scale))


class LinearLog(ToggleButton):
    mode = "log"

    def __init__(self, **kwargs):
        print("hello")
        super(ToggleButton, self).__init__(**kwargs)

    def on_state(self, widget, value):
        if value == 'down':
            self.text = "Linear"
            self.mode = "linear"
        else:
            self.text = "Log"
            self.mode = "log"


class StartButton(Button):
    screenmanager = ObjectProperty()
    press_action = None

    def set_press_action(self, action):
        self.press_action = action

    def release_action(self):
        if self.press_action:
            self.press_action()


class SelectProperty(BoxLayout):
    title_text = StringProperty("Default value")
    items = ListProperty()
    selection = ListProperty()

    def __init__(self ,**kwargs):
        super(SelectProperty ,self).__init__(**kwargs)

    def set_title(self, text):
        self.title_text = text

    def get_selection(self):
        return self.ids.Options.adapter.selection


class SelectOsc(SelectProperty):
    def __init__(self, **kwargs):
        super(SelectOsc, self).__init__(**kwargs)
        self.set_title("Osc")

        rm = visa.ResourceManager()
        self.items = rm.list_resources()
        print(rm.list_resources())


class SelectGen(SelectProperty):
    gen = None

    def __init__(self, **kwargs):
        super(SelectGen, self).__init__(**kwargs)
        self.set_title("Gen")

        rm = visa.ResourceManager()
        self.items = rm.list_resources()


class ContinueMenu(BoxLayout):
    start_action = None
    back_action = None

    def start(self):
        if self.start_action:
            self.start_action()

    def back(self):
        if self.back_action:
            self.back_action()


class SampleMenu(BoxLayout):
    start_action = None
    back_action = None

    def start(self):
        if self.start_action:
            self.start_action()

    def back(self):
        if self.back_action:
            self.back_action()


class ContainerBox(BoxLayout, Screen):
    main_ref = None

    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)
        self.ids.StartButton.set_press_action(self.go_next_menu)

    def set_main_ref(self, ref):
        self.main_ref = ref

    def go_next_menu(self):
        self.main_ref.set_data("time_delay", self.ids.WaitTimeMenu.get_corrected_value())
        self.main_ref.set_data("v_input", self.ids.VInputMenu.get_corrected_value())
        self.main_ref.set_data("points", self.ids.PointsMenu.get_corrected_value())
        self.main_ref.set_data("start_freq", self.ids.StartFreqMenu.get_corrected_value())
        self.main_ref.set_data("end_freq", self.ids.EndFreqMenu.get_corrected_value())
        self.main_ref.set_data("res", self.ids.ResistorMenu.get_corrected_value())

        print(self.main_ref.data)
        self.manager.current = 'screen2'


class InfoMenu(BoxLayout):
    def __init__(self, **kwargs):
        super(InfoMenu, self).__init__(**kwargs)

    def update_data(self, sample, total, freq, amp, pha, action):
        self.ids.SampleText.text = "Sample:  " + str(sample) + "/ " + str(total)
        self.ids.FreqText.text = "Freq: " + str(freq)
        self.ids.AmpText.text = "Amp: " + str(amp) + " db"
        self.ids.PhaText.text = "Pha: " + str(pha) + " deg"
        self.ids.ActionText.text = action


class BodeMenu(BoxLayout, Screen):
    ref = None
    filename = StringProperty()

    def __init__(self, **kwargs):
        super(BodeMenu, self).__init__(**kwargs)
        self.ids.ContinueMenu.start_action = self.start
        self.ids.ContinueMenu.back_action = self.back

    def set_main_ref(self , ref):
        self.ref = ref

    def on_enter(self, *args):
        pass

    def start(self):
        print("filename:", self.ids.Filename.text)

        if len(self.ids.SelectOsc.get_selection()) == 0:
            print("No osc selected")
            return 0
        if len(self.ids.SelectGen.get_selection()) == 0:
            print("No gen selected")
            return 0
        mod = self.ids.LinearLog.mode
        osc_file = self.ids.SelectOsc.get_selection()[0]
        gen_file = self.ids.SelectGen.get_selection()[0]

        try:
            self.ref.connect(osc=osc_file.text, gen=gen_file.text, filename=self.ids.Filename.text, mode=mod)
            self.manager.current = 'screen3'

        except:
            print("Failure to connect")

    def back(self):
        self.manager.current = 'screen1'


class MeasMenu(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super(MeasMenu, self).__init__(**kwargs)
        self.ids.SampleMenu.back_action = self.cancel

    def set_main_ref(self, ref):
        self.ref = ref

    def update(self, data):
        self.ids.InfoMenu.update_data(
            sample=data["sample"],
            total=data["total"],
            freq=data["freq"],
            amp=data["amp"],
            pha=data["pha"],
            action=data["action"]
        )

    def cancel(self):
        self.ref.cancel()


class EndMenu(BoxLayout, Screen):
    def start_again(self):
        self.manager.screen = 'screen1'
        self.ref.restart()

    def set_main_ref(self, ref):
        self.ref = ref
