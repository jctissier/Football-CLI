#!/usr/bin/python
import requests
import warnings
from bs4 import BeautifulSoup
from termcolor import colored, cprint
import praw
import re

# Get rid of warning messages
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Top League URLs
epl = "national/england/premier-league/20162017/regular-season/r35992/?ICID=TN_02_01_01"
liga = 'national/spain/primera-division/20162017/regular-season/r35880/?ICID=TN_02_01_03'
bundesliga = 'national/germany/bundesliga/20162017/regular-season/r35823/?ICID=TN_02_01_04'
ligue_1 = 'national/france/ligue-1/20162017/regular-season/r35879/?ICID=TN_02_01_05'
serie_A = 'national/italy/serie-a/20162017/regular-season/r36003/?ICID=SN_01_03'

#Champions League
group_stage = 'http://ca.soccerway.com/international/europe/uefa-champions-league/20162017/group-stage/group-'
groups = ['a/g10275/', 'b/g10276', 'c/g10277', 'd/g10278', 'e/g10279', 'f/g10280', 'g/g10281', 'h/g10282']
group_stage_topstats = 'http://ca.soccerway.com/international/europe/uefa-champions-league/20162017/group-stage/r35551/'

# Globals
space = "   "                                                           # Used to prettify formatting
scraper_url = 'http://ca.soccerway.com/'                                # Default url for the web scraper
r = praw.Reddit(user_agent="Football-CLI")                              # Reddit instance


# Menu launched on start
class main:
    def __init__(self):
        self.choose_menu()

    def choose_menu(self):
        menu = colored("\nMain Menu:\n[1]Standings  [2]Match Scores  [3]Top Scorers  [4]Champions League  "
                       "[5]Live Streams  [6]Highlights  [7]Exit"
                       "\n", 'red', attrs=['bold'])
        choose_menu = input(menu)
        menu_guard = ["1", "2", "3", "4", "5", "6", "7"]
        while choose_menu not in menu_guard:
            choose_menu = input(menu)
        if choose_menu == "1":
            ChooseMenu.choose_class(self, class_name="Standings")
        elif choose_menu == "2":
            ChooseMenu.choose_class(self, class_name="MatchScores")
        elif choose_menu == "3":
            ChooseMenu.choose_class(self, class_name="TopStats")
        elif choose_menu == "4":
            ChooseMenu.choose_method_championsleague(self)
            main.choose_menu(self)
        elif choose_menu == "5":
            LiveStreams()
        elif choose_menu == "6":
            Highlights()
        elif choose_menu == "7":
            cprint("Bye", 'yellow')


# Menu chooser for all the classes & methods - requires user input
class ChooseMenu:
    def choose_class(self, class_name):
        if class_name == "Standings":
            ChooseMenu.choose_method(self, class_name="Standings")
        elif class_name == "MatchScores":
            ChooseMenu.choose_method(self, class_name="MatchScores")
        elif class_name == "TopStats":
            ChooseMenu.choose_method(self, class_name="TopStats")

    def choose_method_championsleague(self):
        menu = colored("Champions League: \n[1]Group Stage Standings  [2]Group Stage Results  [3]Results by Group"
                       "  [4]TopScorers  [5]Main Menu\n", 'red', attrs=['bold'])
        choose_menu = input(menu)
        menu_guard = ["1", "2", "3", "4", "5"]
        while choose_menu not in menu_guard:
            choose_menu = input(menu)
        if choose_menu == "1":
            for x in range(0,8):
                ChampionsLeague.champions_league_groupstage(self, group_stage + groups[x], group_name=groups[x][0])
        elif choose_menu == "2":
            MatchScores.match_details(self, index=0, league_url=group_stage_topstats, league_name='Champions League')
        elif choose_menu == "3":
            for x in range(0,8):
                cprint("\nRetrieving Match Scores for Champions League Group " + groups[x][0].title(), 'yellow')
                MatchScores.match_details(self, index=0, league_url= group_stage + groups[x], league_name="")
        elif choose_menu == "4":
            TopStats.top_scorers(self, group_stage_topstats, league_name='Champions League')
        elif choose_menu == "5":
            pass

    def choose_method(self, class_name):
        menu = colored("Which League do you want?\n[1]EPL  [2]Liga BBVA  [3]Serie A  [4]Ligue 1  "
                       "[5]Bundesliga  [6]Main Menu\n", 'red', attrs=['bold'])
        choose_menu = input(menu)
        menu_guard = ["1", "2", "3", "4", "5", "6"]
        while choose_menu not in menu_guard:
            choose_menu = input(menu)
        if choose_menu == "1":
            ChooseMenu.run_method(self, class_name, epl, league_name='Premier League')
        elif choose_menu == "2":
            ChooseMenu.run_method(self, class_name, liga, league_name='Liga BBVA')
        elif choose_menu == "3":
            ChooseMenu.run_method(self, class_name, serie_A, league_name='Serie A')
        elif choose_menu == "4":
            ChooseMenu.run_method(self, class_name, ligue_1, league_name='Ligue 1')
        elif choose_menu == "5":
            ChooseMenu.run_method(self, class_name, bundesliga, league_name='Bundesliga')
        elif choose_menu == "6":
            main()

    def run_method(self, class_name, league_url, league_name):
        if class_name == "Standings":
            Standings.standings(self, scraper_url + league_url, league_name)
            main.choose_menu(self)
        elif class_name == "MatchScores":
            cprint("Retrieving Match Scores and Details for " + league_name + "...\n", 'yellow')
            MatchScores.match_details(self, index=0, league_url= scraper_url + league_url, league_name =league_name)
            main.choose_menu(self)
        elif class_name == "TopStats":
            TopStats.top_scorers(self, scraper_url + league_url, league_name)
            main.choose_menu(self)


