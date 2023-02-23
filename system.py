from gamelist import *
from database import *
from const import *
import triforcetools
from triforcetools import *

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class System(object, metaclass=Singleton):
    database = Database()
    #sub_navigation = "All_System"
    count_system = 0  # number of system installed
    system = []
    current_game = ""  # name game on interface for start to netdimm
    index_system = 0
    current_favgame = ""
    index_game = 0
    current_genre = ""
    index_genre = 0
    gallery = []
    index_gallery = 0
    game_title = ""
    game_player = ""
    game_system = ""
    game_description = ""
    game_editor = ""
    game_genre = ""
    game_button = ""
    fav_descr = ""
    fav_title = ""
    list_allGame_atomiswave = []
    list_allgenre_atomiswave = []
    dict_GenreGame_atomiswave = {}

    list_allGame_Naomi = []
    list_allgenre_Naomi = []
    dict_GenreGame_Naomi = {}

    list_allGame_Naomi2 = []
    list_allgenre_Naomi2 = []
    dict_GenreGame_Naomi2 = {}

    list_allGame_Triforce = []
    list_allgenre_Triforce = []
    dict_GenreGame_Triforce = {}

    list_allGame_Chihiro = []
    list_allgenre_Chihiro = []
    dict_GenreGame_Chihiro = {}

    def __init__(self):
        tmp = []
        tmp = self.sortExistRomsSystem(ATOMISWAVE)
        self.list_allGame_atomiswave = self.lis_all_and_separate_game(tmp, self.list_allgenre_atomiswave,
                                                                      self.dict_GenreGame_atomiswave)

        # Naomi all games
        tmp = []
        tmp = self.sortExistRomsSystem(NAOMI1)
        self.list_allGame_Naomi = self.lis_all_and_separate_game(tmp, self.list_allgenre_Naomi,
                                                                 self.dict_GenreGame_Naomi)

        # Naomi2 all games
        tmp = []
        tmp = self.sortExistRomsSystem(NAOMI2)
        self.list_allGame_Naomi2 = self.lis_all_and_separate_game(tmp, self.list_allgenre_Naomi2,
                                                                  self.dict_GenreGame_Naomi2)

        # Triforce all games
        tmp = []
        tmp = self.sortExistRomsSystem(TRIFORCE)
        self.list_allGame_Triforce = self.lis_all_and_separate_game(tmp, self.list_allgenre_Triforce,
                                                                    self.dict_GenreGame_Triforce)

        # Chihiro all games
        tmp = []
        tmp = self.sortExistRomsSystem(CHIHIRO)
        self.list_allGame_Chihiro = self.lis_all_and_separate_game(tmp, self.list_allgenre_Chihiro,
                                                                   self.dict_GenreGame_Chihiro)

        tmp = None

        self.countSystemPresent
        if self.count_system > 0:
            self.system.sort()

    def sortExistRomsSystem(self, system):
        tmp = []
        list_game = []
        for type_game in GAME_LIST[system][GAMES]:
            for name_game, rom_game in GAME_LIST[system][GAMES][type_game].items():
                tmp.append((name_game, rom_game, type_game))

        tmp.sort()
        for name_game, rom_game, type_game in tmp:
            list_game.append((rom_game, type_game))

        # print(self.testExistPhysicalRoms(list_game))
        return self.testExistPhysicalRoms(list_game)

    def testExistPhysicalRoms(self, list_game):
        missing = []

        for value in list_game:
            if not os.path.isfile(ROM_DIR + value[0]):
                missing.append(value)

        for missing_game in missing:
            pass #to get config page without games
            #list_game.remove(missing_game) #for release

        return list_game

    def lis_all_and_separate_game(self, list_all_game, list_all_genre_available, list_all_game_by_genre):
        tmp = []
        list_game = []

        if len(list_all_game) > 0:
            for value in list_all_game:
                list_game.append(value[0])

                if value[1] not in tmp:
                    tmp.append(value[1])
                    list_all_genre_available.append(value[1])
                    list_all_game_by_genre[value[1]] = []

                list_all_game_by_genre[value[1]].append(value[0])

            list_all_genre_available.sort()

        return list_game

    def setCurrentGame(self, name_game):
        self.current_game = name_game

    def getCurrentGame(self):
        return self.current_game

    def setCurrentfavGame(self, namegame):
        self.current_favgame = namegame

    @property
    def addFavorite(self):
        req = self.database.getcursor.execute('''SELECT * FROM favorites WHERE name_game = ?''',
                                              [self.current_game]).fetchone()

        if req is not None:
            pass
        else:
            self.database.getcursor.execute('''INSERT INTO favorites (name_game) VALUES (?)''', [self.current_game])
            self.database.getconnexion.commit()

    @property
    def delFavorite(self):
        print(self.current_game)
        self.database.getcursor.execute('''DELETE FROM favorites WHERE name_game = ?''', [self.current_game])
        self.database.getconnexion.commit()

    @property
    def delAllFavorite(self):
        self.database.getcursor.execute('''DELETE FROM favorites  ''')
        self.database.getconnexion.commit()

    @property
    def CheckExist(self):
        req = self.database.getcursor.execute('''SELECT * FROM favorites WHERE name_game = ? ''',
                                              [self.current_game]).fetchall()
        if req is not None:
            if len(req) == 0:
                return False
            else:
                return True
        else:
            return False

    @property
    def getFavorite(self):
        self.fav_game = []
        self.favorite_game = False

        req = self.database.getcursor.execute('''SELECT * FROM favorites ''').fetchall()

        if req is not None:
            if len(req) == 0:
                self.fav_game = []
            else:
                self.favorite_game = True
                for row in req:
                    self.fav_game.append(row[1])

        return self.fav_game

    @property
    def getFavoriteInfo(self):

        req = self.database.getcursor.execute(
            f"SELECT true_name,description FROM games WHERE name_game = '{self.current_favgame}'").fetchone()

        if req is not None:
            self.fav_title = req[0]
            self.fav_descr = req[1]
        else:
            self.fav_title = "No information"
            self.fav_descr = "No information"

    @property
    def incrIndexSystem(self):
        self.index_system += 1

    @property
    def decrIndexSystem(self):
        self.index_system -= 1

    @property
    def incrIndexGame(self):
        self.index_game += 1

    @property
    def decrIndexGame(self):
        self.index_game -= 1

    @property
    def incrIndexGenre(self):
        self.index_genre += 1

    @property
    def decrIndexGenre(self):
        self.index_genre -= 1

    @property
    def incrIndexGallery(self):
        self.index_gallery += 1

    @property
    def decrIndexGallery(self):
        self.index_gallery -= 1

    @property
    def viewInfomation(self):
        req = self.database.getcursor.execute('''SELECT * FROM games WHERE name_game = ?''',
                                              [self.current_game]).fetchone()

        if req is not None:
            self.game_title = req[2]
            self.game_player = req[3]
            self.game_system = req[4]
            self.game_description = req[5]
            self.game_editor = req[6]
            self.game_genre = req[7]
            self.game_button = req[8]
        else:
            self.game_title = "No Information"
            self.game_player = "No Information"
            self.game_system = "No Information"
            self.game_description = "No Information"
            self.game_editor = "No Information"
            self.game_genre = "No Information"
            self.game_button = "No Information"

    @property
    def reinitCurrentGenre(self):
        self.index_genre = 0

    # Re-Initialize index game for new display after back page
    @property
    def reinitCurrentGame(self):
        self.index_game = 0

    # Count System installed in dir roms
    @property
    def countSystemPresent(self):
        if len(self.list_allGame_atomiswave) > 0:
            self.count_system += 1
            self.system.append("ATOMISWAVE")

        if len(self.list_allGame_Naomi) > 0:
            self.count_system += 1
            self.system.append("NAOMI")

        if len(self.list_allGame_Naomi2) > 0:
            self.count_system += 1
            self.system.append("NAOMI2")

        if len(self.list_allGame_Triforce) > 0:
            self.count_system += 1
            self.system.append("TRIFORCE")

        if len(self.list_allGame_Chihiro) > 0:
            self.count_system += 1
            self.system.append("CHIHIRO")

    @property
    def getCurrentSystem(self):
        return self.system[self.index_system]

    @property
    def getCountAllSystem(self):
        return self.count_system

    @property
    def viewCoversGames(self):
        self.covers_click = True
        img_location = "%s%s/%s" % (IMAGE_GAME_DIR, self.current_game[:-4], "covers.jpg")

        # test with PNG
        if not os.path.isfile(img_location):
            img_location = "%s%s/%s" % (IMAGE_GAME_DIR, self.current_game[:-4], "covers.png")

        # No Covers, too bad..
        if not os.path.isfile(img_location):
            self.covers_click = False
            img_location = "%s%s" % (IMAGE_GAME_DIR, "no_covers.jpg")
        return img_location

    @property
    def getGallery(self):
        if os.path.isdir(IMAGE_GAME_DIR + self.current_game[:-4]):
            self.display_gallery = True
            self.gallery = []

            for pictures in os.listdir(IMAGE_GAME_DIR + self.current_game[:-4]):
                self.gallery.append(pictures)

            self.gallery.sort()
            count_gallery = len(self.gallery)

            # Index caroussel
            if self.index_gallery < 0:
                self.index_gallery = count_gallery - 1

            if self.index_gallery > count_gallery - 1:
                self.index_gallery = 0

            img = ('%s%s/%s') % (IMAGE_GAME_DIR, self.current_game[:-4], self.gallery[self.index_gallery])

    ############################# karim babouri et sarah hadj-mokhnache
    def sendingGame(self):
        print("sending")
        ip_value = (self.database.getcursor.execute("SELECT ip_naomi FROM setting").fetchone()[0], \
                    self.database.getcursor.execute("SELECT ip_triforce FROM setting").fetchone()[0], \
                    self.database.getcursor.execute("SELECT ip_chihiro FROM setting").fetchone()[0]
                    )
        print(ip_value[0])
        ip = ip_value[0]

        if len(ip) > 0:
            if os.system("ping -c 1 %s" % ip) == 0:
                triforcetools.connect(ip, 10703)
                triforcetools.HOST_SetMode(0, 1)
                triforcetools.SECURITY_SetKeycode("\x00" * 8)
                triforcetools.DIMM_UploadFile(ROM_DIR + self.current_game)
                triforcetools.HOST_Restart()
                triforcetools.TIME_SetLimit(10 * 60 * 1000)

                if self.getPicZeroVirtualKey:
                    time.sleep(1)
                    while not self.pygame.event.get():
                        triforcetools.TIME_SetLimit(10 * 60 * 1000)
                        time.sleep(1)

                triforcetools.disconnect()
