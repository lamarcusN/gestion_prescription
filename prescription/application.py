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
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from entity.MedecinEntity import MedecinEntity
from entity.LoginEntity import LoginEntity
from acces_donnees.LoginDAO import LoginDAO
import hashlib
from kivy.core.window import Window

Window.size = (850, 650)


# MainWondaw : Classe principale de l'application.
# Définit les fonctionnalités de la fenêtre principale de l'application

class MainWondaw(Screen):

    def connect(self):
        sm.current = "indentification"

    def validate(self):
        sm.current = "renseignementPatient"


### SECTION QUI VOUS CONCERNE ####

# identification : s'occupe du système d'authenfication au niveau de
#       l'application.
class Identification(Screen):
    ident = ObjectProperty(None)
    passwd = ObjectProperty(None)
    def checkLogin(self):
        loginE = LoginEntity(self.ident.text,
                self.hashPassword(self.passwd.text))
        logDAO = LoginDAO()
        medecinE = logDAO.connexion(loginE)
        if (medecinE == None):
            self.ident.text = ''
            invalidForm()
        else:
            print("Connexion OK : ")
            #print(medecinE.getNomMedecin())
            self.passwd.text = ''
            sm.current = "renseignementPatient"

    # hashPassword()
    # Renvoie une chaine hashée selon l'algo MD5 du mot passé en paramètre
    def hashPassword(self, mot):
        hashtext = hashlib.md5(mot.encode())
        return hashtext.hexdigest()

def invalidForm():
    pop = Popup(title = 'Erreur Login',
                content=Label(
                        text='Mot de passe ou identifiant incorrect!',
                        halign='center'),
                size_hint=(None,None), size=(400,180))
    pop.open()

# Renseignement sur un patient donnée.

class Renseignement(Screen):
    pass

class RecherchePatient(Screen):
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

class RenseignementPatient(Screen):
    pass

# Les maladies trouvées en fonctions des symptômes renseignés.
class MaladieFind(Screen):
    pass

class RecapVisite(Screen):
    pass

class WindowManager(ScreenManager):
    pass



## FIN DE LA SECTION ##########






# Listviewer

class SelectableBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        # l = ["Marc", "Henri", "Ning", "William"]
        self.data = []

    def update_Data(self, text):
        if len(text) != 0 and len(text) < 2:
            print(text, "HERE")
            self.data = [{'text': str(x)}
                         for x in ["Stark", "Vision", "Thor", "Hunter"]]
        elif len(text) >= 2:
            print(text, "GOAL")
            self.data = [{'text': str(x)}
                         for x in ["Panther", "Wonda", "Focon", "Furry"]]
        elif len(text) == 0:
            self.data = []


class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def update_Data(self):
        print("Nous y sommes")

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''

        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''

        self.selected = is_selected

kv = Builder.load_file("application.kv")

sm = WindowManager()

sm.add_widget(MainWondaw(name="main"))
sm.add_widget(Identification(name="indentification"))
sm.add_widget(RecherchePatient(name="recherchePatient"))
sm.add_widget(Renseignement(name="renseignement"))
sm.add_widget(AddPatient(name="addPatient"))
sm.add_widget(RenseignementMadicament(name="renseignementMadicament"))
sm.add_widget(RenseignementMaladie(name="renseignementMaladie"))
sm.add_widget(RenseignementPatient(name="renseignementPatient"))
sm.add_widget(Constat(name="constat"))
sm.add_widget(MaladieFind(name="maladieFind"))
sm.add_widget(RecapVisite(name="recapVisite"))

sm.current = "main"

class Application(App):

    def build(self):
        return sm


if __name__ == '__main__':
    Application().run()
