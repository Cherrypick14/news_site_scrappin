#    a web scraper that takes in a news site url as input. Scraps all news data from the
#   page and stores it in a text file. It provides the user with the option of viewing the
#   news article on the CLI app

from bs4 import BeautifulSoup
from tkinter import *
import urllib.request


# initialize our screen
window =Tk()

title = window.title("Welcome to your favorite web scraping app")

#   give our window some dimensions
# using canvas to create our dimensions

canvas = Canvas(window, width=800, height=600)

canvas.pack()

window.configure(background='#A6CFA0')

Label= Label(window, text="Enter a URL here: ",font=('Open Sarif', 12))
text_input = Entry(window, width=50)
text_input.insert(END, "https://www.")
text= Text(window)

def news_scrap():
    with urllib.request.urlopen(text_input.get()) as response:
        soup = BeautifulSoup(response.read(), 'html.parser')
    data= soup.body.text
    #my_data= soup.prettify()
    text.insert(1.0,data)


myButton = Button(window, width=20, text=" Start Srap", command=news_scrap)


canvas.create_window(410,50, window=Label)
canvas.create_window(410,80, window=text_input)
canvas.create_window(400,300, window=text)
canvas.create_window(410,520, window=myButton)


window.mainloop()













