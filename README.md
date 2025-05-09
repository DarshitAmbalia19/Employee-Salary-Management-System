# 🧾 Employee Salary Management System

A Python-based console application that allows users to add employee details, compute salary breakdowns (DA, HRA, TA, PF, IT, Net Salary), and identify the top 3 high tax-paying employees. The data is stored using Python's `pickle` module.

## 🚀 Features
* Add new employee details (ID, name, age, gender, salary)
* Compute and display salary breakdown:
  * DA (38%)
  * HRA (16%)
  * TA (₹3600 fixed)
  * PF (10%)
  * IT (10%)
  * Net Salary calculation
* Show the top 3 employees based on salary (indicating high tax payers)
* Stores employee data using `pickle`
* Saves data to a local `.txt` file

## 📂 Project Structure
employee_salary_system.py
README.md
file.txt # auto-generated when saving data using pickle

## 🛠️ How to Run
1. Clone the repository:
   git clone https://github.com/DarshitAmbalia19/employee-salary-system.git
   cd employee-salary-system

2. Run the Python script:
   python employee_salary_system.py

Note: Make sure the file path used for saving (file.txt) is accessible and modifiable on your system. Adjust the path in the code if needed.

📋 Menu Options
Menu:
1. Add Employee
2. Display Salary Details of an Employee
3. Display Top 3 High Tax Paying Employees
4. Exit

📦 Dependencies
Python standard libraries only (pickle)

⚠️ Notes
- Ensure employee ID is unique and used consistently for salary lookup.
- The system does not currently support saving across sessions unless you reload from the file.txt.
- The turtle import is unused and has been removed.
```
📈 Example Output

Enter Employee ID: 1001
Enter Employee Name: John
Enter Employee Age: 35
Enter Employee Gender: M
Enter Employee Basic Salary(Per Year): 750000

--Added Successfully!!--

Salary Details Of Employee John
DA 285000.0
HRA 120000.0
TA 3600
PF 103500.0
IT 115860.0
NET SALARY 933240.0
```
🤝 Contributing
Pull requests are welcome. If you have any suggestions for improvements or new features, please open an issue.

👤 Author

**Darshit Ambalia**  
[GitHub Profile](https://github.com/DarshitAmbalia19)

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
