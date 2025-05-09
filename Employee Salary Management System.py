import pickle
import turtle
employee_data = {}
listl=[]
def employee_details():
    employee_id=int(input("Enter Employee ID:"))
    employee_name=input("Enter Employee Name:")
    employee_age=int(input("Enter Employee Age:"))
    employee_gender=input("Enter Employee Gender:")
    employee_salary=float(input("Enter Employee Basic Salary(Per Year):"))
    employee_data[employee_id] ={'Name':employee_name, "Age" :employee_age,"Gender" :employee_gender,"Basic Salary" :employee_salary} 
    print("\n--Added Succesfully!!--")
    employee=employee_data[employee_id]
    

def employee_salary_details():
    employee_id=int(input("Enter 8 Digit Employee ID: ")) 
    employee=employee_data[employee_id]
    if employee_id in employee_data:
        da = 38/100 * employee["Basic Salary"] 
        hra = 16/100 * employee["Basic Salary"] 
        ta = 3600
        pf = 10/100 * (employee["Basic Salary"] + da)
        it = 10/100 * (employee["Basic Salary"] + da + hra + ta) 
        netsalary = (employee["Basic Salary"] + da + hra + ta - pf - it)
        print ("Salary Details Of Employee" , employee ["Name"] )
        print ("Basic Salary Of Employee employee", ["Basic Salary"])
        print("DA" , da)
        print("HRA",hra)
        print ("TA",ta)
        print(" PF",pf)
        print("IT",it)
        print ("NET SALARY", netsalary)
        

        filel=open("C:\\Users\\krunal\\Downloads\\file.txt","wb") 
        pickle.dump(employee_data,filel)
        filel.close()
    else:
        print ("\n--Employee Data Not Found!!--")
def top_three():
    

    # Step 1: Get the nested dictionary values
    values = [nested_dict['Basic Salary'] for nested_dict in employee_data.values()]

    # Step 2: Convert values to a list
    values_list = list(values)

    # Step 3: Sort the list in descending order
    values_list.sort(reverse=True)

    # Step 4: Get the three highest values
    highest_values = values_list[:3]

    # Step 5: Find the keys corresponding to the highest values
    highest_keys = [key for key, nested_dict in employee_data.items() if nested_dict['Basic Salary'] in highest_values]

    print("Top 3 High Tax Paying Employees")
    for key, value in zip(highest_keys, highest_values):
        
        print(f"{key}: {value}")
     
while True:
    print("\nMenu:")
    print("1. Add Employee")
    print("2. Display Salary Details of an Employee")
    print("3. Display Top 3 High Tax Paying Employees") 
    print("4.  Exit")

    choice = int(input("Enter your choice (1-4): ")) 
    if choice == 1:
        employee_details()  
    elif choice == 2:
        employee_salary_details() 
    elif choice == 3:
        top_three()
        
    elif choice == 4:
        break 
    else:
        print("\n--Invalid choice. Please try again--")
