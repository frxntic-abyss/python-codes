name = input("Enter student name: ")
present = int(input("Enter number of days attended:"))
if present <= 190:
     print("You have been present for", present, "days.")

     print("you have been absent for", 190-present, "days.")
     attendance = (present / 190)*100
     print("your attendance rate is", attendance, "%")
     if attendance >= 75:
      print("You are eligible for the exam.")
     else:
      print("you are not eligible for the exam.")

else:
     print ("you have provided false information.")