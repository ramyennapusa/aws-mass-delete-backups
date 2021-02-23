
mass delete aws backup recovery points

If you have the list of recovery ids in an excel sheet that need to be deleted from AWS Backup, you can use this python script by passing the excel work book as the parameter.

**PreRequisites:**
1.The excel should be in .xls format only.You can change .xlsx to .xls by going to file menu and "save as"
2.You should have been already logged in to aws CLI profile.

**Sample excel:** 
![alt text](https://github.com/ramyennapusa/aws-mass-delete-backups/blob/main/image1.jpeg?raw=true)

When you run the python program , it will ask for three inputs,
1.Absolute path to the .xls file
2.Exact name of the sheet in the workbook
3.The number for the column that has the 'identifier' value.

![alt text](https://github.com/ramyennapusa/aws-mass-delete-backups/blob/main/image2.jpeg?raw=true)

