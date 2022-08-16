import os
import pdf_classifier

path=input("Enter Path: ")
up_type=int(input("1. File Upload\n2. Folder Upload\nSelect Option: "))

if up_type==1:
    if os.splitext(file_name)[1].lower()=='.pdf':
        pdf_classifer.classifier([file_name])