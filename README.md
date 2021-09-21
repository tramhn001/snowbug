# Snowbug

## Goal

There are 5 bugs in this implementation of snowman. Practice using your debugging skills to locate, diagnose, and fix the bugs. For each bug note:

1. In which function it was found
1. The line (or lines) causing the problem
1. What about the line was causing the problem
1. What needed to be done to fix the problem
1. How you located the bug
   
## Activity Setup

Follow these directions once, at the beginning of the activity:

1. Navigate to your projects folder named `projects`

   ```bash
   $ cd ~/Developer/projects
   ```

1. If you would like to be able to keep your work in GitHub, click on the "Fork" button on the GitHub to fork the repository to your GitHub account.  

1. "Clone" (download a copy of this project) into your projects folder. This command makes a new folder called `snowbug`, and then puts the activity into this new folder.  If you forked the activity, be sure to clone from your forked copy.

   ```bash
   $ git clone ...
   ```

   Use `ls` to confirm there's a new activity folder

1. Move your location into this activity folder

   ```bash
   $ cd snowbug
   ```

1. Create a virtual environment named `venv` for this activity:

   ```bash
   $ python3 -m venv venv
   ```

1. Activate this environment:

   ```bash
   $ source venv/bin/activate
   ```

   Verify that you're in a python3 virtual environment by running:

   - `$ python --version` should output a Python 3 version
   - `$ pip --version` should output that it is working with Python 3

1. Install dependencies once at the beginning of this project with

   ```bash
   # Must be in activated virtual environment
   $ pip install -r requirements.txt
   ```

Summary of one-time project setup:

- [ ] `cd` into your `projects` folder
- [ ] Clone the activity onto your machine
- [ ] `cd` into the `snowbug` folder
- [ ] Create the virtual environment `venv`
- [ ] Activate the virtual environment `venv`
- [ ] Install the dependencies with `pip`

## Getting Started

1. While in the activity directory, launch VS Code.

   ```bash
   $ code .
   ```

1. Perform test configuration by going to the Testing panel (shaped like a beaker) and clicking Configure Python Tests. Select pytest as the framework and tests as the location of the tests.

1. Run the tests using the VS Code testing tools.

1. Focus on the top test failure. Read through the test failure, and understand why the failure is happening.

1. Make a plan to fix the test failure.

1. Write code to fix the test failure.

1. Re-run the tests.

1. Continue running tests until all bugs have been fixed.

## Activity Completion

Make note of your investigation, especially the 5 questions in the goal, and be prepared to share your findings with your classmates!