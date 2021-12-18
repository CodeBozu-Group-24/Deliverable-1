from bs4 import BeautifulSoup
import requests
import csv
from csv import writer
#presidents
data21_pres = requests.get('https://en.wikipedia.org/wiki/Category:21st-century_presidents_of_the_United_States').text
soup21_pres = BeautifulSoup(data21_pres, 'lxml')
data20_pres = requests.get('https://en.wikipedia.org/wiki/Category:20th-century_presidents_of_the_United_States').text
soup20_pres = BeautifulSoup(data20_pres, 'lxml') 

#Vice-Presidents
data21_vp = requests.get("https://en.wikipedia.org/wiki/Category:21st-century_vice_presidents_of_the_United_States").text
soup21_vp = BeautifulSoup(data21_vp, 'lxml')
data20_vp = requests.get("https://en.wikipedia.org/wiki/Category:20th-century_vice_presidents_of_the_United_States").text
soup20_vp = BeautifulSoup(data20_vp, 'lxml')
data19_vp = requests.get("https://en.wikipedia.org/wiki/Category:19th-century_vice_presidents_of_the_United_States").text
soup19_vp = BeautifulSoup(data19_vp, 'lxml')

#creating a list of 21st century presidents
for title in soup21_pres.findAll('div', {"id":"mw-pages"}):
    names_21 = title.find_all('li')
list21_pres = []    
for i in range(len(names_21)):
    list21_pres.append(names_21[i].get_text())

#creating a list of 20th century presidents
for title in soup20_pres.findAll('div', {"id":"mw-pages"}):
    names_20 = title.find_all('li')
list20_pres = [] 
for i in range(len(names_20)):
    list20_pres.append(names_20[i].get_text())

#details for 21st century presidents
for presidents in list21_pres:
    data = requests.get("https://en.wikipedia.org/wiki/{}".format(presidents)).text
    soup = BeautifulSoup(data, 'lxml')
    politician = soup.find('div', class_='fn').get_text()
    politician_fullname = soup.find('div', class_="nickname").get_text()
    birth_date = soup.find('span', class_='bday').get_text()
    age = soup.find('span', class_="noprint ForceAgeToShow").get_text()[5:8]
    data_for_birthplace = soup.find_all('span', class_='noprint')
    full_data = data_for_birthplace[0].parent.get_text()
    full_data.split()
    indices = []
    for i in range(len(full_data)):
        if full_data[i] == ')':
            indices.append(i)
    required_index = indices[1] + 1
    birthplace = full_data[required_index:]
    text_list = ['Democratic', 'Republican']
    parties = []
    for text in text_list:
        party_full = soup.find(lambda tag: tag.name == "a" and text in tag.text).text
        parties.append(party_full)
    details21 = []
    details21.append(politician)
    details21.append(politician_fullname)
    details21.append(birth_date)
    details21.append(age)
    details21.append(birthplace)
    details21.append(', '.join(parties))
    details21.append("President")
    details21.append(21)
    with open('details.csv', 'a') as f:
        writer_object = writer(f)
        writer_object.writerow(details21)
        f.close()

#details for 20st century presidents
for presidents in list20_pres:
    data = requests.get("https://en.wikipedia.org/wiki/{}".format(presidents)).text
    soup = BeautifulSoup(data, 'lxml')
    details20 = []
    politician = soup.find('div', class_='fn').get_text()
    details20.append(politician)
    politician_fullname = soup.find('div', class_="nickname")
    if politician_fullname != None:
        details20.append(politician_fullname.get_text())
    if politician_fullname == None:
        details20.append(politician)    
    birth_date = soup.find('span', class_='bday').get_text()
    details20.append(birth_date)
    age = soup.find('span', class_="noprint ForceAgeToShow")
    if age == None:
        details20.append("Died")
    else:
        details20.append(age.get_text()[5:8])   
         
    birthplace_full = soup.find_all('span', class_='bday')[0]
    #b_reduced = birthplace_full.parent.parent.parent.get_text()
    birthplace_full = birthplace_full.parent.parent
    #print(birthplace_full)
    try:
        info = birthplace_full.find_all('a')[0]
        details20.append(info.text)
    except IndexError:
        details20.append(list(birthplace_full.children)[-1])
    text_list = ['Democratic', 'Republican']
    parties = []
    for text in text_list:
        party_full = soup.find(lambda tag: tag.name == "a" and text in tag.text).text
        parties.append(party_full)
    details20.append(', '.join(parties))
    details20.append("President")
    details20.append(20)
    with open('details.csv', 'a') as f:
        writer_object = writer(f)
        writer_object.writerow(details20)
        f.close()

