#import sys
import os
#from datetime import datetime
import pandas as pd
#import vk_api
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
#здесь была авторизация в ВК, с сохранением зашифрованного пароля через ключи Fernet, пока ВК не стал банить за это
#После этого пришлось перейти а парсинг из html нужных слов
#from cryptography.fernet import Fernet
'''
def kG():
    # Создаем ключ и сохраняем его в файл
    key = Fernet.generate_key()
    with open('crypto.key', 'wb') as key_file:
        key_file.write(key)
def load_key():
# Загружаем ключ 'crypto.key' из текущего каталога
    return open('crypto.key', 'rb').read()

def encrypt(filename, key):
# Зашифруем файл и записываем его
    f = Fernet(key)
    with open(filename, 'rb') as file:
        # прочитать все данные файла
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    # Расшифруем файл и записываем его
    f = Fernet(key)
    with open(filename, 'rb') as file:
        # читать зашифрованные данные
        encrypted_data = file.read()
    # расшифровать данные
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data.decode()
'''
class App(tk.Tk):
    def __init__(self):
        global Base
        global opros
        global Metabase
        global key
        global VK
        super().__init__()
        #global login
        #global password
        #global vk_gr_id
        #login=tk.StringVar()
        #vk_gr_id=tk.StringVar()
        #password=tk.StringVar()
        '''
        if os.path.isfile('crypto.key') and os.path.isfile('pswd.txt'):
            key= load_key()
            login.set((decrypt('pswd.txt',key)).split('\t')[0])
            password.set((decrypt('pswd.txt',key)).split('\t')[1])
        else:
            kG()
            key=load_key()
        '''
        btn_file = tk.Button(self, text="Выбрать файл выгрузки",
                             command=self.choose_file_MB,
                            background="#7fc92e",     # фоновый цвет кнопки
             foreground="#ffffff",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font='Cirle 14' )
        btn_file.pack(padx=60, pady=5)
        btn_OBR = tk.Button(self, text="Выбрать файл опроса",
                             command=self.choose_file_OPR,
                            background="#7fc92e",     # фоновый цвет кнопки
             foreground="#ffffff",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font='Cirle 14' )
        btn_OBR.pack(padx=120, pady=5)
        btn_BD = tk.Button(self, text="Выбрать таблицу из БД",
                             command=self.choose_file_BD,
                            background="#7fc92e",     # фоновый цвет кнопки
             foreground="#ffffff",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font='Cirle 14' )
        btn_BD.pack(padx=60, pady=5)
        btn_BD = tk.Button(self, text="Выбрать html из ВК",
                             command=self.choose_file_VK,
                            background="#7fc92e",     # фоновый цвет кнопки
             foreground="#ffffff",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font='Cirle 14' )
        btn_BD.pack(padx=60, pady=5)
        
        btn_GO = tk.Button(self, text="Получить полную таблицу",
                             command=self.Lets_go,
                            background="#ff732b",     # фоновый цвет кнопки
             foreground="#ffffff",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font='Cirle 14' )
        btn_GO.pack(padx=120, pady=5)
        btn_new_rating = tk.Button(self, text="Получить актуальный рейтинг",
                             command=self.new_rating,
                            background="#ff732b",     # фоновый цвет кнопки
             foreground="#ffffff",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font='Cirle 14' )
        btn_new_rating.pack(padx=120,pady=5)
        btn_new_users = tk.Button(self, text="Получить новых учеников",
                             command=self.new_users,
                            background="#ff732b",     # фоновый цвет кнопки
             foreground="#ffffff",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font='Cirle 14' )
        btn_new_users.pack(padx=120,pady=5)
        btn_leave = tk.Button(self, text="Получить покинувших учеников",
                             command=self.leave_users,
                            background="#ff732b",     # фоновый цвет кнопки
             foreground="#ffffff",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font='Cirle 14' )
        btn_leave.pack(padx=120,pady=5)
        btn_file = tk.Button(self, text="Сохранить логин и пароль",
                             command=self.choose_file_MB,
                            background="#7fc92e",     # фоновый цвет кнопки
             foreground="#ffffff",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font='Cirle 14' )
        '''
        btn_save  = tk.Button(self, text="Сохранить логин и пароль",
                             command=self.save,
                            background="#ff732b",     # фоновый цвет кнопки
             foreground="#ffffff",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font='Cirle 14' )
        btn_save.pack(padx=120,pady=5)
    
    def save(self):
        String=(login.get()+'\t'+password.get()).encode()
        f = Fernet(key)
        encrypted_data = f.encrypt(String)
        with open('pswd.txt', 'wb') as file:
            file.write(encrypted_data)
    '''
    def choose_file_MB(self):
        filetypes = (("Таблица","*.xlsx"),
                     ("Текстовый файл", "*.txt"),
                     ("Любой", "*"))
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/",
                                      filetypes=filetypes)
        if filename:
            global Metabase
            Metabase=pd.read_excel(filename)
    def choose_file_OPR(self):
        filetypes = (("Таблица","*.xlsx"),
                     ("Текстовый файл", "*.txt"),
                     ("Любой", "*"))
        filename= fd.askopenfilename(title="Открыть файл", initialdir="/",
                                      filetypes=filetypes)
        if filename:
            global opros
            opros=pd.read_excel(filename)
            
    def choose_file_BD(self):
        filetypes = (("Таблица","*.csv"),
                     ("Текстовый файл", "*.txt"),
                     ("Любой", "*"))
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/",
                                      filetypes=filetypes)
        if filename:
            global Base    
            Base=pd.read_csv(filename)
            new_header = Base.iloc[0] #grab the first row for the header
            Base = Base[1:] #take the data less the header row
            Base.columns = new_header #set the header row as the df header
    def choose_file_VK(self):
        filetypes = (
                     ("Текстовый файл", "*.txt"),
                     ("Любой", "*"))
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/",
                                      filetypes=filetypes)
        if filename:
            global VK
            VK=open(filename,'r',encoding='utf-8')
            VK=VK.readlines()
    def new_users(self):
        #try:
            global Base
            global Metabase
            global VK
            #try:
            #vk_session = vk_api.VkApi(login.get(), password.get(), app_id=2685278)
            #vk_session.auth(token_only=True)
            #users = vk_session.method('messages.getConversationMembers', {'v': 5.81, 'peer_id': 2000000000 + group_id, 'filter': 'all'})
            #except Exception:
            ##    mb.showwarning("Предупреждение", 'Cоединение с VK.com не установлено, проверьте правильность ввода')
            #print(Exception)
            i = 0
            Vk_names=[]
            Vk_url=[]
            Vk_join_date=[]
            mons=['авг','сен','окт','ноя',"дек","янв","фев","мар","апр","мая","июн","июл"]
            new_vk=[]
            for i in range(len(VK)):
                for j in range(len(VK[i])):
                    if VK[i][j:j+9]=='<li class':
                        k=j
                        m=i
                    if VK[i][j:j+5]=='</li>' and i==m:
                        new_vk.append(VK[i][k:j+5])
                    elif VK[i][j:j+5]=='</li>':
                        new_vk.append(VK[m][k:]+VK[i][:j])
            VK=new_vk
            VK.pop(0)
            for i in range(len(VK)):
                name=''
                Url=''
                join_date_=''
                join_date=''
                flag=False
                for j in range(len(VK[i])):
                    
                    if str(VK[i][j:j+19])=='class="Link"><span>':
                        k=j+19
                        while VK[i][k]!='<':
                            name+=VK[i][k]
                            k+=1
                        
                    
                    elif str(VK[i][j:j+25])=='Пригласила Ника Фоксфорд ':
                        k=j+25
                        while VK[i][k]!='"':
                            join_date_+=VK[i][k]
                            k+=1
                        n=0
                        day=''
                        while join_date_[n]!=' ':
                            day+=join_date_[n]
                            n+=1
                        else:
                            if day!='сегодня' and day!='вчера':
                                for m in range(len(mons)):
                                    if join_date_[n+1:n+4]==mons[m]:
                                        month=str((m+8)%12)
                                        if m<5:
                                            year='2021'
                                        else:
                                            year='2022'
                                        break
                                join_date=year+'-'+month+'-'+day
                            else:
                                join_date=''
                        
                    elif str(VK[i][j:j+10]) =='mid&quot;:':
                        k=j+10
                        while VK[i][k]!=',':
                            Url+=VK[i][k]
                            k+=1
                        
                        
                        if name!='' and Url!='' and join_date!='':
                            Vk_names.append(name)
                            Vk_url.append('https://vk.com/id'+Url)
                            Vk_join_date.append(join_date)
                            flag=True
                            break
                if not flag:
                    Vk_names.append(name)
                    Vk_url.append('https://vk.com/id'+Url)
                    if join_date_!='':
                        Vk_join_date.append(join_date)
                    else:
                        Vk_join_date.append(join_date_)
            BD_names=Base['ФИО ученика (Вконтакте)'].tolist()
            BD_urls=Base['Ссылка на ВК'].tolist()
            #for item in users['items']:
            #    Vk_join_date.append(str((datetime.utcfromtimestamp(item['join_date']).strftime('%Y-%m-%d %H:%M:%S')))[:10])
            VK_mb_url=Metabase['vk'].tolist()
            Names_in_fox=Metabase['Ученик'].tolist()
            user_id=Metabase['user_id'].tolist()
            Rating=Metabase['Рейтинг'].tolist()
            for i in range (len(user_id)):
                if len(str(Rating[i]))>4:
                    Rating[i]=str(str(Rating[i]))[:4]
            for i in range(len(user_id)):
                user_id[i]=str(user_id[i]).replace('.0','')
            Emails_in_fox=Metabase['email']
            Dostup=Metabase['Доступ'].tolist()
            for i in range (len(Dostup)):
                Dostup[i]='Да' if Dostup[i]=='Абонемент' else 'Нет'
            course_id=Metabase['course_id'].tolist()
            Ops=open('Новые пользователи.txt','w',encoding='utf-8')
            #вытягиваем имена и ссылки из вк
            '''
            for item in users['profiles']:
                i += 1
                Vk_names.append(item['last_name']+' '+item['first_name'])
                Vk_url.append('https://vk.com/id' + str(item['id']))
            '''
            Ops.write('ФИО ученика (Вконтакте)	Ссылка на ВК	ФИО ученика в Фоксфорде (metabase)	User id	Группа (А/Б)	Номер курса 	Дата вступления в беседу	Ссылка на группу	Абонемент	Текущий уровень знаний (из анкеты ОС)	Ожидания от курса 	Ожидания от сопровождения 	Какие предметы сдает	Хобби, увлечения	Отправлено сообщение–онбординг?	Какие курсы можно предложить	Передали в ОП? 	Предложили реферальную программу  (да/нет) 	сентябрь рейтинг	сентрябрь статус\n')            
            for j in range (len(Vk_names)):
                try:
                    if Vk_names[j] not in BD_names and Vk_url[j] not in BD_urls:
                        for i in range(len(Names_in_fox)):
                            try:
                                if str(Vk_names[j]).lower().replace('ё','е') in str(Names_in_fox[i]).lower().replace('ё','е') or str(Vk_names[j]).split()[1].lower().replace('ё','е')+str(Vk_names[j]).split()[0].lower().replace('ё','е') in str(Names_in_fox[i]).lower().replace('ё','е'):
                                    
                                    try:
                                        String=(str(Vk_names[j])+'\t'+str(Vk_url[j])+'\t'+str(Names_in_fox[i])+'\t'+str(user_id[i])+'\t'+'A'+'\t'+str(course_id[i])[:-2]+'\t'+str(Vk_join_date[j])+'\t'*2+Dostup[i]+'\t'*10+str(Rating[i])+'\t'+str(Metabase['Статус'][i])).replace('\n','')+'\n'
                                    except Exception:
                                        String=(str(Vk_names[j])+'\t'+str(Vk_url[j])+'\t'+str(Names_in_fox[i])+'\t'+str(user_id[i])+'\t'+'A'+'\t'+str(course_id[i])[:-2]+'\t'+'\t'*2+Dostup[i]+'\t'*10+str(Rating[i])+'\t'+str(Metabase['Статус'][i])).replace('\n','')+'\n'
                                    try:
                                        Ops.write(String)
                                    except Exception:
                                        mb.showinfo("Не удалось записать ученика", 'email: '+Emails_in_fox[i]+'\n vk: '+Vk_url[j] +'\nОбработайте вручную или исправьте символы.')

                                
                            
                                
                                elif Vk_url[j]==VK_mb_url[i]:
                                    
                                    try:
                                        String=(str(Vk_names[j])+'\t'+str(Vk_url[j])+'\t'+str(Names_in_fox[i])+'\t'+str(user_id[i])+'\t'+'A'+'\t'+str(course_id[i])[:-2]+'\t'+str(Vk_join_date[j])+'\t'*2+Dostup[i]+'\t'*10+str(Rating[i])+'\t'+str(Metabase['Статус'][i])).replace('\n','')+'\n'
                                    except Exception:
                                        String=(str(Vk_names[j])+'\t'+str(Vk_url[j])+'\t'+str(Names_in_fox[i])+'\t'+str(user_id[i])+'\t'+'A'+'\t'+str(course_id[i])[:-2]+'\t'+'\t'*2+Dostup[i]+'\t'*10+str(Rating[i])+'\t'+str(Metabase['Статус'][i])).replace('\n','')+'\n'
                                    try:
                                        Ops.write(String)
                                    except Exception:
                                        mb.showinfo("Не удалось записать ученика", 'email: '+Emails_in_fox[i]+'\n vk: '+Vk_url[j] +'\nОбработайте вручную или исправьте символы.')
                                        #input('Нажмите Enter, когда скопируете ссылку, чтобы не потерять его')

                                    break
                            except Exception:
                                mb.showinfo("Не удалось записать ученика", '\n vk: '+Vk_url[j] +'\nОбработайте вручную или исправьте символы.')
                                Vk_url.pop(j)
                                Vk_names.pop(j)
                                flag=False
                                break
                except Exception:
                    break
            Ops.close()
            if os.path.isfile('Новые пользователи.csv'): os.remove('Новые пользователи.csv') 
            if os.path.isfile('Новые пользователи.xlsx'): os.remove('Новые пользователи.xlsx') 
            os.rename('Новые пользователи.txt', 'Новые пользователи.csv')
            df = pd.read_csv('Новые пользователи.csv', sep='\t')
            df.to_excel('Новые пользователи.xlsx', 'Sheet1',index=False)
            os.remove('Новые пользователи.csv') 
            mb.showinfo("Информация", "Обработка успешно завершена")
        #except Exception:
            #mb.showwarning("Предупреждение", "Что-то пошло не тк, проверьте файл листа из БД и вводимые логин и пароль")        
    def leave_users(self):
        #try:
            global Base
            global VK
            global Metabase
            user_id=Metabase['user_id'].tolist()
            for i in range(len(user_id)):
                user_id[i]=str(user_id[i]).replace('.0','')
            BD_ids=Base['User id'].tolist()
            BD_names=Base['ФИО ученика (Вконтакте)'].tolist()
            BD_urls=Base['Ссылка на ВК'].tolist()
            Ops=open('Несовпали имена в вк и ссылки с тем, что есть в БД.txt','w',encoding='utf-8')
            Oks=open('Не найдены ID metabase.txt','w',encoding='utf-8')
            Vk_names=[]
            Vk_url=[]
            Vk_join_date=[]
            mons=['авг','сен','окт','ноя',"дек","янв","фев","мар","апр","мая","июн","июл"]
            new_vk=[]
            for i in range(len(VK)):
                for j in range(len(VK[i])):
                    if VK[i][j:j+9]=='<li class':
                        k=j
                        m=i
                    if VK[i][j:j+5]=='</li>' and i==m:
                        new_vk.append(VK[i][k:j+5])
                    elif VK[i][j:j+5]=='</li>':
                        new_vk.append(VK[m][k:]+VK[i][:j])
            VK=new_vk
            VK.pop(0)
            for i in range(len(VK)):
                name=''
                Url=''
                join_date_=''
                join_date=''
                flag=False
                for j in range(len(VK[i])):
                    
                    if str(VK[i][j:j+19])=='class="Link"><span>':
                        k=j+19
                        while VK[i][k]!='<':
                            name+=VK[i][k]
                            k+=1
                        
                    
                    elif str(VK[i][j:j+25])=='Пригласила Ника Фоксфорд ':
                        k=j+25
                        while VK[i][k]!='"':
                            join_date_+=VK[i][k]
                            k+=1
                        n=0
                        day=''
                        while join_date_[n]!=' ':
                            day+=join_date_[n]
                            n+=1
                        else:
                            if day!='сегодня' and day!='вчера':
                                for m in range(len(mons)):
                                    if join_date_[n+1:n+4]==mons[m]:
                                        month=str((m+8)%12)
                                        if m<5:
                                            year='2021'
                                        else:
                                            year='2022'
                                        break
                                join_date=year+'-'+month+'-'+day
                            else:
                                join_date=''
                        
                    elif str(VK[i][j:j+10]) =='mid&quot;:':
                        k=j+10
                        while VK[i][k]!=',':
                            Url+=VK[i][k]
                            k+=1
                        
                        if name!='' and Url!='' and join_date!='':
                            Vk_names.append(name)
                            Vk_url.append('https://vk.com/id'+Url)
                            Vk_join_date.append(join_date)
                            flag=True
                            break
                if not flag:
                    Vk_names.append(name)
                    Vk_url.append('https://vk.com/id'+Url)
                    if join_date_!='':
                        Vk_join_date.append(join_date)
                    else:
                        Vk_join_date.append(join_date_)
            '''
            group_id = int(vk_gr_id.get())
            #try:
            vk_session = vk_api.VkApi(login.get(), password.get(), app_id=2685278)
            vk_session.auth(token_only=True)
            users = vk_session.method('messages.getConversationMembers', {'v': 5.81, 'peer_id': 2000000000 + group_id, 'filter': 'all'})
            #except Exception:
            #    mb.showwarning("Предупреждение", 'Cоединение с VK.com не установлено, проверьте правильность ввода')
            #    print(Exception)
            i = 0
            
            Vk_names=[]
            Vk_url=[]
            
            #вытягиваем имена и ссылки из вк
            for item in users['profiles']:
                i += 1
                Vk_names.append(item['last_name']+' '+item['first_name'])
                Vk_url.append('https://vk.com/id' + str(item['id']))
            '''
            Ops.write('Имя в БД\tUser id\n')
            Oks.write('Имя в БД\tUser id\n')
            for i in range (len(BD_names)):
                if BD_ids[i] not in user_id:
                    Oks.write(str(BD_names[i])+'\t'+str(BD_ids[i])+'\n')
                if len(str(BD_names[i]).split())>1:
                    if str(BD_names[i]).split()[1]+str(BD_names[i]).split()[0]  not in Vk_names and BD_names[i] not in Vk_names and BD_urls[i] not in Vk_url:
                        Ops.write(str(BD_names[i])+'\t'+str(BD_ids[i])+'\n')
                else:
                    if BD_names[i] not in Vk_names and BD_urls[i] not in Vk_url:
                        Ops.write(str(BD_names[i])+'\t'+str(BD_ids[i])+'\n')
            Ops.close()
            Oks.close()
            if os.path.isfile('Несовпали имена в вк и ссылки с тем, что есть в БД.csv'): os.remove('Несовпали имена в вк и ссылки с тем, что есть в БД.csv') 
            if os.path.isfile('Несовпали имена в вк и ссылки с тем, что есть в БД.xlsx'): os.remove('Несовпали имена в вк и ссылки с тем, что есть в БД.xlsx') 
            os.rename('Несовпали имена в вк и ссылки с тем, что есть в БД.txt', 'Несовпали имена в вк и ссылки с тем, что есть в БД.csv')
            df = pd.read_csv('Несовпали имена в вк и ссылки с тем, что есть в БД.csv', sep='\t')
            df.to_excel('Несовпали имена в вк и ссылки с тем, что есть в БД.xlsx', 'Sheet1',index=False)
            os.remove('Несовпали имена в вк и ссылки с тем, что есть в БД.csv') 
            if os.path.isfile('Не найдены ID metabase.csv'): os.remove('Не найдены ID metabase.csv') 
            if os.path.isfile('Не найдены ID metabase.xlsx'): os.remove('Не найдены ID metabase.xlsx') 
            os.rename('Не найдены ID metabase.txt', 'Не найдены ID metabase.csv')
            df = pd.read_csv('Не найдены ID metabase.csv', sep='\t')
            df.to_excel('Не найдены ID metabase.xlsx', 'Sheet1',index=False)
            os.remove('Не найдены ID metabase.csv') 
            mb.showinfo("Информация", "Обработка успешно завершена")
        #except Exception:
            #mb.showwarning("Предупреждение", "Что-то пошло не тк, проверьте файл листа из БД и вводимые логин и пароль")
    def new_rating(self):
        #try:
            global Base
            global Metabase
            BD_ids=Base['User id'].tolist()
            BD_names=Base['ФИО ученика (Вконтакте)'].tolist()
            MB_ids=Metabase['user_id'].tolist()
            Rating=Metabase['Рейтинг'].tolist()
            flags=[0]*len(BD_ids)
            Wr=open('Рейтинг и статус.txt','w',encoding='utf-8')
            Wr.write('Рейтинг из выгрузки\tСтатус из выгрузки\n')
            for i in range (len(BD_ids)):
                for j in range(len(MB_ids)):
                    MB_ids[j]=str(MB_ids[j]).replace('.0','').lower()
                    if BD_ids[i]==MB_ids[j]:
                        try:
                            String=str(Rating[j])[:4]+'\t'+str(Metabase['Статус'][j])+'\n'
                        except Exception:
                            String=str(Rating[j])+'\t'+str(Metabase['Статус'][j])+'\n'
                        Wr.write(String)
                        flags[i]=1
                if flags[i]==0:
                    Wr.write('\t\n')
            Wr.close()
            Ops=open('Рейтинг не проставлен, не нашлось в Metabase.txt','w',encoding='utf-8')
            Ops.write('Имя ученика\tUser id\n')
            for i in range(len(flags)):
                if flags[i]==0:
                    String=str(BD_names[i])+'\t'+str(BD_ids[i])+'\n'
                    Ops.write(String)
            Ops.close()
            if os.path.isfile('Рейтинг и статус.csv'): os.remove('Рейтинг и статус.csv') 
            if os.path.isfile('Рейтинг и статус.xlsx'): os.remove('Рейтинг и статус.xlsx') 
            os.rename('Рейтинг и статус.txt', 'Рейтинг и статус.csv')
            df = pd.read_csv('Рейтинг и статус.csv', sep='\t')
            os.remove('Рейтинг и статус.csv') 
            df.to_excel('Рейтинг и статус.xlsx', 'Sheet1',index=False)
            if os.path.isfile('Рейтинг не проставлен, не нашлось в Metabase.csv'): os.remove('Рейтинг не проставлен, не нашлось в Metabase.csv') 
            if os.path.isfile('Рейтинг не проставлен, не нашлось в Metabase.xlsx'): os.remove('Рейтинг не проставлен, не нашлось в Metabase.xlsx') 
            os.rename('Рейтинг не проставлен, не нашлось в Metabase.txt', 'Рейтинг не проставлен, не нашлось в Metabase.csv')
            df = pd.read_csv('Рейтинг не проставлен, не нашлось в Metabase.csv', sep='\t')
            df.to_excel('Рейтинг не проставлен, не нашлось в Metabase.xlsx', 'Sheet1',index=False)
            os.remove('Рейтинг не проставлен, не нашлось в Metabase.csv') 
            #mb.showinfo("Информация", "Обработка успешно завершена")
        #except Exception:
            #mb.showwarning("Предупреждение", "Что-то пошло не тк, проверьте файлы выгрузок из Metabase и листа из БД")
    def Lets_go(self):
        global Base
        global opros
        global Metabase
        global VK
        is_ok=True
        try:
            dates=opros['Отметка времени'].tolist()
        except Exception:
            print('Столбец "Отметка времени" назван неверно.')
        try:
            Names=opros['Как вас зовут (Ваше Имя и Фамилия Вконтакте)?'].tolist()
        except Exception:
            print('Столбец "Как вас зовут (Ваше Имя и Фамилия Вконтакте)?" назван неверно.')
        
        emails=opros['Напишите, пожалуйста, Вашу электронную почту, которая привязана к аккаунту в Фоксфорде'].tolist()
        try:
            levels=opros['Оцените Ваш текущий уровень знаний. На какой балл Вы сейчас пишете пробники ЕГЭ?'].tolist()
        except Exception:
            print('Столбец "Оцените Ваш текущий уровень знаний. " назван неверно.')
            levels=opros['Оцените Ваш текущий уровень знаний. '].tolist()
            
        try:
            nextlevels=opros['Что Вы будете считать вашим личным успехом после окончания курса?'].tolist()
        except Exception:
            print('Столбец "Что Вы будете считать вашим личным успехом после окончания курса?" назван неверно.')
        
        try:
            difficultss=opros['Какие сложности Вы сейчас испытываете? Расскажите все проблемы, что на душе: учеба, организация времени, самомотивация, отношения с родителями, со сверстниками, стресс перед экзаменами?'].tolist()
        except Exception:
            difficultss=opros['Какие сложности Вы сейчас испытываете? Расскажите все проблемы, что на душе: учеба, организация времени, самомотивация, отношения с родителями, со сверстниками, стресс перед экзаменами?В течение года будут предложены бесплатные вебинары с психологом.'].tolist()
        try:
            Is_in_Foxs=opros['Учились ли Вы ранее в онлайн-школе? Если да, то напишите в какой. Если нет, то поставьте прочерк.'].tolist()
        except Exception:
            print('Столбец "Учились ли Вы ранее в онлайн-школе? Если да, то напишите в какой. Если нет, то поставьте прочерк." назван неверно.')
        try:
            Is_works=opros['Работали ли Вы ранее с куратором (наставником)?'].tolist()
        except Exception:
            print('Столбец "Работали ли Вы ранее с куратором (наставником)?" назван неверно.')
        try:
            Cour_helps=opros['Какую помощь от куратора Вы бы хотели получить в течение курса?'].tolist()
        except Exception:
            print('Столбец "Какую помощь от куратора Вы бы хотели получить в течение курса?" назван неверно.')
        try:
            courses=opros['Какие у Вас ожидания от курса?'].tolist()
        except Exception:
            print('Столбец "Какие у Вас ожидания от курса?" назван неверно.')
        try:
            courators=opros['Какие у Вас есть ожидания от кураторского сопровождения?'].tolist()
        except Exception:
            print('Столбец "Какие у Вас есть ожидания от кураторского сопровождения?" назван неверно.')
        
        poryadok=[]
        freeTimes=opros['Напишите, пожалуйста, Ваши хобби. Самые популярные хобби будут реализовываться в течение года в качестве дополнительных активностей.'].tolist()
        VK_mb_url=Metabase['vk'].tolist()
        Names_in_fox=Metabase['Ученик'].tolist()
        user_id=Metabase['user_id'].tolist()
        Rating=Metabase['Рейтинг'].tolist()
        for i in range (len(user_id)):
            if len(str(Rating[i]))>4:
                Rating[i]=str(str(Rating[i]))[:4]
        for i in range(len(user_id)):
            user_id[i]=str(user_id[i]).replace('.0','')
        Emails_in_fox=Metabase['email']
        Dostup=Metabase['Доступ'].tolist()
        course_id=Metabase['course_id'].tolist()
        #Обработка абониментов 
        for i in range (len(Dostup)):
            Dostup[i]='Да' if Dostup[i]=='Абонемент' else 'Нет'

        flags=[0]*len(emails)
        obr=[]
        #подключение ВК
        f = open('VK_users.txt', 'w', encoding='utf-8')
        Vk_in=[]
        '''
        group_id = int(vk_gr_id.get())
        #try:
        vk_session = vk_api.VkApi(login.get(), password.get(), app_id=2685278)
        vk_session.auth(token_only=True)
        users = vk_session.method('messages.getConversationMembers', {'v': 5.81, 'peer_id': 2000000000 + group_id, 'filter': 'all'})
        #except Exception:
        #mb.showwarning("Предупреждение", 'Cоединение с VK.com не установлено, проверьте правильность ввода')
        #is_ok=False
        #print(Exception)
        
        i = 0
        Vk_names=[]
        Vk_url=[]
        
        Vk_join_date=[]
        #вытягиваем имена и ссылки из вк
        for item in users['profiles']:
            i += 1
            Vk_names.append(item['last_name']+' '+item['first_name'])
            Vk_url.append('https://vk.com/id' + str(item['id']))
        for item in users['items']:
            Vk_join_date.append(str((datetime.utcfromtimestamp(item['join_date']).strftime('%Y-%m-%d %H:%M:%S')))[:10])
        '''
        Vk_names=[]
        Vk_url=[]
        Vk_join_date=[]
        mons=['авг','сен','окт','ноя',"дек","янв","фев","мар","апр","мая","июн","июл"]
        new_vk=[]
        for i in range(len(VK)):
            for j in range(len(VK[i])):
                if VK[i][j:j+9]=='<li class':
                    k=j
                    m=i
                if VK[i][j:j+5]=='</li>' and i==m:
                    new_vk.append(VK[i][k:j+5])
                elif VK[i][j:j+5]=='</li>':
                    new_vk.append(VK[m][k:]+VK[i][:j])
        VK=new_vk
        VK.pop(0)
        for i in range(len(VK)):
            name=''
            Url=''
            join_date_=''
            join_date=''
            flag=False
            for j in range(len(VK[i])):
                
                if str(VK[i][j:j+19])=='class="Link"><span>':
                    k=j+19
                    while VK[i][k]!='<':
                        name+=VK[i][k]
                        k+=1
                    
                
                elif str(VK[i][j:j+25])=='Пригласила Ника Фоксфорд ':
                    k=j+25
        
                    while VK[i][k]!='"':
                        join_date_+=VK[i][k]
                        k+=1
                    n=0
                    day=''
                    while join_date_[n]!=' ':
                        day+=join_date_[n]
                        n+=1
                    else:
                        if day!='сегодня' and day!='вчера':
                            for m in range(len(mons)):
                                if join_date_[n+1:n+4]==mons[m]:
                                    month=str((m+8)%12)
                                    if m<5:
                                        year='2021'
                                    else:
                                        year='2022'
                                    break
                            join_date=year+'-'+month+'-'+day
                        else:
                            join_date=''
                    
                elif str(VK[i][j:j+10]) =='mid&quot;:':
                    k=j+10
                    while VK[i][k]!=',':
                        Url+=VK[i][k]
                        k+=1
                    
                    
                    if name!='' and Url!='' and join_date!='':
                        Vk_names.append(name)
                        Vk_url.append('https://vk.com/id'+Url)
                        Vk_join_date.append(join_date)
                        flag=True
                        break
            if not flag:
                Vk_names.append(name)
                Vk_url.append('https://vk.com/id'+Url)
                if join_date_!='':
                    Vk_join_date.append(join_date)
                else:
                    Vk_join_date.append(join_date_)
        #если в MB нет ссылки, то вписываем
        for i in range(len(Emails_in_fox)):
            if VK_mb_url[i]=='-':
                for j in range(len(Vk_url)):
                    if Vk_names[j] in Names_in_fox[i]:
                        VK_mb_url[i]=Vk_url[j]
                        
        #обработка опроса
        for i in range(len(emails)):
            for j in range (len(Emails_in_fox)):
                if emails[i].lower().replace(' ','') in Emails_in_fox[j].lower() or Emails_in_fox[j].lower() in emails[i].lower().replace(' ',''):
                    poryadok.append(j)
                    flags[i]=1
                    obr.append(Emails_in_fox[j])
            if flags[i]==0:
                poryadok.append('Ученика нет')
        net_u=open('ученики из опроса, которые не нашлись в metabase.txt','w',encoding='utf-8')
        for i in range(len(flags)):
            if flags[i]==0:
                net_u.write(emails[i])
                net_u.write('\n')
        net_u.close()
        c=0
        my_file = open("Обработанный опрос.txt", "w", encoding='utf-8')
        my_file.write('ФИО ученика (Вконтакте)	Ссылка на ВК	ФИО ученика в Фоксфорде (metabase)	User id	Группа (А/Б)	Номер курса 	Дата вступления в беседу	Ссылка на группу	Абонемент	Текущий уровень знаний (из анкеты ОС)	Ожидания от курса 	Ожидания от сопровождения 	Какие предметы сдает	Хобби, увлечения	Отправлено сообщение–онбординг?	Какие курсы можно предложить	Передали в ОП? 	Предложили реферальную программу  (да/нет) 	сентябрь рейтинг	сентрябрь статус\n')
        for g in poryadok:
            if g!='Ученика нет':
                try:
                    String=(str(Names[c])+'\t'+str(Metabase['vk'][g])+'\t'+str(Names_in_fox[g])+'\t'+str(user_id[g])+'\t'+'A'+'\t'+str(course_id[g])[:-2]+'\t'+str(Vk_join_date[c])+'\t'*2+Dostup[g]+'\t'+str(levels[c])+'\t'+str(courses[c])+'\t'+str(courators[c])+'\t'+'\t'+freeTimes[c]+'\t'*5+str(Rating[g])+'\t'+str(Metabase['Статус'][g])).replace('\n','')+'\n'
                except:
                    String=(str(Names[c])+'\t'+str(Metabase['vk'][g])+'\t'+str(Names_in_fox[g])+'\t'+str(user_id[g])+'\t'+'A'+'\t'+str(course_id[g])[:-2]+'\t'+'\t'*2+Dostup[g]+'\t'+str(levels[c])+'\t'+str(courses[c])+'\t'+str(courators[c])+'\t'+'\t'+freeTimes[c]+'\t'*5+str(Rating[g])+'\t'+str(Metabase['Статус'][g])).replace('\n','')+'\n'
                my_file.write(String)
                Vk_in.append(str(Metabase['vk'][g]))
            c+=1
            #my_file.write(g)
            #my_file.write('\n')
        f= open("Vk_users.txt", "w", encoding='utf-8')
        f.write('ФИО ученика (Вконтакте)	Ссылка на ВК	ФИО ученика в Фоксфорде (metabase)	User id	Группа (А/Б)	Номер курса 	Дата вступления в беседу	Ссылка на группу	Абонемент	Текущий уровень знаний (из анкеты ОС)	Ожидания от курса 	Ожидания от сопровождения 	Какие предметы сдает	Хобби, увлечения	Отправлено сообщение–онбординг?	Какие курсы можно предложить	Передали в ОП? 	Предложили реферальную программу  (да/нет) 	сентябрь рейтинг	сентрябрь статус\n')
        #Если опроса не нашлось, то заполняем без него
        for i in range(len(Emails_in_fox)):
            if Emails_in_fox[i].lower() not in obr:
                for j in range(len(Vk_url)):
                    try:
                        if str(Vk_names[j]).lower().replace('ё','е') in str(Names_in_fox[i]).lower().replace('ё','е') or str(Vk_names[j]).split()[1].lower().replace('ё','е')+str(Vk_names[j]).split()[0].lower().replace('ё','е') in str(Names_in_fox[i]).lower().replace('ё','е'):
                            try:
                                String=(str(Vk_names[j])+'\t'+str(Vk_url[j])+'\t'+str(Names_in_fox[i])+'\t'+str(user_id[i])+'\t'+'A'+'\t'+str(course_id[i])[:-2]+'\t'+str(Vk_join_date[j])+'\t'*2+Dostup[i]+'\t'*10+str(Rating[i])+'\t'+str(Metabase['Статус'][i])).replace('\n','')+'\n'
                            except Exception:
                                String=(str(Vk_names[j])+'\t'+str(Vk_url[j])+'\t'+str(Names_in_fox[i])+'\t'+str(user_id[i])+'\t'+'A'+'\t'+str(course_id[i])[:-2]+'\t'+'\t'*2+Dostup[i]+'\t'*10+str(Rating[i])+'\t'+str(Metabase['Статус'][i])).replace('\n','')+'\n'
                            try:
                                f.write(String)
                            except Exception:
                                mb.showinfo("Ученик с нераспознанными символами", 'email: '+Emails_in_fox[i]+'\n vk: '+Vk_url[j] +'\nОбработайте вручную или исправьте символы.')
                            obr.append(Emails_in_fox[i])
                            Vk_in.append(Vk_url[j])
                            break
                        elif Vk_url[j]==VK_mb_url[i]:
                            try:
                                String=(Vk_names[j]+'\t'+str(Vk_url[j])+'\t'+str(Names_in_fox[i])+'\t'+str(user_id[i])+'\t'+'A'+'\t'+str(course_id[i])[:-2]+'\t'+str(Vk_join_date[j])+'\t'*2+Dostup[i]+'\t'*10+str(Rating[i])+'\t'+str(Metabase['Статус'][i])).replace('\n','')+'\n'
                            except Exception:
                                String=(str(Vk_names[j])+'\t'+str(Vk_url[j])+'\t'+str(Names_in_fox[i])+'\t'+str(user_id[i])+'\t'+'A'+'\t'+str(course_id[i])[:-2]+'\t'+'\t'*2+Dostup[i]+'\t'*10+str(Rating[i])+'\t'+str(Metabase['Статус'][i])).replace('\n','')+'\n'
                            try:
                                f.write(String)
                            except Exception:
                                mb.showinfo("Ученик с нераспознанными символами", 'email: '+Emails_in_fox[i]+'\n vk: '+Vk_url[j] +'\nОбработайте вручную или исправьте символы.')
                                #input('Нажмите Enter, когда скопируете ссылку, чтобы не потерять его')
                            obr.append(Emails_in_fox[i])
                            Vk_in.append(Vk_url[j])
                            break
                    except Exception:
                        mb.showinfo("Не удалось записать ученика", '\n vk: '+Vk_url[j] +'\nОбработайте вручную или исправьте символы.')
                        Vk_url.pop(j)
                        Vk_names.pop(j)
                        flag=False
                        break
        f.close()       
        my_file.close()
        Not_in_VK = open('Не оказалось в ВК.txt', 'w', encoding='utf-8')
        Not_in_VK.write('Email\n')
        for i in range(len(Emails_in_fox)):
            if Emails_in_fox[i] not in obr:
                try:
                    Not_in_VK.write(Emails_in_fox[i])
                    Not_in_VK.write('\n')
                except Exception:
                    mb.showinfo("Ученик с нераспознанными символами", Emails_in_fox[i]+' - Обработайте вручную или исправьте символы.')
                    #input('Нажмите Enter, когда скопируете, чтобы не потерять его')        
        Not_in_VK.close()
        Not_in_MB = open('Вк не оказалось в Metabase.txt', 'w', encoding='utf-8')
        Not_in_MB.write('Имя в VK\tСсылка на VK\n')
        for i in range(len(Vk_url)):
            if Vk_url[i] not in Vk_in:
                String=Vk_names[i]+'\t'+Vk_url[i]
                try:
                    Not_in_MB.write(String)
                    Not_in_MB.write('\n')
                except Exception:
                    mb.showinfo("Ученик с нераспознанными символами", Emails_in_fox[i]+' - Обработайте вручную или исправьте символы.')
                    #input('Нажмите Enter, когда скопируете, чтобы не потерять его') 
        Not_in_MB.close()
        if os.path.isfile('Не оказалось в ВК.csv'): os.remove('Не оказалось в ВК.csv') 
        os.rename('Не оказалось в ВК.txt', 'Не оказалось в ВК.csv')
        df = pd.read_csv('Не оказалось в ВК.csv', sep='\t')
        if os.path.isfile('Не оказалось в ВК.xlsx'): os.remove('Не оказалось в ВК.xlsx')
        df.to_excel('Не оказалось в ВК.xlsx', 'Sheet1',index=False)
        os.remove('Не оказалось в ВК.csv')
        if os.path.isfile('VK_users.csv'): os.remove('VK_users.csv')
        os.rename('VK_users.txt', 'VK_users.csv')
        df = pd.read_csv('VK_users.csv', sep='\t')
        if os.path.isfile('VK_users.xlsx'): os.remove('VK_users.xlsx')
        df.to_excel('VK_users.xlsx', 'Sheet1',index=False)
        os.remove('VK_users.csv')
        if os.path.isfile('Обработанный опрос.csv'): os.remove('Обработанный опрос.csv')
        os.rename('Обработанный опрос.txt', 'Обработанный опрос.csv')
        df = pd.read_csv('Обработанный опрос.csv', sep='\t')
        if os.path.isfile('Обработанный опрос.xlsx'): os.remove('Обработанный опрос.xlsx')
        df.to_excel('Обработанный опрос.xlsx', 'Sheet1',index=False)
        os.remove('Обработанный опрос.csv')
        if os.path.isfile('Вк не оказалось в Metabase.csv'): os.remove('Вк не оказалось в Metabase.csv') 
        os.rename('Вк не оказалось в Metabase.txt', 'Вк не оказалось в Metabase.csv')
        df = pd.read_csv('Вк не оказалось в Metabase.csv', sep='\t')
        if os.path.isfile('Вк не оказалось в Metabase.xlsx'): os.remove('Вк не оказалось в Metabase.xlsx') 
        df.to_excel('Вк не оказалось в Metabase.xlsx', 'Sheet1',index=False)
        os.remove('Вк не оказалось в Metabase.csv') 
        
        if is_ok: mb.showinfo("Информация", "Обработка успешно завершена")



if __name__ == "__main__":    
    app = App()
    app.geometry('1200x900')
    app.configure(bg='#f2f3f4')
    app.title("Привет, куратор!")
    app.mainloop()
