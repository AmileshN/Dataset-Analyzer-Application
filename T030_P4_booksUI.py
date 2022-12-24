#Group: T030  Members: Amilesh Nanthakumaran, George Reda Gad, Ayo Owolabi & Eliana Schartner 
#Version: 1.0
#Date: April 12, 2022


from T030_P5_load_data import * 
from T030_P2_add_remove_search_dataset import * 
from T030_P3_sorting_fun import *


def display() -> None: #Amilesh Nanthakumaran
        ''' Returns the user interface for the interactive dataset analyzer program
        
        >>>display()
        The available commands are:
            1- L)oad data
            2- A)dd book
            3- R)emove book
            4- G)et books
                T)itle R)ate P)ublisher A)uthor
            5- GCT)Get all Categories for book Title
            6- S)ort books
                T)itle R)ate P)ublisher A)uthor
            7- Q)uit

        Please type your command:  
        '''
        print("The available commands are:")
        print("    1- L)oad data")
        print("    2- A)dd book")
        print("    3- R)emove book")
        print("    4- G)et books")
        print("\t T)itle R)ate P)ublisher A)uthor")
        print("    5- GCT)Get all Categories for book Title")
        print("    6- S)ort books")
        print("\t T)itle R)ate P)ublisher A)uthor")
        print("    7- Q)uit\n")

def load_data() -> dict: #Amilesh Nanthakumaran
        '''Returns a dictionary of the inputted dataset based on the category of the book  
        Precondition: The file must be a csv or txt file. 
        
        >>>load_data()
        Enter the name of the file to be loaded: google_books_dataset.csv
        {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400}, {'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': 'English', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'language': 'English', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368},{another element}]
        
        '''
        user_input_file_name = input("Enter the name of the file to be loaded: ")
        data = book_category_dictionary(user_input_file_name)
        return data

#case 1 function (add and remove)
def add_remove_book(data: dict, inputs: str) -> str: #Eliana Schartner 
        '''Returns a string whether the book was added/removed correctly or not.  
        Precondition: Only uses one dataset.
        
         Enter book details - 
         Title: 
         >>> James Big Adventures
         Author: 
         >>> Jon Gaming
         Language: 
         >>> Tagalog
         Publisher: 
         >>> Agorg Productions
         Category: 
         >>> Detective
         Rating: 
         >>> 1.0
         Pages: 
         >>> 390
         The book has been added correctly
    
         Please type your command: 
         >>> R
         Print title of book to remove: 
         >>> Antiques Roadkill: A Trash 'n' Treasures Mystery
         Print category of book to remove: 
         >>> Fiction
         Book has been removed.
         
        '''
        if inputs == "A":
                book_title = str(input("Enter book details - \nTitle: "))
                book_author = str(input("Author: "))
                book_language = str(input("Language: "))
                book_publisher = str(input("Publisher: "))
                book_category = str(input("Category: "))
                book_rating = float(input("Rating: "))
                book_pages = int(input("Pages: "))
                        
                user_input_book_details = (book_title, book_author, book_language, book_publisher, book_category, book_rating, book_pages)
                adding_book = add_book(data, user_input_book_details) 
                
                return adding_book
                    
        elif inputs == "R":
                user_input_title = input("Print title of book to remove: ")
                user_input_category = input("Print category of book to remove: ")
                removing_book = remove_book(data, user_input_title, user_input_category)
                
                return removing_book  

        else:
                return print("No such command")
