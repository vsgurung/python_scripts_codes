#!/usr/bin/python 
# -*- coding: utf-8 -*-

# Importing modules
import arcpy
import xlwt
import pythonaddins
import os

# Selecting the layer and choosing the fields to be exported
inputLayer = arcpy.GetParameterAsText(0)
fieldsName = arcpy.GetParameterAsText(1)
fdList = fieldsName.split(";")
fileName = arcpy.GetParameterAsText(2)
fileLoc = arcpy.GetParameterAsText(3)
fileExtension = '.xls'

# Creating folder

#currDir = os.getcwd()

folderLoc = fileLoc+'\\test'

if os.path.isdir(folderLoc):
    arcpy.AddMessage('Exporting data....')
else:
    folderLoc = os.chdir(os.mkdir(fileLoc+'\\test'))
    
book = xlwt.Workbook(encoding ="utf-8")

sheet1=book.add_sheet("Data Source")
cursor = arcpy.da.SearchCursor(inputLayer,fdList)
for k,header in enumerate(fdList):
    sheet1.write(0,k,header)
    for i,row in enumerate(cursor):
        for j,col in enumerate(row):
            sheet1.write(int(i)+1,int(j),col)
    
book.save(folderLoc+'\\'+fileName+fileExtension)




