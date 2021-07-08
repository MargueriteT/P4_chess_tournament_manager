TOURNAMENT MANAGER
=================

Description
-----------
This program is a **Chess Tournament Manager**. It can be used to manage the
 course of a chess tournament. You will be able to :
 - **Create** a new tournament 
 - **Register** a tournament in the database
 - **Resume a tournament** already started
 - **Display all the players** registered in the database
 - **Display all tournaments** registered in the database

 The program will ask you to enter the main data about the tournament and
  players but then it will calculate the final score of each player and
   update their rank.
   
Clone the repository
--------------------
Download the repository from this link to the local folder you want.

Installation
------------
First, make sure you already have python3 install on your computer. If not, 
please go to this link: https://www.python.org/downloads/ and follow the
 instructions.
Open your Cmd and proceed as indicated: 
- Navigate to your repository folder: cd *path/to/your/folder*
- Create a virtual environment: python -m venv env (windows) python3 -m venv
 env (macos ou Linux)
- Activate this virtual environment: env\Scripts\activate (windows) ou source
 env/bin/activate (macos ou linux)
- Install project dependencies: pip install -r requirements.txt
- Run the program: python main.py

Flake8 Report
-------------
Run the following command line :
flake8 --exclude .git,__pycache__,venv/,env/ --format=html --htmldir=flake
-report

 

