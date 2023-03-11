#this code will download the html code of the entered link
#inputing link and file name to store file in
from requests_html import HTMLSession
import requests
link = input('Paste your link here: ')
file_name = input('Enter the file or file location you want to store the webpage in (dont forget to add file attributes such as .html .exe .txt etc) :')
#this code will check if the link entered is wrong and will correct it. eg if value is entered as 'google.com' it will automatically add 'https://'
#we will split each character to check what the user has forgotten to put
separated_link = link.split('.',maxsplit=(3))

#check missing characters and add them to link variable

if separated_link[0] == 'www':
    link = 'https://'+ link

elif separated_link[0] != 'https://www.':
    link = 'https://'+link

#checking if user has forgot to put '.com' or it is intentional like '.in' or '.co' or '.net' or '.org'
if separated_link[-1] != 'in' or separated_link[-1] != 'org' or separated_link[-1] != 'in' or separated_link[-1] != 'net' or separated_link[-1] != 'co':
    if separated_link[-1] != '.com':
        link = link + '.com'

#requesting file
file_value = requests.get(link)

#saving file
with open(str(file_name), 'w', encoding='utf-8') as website_file:
    website_file.write(file_value.text)

print(file_value.text)
print(link)
