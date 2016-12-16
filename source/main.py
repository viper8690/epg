from get_guides import Guides
import xml_merger

if __name__ == '__main__':
    Guides().cleanup()
    Guides().get_guides()
    xml_merger.merge_xmls()
    xml_merger.copy_guide()
    xml_merger.upload_to_github()