# Standings for Champions League Group Stages A-H
class ChampionsLeague():
    def champions_league_groupstage(self, group_number, group_name):
        r = requests.get(group_number)
        soup = BeautifulSoup(r.content, "lxml")
        cprint("\nChampions League Group " + group_name.capitalize(), 'red', attrs=['bold'])
        cprint("Rank  Team Name            MP  W   D   L  GD  Pts ", 'red', attrs=['bold', 'underline'])
        try:
            for x in range(0, 8):
                team_name = soup.find_all("td", {"class": "text team large-link"})[x].text
                match_played = soup.find_all("td", {"class": "number total mp"})[x].text
                wins = soup.find_all("td", {"class": "number total won total_won"})[x].text
                draws = soup.find_all("td", {"class": "number total drawn total_drawn"})[x].text
                losses = soup.find_all("td", {"class": "number total lost total_lost"})[x].text
                goal_diff = soup.find_all("td", {"class": "number total lost total_lost"})[x].text
                points = soup.find_all("td", {"class": "number points"})[x].text
                stats = ("{:<18}".format(team_name), space, match_played, space, wins, space, draws, space, losses,
                        space, goal_diff, space, points, space)
                if x == 0 or x == 1:
                    cprint(" " + str(x + 1) + ".   " + str("".join(stats)), 'green')
                if x == 2 or x == 3:
                    print(" " + str(x + 1) + ".   " + str("".join(stats)))
        except IndexError:
            pass


# Retrieves up-to-date standings for top 5 leagues
class Standings:
    def standings(self, league_url, league_name):
        cprint("Retrieving Standings for " + league_name + "...\n", 'yellow')
        r = requests.get(league_url)
        soup = BeautifulSoup(r.content, "lxml")
        cprint("Rank   Team Name           MP  W   D   L  GD  Pts ", 'red', attrs=['bold', 'underline'])
        try:
            for x in range(0, 21):
                team_name = soup.find_all("td", {"class": "text team large-link"})[x].text
                match_played = soup.find_all("td", {"class": "number total mp"})[x].text
                wins = soup.find_all("td", {"class": "number total won total_won"})[x].text
                draws = soup.find_all("td", {"class": "number total drawn total_drawn"})[x].text
                losses = soup.find_all("td", {"class": "number total lost total_lost"})[x].text
                goal_diff = soup.find_all("td", {"class": "number total lost total_lost"})[x].text
                points = soup.find_all("td", {"class": "number points"})[x].text
                stats = ("{:<18}".format(team_name), space, match_played, space, wins, space, draws, space, losses,
                         space, goal_diff, space, points, space)
                if x + 1 == 1:                                                          # 4 if-statements for formatting
                    cprint(" " + str(x + 1) + ".   " + str("".join(stats)), 'green')
                elif 1 < x + 1 < 10:
                    cprint(" " + str(x + 1) + ".   " + str("".join(stats)), 'blue')
                elif 9 < x + 1 < 18:
                    cprint(" " + str(x + 1) + ".  " + str("".join(stats)), 'blue')
                elif 18 <= x + 1 <= 20:
                    cprint(" " + str(x + 1) + ".  " + str("".join(stats)), 'red')
        except IndexError:
            print("\n")
            pass


