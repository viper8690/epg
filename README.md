# Setup

This is an automated way to pull epg guides. mc2xml is used to do the pull with Schdules Direct service. 

Note: mc2xml for Mac OS X Sierra does not work due to a problem with UPX. I've read that they are working on a release to fix this. Also, the code is not written to work with windows because it uses unix dir structure.

An Ubuntu 14.04LTS Linux distribution is being used with Python 3. The structure for on the server is as follows: `/github/epg/` where the guide goes and pushed to github in the code automatically and `/github/epg-updater/` which is where the python scripts are stored. I initially had 2 different dirs setup because I was not planning on releasing the code to the public repo i.e. `epg` dir. 

Basically, the code works by pulling the guides from SD by using the console commands from the `get_guides.py` script, `xml_merger.py` loops through the xmls in the directory, combines them, removes certain unnecessary tags in order to lower the size of the guide, copies the guide into the `epg` dir, and commits the `guide.xml` to github. All of these are run in sequential order through `main.py`.

epgs are sky ireland, directv, and bell.

An ssh key was added to github in order to commit without the need for a password.

A cron was created every day at midnight UTC using the following:

`0 0 * * * cd /home/ubuntu/github/epg-updater/; /usr/bin/python3 /home/ubuntu/github/epg-updater/main.py > cron-output`

# How to Run Manually:
`cd home/username/github/epg-updater`

`python3 main.py`
