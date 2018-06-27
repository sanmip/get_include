import re
import os
import shutil

def get_cmd_list(cmd):
    """get return list after cmd"""
    return_list = os.popen(cmd).readlines()
    return_new_list = []
    for ele in return_list:
        return_new_list.append(ele.replace("\n", ""))
    return return_new_list

def flatten_list(nested):
    if isinstance(nested, list):
        for sublist in nested:
            for item in flatten_list(sublist):
                yield item
    else:
        yield nested

file_name = raw_input("input dts file name:")

cmd1 = "cpp -nostdinc -I include -undef -x assembler-with-cpp " + file_name
list1 = get_cmd_list(cmd1)

list2 = []
for line in list1:
    if line.find(".dts")>=0:
        list2.append(re.compile('"(.*)"').findall(line))

list3=[]
for i in list2:
    if not i in list3:
        list3.append(i)

list4 = list(flatten_list(list3))

for i in list4:
    print i

dir_name = raw_input("output dir name:")

os.mkdir(dir_name)

for i in list4:
    if os.path.exists(i):
        shutil.copy(i,dir_name+"/"+i)
    else:
        print "copy "+i+" error"





