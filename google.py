# import libraries
try:
    from googlesearch import search
    from bs4 import BeautifulSoup
    import requests
except ImportError:
    print("A library is not found")

# search google
keyword = "Logo Design"
query = "Top 5 " + keyword + "companies"
res = []

# run google search
for j in search(query, tld="com", num=10, stop=10, pause=2):
    res.append(j)

url = res[1]

# send a request
r = requests.get(url)

# structuring data for scrapping
soup = BeautifulSoup(r.content, 'html5lib')


companyData = []  # a list of company data 

# getting data
data = soup.find('div', attrs = {'class':'view-content container'}) 

# finding company info
for row in data.findAll('li', attrs = {'class':'views-row'}):
    companyData.append(row)

print(len(companyData))
print(companyData[0])

