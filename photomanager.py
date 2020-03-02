import os,glob,shutil


def manager():
    content = os.listdir()
    if 'photos' not in content:
        os.mkdir('photos')
    source_to=os.path.abspath("photos")
    source_from=input("ENTER PATH :")
    
    for items in glob.glob(source_from+'/*.jpg'):
        content_to=os.listdir(source_to)
        item=os.path.basename(items)
        if item not in content_to:
            shutil.copy(items,source_to)
    
    for items in glob.glob(source_from+'/*.jpeg'):
        content_to=os.listdir(source_to)
        item=os.path.basename(items)
        if item not in content_to:
            shutil.copy(items,source_to)

    
    for items in glob.glob(source_from+'/*.png'):
        content_to=os.listdir(source_to)
        item=os.path.basename(items)
        if item not in content_to:
            shutil.copy(items,source_to)
    print("TASK SUCCESSFULLY DONE")

    
manager()