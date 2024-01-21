from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager 
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import webbrowser
from kivy.core.window import Window





class Content(BoxLayout):
    manager = ObjectProperty()
    nav_drawer = ObjectProperty()



class Demo(ScreenManager):
   pass
class Main(MDApp):
    def build(self):
        Window.size=[400,600]
        Builder.load_file("layout.kv")
        return Demo()
if __name__== "__main__":  
    app = Main()
    app.run()

