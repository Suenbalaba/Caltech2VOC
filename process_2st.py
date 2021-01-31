import os
import shutil
from tqdm import tqdm

xml_path = "VOC_data/Anno"
jpg_path = "VOC_data/JPEGImages"
save_path = "VOC_data/JPEG"


if __name__ == '__main__':
    filter = []
    print("filter loading...")
    for file in tqdm(os.listdir(xml_path)):
        filter.append(os.path.splitext(file)[0])

    for file in os.listdir(jpg_path):
        if os.path.splitext(file)[0] in filter:
            old_path = os.path.join(jpg_path, file)
            new_path = os.path.join(save_path, file)
            shutil.copyfile(old_path, new_path)
            print("Success save jpg file: {}".format(new_path))

    print("Success!")