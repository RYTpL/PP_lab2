from task1 import run1
from task2 import run2
from task3 import run3
from task4 import get_next_element

if __name__== '__main__':
    run1('zebra', 'annotation1.csv')
    run2('datasetcopy1', 'annotation.csv')
    run3('datasetcopy2', 'annotation.csv')


    for item in get_next_element('zebra'):
        print(item)
