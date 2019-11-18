# import libraries
try:
    from googlesearch import search
    from bs4 import BeautifulSoup
    import requests
    import csv
except ImportError:
    print("A library is not found")

comData = []

# GET Product or Niche Keyword from user and validate it.
def getKeyword():
    keyword = input("What is your product/niche? ")
    if keyword.strip() != "":
        if type(keyword) == type(str()):
           return keyword
    return None

# Search for the keyword based on STAGE 1 query
def searchGoogle():
    res = []
    keyword = getKeyword()
    print(keyword)
    if keyword != None:
        query = "Top 5 " + keyword + "companies"
        # run google search
        for j in search(query, tld="com", num=10, stop=10, pause=2):
            res.append(j)
    return res

# GET data from search results
def getData():
    res = searchGoogle()
    print(res)
    if len(res) != 0:
        for url in res:
            r = requests.get(url)
            # structuring data for scrapping
            soup = BeautifulSoup(r.content, 'html5lib')
            data = findData(soup)
            # print(data)
            if data != None:
                rows = findRows(data)
                for row in rows:
                    companyData = {}
                    companyData['name'] = getCompanyName(row)
                    companyData['link'] = getCompanLink(row)
                    companyData['rating'] = getCompanyRating(row)
                    companyData['reviews'] = getCompanyReviews(row)
                    comData.append(companyData)
                    cleanData()
            else:
                print("Data not Found")
    else:
        print("No search result on this product/niche")
    return comData

# Find Data from Webpage
def findData(soup):
    if soup.find('div', attrs = {'class':'view-content container'}) != None:
        return soup.find('div', attrs = {'class':'view-content container'})
    return None

# Find row containing needed data
def findRows(data):
    if data.findAll('li', attrs = {'class':'views-row'}) != None:
        return data.findAll('li', attrs = {'class':'views-row'})
    return None

# GET company name from row
def getCompanyName(row):
    if row.h3.a.span.text.strip() != None:
        return row.h3.a.span.text.strip()
    return None
# GET company website url link from row
def getCompanLink(row):
    if row.h3.a['href'].strip() != None:
        return row.h3.a['href'].strip()
    return None
# GET company rating from row
def getCompanyRating(row):
    if row.find('div', attrs = {'class':'widget-total-reviews'}) != None:
        rating = row.find('div', attrs = {'class':'widget-total-reviews'})
        return rating.text.strip()
    return None
# GET company reviews from row
def getCompanyReviews(row):
    if row.find('div', attrs = {'class':'widget-reviews-count'}) != None:
        reviews = row.find('div', attrs = {'class':'widget-reviews-count'})
        return reviews.find('span', attrs = {'class':'count'}).text.strip()
    return None

# Cleaning data by removing null fields and nosie
def cleanData():
    for data in comData:
        if(data['rating'] == None):
            comData.remove(data)

# Save data as csv
def exportCSV():
    organize = sorted(comData, key = lambda i: i['rating'],reverse=True) # Organizing data by sorting it desc
    # print(organize)
    filename = 'companyData.csv'
    with open(filename, 'w') as f:
        w = csv.DictWriter(f,['name','link','rating','reviews']) 
        w.writeheader()
        if len(organize) != 0:
            for data in organize:
                w.writerow(data)
        else: print('Data is empty')
    print("Export to csv completed")

if __name__ == '__main__':
    comData = getData()
    exportCSV()
