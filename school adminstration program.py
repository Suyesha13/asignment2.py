import csv
def write_into_csv(info_list):
    with open('student_info.csv','a',newline='')as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact number", "Email-ID"])
        writer.writerow(info_list)
        
if__name__== ' __ main __':
    condition = True
    student_num = 1
   
    while(condition):
         student_info = input("enter some student information for student# {}in the following format (Name Age Contact_Number E-mail ID): ".format(student_num))
    
    
    #split
    student_info_list = student_info.split(' ')
                       
    print("\nThe entered information is-\nName: {}\nContact_number:{}\nE-mail ID; {}".format(student_info_list[0], student_info_list[1], student_info_list[2], student_infolist[3]))
    choice_check = input("Is the entered information correct? (yes/no): "))
    if choice_check == 'yes':
        write_into_csv(student_info-list)

        condition_check = input("enter (yes\no)if you want to enter information for another student: ")
        if choice_check =="yes":
            condition = true
            student_num = student_num + 1
        elif condition_check == "no":
            condition = false
        elif choice_check == "no":
            print("\nPlease re-enter the values!")
    

    write_into_csv(student_info_list)
    
    condition_check = input("enter (yes/no) if you wnat to enter onformtaion for another student : ")
    if condition_check =='yes':
        condition = True
    elif condition_check =='no':
        condition = False
