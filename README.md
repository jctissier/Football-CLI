#:soccer:Live Football Stats & Game Links:tv: [![Watch How it works!](https://github.com/jctissier/Football-CLI/blob/master/Documentation/watch.png)](#standings)
Python web-scraper that automatically retrieves the latest stats for major Football leagues and working streams for live games and game highlights directly from your terminal.  
 
 >**Leagues Available:** Premier League, La Liga, Serie A, Ligue 1, Bundesliga (Add more to your liking!) <br/>
 >**Competitions:** Champions League <br/>
 >**Stats:** Top Scorers (All leagues & competitions) <br/>
 >**Video:** Live streams & Full game highlights

##Who Is It For?
**Anyone who wants to find Football information quickly, without a hassle and most importantly without ADs!**:thumbsup: <br/> I always like to stay up to date with game scores, details and watching highlights but I hate having to search through a lot of different websites to find what I need.

##Content
* [Description](#soccerlive-football-stats--game-linkstv-)
* [Functionalities](#what-it-does)
  * [Standings](#standings), [Match Scores](#match-scores), [Top Scorers](#top-scorers), [Champions League](#champions-league), [Live Streams](#live-streams), [Highlights](#highlights)
  * [How it works](#how-it-works)
* [How to install](#how-to-install)
  * [Dependencies](#dependencies)
* [My Setup](#my-setup)
 
##What It Does

###Standings
Up-to-date leagues and competitions standings:
![alt text] (https://github.com/jctissier/Football-CLI/blob/master/Documentation/Standings.gif "Standings for Football Leagues & Champions League")

###Match Scores
Game date, final score and game details such as goal scorers, assists and time scored: <br/> 
![alt text] (https://github.com/jctissier/Football-CLI/blob/master/Documentation/MatchScores.gif "Match details for each Football Leagues")

###Top Scorers
Top scorers for all leagues available:
![alt text] (https://github.com/jctissier/Football-CLI/blob/master/Documentation/TopScorers.gif "Top Scorers for each Football Leagues")

###Champions League
Standings, Match Scores and Top Scorers for the Champions League competition:
<ul>
<li><b>Group Stage Standings:</b> Up-to-date standings for the group stage</li> 
<li><b>Group Stage Results:</b> Match scores and details for each Champions League game week</li>
<li><b>Resuts by Group:</b> Match scores and details for each Group A-H</li>
<li><b>Top Scorers:</b> Champions League top scorers for the whole competition</li>
</ul>
![alt text](https://github.com/jctissier/Football-CLI/blob/master/Documentation/Champions%20League%20Standings.gif "Champions League Standings")
![alt text](https://github.com/jctissier/Football-CLI/blob/master/Documentation/Champions%20League%20Match%20Scores.gif "Champions League Match Scores per Groups")

###Live Streams
Finds live games that can be watched (**Requires an active Reddit account**):
<ul>
<li>Search input must include one of the team names (ex: Barcelona) or it will redirect you back to the Main Menu </li> 
<ul><li>Case Insensitive</li></ul>
<li><b>Command + Double click on link</b> - Open link in browser from terminal</li>
</ul>
![alt text] (https://github.com/jctissier/Football-CLI/blob/master/Documentation/Football-Live%20Streams.gif "Find WORKING links to live streams")

###Highlights
List of highlights from all competitions:
<ul>
<li>Search input must include one of the team names (ex: Barcelona) or it will redirect you back to the Main Menu </li> 
<ul><li>Case Insensitive</li>
<li>These highlights do have ads but the quality is perfect and always reliable, 10 seconds in the beginning + 10 seconds if video is longer than 4 minutes</ul>
<li><b>Command + Double click on link</b> - Open link in browser from terminal</li>
<li>I have formatted the titles to make it more convenient, the format is:</li>
<ul><li><i>[League/Competition Name]   [Date of Game]   [Team 1 vs. Team 2]</i></li></ul>
</ul>
![alt text] (https://github.com/jctissier/Football-CLI/blob/master/Documentation/Highlights.gif "League/Competition Football Highlights")

###How It works
<b>Navigating through the Main Menu is easy:</b>
<ul><li>Enter the number assigned to the menu you want to navigate to and press 'Enter'</li></ul>
![alt text](https://github.com/jctissier/Football-CLI/blob/master/Documentation/menu.png "Main Menu")
  <ul><li>Example: I want to see the Standings for Liga BBVA</li></ul>
<ol><li>Main Menu > Press 1 and 'Enter'</li>
<li>Choose Liga BBVA > Press 2 and 'Enter'</li></ol>
  <i>You may only choose the numbers assigned in the menu, otherwise the menu will reload</i>
![alt text](https://github.com/jctissier/Football-CLI/blob/master/Documentation/menu2.png "Main Menu")

##How To Install?
**Use pip to install**</br>
<br/>
Football-CLI runs the program directly from your terminal<br/>
1. Open your terminal and type:
```
pip install Football-CLI          #pip3 install Football-CLI   <- also works
Football-CLI                      #This will automatically run the program!
```


###Dependencies
If this doesn't work for you yet, I'm working on making the deployment as user friendly as possible, check back in a day or so. Thanks!

Packages: .....



##Final Notes [![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/jctissier/Football-CLI/blob/master/LICENSE)
**Author:** Jean-Claude Tissier<br/>
Feel free to contribute or request new features and leave an issue if you have any problems/questions!

__No API needed! All data is scraped from [ca.soccerway.com](www.ca.soccerway.com) and Subreddits, [Soccerstreams](https://www.reddit.com/r/soccerstreams/) & [Footballhighlights](https://www.reddit.com/r/footballhighlights/).__


