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

 - One such bug is that intermittently the seek and destroy function may target a cell outside the bounds of the board which causes it to wrap to the next line. This Bug is currently a priority and will be rectified in a future update of the game.

 - During the development of the game numerous bugs came to light and required rectification in order to execute the game as such bugs were resulting in crashes and infinite loops which required the modification of numerous functions to rectify this issue.

 - During the development phase the users guess function was written numerous ways implementing different methods as each method prior to the existing method carried their own bugs and faults. An intermittent bug was evident which occurred seldomly which caused the seek and destroy function to run in an infinite loop and this has been addressed however there are time constraints of the submission of this project and to date the infinite loop appears to be rectified, although as it was seldom occurrence we would be uncertain if this bug is truly irradicated.

 - It was noted while developing this game that the console or terminal was crowded and causing the game screen to scroll downwards and reprint the game boards below the previous game board and print statements, and in an attempt to print the game boards in a cleaner enviornment, the clear function is used to clear the terminal after each turn cycle and it was found that the game scrolled down one line and the clear function only clears the terminal area visible to the user, and thus after each turn cycle the game would print a new game board, leaving the title line repeatedly in the upper lines of the terminal. After discussing this with my mentor we increased the size of the terminal and this issue has been irradicated as a result, however on the standard sized terminal this issue will remain.


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
        -	A fun but competitive game that is easy to play and offers feedback by way of the seek and destroy function to make the user sense that the computer is operating such as a human player would which is enjoyable for the user..
        -	A Quiz to challenge and entertain the user.        

  - #### __Features and Content__
    - __Example__: A user wishes to play a challenging logic based game.. 
      - ![scope Diagram](/assets/readme/readme-images/scope.JPG)
    

- ### __Strategy__
    -	To create an entertaining quiz game for the user.
    - The ability to select different game types depending on interests and age.
    - The aim is to offer an entertaining and informative quiz game that caters for a multitude of user types.
    - To offer an enticing Peppa Pig quiz game for young children with an interest in Peppa Pig.
    - To offer an interesting quiz game based on the hit RTE crime drama Love/Hate for adolescents and adults with an interest in   the Love/Hate crime drama.
    - To offer an enticing Music trivia quiz game for all ages of users with an interest in Music.
    - To provide the users with facts relating to the relevant questions asked and the correct answers for these questions.

  - #### __Relevance of Content__
      - The content will be relevant, as the game types offered to the user are directly related to the game types. The game will be easy to navigate, it will be click and go to where you want to get to. The majority of the game will be structured on the one page with the content required being showed and the unused content hidden, until required by the user or at differing intervals of the relevant game types.

  - #### __Why is it special?__    
      - This quiz game is special in that it offers an easy-to-use platform which is easy to navigate through and is both entertaining and educational.
  Future Developments of the game could include the addition of game types to expand the platform. 
  - #### __Why would you want this?__
    - As the game content is limited the user may grow tired of the available questions or the content available and the addition of new content in future updates will help to keep the content relevant to the user and may keep the user interacting with the game. 

  - #### __What makes a great experience__
    -	The ability to view all your favourite games in the one place. 
    -	Having the personal choice of which game you want to play. 
    -	The ability to view the current scores as you play the game. 
    -	Having the correct answer highlighting and an informative message displaying content relative data pertaining to the questions asked. 
    -	The ability to add more game types in future updates of the game to offer the user more content and keep the quiz game relevant to the user. 
  
  - #### __What can a user expect?__
      - __Does it offer me what I want__
            - Yes, to have the ability to view all your favourite games on offer.  
      - __As a user I expect to see__
            - Visually, the game screen backgrounds are decorated with images relating to the current game selection.
      - __Can I contact somebody?__ 
            - Yes, there are social media links found in the footer to contact the developer. 
      - __What can I learn?__ 
            - Each question has an informative message displayed relating to its correct answer. 


- ### __Structure__ 
  
  #### __Information Architecture (IA)__ 
    ##### A basic tree structure layout . 
     ![Structure layout](/assets/readme/readme-images/structure.JPG)

    - __Interaction Design (IXD)__ 
      - The first area the user will encounter is the quiz Entry screen, where an enter button and rules button are located at the lower central area of the page. On clicking the enter button the user will be displayed a choice of game types. On clicking the rules button, a modal is displayed containing the rules of the game.
      - The game selection screen displays large images of the game types and a button to select the game type is located below each image. 
      - Once the user selects which game type they wish to play, the relevant game background and styles are applied and a display box which housed the question box and answer buttons is displayed in the central area of the page. A start button is displayed for the user to initiate the game start function to display a question and the four possible answers relating to the question.   
      - On clicking the selected answer the correct answer button changes to green and the incorrect answer buttons change to red to give the user an immediate indication of the truth of their answer choice, and the game displays an informative message to the user relating to the question asked and the correct answer. The answer buttons then disappear to reveal the next button to take the user to the next question. 
      - A correct and incorrect answer tally is displayed in the lower right and left areas of the screen respectively which increments the answer tally depending on whether the user answers correctly or incorrectly.
      - Should the user wish to leave the game an exit button is located on the lower central area of the screen which redirects the user to the entry screen where the user can begin their navigation through the game again.
      - On completing the quiz an end screen is displayed with an alternative background image and displays a message to the user displaying the correct score out of 10.
      - The user can then decide whether they wish to restart the current game or exit to the game selectors screen to choose a different game.
      - The buttons throughout the game feature a hover feature so the user can instantly see their current selection prior to clicking the selected button.
      - Each social media link also has a hover effect so the user knows the link is active and it will take the user to the relevant platform requested. 

  
 
 - ### __Skeleton__

    - Below is a set of wireframes created on balsamiq illustrating the Entry screen, game selection screen, Peppa pig game screen, Peppa Pig game end screen, Love/Hate game screen, Love/Hate game end screen, Music game screen, and Music game end screen.
      - The Initial Game Entry screen
         ![Entry Screen Wireframe from Balsamiq](/assets/readme/wireframe/entry-screen.JPG)
      - The Game selection screen
         ![Selectors screen Wireframe from Balsamiq](/assets/readme/wireframe/selectors-screen.JPG)
      - The Peppa Pig Game Screen
         ![Peppa Pig Game Screen Wireframe from Balsamiq](/assets/readme/wireframe/peppa-game-screen.JPG)
      - The Peppa Pig Game End Screen
         ![Peppa Pig End Game Screen Wireframe from Balsamiq](/assets/readme/wireframe/peppa-game-end-screen.JPG)
      - The Love/Hate Game Screen
         ![Love/Hate Game Screen Wireframe from Balsamiq](/assets/readme/wireframe/love-hate-game-screen.JPG)
      - The Love/Hate Game End Screen
         ![Love/Hate Game End Screen Wireframe from Balsamiq](/assets/readme/wireframe/love-hate-game-end-screen.JPG)
      - The Music Game Screen
         ![Music Game Screen Wireframe from Balsamiq](/assets/readme/wireframe/music-game-screen.JPG)
      - The Music Game End Screen
         ![Music Game Screen Wireframe from Balsamiq](/assets/readme/wireframe/music-game-end-screen.JPG)
 




