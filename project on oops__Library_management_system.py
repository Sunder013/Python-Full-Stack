class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    def issue(self):
        self.available = False
    def return_book(self):
        self.available = True
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.active = True
    def get_member_id(self):
        return self.__member_id
    def membership_details(self):
        status = "Active" if self.active else "Inactive"
        print(f"Name: {self.name}")
        print(f"Member_id: {self.member_id}")
        print(f"Status: {status}")
class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully.")
    def add_member(self, name, member_id):
        for member in self.members:
            if member.get_member_id() == member_id:
                print("Member ID already exists.")
        new_member = Member(name, member_id)
        self.members.append(new_member)
        print(f" members '{name}' added successfully.")
    def show_books(self):
        print("========= BOOK LIST =========")
        if len(self.books) == 0:
            print("No Books available in the Library.")
            return
        count = 1
        for book in self.books:
            if book.available == True:
                status = "Available"
            else:
                status = "Issued"
            print(f" {count}. {book.title} - {book.author} - {status}")
            count = count + 1
    def search_book(self, title):
            for book in self.books:
                if book.title == title:
                    if book.available == True:
                        status = "Available"
                    else:
                        status = "Issued"
                    print("Book Found")
                    print(f"Title: {book.title}")
                    print(f"Author: {book.author}")
                    print(f"Status: {status}")
                    return
            print("Book not found.")
    def issue_book(self, member_id, title):
        found_member = None
        for member in self.members:
            if member.get_member_id() == member_id:
                found_member = member
                break
        if found_member is None:
            print("Invalid Member ID.")
            return
        if found_member.active == "False":
            print("Membership Is not Active.")
            return

        found_book = None
        for book in self.books:
            if book.title == title:
                found_book = book
                break
        if found_book is None:
            print("Book not found.")
            return
        if found_book.available == False:
            print("Book is Already Issued.")
            return
        found_book.issue()
        print("Book Issued Successfully")
    def return_book(self, member_id, title):
        for book in self.books:
            if book.title == title:
                if book.available == True:
                    print("Book is Already returned And It Is Now  Available.")
                else:
                    book.return_book()
                    print("Book Returned successfully.")
                return
        print("Book Not Found.")

    def show_member(self, member_id):
        for member in self.members:
            if member.get_membership_id() == member_id:
                member.membership_details()
                return
        Print("Member not found.")

    def membership_status(self, member_id):
            for member in self.members:
                if member.get_member_id() == member_id:
                    if member.active == True:
                        print("Membership Is Active.")
                    else:
                        print("Membership Is Inactive.")
                    return
            print("Invalid Member Id.")

    def library_statistics(self):
        total_books = len(self.books)
        available_books = 0
        for book in self.books:
            if books.available == True:
                available_books = available_books + 1
        issued_books = total_books - available_books
        total_members = len(self.members)
        active_members = 0
        for member in self.members:
            if member.active == True:
                active_members = active_members + 1
        print("====== LIBRARY STATISTICS ======")
        print(f"Total books: {total_books}")
        print(f"Available Books: {available_books}")
        print(f"Issued books : {issued_books}")
        print(f"Total members: {total_members}")
        print(f"Active_members: {active_members}")

def main():
    library = Library()

    while True:
        print("\n====== LIBRARY MANAGEMENT SYSTEM ======")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. return Book")
        print("6. Add member")
        print("7. member Details")
        print("8. Membership Status")
        print("9. Library Statistics")
        print("10. Exit")

        choice = input("Enter Your Choice:")
        if choice == "1":
            title = input("Enter book Title")
            author = input("Enter book author:")
            library.add_book(title, author)
        elif choice == "2":
            library.show_books()
        elif choice == "3":
            library.search_book(title)
        elif choice == "4":
            member_id = int(input("enter member ID:"))
            title = input("enter book title: ")
            library.issue_book(member_id, title)
        elif choice == "5":
            member_id = int(input("enter member ID: "))
            title = input("enter book title: ")
            library.return_book(member_id, title)
        elif choice == "6":
            name = input("enter member name")
            member_id = int(input("enter member ID: "))
            library.add_member(name, member_id)
        elif choice == "7":
            member_id = int(input("enter member ID: "))
            library.show_member_details(member_id)
        elif choice == "8":
            member_id = int(input("enter member ID: "))
            library.membership_status(member_id)
        elif choice == "9":
            library.library_statistics()
        elif choice == "10":
            print("thank you for using Library management system.")
            break
        else:
            print("Invalid choice. Please try again.")
main()
                
                
            
        
        
        
        
                    
        
            
                    
        
