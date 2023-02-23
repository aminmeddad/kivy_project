# import all necessary libraries from kivy and kivyMD
from kivy.app import App
import os
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.config import Config
from kivymd.uix.button import MDFlatButton
from kivy.properties import ObjectProperty, StringProperty
from database import Database
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.uix.carousel import Carousel
from kivy.uix.gridlayout import GridLayout
from kivy.uix.switch import Switch
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.spinner import SpinnerOption
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.toast import toast
import sqlite3
from const import *
from system import *
from settings import *

import re

# Setup touchscreen
# os.environ['SDL_VIDEODRIVER']= 'fbcon'
# os.environ['SDL_FBDEV']= '/dev/fb1'
# os.environ['SDL_MOUSEDRV'] = 'TSLIB'
# os.environ["SDL_MOUSEDEV"] = '/dev/input/touchscreen'
# on X11 PC
os.environ['KIVY_WINDOW'] = 'sdl2'  # https://kivy.org/doc/stable/guide/environment.html
# os.environ['KIVY_CLIPBOARD'] = 'sdl2' #https://kivy.org/doc/stable/guide/environment.html
# os.environ['KIVY_GL_BACKEND'] = 'gl'

# for raspberry
# os.environ['KIVY_WINDOW'] = 'egl_rpi'  # https://kivy.org/doc/stable/guide/environment.html
# os.environ['KIVY_GL_BACKEND'] = 'gl'


# set window size
Config.set('graphics', 'resizable', '0')
Window.size = (480, 320)


# creation of screen
class Page1(Screen):
    pass

class Page2(Screen):
    pass

class Page3(Screen):
    pass

class Page4(Screen):
    pass

class Page5(Screen):
    pass

class Page6(Screen):
    pass

# management of the screens
class ScreenManagement(ScreenManager):
    pass

# import the kv file
presentation = Builder.load_file("interface.kv")


