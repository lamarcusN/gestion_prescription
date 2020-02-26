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
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


# MainWondaw : Classe principale de l'application.
# Définit les fonctionnalités de la fenêtre principale de l'application

class MainWondaw(Screen):

    def connect(self):
        sm.current = "indentification"

    def validate(self):
        sm.current = "renseignementPatient"

# identification : s'occupe du système d'authenfication au niveau de
#       l'application.
class Identification(Screen):
    pass

# Traite les demandes de renseignement sur un patient, un médecin ou
#       un médicament.
class Renseignement(Screen):
    pass

# Renseignement sur un patient donnée.
class RenseignementPatient(Screen):
    pass

# Gère l'ajoute un patient dans la base de données.
class AddPatient(Screen):
    pass

# Le constat fait par le médecin
class Constat(Screen):
    pass

# Renseignement sur un médecin
class RenseignementMadicament(Screen):
    pass

# Renseignement sur une maladie
class RenseignementMaladie(Screen):
    pass

# Les maladies trouvées en fonctions des symptômes renseignés.
class MaladieFind(Screen):
    pass

class RecapVisite(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("application.kv")

sm = WindowManager()

sm.add_widget(MainWondaw(name="main"))
sm.add_widget(Identification(name="indentification"))
sm.add_widget(RenseignementPatient(name="renseignementPatient"))
sm.add_widget(RenseignementPatient(name="renseignement"))
sm.add_widget(AddPatient(name="addPatient"))
sm.add_widget(Constat(name="constat"))
sm.add_widget(MaladieFind(name="maladieFind"))

sm.current = "main"

class Application(App):

    def build(self):
        return sm


if __name__ == '__main__':
    Application().run()
