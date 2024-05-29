# HANGMAN!!!

![Responsive Mockup](documentation/features/mockup.png)

*The link to [Hangman!](https://)*!!!!!!!!!!!

Hangman is a Python terminal project whose primary purpose is to boost users' moods and provide entertainment, challenges and fun.

Users can quickly learn the rules of the game and then play along following the terminal prompts. Guess a letter, and try to make sure that man doesnt hang!

---

## How to play:

  1. Click this *[link](...........)* or copy this text: ............. and paste it in your browser's address bar. !!!!!!!!
  2. As soon as the page is loaded, click 'RUN PROGRAM'.
  3. select and option from the main menu.
  4. Learn the rules if needed.
  5. A word is selected from an imported word bank of approximatley 2000 words. 
     Look at how long your word to guess is and start thinking about what it could be. Add your letter guesses when prompted.
  6. As you add each letter it will either appear and take the place of a blank soace in the word, or it will add another part onto the hangman.
  7. You have 9 wrong attempts to to guess the word before the hanging takes place!
  8. If you fail and get it wrong, the full hangman is displayed and "game over! :(" is printed, and the word you were trying to guess is revealed. 
  9. If you successfully guess the word, congratulations, you win!!!! The main menu pops up, and you can either choose to play again or leave the game.

  Link to the game: *................*!!!!!!!!!!

---
## User Stories
### First Time Visitor Goals:

* As a First Time Visitor, I want to quickly understand the program's primary purpose so that I can learn more about this program.
* As a First Time Visitor, I want to navigate through the program easily so that I can find the content.
* As a First Time Visitor, I want to find the program useful for myself so that I can fulfill my expectations and have fun.
* As a First Time Visitor, I want to see different text colors so it looks more enticing, and the different parts of the game are easily distinguishable.

### Frequent Visitor Goals:
* As a Frequent User, I want to be able to play as many times as i like and not worry about a word being repeated, variation is key in this game.
* As a Frequent User, I will want to explore the other game option, multiplayer.

---

## Features
  
  - **When the program is loaded**

  - The user can see a title using Ascii art, "HANGMAN!" a menu appears and asks for the users input for menu selection.

  - **When the user selects a menu option**

  - Shows the terminal menu with three options:

    1. Play Game;

    2. Rules;

    3. Exit Game;

![loading Program](documentation/features/ascii_art.png)

  The user can enters a number into the terminal in relation to which menu option they wish to select.

  - **When the user chose "Rules"**

  The user will see the main rules of the game which are required to be followed.
  Below the rules, the user can find the main menu where they may choose another option.

  ![loading Program](documentation/features/rules_feature.png)

  - **When the user choose's "Play Game"**
  
  1. The game will ask how many players and the names, then will start to run;

  2. Keep adding letters as your guesses until you guess the word, or you "hangman!"

  3. Special characters and numbers are not allowed to be used, and will be greeted with an error message telling the user to select another option.

  ![loading Program](documentation/features/multi_feature.png)
  ![loading Program](documentation/features/)!!!!!!!!!!!!!!!!!!!!

  - **When the user chose "Quit"**

  The user will see a goodbye message, and the program will be stopped.

  ![loading Program](documentation/features/goodbye_message.png)!!!!!!!!!!!!!!!!!!!!!!!!!

---

## Flowchart

The flowchart represents the logic of the application:

  ![Flash Card Page](documentation/features/flowchart.png)

---
## Technologies Used

### Languages:

- [Python 3.8.5](https://www.python.org/downloads/release/python-385/): used to anchor the project and direct all application behavior

- [JavaScript](https://www.javascript.com/): used to provide the start script needed to run the Code Institute mock terminal in the browser?????????

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) used to construct the elements involved in building the mock terminal in the browser??????????

### Frameworks/Libraries, Programmes and Tools:
#### Python modules/packages:

##### Standard library imports:

- [random](https://docs.python.org/3/library/random.html) was used to implement pseudo-random word selection from word bank.
- [os](https://docs.python.org/3/library/os.html ) was used to clear the terminal before running the program.???????????????

##### Third-party imports:

- [Random Lists](https://www.randomlists.com/data/words.json) Word bank used for word pool for the game.
- [Colorama](https://pypi.org/project/colorama/) was used to add colors and styles to the project.

#### Other tools:

- [VSCode](https://code.visualstudio.com/) was used as the main tool to write and edit code.
- [Git](https://git-scm.com/) was used for the version control of the website.
- [GitHub](https://github.com/) was used to host the code of the website.
- [GIMP](https://www.gimp.org/) was used to make and resize images for the README file.
- [Miro](https://miro.com/app/dashboard/) was used to make a flowchart for project planning and the README file.
- [render.com](https://render.com/) was used to deploy the project.????????????????????

---

## Bugs

+ **Solved bugs**


1. Special characters and numbers were being read and allowed by the program.

    - *Solutions:* I defined a function that checked for "invalid chars" and provided a print statement saying "Valid characters are A-Z & a-z" if one is used.

     ```python
    def checkValid(char):
        if char in invalid_chars:
            return False
        else:
            return True

        &

            isValid = checkValid(letterGuessed)
        if not isValid: 
            print("Valid characters are A-Z & a-z")
      ```

2. The counter wasnt working, and a piece of the hangman was being added each time a letter was guessed, even if it was correctly part of the word.

    - *Solutions:* 

     ```python
    # counter
    def printWord(randomWord, guessedLetters):
        counter=0
        rightLetters=0
        for char in randomWord:
            if(char in guessedLetters):
                print(randomWord[counter], end=' ')
                rightLetters += 1 # ADDED - to fix main bug, it wasn't being updated so was always 0
            else:
                print(" ", end=" ")
            counter += 1
        return rightLetters
    ```


3. Invalid escape sequence, syntax warning. characters being used for the hangman visual and welcome game title.

    - *Solutions:* 
    backlash "\" was used in may places, as its an escape sequence it was showing an error, I had to double all backslashes used to remove the error message.

    (documentation/bug_screenshots/invalid_escape_sequence_bug.png)

4. Main not being defined when you try to exit the game. 
    ```python
    1) Play Game
    2) Rules
    3) Language Select Mode
    4) Multiplayer
    5) Exit Game

    Menu Select: 
    5
    Thank you for playing!!!
    Traceback (most recent call last):
    File "/workspace/hang_man/run.py", line 217, in <module>
        main()
NameError: name 'main' is not defined. Did you mean: 'min'?        ^^^^```

    - *Solution:* Indentation mistake.

5. if you press enter without any input in "guess a letter" input, it resets the game and picks a new random word.
+ **Unsolved bugs**

---
## Testing

Please refer to the [TESTING.md](TESTING.md) file for all test related documentation.??????????????????????????

---
## Deployment

- The program was deployed to [Heroku](https://dashboard.heroku.com).
- The program can be reached by the [link](https://the-maddest-madlib.onrender.com/)!!!!!!!!!!!!!!!!!!!!!!!!
### To deploy the project as an application that can be **run locally**:

*Note:*
  1. This project requires you to have Python installed on your local PC:
  - `sudo apt install python3`

  1. You will also need pip installed to allow the installation of modules the application uses.
  - `sudo apt install python3-pip`

Create a local copy of the GitHub repository by following one of the two processes below:

- Download ZIP file:
  1. Go to the [GitHub Repo page](https://github.com/IuliiaKonovalova/madlib_with_python).!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  1. Click the Code button and download the ZIP file containing the project.
  1. Extract the ZIP file to a location on your PC.

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/IuliiaKonovalova/madlib_with_python.git`!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

- Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

  [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/IuliiaKonovalova/madlib_with_python)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  1. Install Python module dependencies:
     
      1. Navigate to the folder madlib_with_python by executing the command:
      - `cd madlib_with_python` !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      1. Run the command pip install -r requirements.txt
        - `pip3 install -r requirements.txt`
      1. *Note:* If you are located in China ![China](https://www.countryflags.io/cn/flat/32.png) or any other country with restricted internet access, you may need to add the following code in order to be able to use the nltk package.
      
       - For example:

        ```python
        nltk.set_proxy('127.0.0.1:41091')??????????????????????????????????????????
        ```
      - To set the proxy, you need to open setting in preferred VPN, find Server address and HTTP/HTTPS Proxy Port joining them by colons as it is shown in the example above:
      ![Settings VPN](documentation/deployment/settings_vpn.png)????????????????????????????????????????

      

**The app was initially deployed to Heroku then moved to Render since Heroku has removed its free tier services from November 29 2022**????????????????????????????????????????

### To deploy the project to Heroku so it can be run as a remote web application:
- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/IuliiaKonovalova/madlib_with_python.git`!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  1. Create your own GitHub repository to host the code.
  1. Run the command `git remote set-url origin <Your GitHub Repo Path>` to set the remote repository location to your repository.

  1. Push the files to your repository with the following command:
  `git push`
  1. Create a Heroku account if you don't already have one here [Heroku](https://dashboard.heroku.com).
  1. Create a new Heroku application on the following page here [New Heroku App](https://dashboard.heroku.com/apps):

      - ![New Heroku App](documentation/deployment/new_heroku_app.png)!!!!!!!!!!!

  1. Go to the Deploy tab:

      - ![Deploy Tab](documentation/deployment/deploy_tab.png)!!!!!!!!!!!!!!

      - ![Deployment Method](documentation/deployment/deployment_method.png)!!!!!!!!!!!!!!!!!!!!

  1. Link your GitHub account and connect the application to the repository you created.

      - ![Link GitHub account](documentation/deployment/link_to_github.png)!!!!!!!!!!!!!!!!!

  1. Go to the Settings tab:
  
      - ![Settings Tab](documentation/deployment/settings_tab.png)!!!!!!!!!!!!!!!!!!!!!

  1. Click "Add buildpack":

      - ![Add Buildpack](documentation/deployment/add_buildpack.png)!!!!!!!!!!!!!!!!!!!!!!!!!

  1. Add the Python and Node.js buildpacks in the following order:

      - ![Add Python and Node.js](documentation/deployment/add_python_and_node_js.png)!!!!!!!!!!!!

  1. Click "Reveal Config Vars."

      - ![Reveal Config Vars](documentation/deployment/reveal_config_vars.png)!!!!!!!!!!!!!!!!!!

  1. Add 1 new Config Vars:
      - Key: PORT Value: 8000
      - *This Config was provided by [CODE INSTITUTE](https://codeinstitute.net/)*.

  1. Go back to the Deploy tab:

      - ![Deploy Tab](documentation/deployment/deploy_tab.png)!!!!!!!!!!!!!!!!

  1. Click "Deploy Branch":

      - ![Deploy Branch](documentation/deployment/deploy_branch.png)!!!!!!!!!!!!!!!!!!!!!!

      - Wait for the completion of the deployment.

      - ![Deploying Branch](documentation/deployment/deploying_branch.png)!!!!!!!!!!!!!!!!!!!!

  1. Click "Open app" to launch the application inside a web page.

      - ![View Button](documentation/deployment/view_app.png)!!!!!!!!!!!!!!!!!!!!!!!!!!!!

---
## Credits

- List of Uncountable Nouns was made based on the [7ESL](https://7esl.com/uncountable-nouns/).
- dictionary for idioms was made out of the tables published by [EF](https://www.ef.edu/english-resources/english-idioms/).
- Color formatting: [Colorama](https://pypi.org/project/colorama/).
- Terminal menu: [Simple Terminal Menu](https://pypi.org/project/simple-term-menu/).
- Pluralizing and transforming verb into past time: [Pattern Package](https://stackabuse.com/python-for-nlp-introduction-to-the-pattern-library/) and [NLTK Package](https://www.nltk.org/)\
- [render.com](https://render.com/) for hosting the application.


---
## Acknowledgements

- Martyn Harris - My Friend, has given valuable advice with the different issues ive encountered.
- My Mentor Iuliia Konovalova. I had issues with the help i was recieving with my previous mentor, 
  but i noticed a huge difference with the way Julia spoke to me and how she managed my situation, 
  she deserves alot of credit and praise for how she dealt with it.
- 