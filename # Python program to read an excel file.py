# Python program to read an excel file
 
# import openpyxl module
import openpyxl
 
# Give the location of the file
path = "C:\\Users\\10383563\\Downloads\\Proposal-Project Numbers1.xlsx"
 
# To open the workbook 
# workbook object is created
wb_obj = openpyxl.load_workbook(path)
 
# Get workbook active sheet object
# from the active attribute
sheet_obj = wb_obj.active
 