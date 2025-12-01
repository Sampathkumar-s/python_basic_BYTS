print(''' ----- Student Recoard Management System -----
      1. add student
      2. view student
      3. search student
      4. delete student ''')
choice=int(input("Enter your choice"))

if choice == 1:
      add_student()
elif choice == 2:
      view_student()   
elif choice == 3:
      search_student() 
elif choice == 4:
      delete_student()  
else:
      print("Entered the Wrong choice ")
      
      