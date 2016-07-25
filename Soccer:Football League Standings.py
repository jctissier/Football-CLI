# Football Cli
import requests
from bs4 import BeautifulSoup
from termcolor import cprint, colored

# League links
epl = "http://www.livescore.com/soccer/england/premier-league/"
liga = 'http://www.livescore.com/soccer/spain/primera-division/'
serie_a = 'http://www.livescore.com/soccer/italy/serie-a/'
ligue1 = 'http://www.livescore.com/soccer/france/ligue-1/'
bundesliga = 'http://www.livescore.com/soccer/germany/bundesliga/'


class MainMenu:
    def __init__(self):
        self.choose_menu()

    def choose_menu(self):
        menu = colored("[1]Standings  [2]Fixtures  [3]Live Scores  [4]Results  "
                       "[5]Live Streams  [6]Highlights\n", 'red', attrs=['bold'])
        choose_menu = input(menu)
        menu_guard = ["1", "2", "3", "4", "5", "6"]
        while choose_menu not in menu_guard:
            choose_menu = input(menu)
        if choose_menu == "1":
            Standings()
            MainMenu.restart(self)
        if choose_menu == "2":
            Fixtures()
            MainMenu.restart(self)
        if choose_menu == "3":
            Livescores()
            MainMenu.restart(self)
        if choose_menu == "4":
            Results()
            MainMenu.restart(self)

    def restart(self): 
        MainMenu.choose_menu(self)
