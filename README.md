# Caltech2VOC
#1、将seq文件转为jpg文件并保存在一个文件夹下，利用seq2jpg.py，只需要更改路径。
#2、将vvb文件转为xml文件并保存在一个文件夹中，利用vbb2xml.py，只需要更改路径。
#3、Caltech数据集中图片和标注文件数量不一致，所以需要处理xml文件和jpg文件，并且删除目标极小极小的文件，肉眼根本看不出来的那种，利用process1.py处理xml文件，只需要更改路径
#4、根据xml文件保存相应的jpg文件，利用process2.py处理jpg文件，只需要更改路径。
#5、根据xml文件生成trian.txt、val.txt、test.txt、trainval.txt,利用generateTXT文件。更改路径，并且可以设置数据集的划分比例。
#6、利用txt文件和xml文件生成各数据集对应的json文件，利用voc2coco.py。需修改main函数中的a、b、c路径。