# main class that generates the App
class KivyForcetools(MDApp):
    database = Database()
    like_dialog = None
    fav = []
    img_list = []
    count = 0
    rootDir = 'img/games/'
    i = 1
    j = int()
    k = 0
    switcher = None
    pathpersys = []
    game_system = None
    game_settings = None
    gamepersystem = []
    im_int = BACKGROUND_NOGAME
    label_int = "No game selected"
    screens = []
    game_system = System()
    game_settings = Setting()

    def build(self):
        sm = ScreenManagement(transition=FadeTransition())
        self.screens = [Page1(name="splashscreen"), Page2(name="settings"), Page3(name="game"), Page4(name="favorites"),
                        Page5(name="par"), Page6(name="image")]
        for screen in self.screens:
            sm.add_widget(screen)
        return sm

    def on_start(self):
        for dirName, subdirList, fileList in os.walk(self.rootDir):
            self.count += 1
            self.img_list.append(f"{dirName}")
        self.root.get_screen("game").ids.image01.source = BACKGROUND_NOGAME
        self.root.get_screen("game").ids.game_label.text = self.label_int
        self.root.get_screen("favorites").ids.image02.source = BACKGROUND_NOGAME
        self.root.get_screen("favorites").ids.fav_label.text = self.label_int
        self.root.get_screen("settings").ids.jj.values = self.game_system.system
        self.initFav()

    def setCurrentSystem(self):
        if self.root.get_screen("settings").ids.jj.text == "ATOMISWAVE":
            self.game_system.index_system = 0
        elif self.root.get_screen("settings").ids.jj.text == "CHIHIRO":
            self.game_system.index_system = 1
        if self.root.get_screen("settings").ids.jj.text == "NAOMI":
            self.game_system.index_system = 2
        elif self.root.get_screen("settings").ids.jj.text == "NAOMI2":
            self.game_system.index_system = 3
        elif self.root.get_screen("settings").ids.jj.text == "TRIFORCE":
            self.game_system.index_system = 4

    def lis_gamePerSys(self):
        print("sys ind", self.game_system.index_system)
        if self.game_system.index_system == 0:
            self.gamepersystem = self.game_system.list_allGame_atomiswave
        elif self.game_system.index_system == 1:
            self.gamepersystem = self.game_system.list_allGame_Chihiro
        elif self.game_system.index_system == 2:
            self.gamepersystem = self.game_system.list_allGame_Naomi
        elif self.game_system.index_system == 3:
            self.gamepersystem = self.game_system.list_allGame_Naomi2
        else:
            self.gamepersystem = self.game_system.list_allGame_Triforce

    #######################  ################################## karim babouri et sarah hadj-mokhnache
    def img(self):
        print(f"{self.pathpersys[self.i - 1]}/covers.jpg")
        self.root.get_screen("game").ids.image01.source = f"{self.pathpersys[self.i - 1]}/covers.jpg"
        game = self.pathpersys[self.i - 1].split("/")
        self.game_system.setCurrentGame(f"{game[2]}.bin")
        self.game_system.viewInfomation
        self.root.get_screen("game").ids.game_title.text = self.game_system.game_description
        self.root.get_screen("game").ids.game_label.text = self.game_system.game_title

    ################ afficher les images de chaque jeux ###############################  karim babouri et sarah hadj-mokhnache
    def imgGame_inc(self):
        G = self.game_system.getCurrentGame()
        G = re.sub(".bin", "", G)
        chemin = f"img/games/{G}"
        if self.k == 2:
            self.k = 0
        else:
            self.k += 1
        chemin = f"{chemin}/{self.k}.jpg"
        if os.path.isfile(chemin):
            self.root.get_screen("image").ids.image.source = chemin
        else:
            try:
                self.imgGame_inc()
            except:
                self.root.get_screen("image").ids.image.source = BACKGROUND_NO_IMAGE

    ########################### Défiler les jeux ########################### karim babouri et sarah hadj-mokhnache
    def img_inc(self, n):
        for chemin in self.img_list:
            for game in self.gamepersystem:
                if chemin.endswith(f"{str(game[:len(game) - 4])}"):
                    self.pathpersys.append(chemin)
        if n == 1:
            if self.i == len(self.gamepersystem) - 1:
                self.i = 1
            else:
                self.i += 1
        else:
            if self.i == 1:
                self.i = len(self.gamepersystem) - 1
            else:
                self.i -= 1
        try:
            self.img()
        except:
            pass

    ####################################### karim babouri et sarah hadj-mokhnache
    def initFav(self):
        self.root.get_screen("favorites").ids.image02.source = BACKGROUND_NOGAME
        self.root.get_screen("favorites").ids.fav_label.text = ("")
        self.root.get_screen("favorites").ids.fav_title.text = self.label_int

    def getFav(self):
        self.root.get_screen("favorites").ids.image02.source = f"img/games/{str(self.fav[self.j])[:-4]}/covers.jpg"
        fav_game = self.fav[self.j]
        self.game_system.setCurrentfavGame(fav_game)
        self.game_system.getFavoriteInfo
        self.root.get_screen("favorites").ids.chkfav.active = True
        self.root.get_screen("favorites").ids.fav_label.text = self.game_system.fav_descr
        self.root.get_screen("favorites").ids.fav_title.text = self.game_system.fav_title
        self.game_system.setCurrentGame(f"{str(self.fav[self.j])[:-4]}.bin")

    ##################################################### karim babouri et sarah hadj-mokhnache
    def favorite_inc(self):
        self.fav = self.game_system.getFavorite
        print(self.j)
        if len(self.fav) == 0:
            self.initFav()

        else:
            if self.j == len(self.fav) - 1:
                self.j = 0
            else:
                self.j += 1
            try:
                self.getFave()
            except:
                print("Error")

    def favorite_dec(self):
        self.fav = self.game_system.getFavorite
        print(self.j)
        if len(self.fav) == 0:
            self.initFav()
        else:
            if self.j == 0:
                self.j = len(self.fav) - 1
            else:
                self.j -= 1
            try:
                self.getFave()
            except:
                pass

    ########################################################## karim babouri et sarah hadj-mokhnache

    def checkbox_click(self, instance, value):
        if value == True:
            self.game_system.addFavorite
        else:
            self.game_system.delFavorite

    def clearFavorite(self):
        self.initFav()
        self.game_system.delAllFavorite
        self.root.get_screen("favorites").ids.chkfav.active = False

    def checkfavorite(self):
        a = self.game_system.CheckExist
        if a:
            self.root.get_screen("game").ids.chk.active = True
        else:
            self.root.get_screen("game").ids.chk.active = False
        # self.checkfavorite()

    def gettxtIP(self):
        return self.root.get_screen("par").ids.ip_input.text

    def button_press(self, button):
        if len(self.gettxtIP()) <= 14:
            self.root.get_screen("par").ids.ip_input.text = f"{self.gettxtIP()}{button}"

    def ip_init(self):
        if self.game_system.index_system < 3:
            print(self.game_system.index_system)
            self.game_settings.current_ip = self.game_settings.getIpSystem("ip_naomi")
        elif self.game_system.index_system == 3:
            self.game_settings.current_ip = self.game_settings.getIpSystem("ip_chihiro")
        else:
            self.game_settings.current_ip = self.game_settings.getIpSystem("ip_triforce")
        try:
            self.root.get_screen("par").ids.ip_iplabel.text = f"{self.game_settings.current_ip}"
            self.root.get_screen(
                "par").ids.ip_machinelabel.text = f"{self.game_system.system[self.game_system.index_system]}"
        except:
            pass

    def clear(self):
        req = f'{self.root.get_screen("par").ids.ip_input.text}'
        req = req[:-1]
        self.root.get_screen("par").ids.ip_input.text = req

    def set_ip(self):
        new = f'{self.root.get_screen("par").ids.ip_input.text}'
        self.game_settings.current_indexsys = self.game_system.index_system
        if self.game_system.index_system < 3:
            sys = "ip_naomi"

        elif self.game_system.index_system == 3:
            sys = "ip_chihiro"
        else:
            sys = "triforce"

        ip = self.root.get_screen("par").ids.ip_input.text
        formatip = ip.split(".")
        self.game_settings.setNewIpAddress(formatip, sys)
        self.root.get_screen("par").ids.ip_iplabel.text = ip

    ############################# karim babouri et sarah hadj-mokhnache
    def upload(self):
        System.sendingGame(self)

    ##############################

    def ping_ip(self):
        self.ip_init()
        self.root.get_screen("par").ids.ip_pinglabel.text = "..."
        self.game_settings.pingIdAddress
        ping = self.game_settings.view_ping_success

        if ping:
            self.root.get_screen("par").ids.ip_pinglabel.text = "SUCCESS"
        else:
            self.root.get_screen("par").ids.ip_pinglabel.text = "FAIL"
        print(ping)

    ############################ karim babouri et sarah hadj-mokhnache
    def imgGo(self):
        self.switcher = self.root.current
        self.root.current = "image"

    def switch(self):
        if self.switcher == "game":
            self.root.current = "game"
        else:
            self.root.current = "favorites"

    def appli_stop(self):

        layout = GridLayout(cols=1, padding=10)
        # layout.size=(240,160)
        # layout.opacity=0.75
        popupcancel = Button(text="Cancel")
        closeButton = Button(text="Quit")

        layout.add_widget(popupcancel)
        layout.add_widget(closeButton)

        # Instantiate the modal popup and display 
        popup = Popup(title='Do you really want to quit?',
                      content=layout, auto_dismiss=False, size_hint=(None, None), size=(240, 160))
        popup.open()

        # Attach close button press with popup.dismiss action 
        popupcancel.bind(on_press=popup.dismiss)
        closeButton.bind(on_press=self.stop)


KivyForcetools().run()
