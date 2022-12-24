#Group: T030  Members: Amilesh Nanthakumaran, George Reda Gad, Ayo Owolabi & Eliana Schartner 
#Version: 1.0
#Date: April 12, 2022

#imports 
import string 
from T030_P5_load_data import *

#The eight functions from P2 - Task 1 
def add_book(dictionary: dict, book_details: tuple) -> dict: #George Reda Gad
    """ Returns an updated dictionary after the book's title, author, language, publisher, category, rating, and pages has been added in a tuple. Function also returns a message stating “The book has been added correctly” or “There was an error adding the book”.
    Precondition: Cant have more or less than 7 added values.
    
    >>> add_book(load_dataset('google_books_dataset.csv'), 'Biography of Kanye West', 'Ye', 'English', 'Graduation Industries', 'Biography', '5.0')
    >>> There was an error adding the book
    >>> {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {another element}]}
    
    >>> add_book(book_category_dictionary('google_books_dataset.csv'), ('Nazeef Halal adventures', 'Jon Gaming', 'Tagalog', 'Agorg Productions', 'Detective', '1.0', '3'))
    >>> The book has been added correctly
    >>> {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {another element}, {'Title': 'Nazeef Halal Adventures', 'Author': 'Jon Gaming', 'Language': 'Tagalog', 'Publisher': 'Agorgg Productions', 'Category': 'Detective', 'Rating': 1.0, 'Pages': 3}]}
    """

    if len(book_details) == 7:
        
        new_book_dictionary = {'Title':book_details[0],
                'Author':book_details[1],
                'Language':book_details[2],
                'Publisher':book_details[3],
                'Category':book_details[4],
                'Rating':float(book_details[5]),
                'Pages':int(book_details[6])}
        
        if not book_details[4] in dictionary.keys():
            dictionary[book_details[4]] = []
            
        dictionary[book_details[4]].append(new_book_dictionary)
        print("The book has been added correctly")
        
    else:
        print("There was an error adding the book")

    return dictionary
def remove_book(dictionary: dict, title: "str", category: "str") -> str: #Eliana Schartner
    """
    Removes a book given its title from a given category. 
    Precondition: category is in the dataset.
    >>>remove_book(book_category_dictionary('google_books_dataset.csv'), "Antiques Roadkill: A Trash 'n' Treasures Mystery", "Fiction")
    The book has been removed correctly. 
    {'Fiction': [{'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5 ... }]}
    
    >>> remove_book(book_category_dictionary('google_books_dataset.csv'), "Gone", "Fiction")
    There was an error removing the book. Book not found.
    """
    if category in dictionary:         
        bookList = dictionary.get(category)
        for book in bookList:
            if book['title'] == title:
                bookList.remove(book)
                print("The book has been removed correctly") 
                break
        else:
            print("There was an error removing the book. Book not found.")         
        
    else:
        print("There was an error removing the book. Book not found.") 
    
    return dictionary 
    
