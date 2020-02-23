import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup


class Face(GridLayout):

    def connect(self):
        con = Connexion()
        con.connect()
    
    def validate(self):
        print("Is validate")

class Connexion(FloatLayout):

    def connect(self):
        show_popup()

def show_popup():
    show = Connexion()

    popupWindow = Popup(title = "Entrer vos identifiants", content = show,
                        size_hint = (None, None), size = (450, 400))

    # open popup window
    popupWindow.open()

class Application(App):
    def build(self):
        return Face()


if __name__ == '__main__':
    Application().run()
