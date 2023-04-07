import os

File="AAA_1776.ars"
Data=open(File,"r")

Data.readline()
Data.readline()
Data.readline()
Fourth=Data.readline()
one=Fourth.find('"1"')
SampleBegin=Fourth.find('"',one+3)
SampleEnd=Fourth.find('"',SampleBegin+1)
SampleName=Fourth[SampleBegin+1:SampleEnd]+".ars"
Data.close()

print(one)
print(SampleBegin)
print(SampleEnd)
print(SampleName)

os.rename(File,SampleName)
