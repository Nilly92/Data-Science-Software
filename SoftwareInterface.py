# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:37:40 2021

@author: las_v
"""

from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image


class GridLay(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Image(source ="Logo.jpg"))
        self.box = BoxLayout(orientation='vertical')
        self.button1 = Button(text="Load The File")
        self.button2 = Button(text="Chose The Data Visualization Graph Type")
        self.save = Button(text="Close")
        self.box.add_widget(self.button1)
        self.box.add_widget(self.button2)
        self.box.add_widget(self.save)
        self.add_widget(self.box)



class DataVisu(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.connect_page = ConnectPage()
        screen = Screen(name="Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        #return self.screen_manager



if __name__ == "__main__":
    DataVisu().App()