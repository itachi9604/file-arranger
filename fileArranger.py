import os
import re
import tkinter
from tkinter import filedialog
root = tkinter.Tk()
root.withdraw()
ch=''
while ch!='y':
    userPath = filedialog.askdirectory()
    print("Confirm modification on : ",userPath)
    ch=input("y/n?")

# userPath=input("")
extensionSet={}
os.chdir(userPath)
arr=os.listdir(userPath)

extArr=[]
extArrFinal=[]
folderNames=[]
listNames=[]
listNamesFinal=[]

# for finding aut the total extensions and collecting it to a set

patternExt="\.{1}[a-zA-Z34]*$"
for items in arr:

    matches = re.compile(patternExt)
    extArr.append((matches.findall(items)))
for ext in extArr:
    for e in ext:
        extArrFinal.append(e)
extensionSet=set(extArrFinal)


# to get folders names with the names of extensions.

regexFolder="[a-zA-Z34]*$"
for item in extensionSet:
    foldMatch=re.compile(regexFolder)
    listNames.append((foldMatch.findall(item)))
for name in listNames:
    for items in name:
        if len(items)>0:
            listNamesFinal.append(items)


# creating folders
for name in listNamesFinal:
    if(os.path.exists(name))==0:
        os.mkdir(name)

# finding file pattern
for items in arr:
    moveFilePat=re.compile(patternExt)
    fileExtension=(moveFilePat.findall(items))
    for item in fileExtension:
        if item in extensionSet:
            getFolderName=foldMatch.findall(item)
            for name in getFolderName:
                if len(name)>0:
                    getFolderName=name
            os.rename(f"{items}",f"{userPath}/{getFolderName}/{items}")










