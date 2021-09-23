# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:37:40 2021

@author: las_v
"""

from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window


Window.clearcolor = (1,1,1,1)


        
class Frame(Widget):
    pass    
class Logo(Widget):
    pass    
            
class DataVisu(App):
    def build(self):

        root = GridLayout(cols = 1)
        root.add_widget(Frame())
        root.add_widget(Logo())
        # root.add_widget(Image(source ="DataVisu.jpeg"))
        # self.start_page = Label(text = "Data Scince Program", color = [1,0,1,1])
        # self.root.add_widget(self.start_page)
        return root
    
    
    
    
    
if __name__ == "__main__":
      DataVisu().run()