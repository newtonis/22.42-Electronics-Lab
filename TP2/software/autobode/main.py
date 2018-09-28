"""
Auto-Bode

Dependencias:
    - pyvisa
    - kivy
    - numpy
    - Keysight connection expert

Los archivos de salida son almacenados en la caperta 'output'
"""

import visa
from kivy import Config
from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
import bode
import gen, osc
from menus import *

# To configure kivy
Config.set('graphics', 'multisamples', '0')


# Graphics structure
Builder.load_file("test.kv")


class MainApp(App):
    """
        Control principal de la interfaz de usuario, todas los eventos principales son llamados desde aqui
    """

    # Instancias de generador y osciloscopio
    my_osc = osc.Oscilloscope()
    my_gen = gen.Gen()

    # Encargado de la administracion de las mediciones
    bode = bode.Bode()

    # Entidades graficas de cada menu
    my_screenmanager = ScreenManager()
    container_box = ContainerBox(name='screen1')
    bode_menu = BodeMenu(name='screen2')
    meas_menu = MeasMenu(name='screen3')
    end_menu = EndMenu(name='screen4')

    # Informacion retenida de algunos menus, requerida por otros
    data = dict()

    def build(self):
        # Inicializamos los menus, les damos una instancia de MainApp para que puedan controlar las transcisiones
        self.bode_menu.set_main_ref(self)
        self.container_box.set_main_ref(self)
        self.meas_menu.set_main_ref(self)
        self.end_menu.set_main_ref(self)

        self.my_screenmanager.add_widget(self.container_box)
        self.my_screenmanager.add_widget(self.bode_menu)
        self.my_screenmanager.add_widget(self.meas_menu)
        self.my_screenmanager.add_widget(self.end_menu)

        return self.my_screenmanager

    def connect(self, osc, gen, filename, mode):
        print("mod=", mode)
        m = 10**6
        self.data["filename"] = filename

        self.my_osc.connect(osc)
        self.my_gen.connect(gen)

        self.bode.set(self.my_osc, self.my_gen)
        self.bode.start(self.data["start_freq"],
                        self.data["end_freq"],
                        self.data["points"],
                        self.data["v_input"],
                        self.data["time_delay"],
                        self.data["res"],
                        mode=mode)

    def set_data(self, key, content):
        self.data[key] = content

    def get_data(self, key):
        return self.data[key]

    def update(self, dt):
        if self.bode.update():
            print("Fininshed ")
            self.my_screenmanager.current = 'screen4'
            self.bode.save_csv(self.data["filename"])

        self.meas_menu.update(self.bode.get_data())

    def cancel(self):
        print("Cancelling")
        self.bode.cancel()
        self.my_screenmanager.current = 'screen2'

    def restart(self):
        self.bode.cancel()
        self.my_screenmanager.current = 'screen1'


mainApp = MainApp()

Clock.schedule_interval(mainApp.update, TIME_UPDATE)

if __name__ == '__main__':
    mainApp.run()