def get_books_by_category(stored_data: dict, category: str) -> int: #Author: Amilesh Nanthakumaran 
    ''' Returns the number of books in that category and prints all the books of that category
    Precondition: This code only works for the 'google_books_dataset.csv' file. 
    
    >>>get_books_by_category(book_category_dictionary("google_books_dataset.csv"),"Biography")
    The category Biography has 7 books. This is the list of books:
    Book 1 : Boy Erased: A Memoir by Garrard Conley
    Book 2 : No One Is Too Small to Make a Difference by Greta Thunberg
    Book 3 : Tall Tales and Wee Stories: The Best of Billy Connolly by Billy Connolly
    Book 4 : Boy Erased: A Memoir by Garrard Conley
    Book 5 : Permanent Record by Edward Snowden
    Book 6 : Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader by Brent Schlender
    Book 7 : Permanent Record by Edward Snowden
    
    >>>get_books_by_category(book_category_dictionary("google_books_dataset.csv"),"Mystery")
    The category Mystery has 18 books. This is the list of books:
    Book 1 : Total Control by David Baldacci
    Book 2 : Watching (The Making of Riley Paige Book 1) by Blake Pierce
    Book 3 : Little Girl Lost: A Lucy Black Thriller by Brian McGilloway
    Book 4 : The Red Signal: An Agatha Christie Short Story by Agatha Christie
    Book 5 : Antiques Con by Barbara Allan
    Book 6 : Homecoming (A Chloe Fine Psychological Suspense Mystery Book 5) by Blake Pierce
    Book 7 : After Anna by Alex Lake
    Book 8 : Antiques Knock-Off by Barbara Allan
    Book 9 : Final Option: 'The best one yet' by Clive Cussler
    Book 10 : Once Missed (A Riley Paige Mystery Book 16) by Blake Pierce
    Book 11 : Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2) by Blake Pierce
    Book 12 : And Then There Were None by Agatha Christie
    Book 13 : A Trace of Crime (a Keri Locke Mystery Book #4) by Blake Pierce
    Book 14 : The Girl in the Spider's Web: A Lisbeth Salander novel: continuing Stieg Larsson's Millennium Series by David Lagercrantz
    Book 15 : The Memoirs of Sherlock Holmes by Arthur Conan Doyle
    Book 16 : Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
    Book 17 : The Black Box by Michael Connelly
    Book 18 : Antiques Chop by Barbara Allan
    
    >>>get_books_by_category(book_category_dictionary("google_books_dataset.csv"),"Space")
    Invalid category
    
    '''
    category = string.capwords(category)
    number_of_books = 0
    book_count = 0
    if category in stored_data.keys():
        valid_category = True
    else:
        valid_category = False
    if valid_category == True:
        
        book_list_category = stored_data.get(category)
        number_of_books = len(book_list_category)
        print("The category",category,"has",number_of_books,"books. This is the list of books:") 
            
        for book in book_list_category: 
            book_count += 1
            title,author = book["title"],book["author"]
            print("Book",book_count,":",title,"by",author) 
    else:
        print("Invalid category")    
  
    return number_of_books

def get_books_by_rate(dictionary: dict, rate: int)-> int: #Ayo Owolabi 
    """
    Returns the number of books whose rate is greater than or equal to the rate given, but also less than the rate higher than the rate given.
    Precondition: The function works if the rate provided is included in the dataset provided.
    
    >>>get_books_by_rate(book_category_dictionary('google_books_dataset.csv'), (3))
    There are 8 books whose rate is between 3 and 4. This is the list of book(s): 
    Book 1: Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
    Book 2: Bring Me Back by B A Paris
    Book 3: How to Understand Business Finance: Edition 2 by Bob Cinnamon  
    Book 4: The Infinite Game by Simon Sinek 
    Book 5: Mrs. Pollifax Unvailed by Dorothy Gilman 
    Book 6: The Secrets of Saving and Investing With Alvin Hall: Simple by Alvin Hall 
    Book 7: Selling 101: What Every Successful Sals Professional Needs to Know by Zig Ziglar 
    Book 8: Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything by Steven D.Levitt
    
    >>>get_books_by_rate(book_category_dictionary('google_books_dataset.csv'), (2))
    There are 0 books whose rate is between 2 and 3. This is the list of book(s): 
     
    >>>get_books_by_rate(book_category_dictionary('google_books_dataset.csv'), (5))
    There are 5 books whose rate is between 5 and 6. This is the list of book(s): 
    Book 1: The Red Signal: An Agatha Christie Short Story by Agatha Christie 
    Book 2: Start Day Trading Now: A Quick and Easy Introduction to making Money While Managing Your Risk by Michael Sincere 
    Book 3: Final Option: 'The best one yet' by Clive Cussler 
    Book 4: Tall Tales and Wee Stories: The Best of Billy Connolly by Billy Connolly
    Book 5: No One Is Too Small to Make a Difference by Greta Thunberg
    """
    bk_list = []
    count = 0
    for bk_cat in dictionary.keys():
        category_of_books = dictionary.get(bk_cat)
        for i in category_of_books:
            rating = i.get('rating')
            if not rating == 'N/A':
                if rate <= int(rating) and int(rating) < rate+1:  
                    if i not in bk_list:
                        bk_list.append(i)
    print('There are', len(bk_list), 'books whose rate is between', rate, 'and' ,rate+1,'. This is the list of books:')
      
    for book in bk_list:
        count += 1
        print('Book', str(count) +':' ,book.get('title'), 'by', book.get('author'))    
      
    return len(bk_list)

