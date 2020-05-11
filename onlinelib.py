class Library:

    book_name = ""
    lend_info = {}
    name = ""

    def __init__(self, books, libraryname, password):
        self.books = books
        self.libraryname = libraryname
        self.password=password

    def displaybooks(self):
        k=1
        for i in self.books:
            print(f"{k}:" +i)
            k=k+1
        for i in self.lend_info:
            print(f"{k}:" +i)
            k=k+1



    @staticmethod
    def displaydetails():
        f = open("library.txt", "r")
        context = f.read()
        print(context)
        f.close()

    @classmethod
    def Bookentry(cls, book, name, operation):
        cls.book_name = book
        cls.name = name
        cls.operation=operation

    @staticmethod
    def getdate():
        # import datetime
        # now = datetime.datetime.now()
        # return now.strftime
        import time
        return time.asctime(time.localtime(time.time()))

    def fileentry(self):
        f = open("libarary.txt", "a")
        f.write("\n")
        date1 = str(self.getdate())
        f.write(date1)
        f.write("\t")
        f.write(self.book_name + f"         {self.operation}")
        f.write("\t")
        f.write(self.name)
        f.close()

    def lend(self):
        for i in self.books:
            if i == self.book_name :
                print("BOOK AVALIABLE")
                self.lend_info[self.book_name] = self.name
                self.books.remove(self.book_name)
                self.fileentry()

        else:
            for i in self.lend_info:
                if self.book_name == i:
                    print("The book {}  is issued by {} ".format(self.book_name, self.lend_info[i]))

            else:
                print("You entered a wrong book name please enter")



    def Return(self):
        self.books = self.books+[self.book_name]
        self.lend_info.pop(self.book_name, None)
        self.fileentry()

    def Add(self):
        self.name = input("ENTER YOUR NAME")
        self.books = self.books + [self.book_name]
        self.fileentry()


pawan_library = Library(["harry potter", "narendra modi", "ruskin bond"], "the great library","1234")
flag=1
while flag==1:
    print(" Welcome to the Library ")
    status=int(input("1:USER \n2:ADMIN\n"))
    if status==1:
        name=input("Kindly Enter Your Name")

        choice=int(input("1: Lend Book\n2: Return Book\n3: Add Book\n"))
        if choice==1:
           print("==============BOOKS AVAILABLE==============")
           pawan_library.displaybooks()
           print()
           bookname=input()
           pawan_library.Bookentry(bookname,name,"L")
           pawan_library.lend()

        elif choice==2:
            print("==============RETURN==============")
            bookname = input("Enter the book which you want to return")
            pawan_library.Bookentry(bookname, name, "R")
            pawan_library.Return()

        elif choice==3:
            print("==============WE ARE THANKFUL FOR YOUR CONTRIBUTION ==============")
            bookname = input("Enter the book which you want to return")
            pawan_library.Bookentry(bookname, name, "A")
            pawan_library.Return()

    elif status==2:
        password=input("Enter Password")
        if password==pawan_library.password:
            print("===Welcome Admin====")
            demand = int(input("1: current information\n 2: complete info"))

            if demand == 1:

                print(pawan_library.lend_info)

            elif demand == 2:

                f = open("libarary.txt","r")
                context=f.read()
                print(context)
                print(2)
        else:
            print("wrong password try again")






