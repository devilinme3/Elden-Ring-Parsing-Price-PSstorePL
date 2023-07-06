from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter import ttk
from datetime import datetime 

def time():
    global now, current_time
    now = datetime.now() 
    current_time = now.strftime("%H:%M:%S") 

def windows():
    global wqe, wqe2, main
    main = Tk()
    main.geometry("300x300")
    main.title("Скидки на Elden Ring")
    wqe = Label(text = "В данный момент цена:" + str(price))
    wqe.pack()
    wqe2 = Label(text= f"Последний раз обновлялось в:{current_time}")
    wqe2.pack()
    btn = ttk.Button(text = "Обновить",command = update)
    btn.pack()
    main.mainloop()

def update():
    time()
    current_time = now.strftime("%H:%M:%S") 
    wqe2["text"]= current_time
    main.destroy()
    windows()     

time()
url = 'https://store.playstation.com/pl-pl/product/EP0700-PPSA04609_00-ELDENRING0000000'
page = requests.get(url)
 
soup = BeautifulSoup(page.text, "html.parser")

price = soup.find('span', class_='psw-t-title-m')
price = price.text[0:-3]
price = price.replace(',','.')
price = float(price)
if price == 299.00: 
    windows()
elif price < 299.00:
    print(f"Появилась скидка, в данный момент игра стоит {price}zl.")
