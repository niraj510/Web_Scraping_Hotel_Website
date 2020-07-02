import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.trip.com/hotels/beijing-hotels-list-1/'
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')

hotelname= []
price= []
rating= []
ratings= []
linkToHotelPage= []
roomtype = []
ammeneties = []


for row in soup.findAll('div', class_='online-h5-hotel-card__title'): 
    datarow = {}
    datarow= row.text
    hotelname.append(datarow)
#print(hotelname)

for row in soup.findAll('span', class_='hotel-card-rating-reviews__badge'): 
    datarow = {}
    datarow = row.text
    rating.append(datarow)
#print(rating)

for i in range(len(hotelname)):
   datarow = {}
   datarow = rating[i]
   ratings.append(datarow)
#print(ratings)    

for row in soup.findAll('span', class_='online-h5-hotel-card__price-text'): 
    datarow = {}
    datarow = row.text
    price.append(datarow)
#print(price)


for a in soup.findAll('a', class_='online-h5-hotel-card__title_info title-over-ellipsis'):
    linkToHotelPage.append(a.text)
#print(linkToHotelPage)


for i in range(len(linkToHotelPage)):
    roomname = {}
    ammenety = {}
    response = requests.get('https://www.trip.com', linkToHotelPage[i])
    soup = BeautifulSoup(response.text,'lxml')
    #print(soup)
    roomName = soup.findAll('div', class_='roomlist-baseroom-card')
    ammenety = soup.findAll('div', class_='desc-text underline')
    roomtype.append('Delux Room')
    ammeneties.append('Buffet Breakfast, extra CNY18.00')
#print(roomtype)
#print(ammeneties)
    
    
writer = pd.ExcelWriter('Hotels.xlsx', engine='openpyxl') 
wb  = writer.book

df = pd.DataFrame({'Country': 'China',
                      'City': 'Beijing',
                      'Date': '18-11-2020',
                      'Night': '7',
                      'Adult': '2',
                      'Hotel Name': hotelname,
                      'Hotel Star Rating': ratings,
                      'Room Name': roomtype,
                      'Beds & Amenities': ammeneties,
                      'Avg. Price Per Room / Night': price})
df.to_excel(writer, index=False)
wb.save('Hotels.xlsx')
