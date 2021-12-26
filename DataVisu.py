# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:37:40 2021

@author: las_v
"""


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from kivy.uix.label import Label
from kivy.core.text import Text
from kivy.uix.accordion import Accordion

Window.clearcolor = (1, 1, 1, 1)




class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass


py = Builder.load_file("Data_Science_Software.py")
kv = Builder.load_file("DataVisu.kv")

class DataVisu(App):
    def build(self):

        return 


if __name__ == "__main__":
    DataVisu().run()
