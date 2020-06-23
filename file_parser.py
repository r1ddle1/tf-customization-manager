from os import remove
import requests
import xml.etree.ElementTree as et


SOUNDS_DB_LINK = 'https://raw.githubusercontent.com/r1ddle1/tfcm-databases/master/sounds.xml'
HUDS_DB_LINK = 'https://raw.githubusercontent.com/r1ddle1/tfcm-databases/master/huds.xml'
CFG_DB_LINK = 'https://raw.githubusercontent.com/r1ddle1/tfcm-databases/master/cfgs.xml'


def get_remote_file(url):
    req = requests.get(url)

    if req.status_code != 200:
        print("Oops! Couldn't download file!")
        exit(-1)

    return req.text


def get_config(data_type):
    try:
        tree = et.parse('data.xml')
        root = tree.getroot()
        settings = root.find(data_type)
        res = {}
        for i in settings:
            res[i.tag] = i.text
        return res

    except FileNotFoundError:
        return None


def write_config(settings: dict, settings_type):
    try:
        tree = et.parse('data.xml')
        root_node = tree.getroot()

        to_remove = root_node.find(settings_type)
        if to_remove:
            root_node.remove(to_remove)

        new_node = et.SubElement(root_node, settings_type)

        for i in settings.keys():
            sub_element = et.SubElement(new_node, i)
            sub_element.text = settings[i]
        tree.write('data.xml')

    except FileNotFoundError:
        with open('data.xml', 'w') as file:
            file.write('<configuration></configuration>')
        write_config(settings, settings_type)


def get_db(db_type):
    try:
        tree = et.parse(db_type + '.xml')
        root = tree.getroot()
        res = []

        for i in root:
            title = i.attrib['title']
            author = i.attrib['author']
            download_link = i.attrib['link']
            res.append({
                'title': title,
                'author': author,
                'link': download_link
            })
        return res

    except FileNotFoundError:
        # Database is not downloaded. Let's download it
        with open(db_type + '.xml', 'w') as file:
            if db_type == 'sounds_db':
                data = get_remote_file(SOUNDS_DB_LINK)
            elif db_type == 'huds_db':
                data = get_remote_file(HUDS_DB_LINK)
            elif db_type == 'cfg_db':
                data = get_remote_file(CFG_DB_LINK)
            file.write(data)
        return get_db(db_type)


def refresh_db(db_type):
    try:
        remove(db_type + '.xml')
    finally:
        return get_db(db_type)