#case 2/3 function(all get books) 
def get_books(rd_1: dict) -> str: #Ayo Owolabi & Amilesh Nanthakumaran
        ''' Returns data sorted by title, rate, author, publisher, category and, categories depending on the book title. 
        Precondition: Only uses one dataset
        
        >>>get_books(dataset)
        How do you want to find/get books: 
            T)itle
            R)ate
            A)uthor
            P)ublisher
            C)ategory
            Q)uit
            
        Please type your command: 
        >>> P
        The Publisher of the book you wish to find/get is:
        >>>Kensington Publishing Corp.
        The publisher Kensington Publishing Corp. has published the following book(s):
        Book 1 :  Antiques Knock-Off by Barbara Allan
        Book 2 :  Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
        2
        
        '''
        print("How do you want to find/get books: ")
        print("    T)itle")
        print("    R)ate")
        print("    A)uthor")
        print("    P)ublisher")
        print("    C)ategory")
        print("    Q)uit")
        
        collected_user_input = input("\nPlease type your command: ").upper()
        
        if collected_user_input == 'T':
                collected_user_input = input("The title of the book you wish to find/get is: ")
                print(collected_user_input)
                find_books_by_title = get_books_by_title(rd_1, collected_user_input)
                return str(find_books_by_title)                
        
        elif collected_user_input.upper() == 'R':
                collected_user_input = float(input("The rating of the book you wish to find/get is: "))
                print(collected_user_input)
                find_books_by_rate = get_books_by_rate(rd_1, collected_user_input)
                return str(find_books_by_rate)
            
        elif collected_user_input.upper() == 'A':
                collected_user_input = input("The Author of the book you wish to find/get is: ")
                print(collected_user_input)
                find_books_by_author = get_books_by_author(rd_1, collected_user_input)
                return str(find_books_by_author)
        
        elif collected_user_input.upper() == 'P':
                collected_user_input = input("The Publisher of the book you wish to find/get is: ")
                print(collected_user_input)
                find_books_by_publisher = get_books_by_publisher(rd_1, collected_user_input)
                return str(find_books_by_publisher)
        
        elif collected_user_input.upper() == 'C':
                collected_user_input = input("The Category of the book you wish to find/get is: ")
                print(collected_user_input)
                find_books_by_category = get_books_by_category(rd_1, collected_user_input)
                return str(find_books_by_category)  
        elif collected_user_input.upper() == 'Q':
                return ""        
        else:
                print("No such command.")
                return ""
        
#case 3 function (GCT)
def get_all_categories(data: dict) -> str: #Amilesh Nanthakumaran
        '''
        Returns a list of categories that a given book is in. Precondition: Book is in the database and only uses one dataset.
        
        >>>get_all_categories_for_book_title(data, 'After Anna')
        The book title After Anna belongs to the following categories:
        Category 1: Fiction
        Category 2: Thrillers
        Category 3: Mystery
        Category 4: Adventure
        4
        '''
        
        user_input_book_title = input("Enter book title: ")
        get_categories_book_title =  get_all_categories_for_book_title(data,user_input_book_title)
        return get_categories_book_title

#case 4 function(sorting)
def sort_data(data: dict) -> list: #George Reda Gad
        ''' Returns the sorted list based on the method of sorting chosen by the user
        Precondition: Book is in the database and only uses one dataset.
        >>>sort_data(data)
        How do you want to sort?
            T)itle
            R)ate
            P)ublisher
            A)uthor
            Q)uit
        Enter how you want to sort: r
        [{'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': 'English', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'category': ['Fiction', 'Thrillers', 'Legal']}, {another element} ]

        '''
        print("How do you want to sort?")
        print("    T)itle")
        print("    R)ate")
        print("    P)ublisher")
        print("    A)uthor")
        print("    Q)uit")
        
        user_input_sort = input("Enter how you want to sort: ").upper()
        
        if user_input_sort == 'T':
        
                sort_title = sort_books_title(data)
                return sort_title
            
        elif user_input_sort == 'R':
                sort_rate = sort_books_ascending_rate(data)
                return sort_rate
    
        elif user_input_sort == 'P':
                sort_publisher = sort_books_publisher(data)
                return sort_publisher
    
        elif user_input_sort == 'A':
                sort_author = sort_books_author(data)
                return sort_author 
        elif user_input_sort == 'Q':
                return ""
        else:
                return print("No such command")

#Main Script
data_loaded = False
VALID_COMMANDS = ["L","A","R","G","GCT","S","Q"]
user_input = ""
QUTTING_STATEMENT = "Q was entered, terminating the program"

while user_input != "Q":
        display()
        user_input = input("Please type your command: ").upper()
        if user_input in VALID_COMMANDS:    
                if user_input == "L":
                        data_loaded = True
                        dataset = load_data() 
                        print(dataset)
                if data_loaded == True:
                        if user_input == "GCT":
                                categories = get_all_categories(dataset) 
                                print(categories)  
                        elif user_input == "S":
                                sorting_UI = sort_data(dataset) 
                                print(sorting_UI)
                        elif user_input == "G":
                                get_books_output = get_books(dataset)
                                print(get_books_output)
                        elif user_input == "A":
                                add_book = add_remove_book(dataset,user_input)
                        elif user_input == "R":
                                remove_book = add_remove_book(dataset,user_input)              
                elif data_loaded == False and user_input != "Q":
                        print("File not loaded")
        else:
                print("No such command")         
                
print(QUTTING_STATEMENT)