#Use by placing this file/code in the folder with all the files that need to be renamed - it's doing all relative work.

import os

for File in os.listdir():
    #print(File)
    if File.endswith(".ars"):
        Data=open(File,'r')
        Data.readline()
        Data.readline()
        Data.readline()
        SampleLine=Data.readline()
        #print(SampleLine)
        One=SampleLine.find('"1"')
        SampleBegin=SampleLine.find('"',One+3)
        SampleEnd=SampleLine.find('"',SampleBegin+1)
        SampleName=SampleLine[SampleBegin+1:SampleEnd]+".ars"
        Data.close()
        #print(FileName)
        #print(SampleName)
        FixedSampleName=SampleName.replace("/","&")
        #print(FixedSampleName)
        os.rename(File,FixedSampleName)


