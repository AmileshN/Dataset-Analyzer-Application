#Group: T030 Writer: Amilesh Nanthakumaran Reviewers: George Reda Gad, Ayo Owolabi & Eliana Schartner 
#Version: 1.0
#Date: April 12, 2022

def book_category_dictionary(filename: str) -> dict: #Amilesh Nanthakumaran
    ''' Returns a dictionary of the stored Google Books dataset based on the category of the book
    Precondition: This code only works for the 'google_books_dataset.csv' file.
    
    >>>book_category_dictionary('google_books_dataset.csv')
    There are 196 books in the dictionary.
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400}, {'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': 'English', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'language': 'English', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368},{another element}]
    
    '''    
    book_list = []
    book_dictionary = {}
    category_list = []
    result_list = []

    infile = open(filename,"r")
    keys_for_book = infile.readline().strip()
    for line in infile:
        line = line.strip("\n")
        line = line.split(",")
        
        if line[2] != "N/A":
            line[2] = float(line[2])
        book_list.append({"title":line[0],"author":line[1],"rating": line[2], "publisher":line[3],"pages": int(line[4]),"category":line[5],"language":line[6]}) 
        for book in book_list:
            category = book.get("category")
            if category not in category_list:
                category_list.append(category)
                book_dictionary[category] = [] #gets the cateogries as keys for the dict
                
    for cat in book_dictionary.keys():
        for book in book_list:
            if book['category'] == cat:
                book_dictionary[cat] += [book]
                if book not in result_list:
                    result_list += [book]
                    
                
                
                
    if __name__ == '__main__':
        print("There are", len(result_list),"books in the dictionary.") 
        for category in book_dictionary:
            print('"'+category+'":')
            for book in book_dictionary[category]:
                print(book,",") 
    
    infile.close()
    return book_dictionary

