# import os
#
#
# path='C:\\Users\\gkalaiva\\Pictures\\defectionui\\defectionui\\IA\\media\\sample_file'
# # initialize the size
# total_size = 0
#
# # use the walk() method to navigate through directory tree
# for dirpath, dirnames, filenames in os.walk(path):
#     for i in filenames:
#         # use join to concatenate all the components of path
#         f = os.path.join(dirpath, i)
#
#         # use getsize to generate size in bytes and add it to the total size
#         total_size += os.path.getsize(f)
# mb=total_size/(1024 * 1024)
# print("tolll",mb)

import os
file_name = os.path.basename("/media/sample_file/019_6k5F3KO.png")
extension = os.path.splitext("/media/sample_file/019_6k5F3KO.png")
print("extention",extension)
# file name without extension
file_path = os.path.splitext("".join(list(file_name)))
print("file",file_path)

file1=('019_6k5F3KO', '.png')
sp=" ".join(file1)
print(sp)

import os
current_path = os.getcwd()
print("current_path",current_path)
sp_path = "\\".join(current_path.split("\\")[:-1])
print("sp_path",sp_path)
final_path = sp_path+"\\"+"media\LOT1-bottle"+"\\"
file_li= ["001.png", "002.png", "000.png"]
for i in file_li:
    res=os.path.exists(final_path+i)
    print(res)

ts=[{'name': 'LOT1', 'category': 'capsule'}, {'name': 'LOT1', 'category': 'screw'},
    {'name': 'LOT1', 'category': 'screw'}]
final_li=[]
for i in ts:
    print("iii",i)
    if i not in final_li:
        final_li.append(i)
print(final_li)
