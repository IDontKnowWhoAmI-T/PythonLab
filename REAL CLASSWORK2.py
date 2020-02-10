students = {
    '1':{
        'name':'Арсений',
        'surname':'Гоблин',
        'class': '1A',
        'rating':'2.5'
    },

    '2':{
        'name':'Карыч',
        'surname':'Годов',
        'class': '1A',
        'rating':'5'
    },

    '3':{
        'name':'Балбес',
        'surname':'Иванов',
        'class': '2Б',
        'rating':'4'
    },

    '4':{
        'name':'Алекс',
        'surname':'Шварц',
        'class': '1A',
        'rating':'5'
    },
    '5':{
        'name':'Арсений',
        'surname':'Акимов',
        'class': '1A',
        'rating':'4.7'
    }
    
}

print("База данных учеников школы №320")
while True:
    comand = input("user# ")
    if comand == "-h" or comand == "help":
        print("""
            Команды
         ************
         -s   show   вывод базы данных


         -r   replace   замена данных о пользователе
         ************
        """)
    elif comand == "-s" or comand == "show":
        print("Выберите номер студента")
        print(students.keys())
        n = input("user# №")
        print(students[n])
    elif comand == "-r" or "replace":
        print("Выберите номер студента")
        print(students.keys())
        n = input("user# №")
        print(students[n])
        print("Выберите для изменений")
        print(students[n].keys())
        l = input("user#")
        print(students[n][l])
        x = input("replace: ")
        students[n][l] = x
    elif comand == "-a" or comand == "add":
        print("информация нового пользователя: ")
        n = "Введите номер: "
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        clas = input("Введите класс: ")
        students.setdefault(n)
        students[n].setdefault('name')
        students[n]['name'] = name
        students[n].setdefault('surname')
        students[n]['surname'] = surname
        students[n].setdefault('class')
        students[n]['class'] = clas
        students[n].setdefault('rating')
        students[n]['rating'] = "недавно добавленный"
    elif comand == "exit":
        break
    else:
        print("команда не найденна, введите help or -h")
        
