# __Brians Battleship Game P3 2021__

Brians Battleship game is a logic based game where the user gets the opportunity to take on the computer and seek and destroy, the computers hidden battleships on the game board, while the computer takes aim back at the Users battleships. Neither the user nor the computer know the location of the others battleships and therefore it is a guessing game as to where they are situated.

The Initial welcome screen allows the user to input their username and choose the level of difficulty as they see fit.

The second screen outlines the layout of the game board and the general rules and instructions how to play the game.

The next screen shows the gameboard with the users game board and information to the left side of the screen and the computers game board and information to the right side of the screen.

The Last screen shows the users and computers final score and how many ships are still sailing, announces the winner, and displays the top five high scores leaderboard.


The last screen is visible only when one of the following conditions are met:
 1. The users ships have all been sunk.
 2. The computers ships have all been sunk.
 3. All the users torpedoes have been fired.
 4. All the computers torpedoes have been fired.
 5. The user types the "exit" keyword into the input field.

## __Table of Contents__

<!-- Table of contents -->

* [What does it look like](#what-does-it-look-like)           
* [Features](#features)
* [Technologies](#technologies)
	* [Languages used](#languages-used)
	* [Other Technologies](#other-technologies)
	* [Existing features](#existing-features)
	* [Features left to implement](#features-left-to-implement)
* [Testing](#testing)
* [Validator testing](#validator-testing)
	* [PEP8 validator results](#pep8-code-validator)
* [Unfixed Bugs](#unfixed-bugs)
* [Deployment](#deployment)
* [Credits](#credits)
* [UX](#ux)
	* [Scope](#scope)
	* [Strategy](#strategy)
	* [Structure](#structure)
	* [Skeleton](#skeleton)


<!-- End table of contents -->

## __What does it look like__
![Responsive Mockup](/readme-images/am-i-responsive.JPG )
<a href="https://brian-stritch-p3-battleship.herokuapp.com/" target="_blank">Click Here</a> to access the game.

## __Features__ 
1. The user is awaded the opportuntity to enter their name into the console for a personalised experience.

2. The user is then offered the choice of three game difficulty levels.

3. The user is given a breakdown of the rules of the game, instructions on how to play the game and some general information on the game and is prompted to press the enter key prior to commencing into the game.. 

4. Once the game starts the game boards are generated and the users ships and computers ships are randomly placed within the game boards. The user can see their ships, however the computers ships remain hidden.

5. The game board and number of ships are determined by the game difficulty chosen by the user at the initial welcome screen, and users that choose difficulty level 1 play on a 5 x 5 game board and have 3 ships each. Users that choose difficulty level 2 play on a 7 x 7 game board with 4 ships each. Users that choose difficulty level 3 play on a 10 x 10 game board with 4 ships each. The user and the computer get 20 torpedoes each for all game difficulty levels. 

6. The user is asked to guess a row number relevant to the game board size and a column number relevant to the game board size to fire a torpedo to this location on the computers game board.

7. The user is then displayed the result of their choice and is informed if the torpedo has struck its taget, or whether it has missed.

8. The computer then takes its turn randomly choosing a location on the users game board and a message is displayed to inform the user if the computer was succesful at finding their ships or not. If the Computer hits a ship, a function is triggered to target the adjacent cells in an attempt to seek and destroy the users ships in order to make it a competitive gaming experience where the user gets to experience what it would be like if another human player was targeting their ships.

9. The game will continue until the ships have been sunk or the user and computer have no ammunition remaining.

10. At the end of game screen, a message is displayed to the user notifying them of their score and of the remaining ships still at sea. If the user has been victorious then they are congratulated on their victory, alternatively if the computer is victorious the user is displayed a message notifying them of their loss. A high scores list is then shown to the user showing the top 5 players names and scores.

8. At the end game screen the user can retart the game and is redirected to the welcome screen.

## __Technologies__

### __Languages used__
  The Python programming language was used to create the game:
  

### __Other technologies__

  1. Balsamiq Wireframes
    * To create the wireframes and mock ups.

  2. Gitpod
    * Platform used to develop and test site.

  3. Github
    * Platform used to host the repository.

  4. Heroku
    * This was used to deploy the live terminal version of the game.

  5. Google Sheets
    * This was used to store the usernames and scores and to return the top 5 players names and scores for the high scores rankings displayed at the end game screen.

### __Existing Features__
  - The game has three levels of difficulty.

  - In order to give the user a pleasant gaming experience we implemented a function which clears the terminal after each game turn cycle and clears the terminal after the welcome page, the instructions and rules page, and the end page also.

  - In the intrest of user experience the users game board and computers game boards are printed on the same horizontal axis so that the page does not scroll downwards and appears to refresh after each iteration of the game turn cycle.

  - The game has the functionality to randomly place ships on the horizontal or vertical axis.

  - For a more realistic experience the game has the functionality to allow the computer to fire at randomly selected locations until a target is hit and then activates a function to seek and destroy the remaining part of that ship. Once the ship is destroyed the computers guess reverts to a random guess and the game continues.

  - The game has catch statements implemented to stop the user selecting an area outside the game board size.

  - The game has the functionality to record high scores and add the user to the leaderboard should they be applicable.


### __Features Left to Implement__

- The functionality to allow the user to play a battle-space-ship game where the ships are large square objects.

- The functionality to possibly allow a ship to move location once they have been hit but to stop when sunk.

## __Testing__ 

 - All aspects of the game have been tested and appear to be working as intended with very few errors present. The user should be able to achieve their goal as the game intends, depending on whichever game level they choose to play when they visit. 

 - I have tested the site out on Google Chrome and Android, Edge, Safari however it has not been tested on IOS. The P3 terminal based project is non responsive in relation to device sizes.

 - Community Testing:
    * Family members and friends testing rigorously and reporting on faults or bugs found and putting forward input to imrove the gameplay and functionality of the game.

### __Validator Testing__ 

##### __PEP8 Code Validator__
  - The code for the run.py page was entered into the validator and all aspects of the page passed.

  - No errors or warnings were returned when passing through the official PEP8 validator.
     ![Brians Battleship P3 2021 validator results](/readme-images/pep8-checker.JPG)


### __Unfixed Bugs__

While many bugs have been found during the development phase, numerous bugs have been rectified however some known bugs remain.

 - During the development of the game numerous bugs came to light which required rectification in order for the game to work, as such bugs were resulting in crashes and infinite loops which required the modification of numerous functions to rectify this issue. The crashes were intermittent and have been addressed and this issue may be resolved, however due to time constraints we have tested the game to the best of our ability in the timeframe available and this issue has not since come to light. Should this issue arise in the future, this will be made a priority and will be rectified in a future update of this game.

 - During the development phase the users guess function was written numerous ways implementing different methods as each method prior to the current method carried their own bugs and faults. An intermittent bug was evident which occurred very seldomly which caused the seek and destroy function to run in an infinite loop and this has been addressed however there are time constraints of the submission of this project and to date the infinite loop appears to be rectified, although as it was a very intermittent occurrence we would be uncertain if this bug is truly irradicated until further testing has been completed.

 - It was noted while developing this game that the console or terminal was crowded and causing the game screen to scroll downwards and reprint the game boards below the previous game board and print statements, and in an attempt to print the game boards in a cleaner enviornment, the clear function has been implemented to clear the terminal after each turn cycle and it was found that with all the required content that the game page scrolled down by one line and the clear function only clears the terminal area visible to the user, and thus after each turn cycle the game would print a new game board, leaving the title line repeatedly in the upper lines of the terminal. After discussing this with my mentor we increased the size of the terminal and this issue has been rectified as a result, however on the standard sized terminal this issue will remain.


## __Deployment__

- The site was deployed using Heroku. The steps to deploy are as follows: 
  - Sign up and login to Heroku. 
  - On the right side of the screen choose "new", then "create new app".
  - You follow the prompts giving the app a name and a region and select "create app".
  - On the main page of Heroku select the settings tab, in settings the following buildpacks required to be installed:
    - Heroku/Python
    - Heroku/nodejs
  - In the settings tab, config vars required inputting such as:
    - CREDS as the creds.json file from the repository which contains priviledged information.
    - PORT 8000
  - In the deploy tab the app needs to be deployed.
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.
  - On recieving the message notifying that the app has been deployed you can then click the "open app" button to view the deployed version of the app. 

The live link to the game can be found <a href="https://brian-stritch-p3-battleship.herokuapp.com/" target="_blank">here</a>.


## __Credits__ 
- I would like to thank my mentor Spencer Barriball for the guidance throughout the project.
- I would like to thank all my family and friends for the help in testing the game and searching for errors and bugs.
- I would like to credit Geeks for Geeks for information relating to numerous different areas of the game sourced via google search.
- I have carried out extensive research in relation to many different areas of this game and have obtained information from numerous websites and forums throught the development of this game.

 ## __UX__

- ### __Scope__
   - #### __From Why to What!__

     - ##### __What they say they need:__
        -	A fun and challenging, logic based game.
        -	A game with a variety of levels of difficulty.
        -	A game that tracks and displays the users score.


      - ##### __What they actually need:__
        -	A fun but competitive game that is enjoyable for the user.
        -	A game that offers multiple game difficulty choices, to appeal to a multitude of users. 


      - ##### __What they don’t know they need:__ 
        -	A fun but competitive game that is easy to play and offers feedback by way of the seek and destroy function to make the user sense that the computer is operating such as a human player would which is enjoyable for the user.
        -	A challenging logic based startegy game with varying difficulty levels and the ability to record high scores.        

  - #### __Features and Content__
    - __Example__: A user wishes pass time and enjoy an competitive logical strategy game. 
      - ![scope Diagram](/readme-images/scope.JPG)
    

- ### __Strategy__
    -	To create a competitive strategy game for the user.
    -	The aim is to offer the user a game that caters for a multitude of user difficulty levels.
    -	To allow the computer to play defensively once a torpedo strikes its target and then targets the surrounding cells in order to sink the users ship, which brings an AI feel or a sense of human interaction to the computers decisive actions.
    -	To allow the user to input their name for a personalised experience and to add the users name and score to the high score’s leader board, should their score qualify.


  - #### __Relevance of Content__
      - The content is relevant as the user can choose an area of the map to target and hope to be successful in sinking the computers ships.

  - #### __Why is it special?__    
      - This quiz game is special in that it offers an AI like behaviour for the computer should any of its randomly selected target locations successfully hit their target.
Future Developments of the game could include the addition of game types to expand the platform.  i.e : Space Battleships
 
  - #### __Why would you want this?__
    - As this game offers a selection of difficulty levels and allows the computer to fight back and seek and destroy the users battleships, this makes the game competitive and it is a race between the user and the computer as to who will sink the others battleships and win the game.  

  - #### __What makes a great experience__
    -	The ability enter your name for a personalised experience. 
  	- Having the choice of which difficulty level you want to play. 
    -	The ability to view the current scores, remaining torpedoes, and remaining ships as you play the game. 
  	- The ability to see which cells have been targeted and successful as marked with “@”, the unsuccessful torpedoes fired marked with “X”, and the available cells remaining marked with “ . “ which allows the user to differentiate between the types of cell markings. 
    -	The ability to add more game types and difficulty levels in future updates of the game to offer the user more of a selection. 
   
  - #### __What can a user expect?__
      - __Does it offer me what I want__
            - Yes, to have the ability to play a competitive logic based strategy game.   
      - __As a user I expect to see__
            - Visually, the game boards indicate the level of difficulty as the higher the difficulty level the larger the game board size, and the users ships are visible however the computers ships remain hidden.
      

- ### __Structure__   
    #### __Information Architecture (IA)__ 
     - #### A basic tree structure layout .     
        ![Structure layout](/readme-images/stucture-diagram.JPG)   
  

    - ### __Interaction Design (IXD)__ 
      - #### __Welocome Screen__
        - The first area the user will encounter is the welcome message screen, where the user is prompted to enter their name. On entering their name, the user will be displayed a choice of game difficulty levels with three choices, 1. Beginner, 2. Intermediate, 3. Advanced. Once the user selects their preferred game difficulty level the game then progresses to the rules and instructions page.

          ![Game welcome screen](/readme-images/welcome-screen.JPG) 

      - #### __Rules and Instructions screen__
        - The rules and instructions page describes the game and how it should be played and describes the game display areas and information printed in the game area. The user is prompted to press enter to play the game allowing the user to control the progression to the game screen, to allow the user sufficient time to read and understand the game rules and instructions.

          ![Game rules and instructions screen](/readme-images/instructions-and-rules-page.JPG)

      - #### __Game Screens__
        - Once the user progresses to the game screen, the relevant game board size is printed in relation to the difficulty level chosen by the user, the users ships are randomly placed and are displayed to the user, and the computers ships are randomly placed and hidden from the user.
        - The users current score is displayed above the users gameboard, and the computers current score is displayed above the computers game board.
        - The users and computers remaining ammunition is displayed beneath the relevant game board and the users and computers remaining ships are displayed beneath the relevant game boards.
        - The user is then prompted to enter the row and column numbers to pinpoint their target destination on the computers game board.
        - Once the user takes their guess, the users guess is shown to the user to verify the correct input, and the result of their choice is displayed (whether a hit or a miss), and the computer then takes its turn.
        - Once the computer takes its turn, the computers guess and the results of their choice are shown to the user.
        - The game continues until one of the following conditions is met:
          -	All the users ships have been sunk.
          -	All the computers ships have been sunk.
          -	The user and computer have no ammunition remaining.
        - Should the user wish to leave the game an exit keyword has been programmed into the game so at any of the input fields the user can exit the game simply by typing the exit keyword into the terminal. 
          - __Game difficulty level 1__
          ![Game level 1 screen](/readme-images/level-1-game.JPG)
          - __Game difficulty level 2__ 
          ![Game level 2 screen](/readme-images/level-2-game.JPG)
          - __Game difficulty level 3__
          ![Game level 3 screen](/readme-images/level-3-game.JPG) 

      - #### __Welocome Screen__
        - On completing the game an end screen is displayed where the user is displayed a message indicating who the winner of the game was and the high scores leader board is displayed. Should the users score qualify for a place on the top 5 leader board, the users name and score will appear in the statistics. 
        - The user is then prompted to press the enter key to restart the game.
         ![Game End screen](/readme-images/end-game-screen.JPG) 


 - ### __Skeleton__

    - Below is a simple wireframe created on balsamiq illustrating the game screen deployed on a terminal in heroku.
      - __The game screen__

        ![Wireframe from Balsamiq](/readme-images/battleship-wireframe.JPG)
     
      
 




