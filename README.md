# hdfBot

A bot to automatically complete the HDF form

When one brings the laziness to the next level, this project is born..

---

# Installation


1. Prerequisite:

```markdown
python version: 3.6.x
```
```markdown
$ pip install -r [requirements.txt](https://github.com/jamestansx/hdfBot/blob/daa28971bee5325672ee91cb25e79c03870d2fc4/requirements.txt)
```
```markdown
Download the [chromedriver](https://chromedriver.chromium.org/downloads) according to your Chrome version
```

2. Clone this repo

  * Git
    ```markdown
    git clone https://github.com/jamestansx/hdfBot.git
    ```
  * GitHub CLI
    ```markdown
    gh repo clone jamestansx/hdfBot
    ```

# Usage

Run this command
```markdown
python path/to/main.py &
```
Alternatively, refer to [task scheduler](#Scheduler-Setup-(Workaround))
# Limitation
Currently, only Chrome is supported...

# Scheduler Setup (Workaround)

* ### Windows

    1. Lauch Window's Task Scheduler
    2. Click on the Create Basic Task action
    3. Input the name and description of the task
    4. Select the trigger to "Daily"
    5. Set the appropriate time so that the task will be executed before 11am everyday.
    6. Select "Start a program" option
    7. Enter the path of python.exe in Program/script section, and input the path to the main.py in Add arguments section.
         ```
         "path/to/main.py" &
         ```
    ![alt text](https://i.imgur.com/MUw3SkI.png)

* ### Linux
  Refer to [crontab](https://crontab.guru/crontab.5.html) for more info
# Roadmap

- [ ] Multi browsers support
- [ ] Auto scheduler to startup the program

# TODO
- [ ] Add log files ~!!1
