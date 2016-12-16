from subprocess import Popen, PIPE, STDOUT
import os
import glob
import logging


class Guides:
    def __init__(self):
        logging.basicConfig(filename='error.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
        self.SD_creds = ''
        self.set_dir = 'cd ~/github/epg-updater/'
        self.guide_cmds = [
            './mc2xml -J ' + SD_creds + ' -U -u -a -c us -g 10001 -d 48 -C usa.chl -R usa.ren -o usa.xml -D usa.dat',
            './mc2xml -J ' + SD_creds + ' -U -u -a -c gb -g WC2N -d 48 -C uk.chl -R uk.ren -o uk.xml -D uk.dat',
            './mc2xml -J ' + SD_creds + ' -U -u -a -c ca -g "V5K 0A1" -d 48 -C can.chl -R can.ren -o can.xml -D can.dat']

    def cleanup(self):
        print('deleting xml files...')
        self.xmls = glob.glob('./*.xml')
        for self.xml in self.xmls:
            os.remove(self.xml)

    def get_guides(self):
        print('getting guides...')
        for self.cmd in self.guide_cmds:
            self.final = Popen("{}; {}".format(self.set_dir, self.cmd), shell=True, stdin=PIPE,
                      stdout=PIPE, stderr=STDOUT, close_fds=True)
            self.stdout, self.nothing = self.final.communicate()
            print(self.stdout)
            if self.final.returncode != 0:
                print('unable to get guide for ' + str(self.stdout))
                logging.exception(self.stdout)
