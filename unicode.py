import requests 
import simplejson
import selenium
from selenium import webdriver

string = "Hello World"
a = [1, 2, 3, 4, 5]
size = 5
arr = bytes(size)
# arr = bytes(string, 'utf-8')
arr = bytes(a)
print(arr)
for byte in arr:
    print(byte, end=' ')
# print("\n")

url_pdf = "https://pages.cs.wisc.edu/~remzi/OSTEP/preface.pdf"
url     = "https://pages.cs.wisc.edu/~remzi/OSTEP/"
response = requests.get(url)

# print(r.content)
# print("type: ", type(response.content))
# print(response.encoding)
# print(response.content)
pdf = open("pdf.pdf", 'wb')
pdf.write(response.content)
pdf.close()
# options = webdriver.ChromeOptions()
# options.add_experimental_option('prefs', {
# "download.default_directory": r"C:/Users/ramna/Desktop", #Change default directory for downloads
# "download.prompt_for_download": False, #To auto download the file
# "download.directory_upgrade": True,
# "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
# })
# driver = webdriver.Chrome(r"C:/Users/ramna/Desktop/chromedriver.exe", chrome_options=options)
# driver.get(r"https://pages.cs.wisc.edu/~remzi/OSTEP/preface.pdf")