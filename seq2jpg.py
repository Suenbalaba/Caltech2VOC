import os
import fnmatch


def open_save(file, savepath):
    f = open(file, 'rb')
    # 将seq文件的内容转化成str类型
    string = f.read().decode('latin-1')

    # splitstring是图片的前缀，可以理解成seq是以splitstring为分隔的多个jpg合成的文件
    splitstring = "\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46"  
    # split函数做一个测试,因此返回结果的第一个是在seq文件中是空，因此后面省略掉第一个
    strlist = string.split(splitstring)

    f.close()
    count = 0  

    # 遍历每一个jpg文件内容，然后加上前缀合成图片
    for img in strlist:        
        filename = str(count)+'.jpg'
        filename = savepath + filename
        if count > 0:                                    
            i = open(filename, 'wb+')
            i.write(splitstring.encode('latin-1'))
            i.write(img.encode('latin-1'))
            i.close()
        count = count + 1
        print("Generating JPEGImages jpg file of picture:{}".format(filename))


def main():
    seq_inputdir = "D:\Project\Caltech2VOC\Caltech"
    jpg_outputdir = "D:\Project\Caltech2VOC\VOC_data\JPEGImages"

    for dir_set in os.listdir(seq_inputdir):
        # 若果是set01、set02……这类文件夹
        if dir_set[0:3] == "set" and os.path.splitext(dir_set)[1] == '':
            dir_set_seq = os.path.join(seq_inputdir, dir_set)
            for dir_seq in os.listdir(dir_set_seq):
                if fnmatch.fnmatch(dir_seq, '*.seq'):
                    file_dir = os.path.join(dir_set_seq, dir_seq)
                    save_dir = os.path.join(jpg_outputdir, dir_set) + '_' + dir_seq.split('.')[0] + '_'
                    open_save(file_dir, save_dir)


if __name__ == '__main__':
    main()
    print("Success！")