class Library():
    def __init__(self,books,name):
        self.list_of_books=books
        self.library_name=name
        self.d={}
    def display_books(self):
        return(f'Books available in {self.library_name} are {self.list_of_books}')

    def lend(self,name,book_name,):
        if book_name in self.list_of_books:
            self.list_of_books.remove(book_name)
            self.d[book_name]=name
            return(f'take this {book_name} book, it is lended to you {name}')
        else:
            if book_name in self.d:
                return(f'The {book_name} book was own by {self.d[book_name]}')
            return(f'The {book_name} book is  not available in the library')

    def donate(self,book_name):
        self.list_of_books.append(book_name)
        return(f'Thanq for donating {book_name} book to the library')

    def return_book(self,name,book_name):
        self.list_of_books.append(book_name)
        del self.d[book_name]
        return(f'thanq for returning {book_name} book on time {name}')

if __name__ == '__main__':
    ayush_library=Library(['Math-1','Math-2','Math-3','Math-4','Physics','Social Science','Mechanical Engineering','Python Programming','Digital System Design','Aptitude'],'Ayush Library')
    while True:
        x=int(input('press 1 if you want to display all the books available in the library\npress 2 if you want to lend a book from  the library\npress 3 if you want to donate a book in the library\npress 4 if you want to return a book to the library\n-- '))
        if x==1:
            print(ayush_library.display_books())
        elif x==2:
            name=input('Enter your name : ')
            book_name=input('Enter the book name you want to lend : ')
            print(ayush_library.lend(name,book_name))
        elif x==3:
            book_name=input('Enter the book name you want to donate : ')
            print(ayush_library.donate(book_name))
        elif x==4:
            name = input('Enter your name : ')
            book_name = input('Enter the book name you want to return : ')
            print(ayush_library.return_book(name,book_name))
        else:
            print('please enter a valid input')

        c=input('print y if you want to access library and n if you want to exit : ')
        if c=='y':
            continue
        else:
            break