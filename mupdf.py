import glob, sys, fitz

pdfIn = fitz.open(r"data/text.pdf")

'''

for page in pdfIn:
    print(page)
    texts = ["of", "the"]
    text_instances = [page.search_for(text) for text in texts] 
    
    # coordinates of each word found in PDF-page
    print(text_instances)  

    # iterate through each instance for highlighting
    for inst in text_instances:
        annot = page.add_highlight_annot(inst)
        
        annot.update()


# Saving the PDF Output
pdfIn.save("data/text_output.pdf")

'''


def pdf_to_img():
        # To get better resolution
    zoom_x = 2.0  # horizontal zoom
    zoom_y = 2.0  # vertical zoom
    mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension

    path = 'data/'
    all_files = glob.glob(path + "*.pdf")

    for filename in all_files:
        doc = fitz.open(filename)  # open document
        for page in doc:  # iterate through the pages
            pix = page.get_pixmap(matrix=mat)  # render page to an image
            pix.save("data/out/page-%i.png" % page.number)  # store image as a PNG

pdf_to_img()