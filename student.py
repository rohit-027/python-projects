while True:
    print("Login for student library portal")
    user_name = "rohit"
    password = 123456
    user = input("enter the user name: ")
    if user in user_name:
        student_password = int(input("enter the password: "))
        if student_password == password:
            print("login successful")
    else:
        print("incorrect information")

    print("welcome to the library portal of University of East London")
    books_list = {"math": 40, "science": 20, "english": 10, "data_structure": 25, "microprocessor": 35}

    student_name = input("enter your name: ")
    srn_no = input("enter your university SRN NO: ")
    course_name = input("enter your course name")

    print("""
    choose 1 to add
    choose 2 to borrow
    choose 3 to return""")
    choose = int(input("enter your choice"))
    while True:
        if choose == 1:
            print("select the book which you want to add")
            print("math: 40, science: 20, english:  10, data_structure: 25, microprocessor: 35")
            book = input("enter the book name: ")
            number_of_books = int(input("how many books do you want to add"))
            books_list[book] += number_of_books

        elif choose == 2:
            print("select the book which you want to borrow")
            print("math: 40, science: 20, english:  10, data_structure: 25, microprocessor: 35")
            book = input("enter the book which you want to borrow: ")
            number_of_books = int(input("how many books do you want to borrow: "))
            books_list[book] -= number_of_books

        elif choose == 3:
            print("select the book which you want to return")
            print("math: 40, science: 20, english:  10, data_structure: 25, microprocessor: 35")
            book = input("enter the book which you want to return: ")
            number_of_books = int(input("how many books do you want to return: "))
            books_list[book] += number_of_books
        else:
            print("invalid choice")
        break

    print("_"*50)
    print("student name: ", student_name )
    print("SRN No: ", srn_no)
    print("course: ", course_name)
    if choose == 1:
        print("subject: ", book)
        print("number of adding books:  ", number_of_books)
        print("books remain: ", books_list)
    elif choose == 2:
        print("subject: ", book)
        print("number of borrow books: ", number_of_books)
        print("books remain: ", books_list)
    elif choose == 3:
        print("subject: ", book)
        print("number of return books: ", number_of_books)
        print("books remain: ", books_list)
    else:
        print("invalid")

    print("_" * 50)
    repeat = input("next student please?(yes/no)")
    if repeat == "no" or repeat == "No" or repeat == "NO":
        break
    print("_" * 50)


