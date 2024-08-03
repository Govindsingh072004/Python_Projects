def task():
    tasks=[]
    print("-------Welcome To The Task Management App------")

    total_task=int(input("Enter how many task you want to add ="))
    for i in range(1,total_task+1):
        task_name=input(f"enter task {i} = ")
        tasks.append(task_name)
    print(f"today's tasks are\n {tasks}")

    while True:
        try:
            operation=int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop"))
            if operation ==1:
                add=input("Enter tasl you want to add =")
                tasks.append(add)
                print(f"Task {add} has been successfully Added.... ")
            elif operation ==2:
                updated_val=input("Enter the task name you want to update = ")
                if updated_val in tasks:
                    up =input("Enter new task =")
                    ind=tasks.index(updated_val)
                    tasks[ind] = up
                    print(f"Updated task {up}") 
                else:
                    print("Task Not found")


            elif operation == 3:
                del_val =input("Which task you want to delete =")
                if del_val in tasks:
                    ind=tasks.index(del_val)
                    del tasks[ind]
                    print(f"task {del_val} has been deleted....")
                else:
                    print("Task Not Found")    
            elif  operation == 4:
                print(f"Today's tasks are\n {tasks}")
            
            elif operation == 5:
                print("Closing the program")
                break
            else:
                print("Invalid Input.Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid Input.Please enter a valid number.")
task()  