# Prints formatted dates, teams, scores, and game details for a particular game
class MatchScores:
    def match_details(self, index, league_url, league_name):
        r = requests.get(league_url)
        soup = BeautifulSoup(r.content, "lxml")
        for x in range(index, 20):
            try:                                                                        # Try block for all games
                day = soup.find_all("td", {"class": "day no-repetition"})[x].text
                date = soup.find_all("td", {"class": "date no-repetition"})[x].text
                team_a = soup.find_all("td", {"class": "team team-a "})[x].text
                score = soup.find_all("td", {"class": "score-time score"})[x].text
                team_b = soup.find_all("td", {"class": "team team-b "})[x].text
                all_games = (day, " ", date, space, "{:<18}".format(team_a.strip()), score.strip(), space,
                             "{:<18}".format(team_b.strip()))
                print("\n")
                cprint(("".join(all_games)), 'red', attrs=['bold'])
                cprint("Match Details:", 'blue', attrs=['bold'])
                get_href = soup.find_all("td", {"class": "events-button button first-occur"})[x]
                for link in soup.find_all('a'):
                    if link in get_href:
                        r = requests.get('http://ca.soccerway.com/' + link.get('href'))
                        soup = BeautifulSoup(r.content, "lxml")
                        try:                                                            # try block for game details
                            for y in range(0, 15):
                                player_left = soup.find_all("td", {"class": "player player-a"})[y].text
                                detail_score = soup.find_all("td", {"class": "event-icon"})[y].text
                                player_right = soup.find_all("td", {"class": "player player-b"})[y].text
                                if hasattr(player_left, 'property'):                    # Avoids attribute exceptions
                                    pass
                                if hasattr(player_right, 'property'):                   # Avoids attribute exceptions
                                    pass
                                all_details = ("{:<42}".format(player_left.strip()),
                                               detail_score, space, player_right.strip())
                                cprint((space + "".join(all_details)), 'blue')
                        except IndexError:
                            index = x + 1
                            MatchScores.match_details(self, index, league_url, league_name)
            except IndexError:
                pass


# Prints formatted top scorers and top assists in a particular league/competition
class TopStats:
    def top_scorers(self, league_url, league_name):
        cprint("\nRetrieving Top Scorers for " + league_name + "...", 'yellow')
        cprint("Rank   Player                 Team            Goals", 'red', attrs=['bold', 'underline'])
        r = requests.get(league_url)
        soup = BeautifulSoup(r.content, "lxml")
        try:
            for x in range(0, 15):
                player_name = soup.find_all("td", {"class": "player large-link"})[x].text
                team_name = soup.find_all("td", {"class": "team large-link"})[x].text
                goals_count = soup.find_all("td", {"class": "number goals"})[x].text
                if x < 9:
                    topscorer = "{:<20}".format(player_name), space, "{:<15}".format(team_name), space, goals_count
                    cprint(" " + str(x + 1) + ".    " + str("".join(topscorer)), 'blue')
                elif 9 <= x:
                    topscorer = "{:<20}".format(player_name), space, "{:<15}".format(team_name), space, goals_count
                    cprint(" " + str(x + 1) + ".   " + str("".join(topscorer)), 'blue')
        except IndexError:
            pass



