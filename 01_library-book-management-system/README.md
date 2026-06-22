# 📚 Library Book Management System

A simple console-based **Library Book Management System** built using Python fundamentals. This project allows users to manage books through an interactive menu-driven interface and demonstrates modular programming practices by separating business logic from user interaction.

---

## 🚀 Features

* ➕ Add a new book
* 📖 View all available books
* 🔍 Search for a book by name
* ❌ Remove the last added book
* 📊 Show total number of books
* 🚪 Exit the application gracefully

---

## 🛠️ Technologies Used

* Python 3.x

---

## 📂 Project Structure

```text
library-book-management-system/
│
├── main.py
│
└── services/
    └── LibraryService.py
```

### main.py

Responsible for:

* Displaying menu options
* Accepting user input
* Calling service methods
* Managing application flow

### services/LibraryService.py

Responsible for:

* Managing the book collection
* Implementing business logic
* Performing operations on books

---

## 📋 Functionalities

### 1. Add Book

Allows users to add a book to the library.

Example:

```text
Enter Book Name : Clean Code
Book is added : Clean Code
```

---

### 2. View All Books

Displays all books available in the library.

Example:

```text
Available Books :
1. Clean Code
2. Python Crash Course
```

---

### 3. Search Book

Searches for a specific book by name.

Example:

```text
Enter Book Name : Clean Code
Book Found : Clean Code
```

If the book does not exist:

```text
No Book Found.
```

---

### 4. Remove Last Added Book

Removes the most recently added book.

Example:

```text
Book Removed : Python Crash Course
```

If no books exist:

```text
No Books To Remove
```

---

### 5. Show Total Books

Displays the total number of books.

Example:

```text
Total Books : 5
```

---

### 6. Exit

Terminates the application.

Example:

```text
Thank you for using Library Book Management System.
```

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone <repository-url>
```

### Navigate to the Project Directory

```bash
cd library-book-management-system
```

### Run the Application

```bash
python main.py
```

---

## 💻 Sample Execution

```text
===== Library Book Management System =====

1. Add Book
2. View All Books
3. Search Book
4. Remove Last Added Book
5. Show Total Books
6. Exit

choice : 1

Enter Book Name : Clean Code
Book is added : Clean Code
```

---

## 🧠 Concepts Practiced

This project helped reinforce the following Python fundamentals:

* Variables and Data Types
* Functions
* Return Statements
* User Input
* Conditional Statements
* Loops
* Match-Case Statements
* Lists
* Modular Programming
* Separation of Concerns

---

## ⚠️ Current Limitations

* Books are stored in memory using a Python list.
* Data is lost when the application terminates.
* Duplicate book entries are allowed.
* Search is case-sensitive.
* No automated tests are included.

---

## 🔮 Future Enhancements

Potential improvements include:

* Prevent duplicate book entries
* Case-insensitive search
* Update book details
* Persistent storage using JSON or CSV
* SQLite database integration
* Unit testing using `unittest` or `pytest`
* Enhanced input validation
* Object-Oriented Programming implementation

---

## 🎯 Learning Outcome

This project demonstrates how to build a small command-line application while applying Python fundamentals and basic software engineering practices. It serves as a strong foundation before progressing to file handling, object-oriented programming, testing, and larger Python applications.

---

## 👨‍💻 Author

**Nikhil Patil**

Built as part of the Python learning journey to strengthen programming fundamentals through hands-on projects.