def get_books_by_title(stored_data: dict, title: str)-> bool: #Amilesh Nanthakumaran
    ''' Returns True if the title exists in the dictionary and False if non-existent 
    Precondition: This code only works for the 'google_books_dataset.csv' file.
    
    >>>get_books_by_title(book_category_dictionary("google_books_dataset.csv"),"Bring Me Back")
    The book has been found
    
    >>>get_books_by_title(book_category_dictionary("google_books_dataset.csv"),"B")
    The book has NOT been found
    
    >>>get_books_by_title(T030_P1_load_data.book_category_dictionary("google_books_dataset.csv"),"Antiques Roadkill: A Trash 'n' Treasures Mystery")
    The book has been found
    
    '''
    
    is_title = False
    for category in stored_data:
        for book in stored_data[category]:
            if title == book["title"]:
                is_title = True
            else:
                pass
    if is_title == False:
        print("The book has NOT been found")
    else:
        print("The book has been found")
            
    return is_title

def get_books_by_author(dictionary: dict, authors_name: str) -> int: #George Reda Gad
    """ Returns the full name of the author, number of books they have written and the names of the books that they wrote. It also shows the rating.
    Precondition: Author's name must be in the database.
    
    >>> x = get_books_by_author(book_category_dictionary('google_books_dataset.csv'), ('Stephen King'))
    >>> Book # 1 :  A Feast for Crows (A Song of Ice and Fire. Book 4) , rate:  4.5
    >>> Book # 2 :  A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire) , rate:  4.5
    >>> 2
    
    >>> x = get_books_by_author(book_category_dictionary('google_books_dataset.csv'), ('George R'))
    >>> Error, author not found
    >>> 0
    
    
    """
    
    books = []
    num = 0
    list_of_titles = []
    print("The author", authors_name, "has published these/this book(s):")    
    for i in dictionary.keys():
        list1 = dictionary.get(i)
        for x in list1:
            if (authors_name == x['author']):
                titles = x.get('title')
                ratings = x.get('rating')
                if not titles in list_of_titles:
                    num += 1
                    list_of_titles.append(titles)
                    print("Book #", num, ": ", titles, ", rate: ", ratings)
                    
    if list_of_titles == []:
        print("Error, author not found")
    
    return num


   
def get_books_by_publisher(dictionary: dict, pub_name: str) -> str: #Ayo Owolabi
    """
    returns the number of books and the titles of the book written by the given author. 
    Precondition: The publisher must be included in the dataset provided, the google_books_dataset.csv.
    
    >>>get_books_by_publisher(T030_P1_load_data.book_category_dictionary('google_books_dataset.csv'), ('AMACOM'))
    The publisher AMACOM has published the following book(s): 
    Book 1: Marketing (The Brian Tracy Success Library) by Brian Tracy   
    Book 2: Business Strategy (The Brian Tracy Success Library) by Brian Tracy   
    Book 3: Management (The Brian Tracy Success Library) by Brian Tracy
    Book 4: Personal Success (The Brian Tracy Success Library) by Brian Tracy 
    Book 5: The Essentials of Finance and Accounting for Nonfinancial Managers by Edward Fields  
    
    >>>get_books_by_publisher(T030_P1_load_data.book_category_dictionary('google_books_dataset.csv'), ('Red Wheel/Weiser '))
    The publisher Red Wheel/Weiser has published the following books:
    Book 1: Financial Statements. Revised and Expanded Edition: A Step-by-Step Guide to Understanding and Creating Financial Reports by Thomas Ittelson 
    
    >>>get_books_by_publisher(T030_P1_load_data.book_category_dictionary('google_books_dataset.csv'), ('Marvel Entertainment'))
    The publisher Marvel Entertainment has published the following books:
    Book 1: Deadpool Kills the Marvel Universe by Cullen Bunn
    Book 2: Ultimate Spider-Man Vol.11: Carnage by Brian Michael Mendis
    Book 3: Immortal Hulk Vol. 1: Or Is He Both? by Al Ewing 
    Book 4: Spider-Man: Anti-Venom by Dan Slott
    Book 5: Venomized by Cullen Bunn
    
    """
    books = []
    count = 0
    print("The publisher", pub_name, "has published the following book(s):")
    book_lst=[]
    book_set = set()
    
    for i in dictionary.keys():
        pubs = dictionary.get(i)
        for z in pubs:
            if (pub_name == z['publisher']):
                title = z.get('title')
                author = z.get('author')
                book_tup = (title,author)
                book_set.add(book_tup)
                book_lst= list(book_set)
    count = len(book_lst)
    num = 1
    
    for x in range(count):
        print("Book", num , ": ", book_lst[x][0],"by", book_lst[x][1])
        num +=1
    return count
