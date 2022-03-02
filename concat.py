# Ideas:
# 1: Sorting by page number and merging - X
# 2: By color of columns
# 3: By small number right beside them
# 4: Html attributes

import requests 
from bs4 import BeautifulSoup
import collections
from PyPDF2 import PdfFileMerger, PdfFileReader

url_pref = "https://pages.cs.wisc.edu/~remzi/OSTEP/"

def download_pdf(url, name = "test"):
    # Get response object for link
    print("downloading: ", name)
    print("url: ", url)
    response = requests.get(url)

    # Write content in pdf file
    pdf_name = "three_easy_pieces/" + name
    pdf = open(pdf_name, 'wb')
    pdf.write(response.content)
    pdf.close()
    print("download_complete")
    # return pdf_name

def merge_pdfs(pdfs):
    mergedObject = PdfFileMerger()    

    for pdf in pdfs:
        mergedObject.append(PdfFileReader("three_easy_pieces/" + pdf, 'rb'))

    mergedObject.write("final_book.pdf")    

###################################### SORTING BY PAGE NUMBER AND THEN MERGIN #####################################################
#Won't work as each pdf has numbering from 0
# def process_pdf(pdf_name):
#     pdfFileObj = open(pdf_name, 'rb')
#     pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#     num_of_pages = pdfReader.numPages
#     page_object = pdfReader.getPage(1)
#     print(pdfReader.getPageNumber(page_object))
###################################################################################################################################

###################################### BY COLOR OF COLUMNS ########################################################################
#Works
def get_colors():
    url = "https://pages.cs.wisc.edu/~remzi/OSTEP/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    hrefs = []
    for link in links:
        if '.pdf' in link.get('href', []):
            hrefs.append(link)
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    c5 = []
    c6 = []
    flag = 0
    over  = 0
    for link in hrefs:
        color = link.parent.get('bgcolor')
        if not color:
            color = link.parent.parent.get('bgcolor')
        # print(color)    
        pdf_name = link.get('href', [])
        if color == "yellow":
            c1.append(pdf_name)
        elif color == "#f88017" and not flag and not over:
            c2.append(pdf_name)
            flag = 1    
        elif color == "#f88017" and flag:
            c3.append(pdf_name)
            if not over:
                flag = 0
        elif color == "#00aacc":
            c4.append(pdf_name)
        elif color == "#4CC417":
            c5.append(pdf_name)    
        else:
            c6.append(pdf_name)    

        if pdf_name == "cpu-dialogue.pdf":
            over = 1    
            flag = 1
    
    c1 += c2
    c1 += c3
    c1 += c4
    c1 += c5
    c1 += c6

    # print(c1)
    for pdf in c1:
        download_pdf(url_pref+pdf, pdf)
    return c1    
###################################################################################################################################

pdfs = get_colors()
merge_pdfs(pdfs)