# Scrapes subreddit in Reddit to display URLs to live streams (when available) based on user input
class LiveStreams:
    def __init__(self):
        self.find_streams()
        main()

    def find_streams(self):
        subreddit = r.get_subreddit('soccerstreams')
        cprint("Live games that you can stream...\n", 'yellow')
        count = 0
        for submission in subreddit.get_hot(limit=20):
            if "Match Thread" in submission.title:
                print(colored("Game Name:", 'blue',attrs=['bold']) + " " + submission.title[13:])
                count -= 1
            else:
                count += 1
        if count == 2:
            cprint("There are currently no live games for streaming, please try again later...", 'yellow')
            main.choose_menu(self)
        game_name = input(colored("\n\nEnter the name of the game you want to watch (Any team's name that you see above"
                                  " will work) [1]Exit: \n", 'red', attrs=['bold']))
        for submission in subreddit.get_hot(limit=40):
            if re.search(game_name, submission.title, re.IGNORECASE):
                print(colored("\nTitle: ",'blue', attrs=['bold']), submission.title,
                      colored("\nLink: ",'blue', attrs=['bold']), submission.url, "\nPick your link!\n")
                comments = submission.comments
                for comment in comments[1:8]:                       # Skip first comment because it's a bot moderator
                    if "acestream" not in comment.body:             # Don't include acestream links
                        print(comment.body.strip())                 # Prints top comments starting from 2nd top comment
            elif game_name == "1":
                pass

# Scrapes subreddit in reddit to display URLs to game highlights based on user input
class Highlights:
    def __init__(self):
        self.choose_highlights()
        main()

    def choose_highlights(self):
        subreddit = r.get_subreddit("footballhighlights")
        print("\n")
        for submission in subreddit.get_hot(limit=50):              # Finds first 50 posts in the subreddit
            if "vs" in submission.title:
                date = submission.title[-11:]
                game_name = submission.title[:-13]
                if "Premier League" in submission.title:            # All string/color formatting for convenience
                    game_string = game_name.replace("– Premier League", "")
                    print(colored("{:<28}".format("Premier League Highlights:"), 'red', attrs=['bold']),
                          date, " ", game_string)
                elif "La Liga" in submission.title:
                    game_string = game_name.replace("– La Liga", "")
                    print(colored("{:<28}".format("La Liga Highlights:"), 'green', attrs=['bold']),
                          date, " ", game_string)
                elif "Bundesliga" in submission.title:
                    game_string = game_name.replace("– Bundesliga", "")
                    print(colored("{:<28}".format("Bundesliga Highlights:"), 'cyan', attrs=['bold']),
                          date, " ", game_string)
                elif "Ligue 1" in submission.title:
                    game_string = game_name.replace("– Ligue 1", "")
                    print(colored("{:<28}".format("Ligue 1 Highlights:"),'yellow',attrs=['bold']),
                          date, " ", game_string)
                elif "Serie A" in submission.title:
                    game_string = game_name.replace("– Serie A", "")
                    print(colored("{:<28}".format("Serie A Highlights:"), 'magenta', attrs=['bold']),
                          date, " ", game_string)
                elif "MLS" in submission.title:
                    game_string = game_name.replace("– MLS", "")
                    print(colored("{:<28}".format("MLS Highlights:"), 'blue', attrs=['bold']),
                          date, " ", game_string)
                elif "Super Lig" in submission.title:
                    game_string = game_name.replace("- Super Lig", "")
                    print(colored("{:<28}".format("Super Lig Highlights:"), 'blue', attrs=['bold']),
                          date, " ", game_string)
                elif "Eredivisie" in submission.title:
                    game_string = game_name.replace("– Eredivisie", "")
                    print(colored("{:<28}".format("Eredivisie Highlights:"), 'blue', attrs=['bold']),
                          date, " ", game_string)
                elif "Europa League" in submission.title:
                    game_string = game_name.replace("– UEFA Europa League", "")
                    print(colored("{:<28}".format("Europe League Highlights:"), 'grey', attrs=['bold']),
                          date, " ", game_string)
                elif "Champions League" in submission.title:
                    game_string = game_name.replace("– UEFA Champions League", "")
                    print(colored("{:<28}".format("Champions League Highlights:"), 'grey', attrs=['bold']),
                          date, " ", game_string)
                elif " " in submission.title:
                    print(colored("{:<28}".format("Other Highlights:"), 'blue', attrs=['bold']), date, " " ,
                          game_name)
        highlight = input(colored("\nWhich game highlights do you want (Search by Team Name)?\n"
                                  "", 'red', attrs=['bold']))
        for submission in subreddit.get_hot(limit=100):              # Searches first 100 posts based on search criteria
            if re.search(highlight, submission.title, re.IGNORECASE):
                colored_title = colored("\nTitle:", 'blue', attrs=['bold', 'bold'])
                colored_title2 = colored(" " + submission.title, 'blue')
                print(colored_title + colored_title2, "\n", submission.selftext)


# Starts the Program
if __name__ == "__main__":
    main()


