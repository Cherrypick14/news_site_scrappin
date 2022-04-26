#    a web scraper that takes in a news site url as input. Scraps all news data from the
#   page and stores it in a text file. It provides the user with the option of viewing the
#   news article on the CLI app

from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
import os
import urllib.request


# initialize our screen
window =Tk()

title = window.title("Welcome to your favorite web scraping app")

#   give our window some dimensions
# using canvas to create our dimensions

canvas = Canvas(window, width=800, height=600)

canvas.pack()

window.configure(background='#A6CFA0')

# Creating our widgets

Label= Label(window, text="Enter a URL here: ",font=('Open Sarif', 12))
text_input = Entry(window, width=50)
text_input.insert(END, "https://www.")
text= Text(window) 
scrollbar=ttk.Scrollbar(window, orient='vertical', command=text.yview)
text.config(yscrollcommand=scrollbar.set,font=('Arial', 8, 'bold', 'italic'))
text.config(state=NORMAL)
text['yscrollcommand'] = scrollbar.set

# defining our functionalities
def news_scrap():
    with urllib.request.urlopen(text_input.get()) as response:
        soup = BeautifulSoup(response.read(), 'html.parser')
      
    data= soup.body.text
    text.insert(1.0,data)
    f=open('data.txt','w+') 
    print(f.write(data))
    os.startfile('data.txt')
    
def delete_text():
    text.delete('1.0','end') 
    f =open('data.txt', 'r+')
    f.truncate(0)
# text_input.delete('0', 'end')
   # f_name=open(text_input)
   # f_name.truncate(0)
    
def clear_url():
    text_input.delete('0','end')
# defining our buttons
myButton = Button(window, width=20, text=" Start Srap", command=news_scrap)
myDeletebtn = Button(window, width=20,text=" Delete Content", command= delete_text)
myaClearUrlbtn = Button(window, width=20,text=" Clear URL", command= clear_url).pack()


# loading the widgets to our GUI
canvas.create_window(410,50, window=Label)
canvas.create_window(410,80, window=text_input)
canvas.create_window(400,300, window=text)
canvas.create_window(650,330, window=scrollbar)
canvas.create_window(410,520, window=myButton)
canvas.create_window(410,570, window=myDeletebtn)

window.mainloop()













