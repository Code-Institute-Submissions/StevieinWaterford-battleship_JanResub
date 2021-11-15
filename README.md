
# Battelships Project
Battleships is a  terminal game that runs on Heroku. The object of the game is to beat the computer at the game before it beats you

![Battleship]()




https://dashboard.heroku.com/apps/battleship23

## Features
This battleship game allows the user to sink the battleship with 4 turns before it's game over. Its a simplified version of the game. The main features of the game are.
* A welcome message with the a brief message and a description of the game 

* There is a feature which you can enter your name and a prompt which greets the player

* If you hit a ship a prompt with the message "You've hit a battlship!" appears on the screen.

* If you miss the co-ordinates by a wide margin, the message "Missed by miles that's not even close" appears.

* If you entee in a letter rather thab a number ,the message "You have to enter a number, plesae try again" appears

* If you take a shot that has already been taken the message "You guessed that already" appears

* Your misses are marked by an "X" with the following messsage "You've missed"

* After 4 consecutive misses you need to play a new game, the terminal prompts the message "Game over"

* When the game s is completed  the terminal prompts you with the "Would you like to play again" Name" y/n:"

* If you decide to exit out of th game the terminal will prompt you with the message "Good Bye".

## Technology employed

• Gitpod to run the project on as an IDE

• Heroku to run the project on an external terminal

• W3 Schools to learn more about Python and indentation and functions

• PEP8 online checker to check my results and to see   if my Python Code was formatted correctly


## Bugs

Initially , I found it difficult to indent some of my code when passing it through the PEP8 online checker, I had to rely on Tutor support to talk me through this issue , it was easlily rectified in the end. WELCOME = str(input('Welcome to Battleship!!'
                    'The object of the game is to sink the computers ships'))
My indentation initially was out of place with the second line of code place to the left.

* print(*b) I found that this print command was easier to implement  rather than by using join  method which I found I would not work. I tried to print " " .join board which gave an error, print(*b) however worked.

* I employed a try and except statement  in order to  execute successfully, the program will stop at the line that caused the error and the “except” code will run. The try block allows you to test a block of code for errors.

* I also found that line 60 of my code was too long and that when I tried to seperte it and push it to the next line the game would not run correctly

* Another issue which I found problematic the first time I pushed the project to Heroku was that the command prompts did not work correctly . This was rectified by the Try and Except statement so that no errors wer picked up and the /n at the end of the statement.




## Remaining Bugs

No bugs remaining.

## Validator Testing

PEP8. No errors were returned.

## Implementation
The App was tested on PEP8 online checler.
This app can be viewed on a variety of devices such as Desktop, Laptop, iPhone5, iPhone6, iPhone7 and iPhone8. .This website is also compatible with iPad and iPad Pro


# Deployment 

This project is hosted on  Code Institute's mock Heroku terminal


It is deployed using gitpod and github pages. Github was used to write the code and seeing it is linked with github it was easy to use the terminal to commit, and push my code to their server. The deployed website is hosted on github pages.

Deployment was done in the following way:

Click on settings tab on my repository.

Click the pages tab.

Set source branch to master. This created a link to the deployed version of the website.








## Credits

I'd like to thank the Code Institiute Tutoring team for many of their tips when implementing this project . I found their instruction be  extremely helpful.

## Media Credits

I found the following sources of help when trying to implement my project.

* https://www.youtube.com/watch?v=7Ki_2gr0rsE

* https://www.youtube.com/watch?v=Gi0Fdyhk1_0 

* https://www.w3schools.com/python

* https://stackoverflow.com

* http://pep8online.com/checkresult


