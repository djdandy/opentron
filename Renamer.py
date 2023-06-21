#Use by placing this file/code in the folder with all the files that need to be renamed - it's doing all relative work.

import os #Grabbing special commands
import time

FileList=[] #Creating empty list and generic index
i=0

def renamer(Matching): #New definition and grabbing index
    global i
    if Matching not in FileList: #If the input variable is not in the renamed FileList, add it to it and rename accordingly - reset index
        FileList.append(Matching)
        os.rename(File,Matching)
        i=0
    else: #If the input variable is in the renamed field, use OG FixedSampleName and slap a raising index copy value to it and loop
        i=i+1
        SuperFixedSampleName="Copy (" + str(i) + ") - " + FixedSampleName
        renamer(SuperFixedSampleName)

for File in os.listdir(): #Rename all files to unique names to avoid copies already being present when renaming
    if File.endswith(".ars"):
        t = time.localtime()
        current_time = time.strftime("%H.%M.%S.", t)
        i=i+1
        os.rename(File,str(current_time)+str(i)+".ars")

for File in os.listdir(): #With our unique names, open/read, and manipulate desired sample names, then input FixedSampleName into the renamer to make sure that it is unique as well
    if File.endswith(".ars"):
        Data=open(File,'r')
        Data.readline()
        Data.readline()
        Data.readline()
        SampleLine=Data.readline()
        One=SampleLine.find('"1"')
        SampleBegin=SampleLine.find('"',One+3)
        SampleEnd=SampleLine.find('"',SampleBegin+1)
        SampleName=SampleLine[SampleBegin+1:SampleEnd]+".ars"
        Data.close()
        FixedSampleName=SampleName.replace("/","&")
        renamer(FixedSampleName)
