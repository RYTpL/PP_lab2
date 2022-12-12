from task1 import runtask1
from task2 import runtask2
from task3 import runtask3
from task4 import get_next_element


if __name__== '__main__':
    runtask1('zebra', 'annotation1.csv')
    runtask2('datasetcopy1', 'annotation.csv')
    runtask3('datasetcopy27', 'annotation.csv')


    for item in get_next_element('zebra'):
        print(item)
