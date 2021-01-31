import xml.etree.ElementTree as ET
import os

space = 40*70
xml_path = "VOC_data/Annotations"
save_path = "VOC_data/Anno"


def filter_xml():
    for file_name in os.listdir(xml_path):
        file_path = os.path.join(xml_path, file_name)
        print(file_path)
        in_file = open(file_path)
        tree = ET.parse(in_file)  # ET是一个xml文件解析库，ET.parse（）打开xml文件。parse--"解析"
        root = tree.getroot()  # 获取根节点

        write_flag = False

        for obj in root.findall('object'):  # 找到根节点下所有“object”节点
            bbox = obj.find('bndbox')
            x1 = int(bbox.find('xmin').text)
            y1 = int(bbox.find('ymin').text)
            x2 = int(bbox.find('xmax').text)
            y2 = int(bbox.find('ymax').text)

            if (x2-x1)*(y2-y1) >= space:
                write_flag = True
        if write_flag:
            tree.write(os.path.join(save_path, file_name))
            print("save file: {}".format(os.path.join(save_path, file_name)))


if __name__ == '__main__':
    filter_xml()