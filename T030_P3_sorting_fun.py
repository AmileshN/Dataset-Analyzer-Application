#Group: T030  Members: Amilesh Nanthakumaran, George Reda Gad, Ayo Owolabi & Eliana Schartner 
#Version: 1.0
#Date: April 12, 2022

#imports 
import string 
from T030_P5_load_data import *
from T030_check_equal import check_equal

#Functions from P3 - Task 1
def dict_to_list(dictionary:dict) -> list: #George Reda Gad
    """
    Returns the dictionary as a list.
    Precondition: This code works for the 'test_dataset_P2.csv' file and 'google_books_dataset.csv' but not both at the same time. 

    >>>dict_to_list(book_category_dictionary('test_dataset_P2.csv'))
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': ['Fiction']}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': ['Fiction']}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': ['Fiction']}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': ['Fiction']}, {'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': ['Fiction']}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'category': ['Fiction']}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': 'English', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'category': ['Fiction']}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': ['Comics']}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': ['Economics']}]
    """    
    result = []
    for category in dictionary.keys():
        books = dictionary.get(category)
        for i in range(len(books)):
            books[i]['category'] = [category]
        if len(result) == 0:
            result = books
        else: 
            for book in books:
                book_in_list = False 
                for i in range(len(result)):
                    if book['title'] == result[i]['title']:
                        result[i]['category'] += book['category']
                        book_in_list = True 
                if book_in_list == False:
                    result += [book]
    return result

def sort_books_title(stored_data: dict)-> list: #Amilesh Nanthakumaran
    ''' Returns a list with the book data sorted alphabetically by title
    Precondition: This code works for the 'test_dataset_P2.csv' file and 'google_books_dataset.csv' but not both at the same time. 
    
    >>>sort_books_title(book_category_dictionary("test_dataset_P2.csv"))
    [{'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': ['Fiction']}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': ['Fiction']}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': ['Comics']}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': ['Fiction']}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': ['Economics']}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'category': ['Fiction']}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': ['Fiction']}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': 'English', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'category': ['Fiction']}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': ['Fiction']}]


    
    '''
    book_list = []
    for cat in stored_data:
        for book in stored_data[cat]:
            book["category"] = cat
            
    book_list = dict_to_list(stored_data)
    n = len(book_list)    
      
    
    for i in range(n):
        for j in range(0, n-i-1):
            if book_list[j]['title'] > book_list[j+1]['title']:
                book_list[j], book_list[j+1] = book_list[j+1], book_list[j]
                
    
    return book_list
def sort_books_publisher(dictionary: dict) -> list: #Eliana Schartner
    """
    Returns a bubble sorted list of the books in alphabetical order based on the publisher. Books from the same publisher are also alphebetically sorted by title.
    Precondition: This code works for the 'test_dataset_P2.csv' file and 'google_books_dataset.csv' but not both at the same time. 
    Precondition: Uses modified library 'test_dataset_P2.csv' for simplicity
    
    >>> sort_books_publisher(book_category_dictionary('test_dataset_P2.csv')))
    [{'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': ['Fiction']}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': 'English', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'category': ['Fiction']}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'category': ['Fiction']}, {'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': ['Fiction']}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': ['Fiction']}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': ['Fiction']}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': ['Comics']}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': ['Economics']}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': ['Fiction']}]
    
    """  
    book_list = dict_to_list(dictionary)            
    dictionary_length = len(book_list) 
    
    for category in range(dictionary_length):
        for book in range(0, dictionary_length-category-1):
            if book_list[book]['publisher'] > book_list[book+1]['publisher']:
                book_list[book], book_list[book+1] = book_list[book+1], book_list[book]
            elif book_list[book]['publisher'] == book_list[book+1]['publisher'] and book_list[book]['title'] > book_list[book+1]['title']:
                            book_list[book], book_list[book+1] = book_list[book+1], book_list[book]            
                
    return book_list
  
def sort_books_author(dictionary) -> list: #George Reda Gad
    """
    Returns a bubble sorted algorithm of the books based on their author, in alphabetical order.
    Precondition: This code works for the 'test_dataset_P2.csv' file and 'google_books_dataset.csv' but not both at the same time. 
    
    >>> sort_books_author(book_category_dictionary('test_dataset_P2.csv'))
    {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery",
    "author": " Barbara Allan",
    "language ": "English",
    "rating": 3.3,
    "publisher": " Kensington Publishing Corp.",
    "category": ["Fiction", "Comedy"]
    "pages": 288}
    """    
    result = dict_to_list(dictionary)
    n = len(result)

    for i in range(n):
        for j in range(0, n-i-1):
            if result[j]['author'] > result[j+1]['author']:
                result[j], result[j+1] = result[j+1], result[j]
            elif result[j]['author'] == result[j+1]['author'] and result[j]['title'] > result[j+1]['title']:
                result[j], result[j+1] = result[j+1], result[j]
                
    return result