def get_all_categories_for_book_title(dictionary:dict, title: str) -> str:#Eliana Schartner
    """
    Returns a list of categories that a given book is in. Precondition: Book is in the database.
    >>> get_all_categories_for_book_title(book_category_dictionary('google_books_dataset.csv'), 'After Anna')
    The book title After Anna belongs to the following categories:
    Category 1: Fiction
    Category 2: Thrillers
    Category 3: Mystery
    Category 4: Adventure
    4

    >>> get_all_categories_for_book_title(book_category_dictionary('google_books_dataset.csv'), 'Gone')
    The book title Gone belongs to the following categories:
    Error, title not found
    0
    """
    categories = []
    num = 0
    print("The book title", title, "belongs to the following categories:")
   
    for category in dictionary.keys():
        for book in dictionary[category]:
            if (title == book['title']):
                categories += [category]
    
    while num < len(categories):
        category_list = print("Category", str(1 + num) + ":", categories[0 + num])
        num += 1  
    
    if categories == []:
        print("Error, title not found")
    return len(categories)

#The test function 
def check_equal(description: str, outcome, expected) -> None:
    """
    Print a "passed" message if outcome and expected have same type and
    are equal (as determined by the == operator); otherwise, print a 
    "fail" message.
    
    Parameter "description" should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    outcome.
    
    Parameters "outcome" and "expected" are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal. 
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    
    if outcome_type != expected_type:
        
        print("{0} FAILED: expected ({1}) has type {2}, "
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
        return 0

    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
        return 0
    
    else:
        print("{0} PASSED".format(description))
        print("------")
        return 1
    
#Main Script with automated testing
if __name__ == '__main__':
    total_test = 0
    total_pass = 0
    DATASET = book_category_dictionary("google_books_dataset.csv")
    SMALLER_DATASET = book_category_dictionary("test_dataset_P2.csv")
    
    #Testing for the function add_book
    actual_result = add_book(SMALLER_DATASET, ('Biography of Kanye West', 'Ye', 'English', 'Graduation Industries', 'Biography', '5.0'))
    total_pass += check_equal("add_book(SMALLER_DATASET, 'Biography of Kanye West', 'Ye', 'English', 'Graduation Industries', 'Biography', '5.0')",{'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': 'Fiction', 'language': 'English'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': 'Fiction', 'language': 'English'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Fiction', 'language': 'English'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Fiction', 'language': 'English'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'category': 'Fiction', 'language': 'English'}], 'Comics': [{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': 'Comics', 'language': 'English'}], 'Economics': [{'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Economics', 'language': 'English'}]},actual_result)
    total_test += 1
    
    #Testing for the function remove_book
    actual_result = remove_book(SMALLER_DATASET,"Antiques Roadkill: A Trash 'n' Treasures Mystery", "Fiction")
    expected_result = {'Fiction': [{'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': 'Fiction', 'language': 'English'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': 'Fiction', 'language': 'English'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Fiction', 'language': 'English'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Fiction', 'language': 'English'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'category': 'Fiction', 'language': 'English'}], 'Comics': [{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': 'Comics', 'language': 'English'}], 'Economics': [{'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Economics', 'language': 'English'}]}
    
    
    total_pass += check_equal('remove_book(SMALLER_DATASET, "Antiques Roadkill: A Trash n Treasures Mystery", "Fiction")', expected_result, actual_result)
    total_test += 1
    
    
    #Testing for the function get_books_by_category
    actual_result = get_books_by_category(DATASET, 'Biography')
    total_pass += check_equal("get_books_by_category(DATASET, 'Biography')", 7, actual_result)
    total_test += 1
    
    actual_result = get_books_by_category(DATASET, 'Mystery')
    total_pass += check_equal("get_books_by_category(DATASET, 'Mystery')", 18, actual_result)
    total_test += 1
    
    actual_result = get_books_by_category(DATASET, 'Thrillers')
    total_pass += check_equal("get_books_by_category(DATASET, 'Thrillers')", 18, actual_result)
    total_test += 1
    
    
    #Testing for the function get_books_by_rate
    actual_result = get_books_by_rate(DATASET, 3)
    total_pass += check_equal('get_books_by_rate(DATASET, 3)', 19, actual_result)
    total_test += 1
    
    actual_result = get_books_by_rate(DATASET, 2)
    total_pass += check_equal('get_books_by_rate(DATASET, 2)', 0, actual_result)
    total_test += 1
    
    actual_result = get_books_by_rate(DATASET, -1)
    total_pass += check_equal('get_books_by_rate(DATASET, 2)', 0, actual_result)
    total_test += 1
    
    #Testing for the function get_book_by_title
    actual_result = get_books_by_title(DATASET, 'Rework')
    total_pass += check_equal("get_books_by_title(DATASET, 'Rework')", True, actual_result)
    total_test += 1
    
    actual_result = get_books_by_title(DATASET,"B")
    total_pass += check_equal('get_books_by_category(DATASET,"B")',False,actual_result)
    total_test += 1
    
    actual_result = get_books_by_title(DATASET,"Deadpool Kills the Marvel Universe")
    total_pass += check_equal('get_books_by_category(DATASET,"Deadpool Kills the Marvel Universe")',True,actual_result)
    total_test += 1
    
    #Testing for the function get_books_by_author
    actual_result = get_books_by_author(DATASET,"Barbara Allan")
    total_pass += check_equal('get_books_by_author(DATASET,"Barbara Allan")',4,actual_result)
    total_test += 1
    
    actual_result = get_books_by_author(DATASET,"Alex Lake")
    total_pass += check_equal('get_books_by_author(DATASET,"Alex Lake")',1,actual_result)
    total_test += 1
    
    actual_result = get_books_by_author(DATASET,"Jas")
    total_pass += check_equal('get_books_by_author(DATASET,"Jas")',0,actual_result)
    total_test += 1
    
    #Testing for function get_books_by_publisher
    actual_result = get_books_by_publisher(DATASET,"Currency")
    total_pass += check_equal('get_books_by_publisher(DATASET,"Currency")',1,actual_result)
    total_test += 1
    
    actual_result = get_books_by_publisher(DATASET,"DC")
    total_pass += check_equal('get_books_by_publisher(DATASET,"DC")',2,actual_result)
    total_test += 1
    
    actual_result = get_books_by_publisher(DATASET,"D")
    total_pass += check_equal('get_books_by_publisher(DATASET,"D")',0,actual_result)
    total_test += 1
    
    #Testing for the function get_all_categories_for_book_title
    actual_result = get_all_categories_for_book_title(DATASET, 'After Anna')
    total_pass += check_equal("get_all_categories_for_book_title(DATASET, 'After Anna')", 4, actual_result)
    total_test += 1
    
    actual_result = get_all_categories_for_book_title(DATASET, 'Gone')
    total_pass += check_equal("get_all_categories_for_book_title(DATASET, 'Gone')", 0, actual_result)
    total_test += 1
    
    print("Total tests:",total_test)
    print("Total tests passed:",total_pass)
    print("Total tests failed:",(total_test - total_pass))
