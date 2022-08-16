import fitz

def classifier(pdf_file):
    with open(pdf_file,"rb") as f:
        pdf = fitz.open(f)
        res = []
        for page in pdf:
            image_area = 0.0
            text_area = 0.0
            for b in page.get_text("blocks"):
                if '<image:' in b[4]:
                    r = fitz.Rect(b[:4])
                    image_area = image_area + abs(r)
                else:
                    r = fitz.Rect(b[:4])
                    text_area = text_area + abs(r)

            if text_area==0 and image_area !=0:
                res.append(0)
            elif text_area!=0 and image_area==0:
                res.append(1)
        return res,len(pdf)

file_path = "compound.pdf"
classifier_result,no_pages=classifier(file_path)
if len(classifier_result)!=no_pages:
    print("Image is empty or Compounded Image")
elif 0 not in classifier_result:
    print("PDF is text-based!")
elif 1 not in classifier_result:
    print("PDF is image-based!")
