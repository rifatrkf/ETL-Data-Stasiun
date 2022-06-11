import requests
from bs4 import BeautifulSoup
import csv

r = requests.get(f"https://www.bmkg.go.id/profil/stasiun-upt.bmkg")
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.original_encoding)
table = soup.find("table",{"class":"table table-hover table-striped"}) # to select the right table

# cari semua baris data
rows = table.findAll('tr')

# pisahkan header dengan baris
headers = rows[0]
header_text = []

# menambahkan teks header ke array
for th in headers.findAll('th'):
    header_text.append(th.text)

# init row text array
row_text_array = []

# loop setiap baris dan tambahkan ke array
# for row in rows[1:]:
#     row_text = []
#     loop through the elements
#     for row_element in row.findAll(['th', 'td']):
#         append the array with the elements inner text
        # row_text.append(row_element.text.replace('\n', '-').strip())
    # append the text array to the row text array
    # row_text_array.append(row_text)

# with open("data stasiun_raw3.csv", "w") as f:
#     wr = csv.writer(f)
#     wr.writerow(header_text)
#     for row_text_single in row_text_array:
#         wr.writerow(row_text_single)