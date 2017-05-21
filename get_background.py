#!/usr/bin/python3

import urllib.request as urlreq
import xml.etree.ElementTree as ET

bing_url = "http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=ZH-CN"
bing_main_page = "http://www.bing.com"
image_resolution = "_1920x1080.jpg"


def get_target_xml(xml_url):
    xml_res = urlreq.urlopen(xml_url).read().decode("utf-8")
    print("xml_res has type: {0}".format(type(xml_res)))
    print(xml_res)
    return xml_res


def iter_search_url(_xml_root):
    url_list = []
    for child in _xml_root.iter(tag='urlBase'):
        print('get url: ', child.text)
        url_list.append(child.text)
    return url_list


xml = get_target_xml(bing_url)
xml_root = ET.fromstring(xml)
print('xml_root type: ', type(xml_root))
print("xml_root content: {0}".format(xml_root))
print('xml_root attribute: ', xml_root.attrib)
print('list xml_root: ', list(xml_root))


search_res = iter_search_url(xml_root)
image_name = []
if search_res:
    for item_idx, each_list_item in enumerate(search_res):
        each_list_item = bing_main_page + each_list_item + image_resolution
        search_res[item_idx] = each_list_item
        image_name.append(each_list_item.split('/')[-1])
        print('final url: {0}'.format(each_list_item))
        print('now image name: {0}'.format(image_name))

image = dict(zip(image_name, search_res))
print(image)

for single_image, single_image_url in image.items():
    urlreq.urlretrieve(single_image_url, single_image)