#creating a list for 21st century vice-presidents
for title in soup21_vp.findAll('div', {"id":"mw-pages"}):
    names_21 = title.find_all('li')
list21_vp = []    
for i in range(len(names_21)):
    list21_vp.append(names_21[i].get_text())

#details for 21st century vice-presidents     
for vice_presidents in list21_vp:
    data = requests.get("https://en.wikipedia.org/wiki/{}".format(vice_presidents)).text
    soup = BeautifulSoup(data, 'lxml')
    politician = soup.find('div', class_='fn').get_text()
    politician_fullname = soup.find('div', class_="nickname").get_text()
    birth_date = soup.find('span', class_='bday').get_text()
    age = soup.find('span', class_="noprint ForceAgeToShow").get_text()[5:8]
    data_for_birthplace = soup.find_all('span', class_='noprint')
    full_data = data_for_birthplace[0].parent.get_text()
    full_data.split()
    indices = []
    for i in range(len(full_data)):
        if full_data[i] == ')':
            indices.append(i)
    required_index = indices[1] + 1
    birthplace = full_data[required_index:]
    text_list = ['Democratic', 'Republican']
    parties = []
    for text in text_list:
        party_full = soup.find(lambda tag: tag.name == "a" and text in tag.text).text
        parties.append(party_full)    
    details21_vp = []
    details21_vp.append(politician)
    details21_vp.append(politician_fullname)
    details21_vp.append(birth_date)
    details21_vp.append(age)
    details21_vp.append(birthplace)
    details21_vp.append(', '.join(parties))
    details21_vp.append("Vice President")
    details21_vp.append(21)
    with open('details.csv', 'a') as f:
        writer_object = writer(f)
        writer_object.writerow(details21_vp)
        f.close()      

#creating a list of 20th century vice-presidents
for title in soup20_vp.findAll('div', {"id":"mw-pages"}):
    names_20 = title.find_all('li')
list20_vp = []    
for i in range(len(names_20)):
    list20_vp.append(names_20[i].get_text())

#details for 20th century vice-presidents 
for vice_presidents in list20_vp:
    data = requests.get("https://en.wikipedia.org/wiki/{}".format(vice_presidents)).text
    soup = BeautifulSoup(data, 'lxml')
    details20_vp = []
    politician = soup.find('div', class_='fn').get_text()
    details20_vp.append(politician)
    politician_fullname = soup.find('div', class_="nickname")
    if politician_fullname != None:
        details20_vp.append(politician_fullname.get_text())
    if politician_fullname == None:
        details20_vp.append(politician)    
    birth_date = soup.find('span', class_='bday').get_text()
    details20_vp.append(birth_date)
    age = soup.find('span', class_="noprint ForceAgeToShow")
    if age == None:
        details20_vp.append("Died")
    else:
        details20_vp.append(age.get_text()[5:8])   
         
    birthplace_full = soup.find_all('span', class_='bday')[0]
    #b_reduced = birthplace_full.parent.parent.parent.get_text()
    birthplace_full = birthplace_full.parent.parent
    #print(birthplace_full)
    try:
        info = birthplace_full.find_all('a')[0]
        details20_vp.append(info.text)
    except IndexError:
        details20_vp.append(list(birthplace_full.children)[-1])
    text_list = ['Democratic', 'Republican']
    parties = []
    for text in text_list:
        party_full = soup.find(lambda tag: tag.name == "a" and text in tag.text).text
        parties.append(party_full)
    details20_vp.append(', '.join(parties))
    details20_vp.append("Vice President")
    details20_vp.append(20)
    with open('details.csv', 'a') as f:
        writer_object = writer(f)
        writer_object.writerow(details20_vp)
        f.close()

