import boto3
import os
import xlrd
import xlwt

# log into the approrpiate profile defined in your computer's aws config
session = boto3.Session(profile_name='prod')
client = session.client("backup")

# define the name of the aws backup vault that has the backups
vault = 'sample-vault'

# define the name of the aws region where the backups are loacted
region = 'us-west-2'
bookPath = input("Enter the workbook's absolute path - ")
sheetName = input("Enter the name of the sheet in the workbook - ")
columnNumber = int(
    input("Enter the Column Number of the id , 0 being the first column - "))

workbook = xlrd.open_workbook(bookPath)
worksheet = workbook.sheet_by_name(sheetName)

for row in range(worksheet.nrows):
    try:
        if (row != 0):
            id = worksheet.cell(row, columnNumber).value
            arn = ''
            if id.startswith('ami'):
                arn = 'arn:aws:ec2:'+region+'::image/'+id
            elif id.startswith('snap'):
                arn = 'arn:aws:ec2:'+region+'::snapshot/'+id
            else:
                print('invalid id')

            #print(arn)
            
            client.delete_recovery_point(
                BackupVaultName=vault,
                RecoveryPointArn=arn
            )
            print('deleted')

    except:
        print(" invalid id / already deleted")
