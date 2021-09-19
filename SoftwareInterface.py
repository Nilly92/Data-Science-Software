# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:37:40 2021

@author: las_v
"""
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        #add widgets to window


        return self.window

if __name__ == "__main__":
    SayHello().run()