def sort_books_ascending_rate(dic: dict) -> list: # Ayo Owolabi
    """
    The function creates a list with the book data by using bubble sorting algorithm to sort the books by the rate in ascending order. It returns a list with the book data stored by their rate in ascending order. 
    Precondition: This code works for the 'test_dataset_P2.csv' file and 'google_books_dataset.csv' but not both at the same time. 
    
    >>> sort_books_ascending_rate(book_category_dictionary('test_dataset_P2.csv'))
    {"title": "The Guardians: The explosive new thriller from International bestseller John Grisham", 
    "author": "John Grisham", 
    "language": "English", 
    "rating": N/A, 
    "publisher": "Hachette UK", 
    "category": ["Fiction","Thrillers", "Legal"]
    "pages": 384}
    ...
    
    """ 
    bk_lst = dict_to_list(dic)
    num = len(bk_lst)
    for cat in dic.keys():
        book_list_cat = dic.get(cat)
        for book in book_list_cat:
            if book['rating'] == 'N/A':
            
                book['rating'] = 0   
    for i in range(num): 
        for z in range(0, num-i-1):
            rating_order = bk_lst[z]['rating']
            rate = bk_lst[z+1]['rating']
             
            if ((rate == 'N/A') or (rating_order > rate)):
                bk_lst[z], bk_lst[z+1] = bk_lst[z+1], bk_lst[z]
    for cat in dic.keys():
        book_list_cat = dic.get(cat)
        for book in book_list_cat:
            if book['rating'] == 0:
            
                book['rating'] = 'N/A'                 
    return bk_lst

#Main Script with automated testing
if __name__ == '__main__':    
    total_test = 0
    total_pass = 0
    DATASET = book_category_dictionary("google_books_dataset.csv")
    SMALLER_DATASET = book_category_dictionary("test_dataset_P2.csv") #used for simplicity 
    
    #Testing for the function sort_books_title
    actual_result = sort_books_title(SMALLER_DATASET)
    total_pass += check_equal("sort_books_title(SMALLER_DATASET)",[{'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': ['Fiction']}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': ['Fiction']}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': ['Comics']}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': ['Fiction']}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': ['Economics']}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'category': ['Fiction']}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': ['Fiction']}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': 'English', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'category': ['Fiction']}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': ['Fiction']}],actual_result)
    total_test += 1
    
    #Testing for the function sort_books_author
    actual_result = sort_books_author(SMALLER_DATASET)
    total_pass += check_equal("sort_books_author(SMALLER_DATASET)",[{'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': ['Fiction']}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': ['Fiction']}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': ['Fiction']}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': ['Fiction']}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'category': ['Fiction']}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': ['Comics', 'Comics']}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': ['Economics', 'Economics']}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': 'English', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'category': ['Fiction']}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': ['Fiction']}],actual_result)
    total_test += 1
    
    actual_result = len(sort_books_author(DATASET))
    total_pass += check_equal("sort_books_author(DATASET)",88,actual_result)
    total_test += 1
    
    #Testing for the function sort_books_publisher
    actual_result = sort_books_publisher(SMALLER_DATASET)
    total_pass += check_equal("Testing sort_books_publisher for the small dataset created:",[{'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': ['Fiction']}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': 'English', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'category': ['Fiction']}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'category': ['Fiction']}, {'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': ['Fiction']}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': ['Fiction']}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': ['Fiction']}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': ['Comics', 'Comics']}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': ['Economics', 'Economics']}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': ['Fiction']}]
    ,actual_result)
    total_test += 1
    
    #Testing for the function sort_books_ascending_rate
    actual_result = sort_books_ascending_rate(SMALLER_DATASET)
    total_pass += check_equal("sort_books_ascending_rate(SMALLER_DATASET)",[{'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': 'English', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'category': ['Fiction']}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': ['Fiction']}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'category': ['Fiction']}, {'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': ['Fiction']}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': ['Comics', 'Comics']}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': ['Economics', 'Economics']}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': ['Fiction']}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': ['Fiction']}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': ['Fiction']}],actual_result)
    total_test += 1
    
    print("Total tests:",total_test)
    print("Total passes:", total_pass)
    print("Total fails:",total_test - total_pass)