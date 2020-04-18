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
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.scrollview import ScrollView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from entity.MedecinEntity import MedecinEntity
from entity.LoginEntity import LoginEntity
from acces_donnees.LoginDAO import LoginDAO
from kivy.uix.checkbox import CheckBox
import hashlib
from kivy.core.window import Window

Window.size = (850, 640)

kv = Builder.load_file("application.kv")

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
    enabled = BooleanProperty(True)
    recherche_patient = ObjectProperty(None)
    patient = None

    #def setName_Patient(text):
        #RecherchePatient.patient.text = text
        #RecherchePatient.patient.parent.parent.parent.ids['valide_name_patient'].set_disabled(False)

# Gère l'ajoute un patient dans la base de données.
class AddPatient(Screen):
    pass

# Le constat fait par le médecin
class Constat(Screen):
    pass

# Renseignement sur un médecin
class RenseignementMedicament(Screen):
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


sm = WindowManager()

sm.add_widget(MainWondaw(name="main"))
sm.add_widget(Identification(name="indentification"))
sm.add_widget(RecherchePatient(name="recherchePatient"))
sm.add_widget(Renseignement(name="renseignement"))
sm.add_widget(AddPatient(name="addPatient"))
sm.add_widget(RenseignementMedicament(name="renseignementMedicament"))
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
