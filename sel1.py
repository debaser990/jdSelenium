from selenium import webdriver
import csv
import re

#url = jd_scraper.url
#print(url)


phonebook = {"mobilesv icon-acb":0,
             "mobilesv icon-yz":1,
             "mobilesv icon-wx":2,
             "mobilesv icon-vu":3,
             "mobilesv icon-ts":4,
             "mobilesv icon-rq":5,
             "mobilesv icon-po":6,
             "mobilesv icon-nm":7,
             "mobilesv icon-lk":8,
             "mobilesv icon-ji":9,
             "mobilesv icon-fe":"(",
             "mobilesv icon-hg":")",
             "mobilesv icon-dc":"+",
             "mobilesv icon-ba":"-"
                 }

page_number= 1



def numero():
       
    #element1 = driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div/section/div/ul/li[1]/section/div[1]/section/div[1]/p[2]')

    element2 = driver.find_elements_by_css_selector('p.contact-info')
    
    j = []
    
    for i in range(len(element2)):
        j.append(element2[i].get_attribute('innerHTML'))
  
    for i in j:
        j[j.index(i)] =  re.findall(r"mobilesv icon-\w+",i)
    for i in j:
        del i[0:6]
        
    numList = []
    for i in j:
        numList.append(IconMap2Num(i))
    return numList


def IconMap2Num(innerList):
    numstr =''
    for i in innerList:
        numstr+= str(phonebook[i])

    return numstr

def getName():
    elementName = driver.find_elements_by_css_selector('span.lng_cont_name')
    nameLis = []
    for i in elementName:
        nameLis.append(i.text)
    return nameLis

def getAddress():
    elementAdd = driver.find_elements_by_css_selector('span.cont_fl_addr')
    addLis=[]
    for i in elementAdd:
        addLis.append(i.get_attribute('innerHTML'))
    return addLis

def getRatings():
    elementRating = driver.find_elements_by_css_selector('span.green-box')
    ratLis = []
    for i in elementRating:
        ratLis.append(i.text)
    return ratLis

def getRateCounts():
    elementRCounts = driver.find_elements_by_css_selector('span.rt_count')
    rcLis1 = []
    rcLis2 = []
    for i in elementRCounts:
        rcLis1.append(i.text)
    rcLis1.reverse()
    del rcLis1[1::2]
    rcLis1.reverse()
    return rcLis1

def merge_two_dicts(phonebook, ph):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = phonebook.copy()
    z.update(ph)
    return z
  
stop = 2 ######STOP HERE Enter number of pages to crawl

dict1  = {}
fields = ['Name', 'Phone', 'Rating', 'Rating Count', 'Address']
out_file = open('SavedData.csv','w')
csvwriter = csv.DictWriter(out_file, delimiter=',', fieldnames=fields)
csvwriter.writeheader()



for i in range(1,stop+1):
    driver = webdriver.Chrome("C:\Windows\chromedriver.exe")
    url = "https://www.justdial.com/Delhi/Ro-Water-Purifier-Manufacturers/nct-10411295/page-%s" % (i)
    driver.get(url)

    nameList = getName()
    numList = numero()
    addList = getAddress()
    ratList = getRatings()
    rcList = getRateCounts()

    

    if nameList != None:
        for k in range(len(nameList)):
            
                   
            dict1['Name'] = nameList[k]
            print(numList[k])
            dict1['Phone'] = numList[k]
            dict1['Address']= addList[k]
            dict1['Rating'] = ratList[k]
            dict1['Rating Count'] = rcList[k]
             
            csvwriter.writerow(dict1)          
            
        


    print(dict1)
    
    csvwriter.writerow(dict1)
    driver.close()

    

		
#print(numList)
#print(nameList)    
#print(addList)
#print(ratList)#
#print(rcList)
#print(dictz)

out_file.close()
driver.quit()
    















 
