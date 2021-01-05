## **Competitive Programming**

<img src="Github%20CP.png"  alt="coding" height="400"/>



## How to Contribute and Create a PR on this Repository?
### 1. Clone this repository.
You first need to fork the original repo and you need to create a local copy of this repository to be able to contribute to the same. Copy the following command and paste it in your terminal.

`git clone https://github.com/username/Competitive-Programming`


Please ensure that you add YOUR username in the command and do this after Forking the Repository.

### 2. Create a New Branch
After successfully cloning the repository, you need to now create a separate branch for yourself to not disturb the workflow of the repository. If you aren't already inside the main folder copy this command in terminal and press enter.

`cd Competitive-Programming`

Now that you are inside the main folder, use this command to create a new branch for yourself.

`git branch (name of your branch)`

Please ensure that the name of your branch is your username.

### 3. Switch to your New Branch
To start working and to push code from your own branch, please execute the following command in the Terminal.

`git checkout (name of your branch)`

You should receive a notification which will state that you have switched to your newly created branch.

### 4. ADD YOUR FAVORITE PIECE OF CODE IN YOUR FAVOURITE PROGRAMING LANGUAGE
Check the excel sheet to see which problems require solution and update the sheet after making pull request .Whole repo is divided into Four languages. Click the link to view unsolved questions
[Python](https://docs.google.com/spreadsheets/d/1j2M45lmeV6dykp_-xMDf91_6bDhYFeVXwVlgs7CBUxo/edit#gid=2133262884) ,[Java](https://docs.google.com/spreadsheets/d/1j2M45lmeV6dykp_-xMDf91_6bDhYFeVXwVlgs7CBUxo/edit#gid=1055454945), [C](https://docs.google.com/spreadsheets/d/1j2M45lmeV6dykp_-xMDf91_6bDhYFeVXwVlgs7CBUxo/edit#gid=1394665650), [C++](https://docs.google.com/spreadsheets/d/1j2M45lmeV6dykp_-xMDf91_6bDhYFeVXwVlgs7CBUxo/edit#gid=0) Try to optimize the code as much as possible. Leave comments to increase the readability of the program

### 5. Sync all Updates
The part you have been waiting for , execute the following command in your terminal.

`git add .`

This will add all the files in your local repository. After this execute

`git commit -m "ADD YOUR MESSAGE HERE (PREFERABLY THE NAME OF YOUR PROJECT)"`

Note that it is mandatory for you to add a Commit Message for others to understand what from where you have solved the question like ""FROM HACKERRANK" OR "FROM LEETCODE".All the letters must be capitalize. Now finally to push updates to the new branch, execute the following:

`git push --set-upstream origin (name of your branch)`

While you are at it, also execute the following command which will specify a new remote upstream repository (the cone you are looking at).

`git remote add upstream https://github.com/chaudharypraveen98/Competitive-Programming`

### 6. Keep your Repository in Sync
You need to use the following commands to help you sync all the branches with their respective commits associated with this repository and stay in loop. Copy these commands and execute:

`git fetch upstream`

`git checkout master`

Post this you simply need to merge all the changes you made.

`git merge upstream/master`

6. Create a Pull Request (The Part you have been waiting for)
Now that you are done with the most complex parts of the process, you can just go to your forked repository and Click on **New Pull Request** towards the left hand side of the page and You're Done!
Congratulations on successfully creating a Pull Request there!

7. At last please update the excel sheet


## Contributors
Please add your name in the list in the following format:

` - Name - [File Name](File Address)`
- Praveen Chaudhary - [Athlete Sort](Python/Hackerrank/Athlete Sort)