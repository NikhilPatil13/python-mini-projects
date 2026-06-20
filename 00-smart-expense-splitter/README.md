# Smart Expense Splitter

A simple Command Line Interface (CLI) application built using Python to split expenses among multiple people after applying discounts and service charges.

This project was developed as part of my Python learning journey to practice the fundamentals of programming and build a small real-world application.

---

## 📌 Features

- Accepts trip/event name.
- Takes total bill amount as input.
- Accepts the number of people sharing the expense.
- Applies a discount percentage to the bill.
- Adds a service charge percentage.
- Calculates the final payable amount.
- Splits the expense equally among all participants.
- Displays a well-formatted expense summary.

---

## 🛠️ Technologies Used

- Python 3.13
- Command Line Interface (CLI)

---

## 📚 Python Concepts Practiced

This project was built using only the concepts learned so far:

- Variables
- Data Types
- Operators
- Functions
- `return` keyword
- `input()`
- `print()`
- Basic Project Structure
- Modular Programming

---

## 📂 Project Structure

```text
Smart-Expense-Splitter/
│
├── README.md
│
└── src/
    ├── main.py
    │
    └── services/
        ├── expense_split_service.py
        └── __pycache__/
```

---

## 🚀 How to Run the Application

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd Smart-Expense-Splitter
```

### 3. Run the Application

From the project root directory:

```bash
python src/main.py
```

---

## 💻 Sample Execution

```text
===== Smart Expense Splitter =====

Enter trip/event name : Elaichi Resort
Enter total bill amount : 6123
Enter number of people : 4
Enter discount percentage : 7.5
Enter service charge percentage : 2

----- Expense Summary -----

Trip/Event Name      : Elaichi Resort
Original Bill        : ₹ 6123.0
Discount Applied     : 7.5 %
Service Charge       : 2.0 %
Final Bill           : ₹ 5777.05
Each Person Pays     : ₹ 1444.26
```

---

## ⚙️ Calculation Logic

### Final Bill Calculation

```text
Discount Amount
= Original Bill × Discount Percentage ÷ 100

Discounted Bill
= Original Bill − Discount Amount

Service Charge
= Discounted Bill × Service Charge Percentage ÷ 100

Final Bill
= Discounted Bill + Service Charge
```

### Expense Split Calculation

```text
Amount Per Person
= Final Bill ÷ Number of People
```

---

## 🧩 Modules

### `main.py`

Responsible for:

- Taking user input.
- Calling business logic functions.
- Coordinating the application flow.

### `expense_split_service.py`

Responsible for:

- Calculating the final bill.
- Splitting expenses equally.
- Displaying the receipt.

---

## 🎯 Learning Outcome

Through this project, I learned how to:

- Break problems into smaller functions.
- Separate business logic from user interaction.
- Return values from functions.
- Organize Python code into modules.
- Build a complete CLI application using Python fundamentals.

---

## 🔮 Future Enhancements

Possible improvements for future versions:

- Input validation.
- Exception handling.
- Support for uneven expense splitting.
- Saving receipts to files.
- Expense history tracking.
- Graphical User Interface (GUI).
- Web-based version.

---

## 👨‍💻 Author

**Nikhil Patil**

Built as part of a hands-on Python learning journey focused on progressing from Python fundamentals to real-world projects.

---