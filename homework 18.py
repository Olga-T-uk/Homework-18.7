import random
from types import new_class

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}

for student in students:
    students_marks[student] = {}

    for class_ in classes:
        marks = [random.randint(1,5) for i in range(3)]
        students_marks[student][class_] = marks
for student in students:
            print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Добавить ученика
        5. Удалить ученика
        6. Добавить предмет
        7. Удалить предмет
        8. Удалить оценку
        9. Вывести средний балл у ученика по определённому предмету
        10. Вывести учеников с двойками
        11 . Выход из программы
        
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student] [class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
                print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Добавить ученика')
        new_student = input ('Введите имя: ')
        students.append(new_student)
        print('Новый ученик добавлен')
        print(f':{students}')

        for new_student in students:
            students_marks[new_student] = {
                     'Математика':[3,3,5],
                     'Русский язык':[4,4,4],
                     'Информатика':[5,5,5]
            }
    elif command == 5:
        end_student = input('Введите ученика, которого хотите удалить: ')
        if end_student in students_marks.keys():
            del students_marks[end_student]
            print(students_marks)
        else:
            print('Этого ученика в списке нет')

    elif command == 6:
        new_class = input('Введите новый предмет: ')
        classes.append(new_class)
        print('Новый предмет добавлен')
        print(classes)

    elif command == 7:
        end_class = input('Введите предмет,который нужно удалить: ')
        if end_class in classes:
            classes.remove(end_class)
            print(classes)
        else:
            print('Такого предмета в списке нет')

    elif command == 8:
        end_mark = input('Введите оценку, которую нужно удалить:')
        student = input('Введите имя: ')
        if student in students:
            class_ = input('Введите предмет: ')
            if class_ in classes:
                if end_mark in students_marks[student][class_]:
                    print(f'Оценка {end_mark} удалена у {student}  по предмету {class_}')
                else:
                    print('Такой оценки нет')
            else:
                print('Такого предмета нет')
        else:
            print('Такого ученика нет')

    elif command == 9:
        print('Вывести средний балл у ученика по предмету: ')
        student = input('Введите имя: ')
        if student in students:
            class_ = input('Введите предмет: ')
            if class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                averege = marks_sum // marks_count
                print(f'Средний балл по предмету {class_} ученика {student} : {averege}')
            else:
                print('Такого предмета нет в списке')
        else:
            print('Такого ученика нет в списке')

    elif command == 10:
        print('Вывести учеников с двойками')
        students_with_failing_marks = []
        for student in students:
            if student in students_marks:
                for class_ in classes:
                    if class_ in students_marks[student]:
                        if 2 in students_marks[student][class_]:
                            students_with_failing_marks.append(student)
                            break

        if students_with_failing_marks:
            print("Ученики с двойками:")
            for student in students_with_failing_marks:
                print(student)
        else:
            print("Нет учеников с двойками.")



    elif command == 11:
        print('11. Выход из программы')
        break




