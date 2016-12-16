import xml.etree.ElementTree as ET
import logging
import shutil
from subprocess import Popen, PIPE, STDOUT
from datetime import datetime


logging.basicConfig(filename='error.log', level=logging.DEBUG, format='%(asctime)s %(message)s')


def merge_xmls():
    print('merging xmls...')
    xmllist = ['can.xml', 'uk.xml', 'usa.xml']
    with open("guide.xml", "w") as t:
        t.write('''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE tv SYSTEM "xmltv.dtd">
<tv source-info-name="Schedules Direct" generator-info-name="viper8690" generator-info-url="yahyabell.com">
</tv>''')
    for xml in xmllist:
        try:
            print('merging ' + xml + '...')
            new_data_root = ET.parse(xml).getroot()
            template_root = ET.parse('guide.xml').getroot()

            for element in new_data_root:
                template_root.append(element)

            remove_nodes = ['credits', 'episode-num', 'previously-shown', 'audio', 'subtitles','rating', 'length']
            programs = template_root.findall('programme')

            for program in programs:
                for node in remove_nodes:
                    tags = program.findall(node)
                    for tag in tags:
                        program.remove(tag)
                program.find('title').text = program.find('title').text.replace('*', '[New]')
            with open("guide.xml", "w") as t:
                    t.write('''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE tv SYSTEM "xmltv.dtd">
''')
            with open("guide.xml", "ab") as f:
                f.write(ET.tostring(template_root, encoding="utf-8"))
        except:
            print(xml + ' not available; skipping')
            logging.exception(xml + ' not available')

def copy_guide():
    try:
        print('moving guide.xml')
        shutil.copy('guide.xml', '../epg/guide.xml')
    except:
        logging.exception('unable to copy guide to directory')

# Need to ensure that the github account is setup with ssh key from AWS.
def upload_to_github():
    try:
        print('uploading to github...')
        git_cmd = 'cd ~/github/epg/; git commit -a -m "New Guide Push ' + str(datetime.utcnow()) + '"; git push'
        console_push = Popen(git_cmd, shell=True, stdin=PIPE,
                      stdout=PIPE, stderr=STDOUT, close_fds=True)
        stdout, nothing = console_push.communicate()
        print(stdout)
        if console_push.returncode != 0:
            logging.exception(stdout)
    except:
        print('unable to push to github')
        logging.exception('unable to push to github')
