from ast import keyword
import pytesseract
from pytesseract import Output
import PIL.Image
import cv2
import sys

pytesseract.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe' 
#print(os.getcwd())

def text_clean(text):
    text = text.lower()
    text = text.replace(",","")
    text=''.join(e for e in text if e.isalnum())
    return text


def find_keyword_higlight(TestFileName , singlekey, iter_num):

    if(iter_num==0):
        img=cv2.imread(FolderLocation+TestFileName)
    else:
        img=cv2.imread(FolderLocation+'output_'+TestFileName)
    
    
    #Can be added during preprocessing
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    d=pytesseract.image_to_data(image=img, config=pytesseract.pytesseract.tesseract_cmd, output_type=Output.DICT)

    for key in d:
        print(key, '\t',type(d[key]),'\n\n')

    n_boxes = len(d['level'])

    #Can be added during Preprocessing
    #img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    
    overlay=img.copy()
    # For roll back when next occurance word not found
    original_img = img.copy()


    for i in range(n_boxes):
        Flag=True
        if text_clean(d['text'][i])==text_clean(singlekey[0]):

            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            (x1, y1, w1, h1) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            cv2.rectangle(overlay, (x, y), (x1 + w1, y1 + h1), (255, 0, 0), -1)

            alpha = 0.4
            img_new = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)

            '''
            r = 1000.0 / img_new.shape[1]  # resizing image without loosing aspect ratio
            dim = (1000, int(img_new.shape[0] * r))

            # perform the actual resizing of the image and show it
            resized = cv2.resize(img_new, dim, interpolation=cv2.INTER_AREA)
            '''

            for counter in range(1,len(singlekey)):
                #print(counter)
                if text_clean(d['text'][i+counter]) == text_clean(singlekey[counter]):
                    #print(d['text'][i+counter])

                    (x, y, w, h) = (d['left'][i+counter], d['top'][i+counter], d['width'][i+counter], d['height'][i+counter])
                    (x1, y1, w1, h1) = (d['left'][i+counter], d['top'][i+counter], d['width'][i+counter], d['height'][i+counter])
                    cv2.rectangle(overlay, (x, y), (x1 + w1, y1 + h1), (255, 0, 0), -1)

                    alpha = 0.4  # Transparency factor.
                    # Following line overlays transparent rectangle over the image
                    img_new = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)


                    '''
                    r = 1000.0 / img_new.shape[1]  # resizing image without loosing aspect ratio
                    dim = (1000, int(img_new.shape[0] * r))

                    # perform the actual resizing of the image and show it
                    resized = cv2.resize(img_new, dim, interpolation=cv2.INTER_AREA)
                    '''

                    # For rollback
                    Flag = False

                #print(Flag)
                if Flag:
                    # Rolling back since no next occurance word is found
                    overlay = original_img.copy()

    cv2.imwrite(FolderLocation + 'output_'+TestFileName ,img_new)
    return FolderLocation + 'output_'+TestFileName
    
    cv2.imshow("boxes",img_new)
    cv2.waitKey(0)

FolderLocation=input("Enter path of file: ")
TestFileName=input("Enter filename: ")

keywords=[]
line=input("Enter list of keywords: \n")
keywords.append(line)
while (line!=''):
    line=input()
    if(line!=''):
        keywords.append(line)

# Main Function
for i in range(len(keywords)):
    singlekey=keywords[i]
    singlekey = singlekey.split(' ')
    print(singlekey)
    
    find_keyword_higlight(TestFileName,singlekey,i)
    
    #break # Break for keywords