#creating a list of 19th century vice-presidents
for title in soup19_vp.findAll('div', {"id":"mw-pages"}):
    names_19 = title.find_all('li')
list19_vp = []    
for i in range(len(names_19)):
    list19_vp.append(names_19[i].get_text())    

#details for 19th century vice-presidents 
for vice_presidents in (list19_vp[0:3] + list19_vp[4:]):
    data = requests.get("https://en.wikipedia.org/wiki/{}".format(vice_presidents)).text
    soup = BeautifulSoup(data, 'lxml')
    details19_vp = []
    politician = soup.find('div', class_='fn').get_text()
    details19_vp.append(politician)
    politician_fullname = soup.find('div', class_="nickname")
    if politician_fullname != None:
        details19_vp.append(politician_fullname.get_text())
    if politician_fullname == None:
        details19_vp.append(politician)    
    birth_date = soup.find('span', class_='bday').get_text()
    details19_vp.append(birth_date)
    age = soup.find('span', class_="noprint ForceAgeToShow")
    if age == None:
        details19_vp.append("Died")
    else:
        details19_vp.append(age.get_text()[5:8])   
         
    birthplace_full = soup.find_all('span', class_='bday')[0]
    birthplace_full = birthplace_full.parent.parent
    try:
        info = birthplace_full.find_all('a')[0]
        details19_vp.append(info.text)
    except IndexError:
        details19_vp.append(list(birthplace_full.children)[-1])
    text_list = ['Democratic', 'Republican']
    parties = []
    for text in text_list:
        party_full = soup.find(lambda tag: tag.name == "a" and text in tag.text).text
        parties.append(party_full)
    details19_vp.append(', '.join(parties))
    details19_vp.append("Vice President")
    details19_vp.append(19)
    with open('details.csv', 'a') as f:
        writer_object = writer(f)
        writer_object.writerow(details19_vp)
        f.close()       

#adding George Clinton separately
clinton = []
link = "https://en.wikipedia.org/wiki/George_Clinton_(vice_president)"
page = requests.get(link)

soup = BeautifulSoup(page.content, 'lxml')

politician = soup.find('div', class_='fn').get_text()
clinton.append(politician)

politician_fullname = soup.find('div', class_="nickname")
if politician_fullname != None:
    clinton.append(politician_fullname.get_text())
if politician_fullname == None:
    clinton.append(politician)

item = soup.find_all('a', {"href": "/wiki/Old_Style_and_New_Style_dates"})[0]

item = list(item.parent.parent.children)[1]
item = list(item.children)
for i in range(len(item)):
    item[i] = item[i].text
dob = ''.join(item[:3])
dob = dob.replace(u'\xa0', u' ')
clinton.append(dob)

age = soup.find('span', class_="noprint ForceAgeToShow")
if age == None:
    clinton.append("Died")
else:
    clinton.append(age.get_text()[5:8])   

clinton.append(''.join(item[3:]))    

text_list = ['Democratic', 'Republican']
parties = []
for text in text_list:
    party_full = soup.find(lambda tag: tag.name == "a" and text in tag.text).text
    parties.append(party_full) #since both parties were same, we can take any one
clinton.append(', '.join(parties))

clinton.append("Vice President")
clinton.append(19)

with open('details.csv', 'a') as f:
    writer_object = writer(f)
    writer_object.writerow(clinton)
    f.close()    
