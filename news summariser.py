import tkinter as tk
import nltk
# from textblob import TextBlob
from newspaper import Article
nltk.download('punkt')

# url entry parser and summarise function
def summarise():
# Retreive text from tkinter url entry box
    url = urlbox.get('1.0', 'end').strip()
    # Downloads article from user entered url and parses through an nlp to summarise
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    # Enables changes to be made to tkinter text boxes
    titlebox.config(state='normal')
    authorbox.config(state='normal')
    pbox.config(state='normal')
    summarybox.config(state='normal')
    
    
    # Clears Boxes and Inserts Newspaper Information 
    titlebox.delete('1.0', 'end')
    titlebox.insert('1.0', article.title)
    
    authorbox.delete('1.0', 'end')
    authorbox.insert('1.0', article.authors)
    
    pbox.delete('1.0', 'end')
    pbox.insert('1.0', article.publish_date)
    
    summarybox.delete('1.0', 'end')
    summarybox.insert('1.0', article.summary)
    
    # Disables changes for tkinter text boxes
    titlebox.config(state='disabled')
    authorbox.config(state='disabled')
    pbox.config(state='disabled')
    summarybox.config(state='disabled')

    

root = tk.Tk()
root.title('News Summariser')
root.geometry('1200x600')

# Title
tlabel = tk.Label(root, text = 'Title')
tlabel.pack()
titlebox = tk.Text(root, height=1, width=140)
titlebox.config(state='disabled', bg='#dddddd')
titlebox.pack()

# Author
authorlabel = tk.Label(root, text = 'Author')
authorlabel.pack()
authorbox = tk.Text(root, height=1, width=140)
authorbox.config(state='disabled', bg='#dddddd')
authorbox.pack()

# Publish Date
plabel = tk.Label(root, text = 'Publishing Date')
plabel.pack()
pbox = tk.Text(root, height=1, width=140)
pbox.config(state='disabled', bg='#dddddd')
pbox.pack()

# Summary
summarylabel = tk.Label(root, text = 'Sumamry')
summarylabel.pack()
summarybox = tk.Text(root, height=20, width=140)
summarybox.config(state='disabled', bg='#dddddd')
summarybox.pack()

# Url Entry Form

ulabel = tk.Label(root, text = 'URL')
ulabel.pack()
urlbox = tk.Text(root, height=1, width=140)
urlbox.pack()
# The button
thebutton = tk.Button(root, text='Summarise', command=summarise)
thebutton.pack()


root.mainloop()