#
# Hina Sekine
# IB Computer Science Y1 

# MAKE ALL THE DOC STRINGS YOU IDIOT 

# Program Intialization 
import sqlite3 as sq
from datetime import datetime, date

databaseLocation = '/Users/yaylife/Documents/ib cs yay life/Novel Console/novel.db'
con = sq.connect(databaseLocation)
c = con.cursor()

# Functions
def get_books():
    ''' This gets the table Book combined with the table Writer where
        the WriterID is the same
    '''
    res = c.execute('SELECT Book.Title, Book.Genre, Writer.Name FROM Book JOIN Writer WHERE Book.WriterID = Writer.WriterID')
    data = c.fetchall()
    return data

def get_writers():
    ''' This gets the table Writer from the database '''
    res = c.execute('SELECT * FROM Writer')
    data = c.fetchall()
    return data

def display_data(data):
    ''' This function displays the data from a table so all the colums are the
        same length
    '''
    lenMax = [0, 0, 0, 0]
    for row in data:
        for i in range(len(data[0])):
            if len(str(row[i])) > lenMax[i]:
                lenMax[i] = len(str(row[i]))

    end = '-' * sum(lenMax) + '-' * 3 * len(lenMax)
    print(end)
    for row in data:
        string = ''
        for k in range(len(row)):
            string = string + ' ' + str(row[k]) + (' ' * (lenMax[k] - len(str(row[k])))) + ' |'
        print(string)
    print(end)

def add_books(title, genre, writerchoice):
    ''' This adds a book into the Book table '''
    ins_str = 'INSERT INTO Book (Title, Genre, WriterID) VALUES ("' + str(title) + ' ", "' + str(genre) + '", ' +  str(writerchoice) + ');'
    res = c.execute(ins_str)
    con.commit()

def check_and_enter_selection(title, genre, writerchoice):
    ''' This checks if the book is able to be added to the Book table. If not,
        the user can see possible errors
    '''
    try:
        add_books(title, genre, writerchoice)
        print('Success Your reservation has been added!')

    except:
        print("Error- Try again", "Possible errors:  \nthere is already a book for that combination, you chose an invalid writer\nsomeone else is entering a book at the same time")
        return
    
def render_menu():
    ''' This is the menu that directs the user to the possible things they can
        do with the Novel database
    '''
    print('1. Display all novel names')
    print('2. Add a novel')
    print('3. Quit')
    choice = input('Choose an option: ')
    while not choice in ['1', '2', '3']:
        choice = input('Choose an option (1 - 3): ')

    if choice == '1':
        render_book_report()
    elif choice == '2':
        render_book_request()
    elif choice == '3':
        end_program()
        return False

    return True

def render_book_report():
    ''' Option 1: This allows the user to see all the books in the Book table'''
    books = get_books()
    display_data(books)

def render_book_request():
    ''' Option 2: This allows the user to add a book to the Book table'''
    title = input('\nEnter Title: ')
    genre = input('Enter Genre: ')
    
    writers = get_writers()
    display_data(writers)
    writerchoice = input('Choose a writer by ID number: ')

    check_and_enter_selection(title, genre, writerchoice)

def end_program():
    ''' Option 3: This function ends the program '''
    con.close()

# Main
print('This program allows you to do things with the novel database\n')
print('Welcome to our reservation system')

while(render_menu()):
    print('\n\nWelcome to our reservation system')
