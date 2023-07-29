import os,shutil

path=r'C:/Users/vivek/Downloads/'

file_name=os.listdir(path)
folder_names=[]

for file in file_name:
    if '.' in file:
        extension=file.split('.')
        name=path+extension[1]
        if not os.path.exists(name):
              os.makedirs(name)
        if name not in folder_names:
            folder=name.split('/')[-1]
            folder_names.append(folder)
    

# print(folder_names)

for file in file_name:
    if '.' in file:
        name=file.split('.')[1]
    else:
        name=file
    for folder in folder_names:
        if name==folder:
            src=path+file
            dest=path+folder+'/'+file
            if os.path.isfile(src):
                shutil.move(src,dest)
          




    
    