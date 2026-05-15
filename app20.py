# Kutubxona boshqaruv tizimi
# Python OOP loyiha

from datetime import datetime


class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.is_borrowed = False

    def get_info(self):
        holat = "Band" if self.is_borrowed else "Bo'sh"
        return f"{self.title} | {self.author} | {self.year} | {self.pages} bet | {holat}"

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        self.is_borrowed = False


class User:
    def __init__(self, fullname, user_id):
        self.fullname = fullname
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.fullname} kitob oldi: {book.title}")
        else:
            print("Kitob hozir band!")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
            print(f"{self.fullname} kitobni qaytardi: {book.title}")
        else:
            print("Siz bu kitobni olmagansiz!")

    def show_books(self):
        print(f"\n{self.fullname} olgan kitoblar:")
        if not self.borrowed_books:
            print("Kitob yo'q")
        for book in self.borrowed_books:
            print("-", book.title)


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Kutubxonaga qo'shildi: {book.title}")

    def add_user(self, user):
        self.users.append(user)
        print(f"Foydalanuvchi qo'shildi: {user.fullname}")

    def show_books(self):
        print(f"\n=== {self.name} Kitoblari ===")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book.get_info()}")

    def search_book(self, title):
        print(f"\nQidiruv natijasi: {title}")
        found = False
        for book in self.books:
            if title.lower() in book.title.lower():
                print(book.get_info())
                found = True
        if not found:
            print("Kitob topilmadi!")

    def statistics(self):
        jami = len(self.books)
        band = 0

        for book in self.books:
            if book.is_borrowed:
                band += 1

        bosh = jami - band

        print("\n=== Statistika ===")
        print("Jami kitob:", jami)
        print("Band kitob:", band)
        print("Bo'sh kitob:", bosh)
        print("Foydalanuvchilar:", len(self.users))


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if self.username == username and self.password == password:
            print("Admin tizimga kirdi!")
            return True
        else:
            print("Login yoki parol noto'g'ri!")
            return False


class History:
    def __init__(self):
        self.logs = []

    def add_log(self, text):
        time = datetime.now().strftime("%H:%M:%S")
        self.logs.append(f"[{time}] {text}")

    def show_logs(self):
        print("\n=== Tarix ===")
        for log in self.logs:
            print(log)


# Kutubxona yaratish
library = Library("Central Library")

# Tarix yaratish
history = History()

# Kitoblar
book1 = Book("Python Asoslari", "Ali Valiyev", 2021, 320)
book2 = Book("Suniy Intellekt", "John Smith", 2023, 450)
book3 = Book("Django Framework", "Bekzod Karimov", 2020, 280)
book4 = Book("Data Science", "Akmal Aliyev", 2022, 500)
book5 = Book("Machine Learning", "Andrew Ng", 2019, 600)

# Kutubxonaga qo'shish
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)

# Userlar
user1 = User("Xursandbek", 1)
user2 = User("Javohir", 2)

# User qo'shish
library.add_user(user1)
library.add_user(user2)

# Admin
admin = Admin("admin", "1234")

# Login
admin.login("admin", "1234")

# Kitoblarni ko'rsatish
library.show_books()

# Kitob qidirish
library.search_book("Python")

# Kitob olish
user1.borrow_book(book1)
history.add_log("Xursandbek Python Asoslari kitobini oldi")

user2.borrow_book(book2)
history.add_log("Javohir Suniy Intellekt kitobini oldi")

# User kitoblari
user1.show_books()
user2.show_books()

# Statistikalar
library.statistics()

# Kitob qaytarish
user1.return_book(book1)
history.add_log("Xursandbek Python Asoslari kitobini qaytardi")

# Yangi statistika
library.statistics()

# Tarix
history.show_logs()

# Yangi kitob qo'shish
new_book = Book("Cyber Security", "Bobur Xasanov", 2024, 390)
library.add_book(new_book)

# Yangi foydalanuvchi
new_user = User("Sardor", 3)
library.add_user(new_user)

# Yangi kitob olish
new_user.borrow_book(new_book)
history.add_log("Sardor Cyber Security kitobini oldi")

# Hamma kitoblar
library.show_books()

# Hamma userlar
print("\n=== Userlar ===")
for user in library.users:
    print(user.fullname)

# Eng katta kitobni topish
max_pages = 0
biggest_book = None

for book in library.books:
    if book.pages > max_pages:
        max_pages = book.pages
        biggest_book = book

print("\nEng katta kitob:")
print(biggest_book.get_info())

# O'rtacha sahifa soni
total_pages = 0

for book in library.books:
    total_pages += book.pages

average = total_pages / len(library.books)

print("\nO'rtacha sahifa soni:", average)

# Band kitoblarni chiqarish
print("\n=== Band kitoblar ===")
for book in library.books:
    if book.is_borrowed:
        print(book.title)

# Bo'sh kitoblar
print("\n=== Bo'sh kitoblar ===")
for book in library.books:
    if not book.is_borrowed:
        print(book.title)

# Sana va vaqt
now = datetime.now()

print("\nBugungi sana:", now.strftime("%d-%m-%Y"))
print("Hozirgi vaqt:", now.strftime("%H:%M:%S"))

# User ID qidirish
search_id = 2

print("\nUser qidirish:")
for user in library.users:
    if user.user_id == search_id:
        print("Topildi:", user.fullname)

# Kitoblarni yil bo'yicha saralash
print("\n=== Kitoblar yil bo'yicha ===")

sorted_books = sorted(library.books, key=lambda x: x.year)

for book in sorted_books:
    print(book.get_info())

# Kitoblarni sahifa bo'yicha saralash
print("\n=== Sahifa bo'yicha ===")

sorted_pages = sorted(library.books, key=lambda x: x.pages)

for book in sorted_pages:
    print(book.get_info())

# Dastur tugadi
print("\nDastur muvaffaqiyatli yakunlandi!")