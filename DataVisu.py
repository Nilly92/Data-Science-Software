# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:37:40 2021

@author: las_v
"""


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder


Window.clearcolor = (1, 1, 1, 1)




class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

kv = Builder.load_file("DataVisu.kv")

class DataVisu(App):
    def build(self):

        return kv


if __name__ == "__main__":
    DataVisu().run()
