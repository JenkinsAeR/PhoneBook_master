from tkinter import *
from tkinter.filedialog import *
from phonebook_serv import * #Импортирование модуля с классом PhoneBook

root = Tk()
root.title("Телефонный справочник v 1.0")
root.iconbitmap('\\images\\rust.ico')
root.geometry('500x400+500+400') #(геометрия окна)ширина=500, высота=400, x=500, y=400

#Title Label - заголовок
txt = Label(root, text="Телефонный справочник", font='Tahoma')
txt.pack()

#Поле ввода номера телефона и лэйбл
ent_phone = Entry(root, width=20, bg='#7FFF00')
ent_phone.pack(pady=5,)
ent_phone.place(x=350, y=65)
txt_phone = Label(root, text="Телефон: ", font='Verdana 10')
txt_phone.pack()
txt_phone.place(x=350, y=40)

#Поле ввода фамилии и лэйбл
ent_last = Entry(root, width=20, bg='#7FFF00')
ent_last.pack(pady=5,)
ent_last.place(x=350, y=115)
txt_last = Label(root, text="Фамилия: ", font='Verdana 10')
txt_last.pack()
txt_last.place(x=350, y=90)

#Поле ввода имени и лэйбл
ent_first = Entry(root, width=20, bg='#7FFF00')
ent_first.pack(pady=5, side='right')
ent_first.place(x=350, y=165)
txt_first = Label(root, text="Имя: ", font='Verdana 10')
txt_first.pack()
txt_first.place(x=350, y=140)

#Поле ввода отчества и лэйбл
ent_second = Entry(root, width=20, bg='#7FFF00')
ent_second.pack(pady=5, side='right')
ent_second.bind('<Return>', )
ent_second.place(x=350, y=215)
txt_second = Label(root, text="Отчество: ", font='Verdana 10')
txt_second.pack()
txt_second.place(x=350, y=190)

#Создаём экран для вывода полученной информации
text = Text(root, width=30, height=50)
text.pack(side='left') #Прикрепляем к левому краю
text.config(state=DISABLED) #Запрещаем редактирование текстового поля

def adder():
    '''Функция для добавления новых пользователей. Не принимает аргументов,
        добавляется лишь информация, которая была введена в поля: Телефон,
        Фамилия, Имя и Отчество. Принимаются символы любых типов.
    '''
    text.config(state=NORMAL) #Делаем поле доступным для редактирования
    #Полученные значения из Ентри полей записываем в переменные
    lastname1 = ent_last.get()
    firstname1 = ent_first.get()
    secondname1 = ent_second.get()
    number1 = ent_phone.get()
    #Вносим данные из полей в словарь для удобства
    adder_dict = {lastname1:'\nФамилия: ', firstname1:'Имя: ', secondname1:'Отчество: ', number1:'Телефон: '}
    add_phone = PhoneBook('NULL', lastname1, firstname1, secondname1, number1) #Создаём экземпляр класса
    add_phone.add_number() #Вызываем метод класса PhoneBook
    for key, value in adder_dict.items(): #Проходим по элементам словаря(Ключ, значение)
        #Печатаем в текстовое поле информацию о добавленной записи
        text.insert(END, value)
        text.insert(END, key)
        text.insert(END, u"\n")
        #На выходе из цикла печатаем "Запись добавлена!", а так же блокируем текстовое поле, и перемещаемся в его конец
    return text.insert('end', '-' * 20 + u"\nЗапись добавлена!\n"+'-' * 20), text.config(state=DISABLED), text.see(END)

 

def search(event=0):
    '''Функция поиска по справочнику. Ищет все записи, даже с частичным совпадением.
    Но если оставить поле пустым и запустить поиск - покажет все записи.В поле ввода
    так же имеется бинд на запуск
    функции клавишей <Return>.
    '''
    text.config(state=NORMAL)#Делаем поле доступным для редактирования 'экран'
    search_name = ent_search.get() #Получаем из поискового поля данные и записываем в переменную
    x=PhoneBook.find_phone(search_name) #Вызываем напрямую метод find_phone класса PhoneBook
    
    for key in x:
        #Проходим по последовательности и выводим отформатированную информацию
        s = '\nID:{}\nФамилия:{}\nИмя:{}\nОтчество:{}\nТелефон:{}\n{}'.format(key[0], key[1], key[2], key[3], key[4], '-' * 20)
        text.insert(END, s)
    if search_name == '':
        text.insert('end', u'\nПоле было пустым\nВыведен весь справочник.')
    #Не забиваем заблокировать 'экран' от редактирования и остановиться на последней показанной записи
    return text.insert('end', u"\nПоиск закончен!\n"+'-' * 20),text.config(state=DISABLED), text.see(END)


def child_root():
    '''Функция создания дочернего окна для удаления пользователей.
    '''
    def check(event=0):
        '''Функция удаления пользователя принимает только ID введенное в
        Ентри поле 'ent_del'.В поле ввода так же имеется бинд на запуск
        функции клавишей <Return>.
        '''
        id = ent_del.get() #Получаем ID пользователя, которого требуется удалить
        del_num = PhoneBook(id) #Создаём экземпляр класса PhoneBook
        #и передаём в качестве первого параметра id
        text.config(state=NORMAL) #Делаем поле доступным для редактирования
        if id == '': # Если поле пустое 
            text.insert('end', u'\nВведите верный ID\n')#Возвращаем на 'экран' сообщение
                                                        #с просьбой ввести верный ID
        else:
            del_num.del_phone() #Удаляем пользователя PhoneBook.del_phone()
            text.insert('end', u"\nПользователь c ID %s удалён!\n" % (id)) #Выводим на выходе id удалённого пользователя
        #Не забиваем заблокировать 'экран' от редактирования и остановиться на последней показанной записи
        return text.config(state=DISABLED), text.see(END)

    child = Toplevel(root) #Создать дочернее окно
    child.title('Удаление пользователей') #Огравление окна
    child.geometry('300x100+400+300')

    txt_del = Label(child, text="Введите ID пользователя: ", ).pack()
    #Поле ввода ID дочернего окна
    ent_del = Entry(child, width=20, bg='#e9f2c4')
    ent_del.bind('<Return>',check)
    ent_del.pack()
    #Кнопка удалить дочернего окна, при нажатии вызывает функцию check
    butt_delete = Button(child, width=14, text="Удалить",font='Verdana 10',command=check)
    butt_delete.pack()


#Кнопка добавления нового пользователя
butt_add = Button(root, width=14, text="Добавить",font='Verdana 10',command=adder)
butt_add.pack(pady=10)
butt_add.place(x=350, y=240)
#Кнопка удаления
butt_del = Button(root, width=14, text="Удалить",font='Verdana 10',command=child_root)
butt_del.pack(pady=10)
butt_del.place(x=350, y=265)
#Поле ввода поиска
ent_search = Entry(root, width=20, bg='#00ffd0')
ent_search.pack(pady=5, side='right')
ent_search.bind('<Return>',search)
ent_search.place(x=350, y=330)

txt_search = Label(root, text="="*15, ) #Для красоты
txt_search.pack()
txt_search.place(x=350, y=290)
#Кнопка поиска
butt_search = Button(root, width=14, text="Поиск",font='Verdana 10',command=search)
butt_search.pack(pady=10)
butt_search.place(x=350, y=350)

root.mainloop()
