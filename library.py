total_books = 500
borrowed_books = 0
returned_books = 0
add_books = 0
while True:
    print("Login for student library portal")

    user_name = input("enter user name: ")
    password = input("enter the password: ")

    print("welcome to the library portal of University of East London")
    print("total books is: 500")

    student_name = input("enter your name: ")
    srn_no = input("enter your university SRN NO: ")
    course_name = input("enter your course name")
    print("""press 1 to add book
    press 2 to borrow book
    press 3 to return book""")
    choose = int(input("enter your choice"))
    while True:
        if choose == 1:
            adding_books = int(input("how many books do you want to add"))
            add_books += adding_books
            total_books += add_books
            print("add books", add_books)

        elif choose == 2:
            borrow_book = int(input("how many books do you want to borrow"))
            borrowed_books += borrow_book
            total_books -= borrowed_books
            print("borrowed books", borrowed_books)

        elif choose == 3:
            return_book = int(input("how many books do you want to return"))
            returned_books += return_book
            total_books += returned_books
            print("returned books", returned_books)
        repeat = input(" do you want to add/borrow/return more books:(yes/no) ")
        if repeat == "no" or repeat == "No" or repeat == "NO":
            break

    print("_"*50)
    print("Student's name: ", student_name)
    print("student's SRN NO: ", srn_no)
    print("student's course name: ", course_name)
    if choose == 1:
        print("add books: ", add_books)
        print("total books after adding", total_books)
    elif choose == 2:
        print("borrowed books: ", borrowed_books)
        print("total books after borrowing", total_books)
    elif choose == 3:
        print("return books: ", returned_books)
        print("total books after returning", total_books)
    print("_" * 50)
    repeat_student = input("next student please?(yes/no)")
    if repeat_student == "no" or repeat_student == "No" or repeat_student == "NO":
        break












