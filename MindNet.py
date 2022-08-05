#MindNet - Main Project

#Полное описание для понимания:

#Импортирование

import pygame
import time
import pickle
import random

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

Z = 1
pygame.font.init()

inv_cover_point = '80'
width = '350'
height = '263'

current_slot = 0

#
inv_x = 180
inv_y = 270

now_plays = 0
try:
    load_file = open('Files/Saves/new.dat', 'rb')
    sett_param = pickle.load(load_file)
    load_file.close()
except:
    print('При считывании файла new.dat возникла ошибка.')
    print('Инициализирую повторное создание... ...')
    save_file = open('Files/Saves/new.dat','wb')
    new = 1
    pickle.dump(new, save_file)
    print('Файл new.dat был успешно восстановлен.')
    save_file.close()
 
try:
    load_file = open('Files/Saves/sett_param.dat', 'rb')
    sett_param = pickle.load(load_file)
    load_file.close()    
except:
    print('При считывании файла sett_param.dat возникла ошибка.')
    print('Инициализирую повторное создание... ...')
    save_file = open('Files/Saves/sett_param.dat','wb')
    sett_param = [1,1,1,1]
    pickle.dump(sett_param, save_file)
    print('Файл sett_param.dat был успешно восстановлен.')
    save_file.close()
    load_file = open('Files/Saves/sett_param.dat', 'rb')
    sett_param = pickle.load(load_file)
    load_file.close() 



pygame.mixer.init()
if sett_param[2] == 1:
    walk_sound = pygame.mixer.Sound('Files/Soundtrack/walk.ogg')
    walk_sound.set_volume(1)
if sett_param[2] == 0:
    walk_sound = pygame.mixer.Sound('Files/Soundtrack/silent.ogg')
    walk_sound.set_volume(1)    

if sett_param[1] == 1:
    main_theme_1 = pygame.mixer.Sound('Files/Soundtrack/main_theme_1.ogg')
    main_theme_1.set_volume(0.5)
    main_theme_2 = pygame.mixer.Sound('Files/Soundtrack/main_theme_2.ogg')
    main_theme_2.set_volume(0.3)
if sett_param[1] == 0:
    main_theme_1 = pygame.mixer.Sound('Files/Soundtrack/silent.ogg')
    main_theme_1.set_volume(0.5)
    main_theme_2 = pygame.mixer.Sound('Files/Soundtrack/silent.ogg')
    main_theme_2.set_volume(0.3)

if sett_param[0] == 1:
    Click_Sound = pygame.mixer.Sound('Files/Soundtrack/Click_Sound.ogg')
    Click_Sound.set_volume(1)
    Select_Sound = pygame.mixer.Sound('Files/Soundtrack/Select_Sound.ogg')
    Select_Sound.set_volume(1)
if sett_param[0] == 0:
        Click_Sound = pygame.mixer.Sound('Files/Soundtrack/silent.ogg')
        Click_Sound.set_volume(1)
        Select_Sound = pygame.mixer.Sound('Files/Soundtrack/silent.ogg')
        Select_Sound.set_volume(1)
if sett_param[3] == 1:
    Background = pygame.mixer.Sound('Files/Soundtrack/Background.ogg')
    Background.set_volume(0.7)
if sett_param[3] == 0:
    Background = pygame.mixer.Sound('Files/Soundtrack/silent.ogg')
    Background.set_volume(0.7)

play_background = 1

wtim = time.time()
def walk():
    global wtim
    #print(time.time()-wtim)
    if time.time()-wtim>5.5:
        walk_sound.play()
        wtim = time.time()
        
def start_music():
    global now_plays
    if random.randint(1,2)==1:
        now_plays = 1
        
        main_theme_1.play(1)
    else:
        now_plays = 2
        
        main_theme_2.play(1)


start_music()
#now_plays = 1
tim = time.time()
def menu_music():
    global tim
    global now_plays
    if n == 1:
        if now_plays == 1:
            if time.time()-tim>=115:
                
                main_theme_1.stop()
                now_plays = 2
                #main_theme_2.set_volume(1)
                main_theme_2.play(1)    
                tim = time.time()
                
        if now_plays == 2:
            if time.time()-tim>=60:
                main_theme_2.stop()
                now_plays = 1
                #main_theme_1.set_volume(1)
                main_theme_1.play(1)    
                tim = time.time()

#Попытка ускорить игру
clock = pygame.time.Clock()
#Создание окна
window = pygame.display.set_mode((1100,600))
screen = pygame.Surface((1100,600))

#Имя для окна
pygame.display.set_caption('MindNet')

#Класс создания объектов для игры

class Sprite:
    def __init__(self,xpos,ypos,filename,width,height,cover_point):
        self.x=xpos
        self.y=ypos
        self.width = width
        self.height = height
        self.cover_point = cover_point
        self.bitmap=pygame.image.load(filename).convert_alpha()
        #self.bitmap.set_colorkey((255,255,255))
    def render(self):
        screen.blit(self.bitmap,(self.x,self.y))

#Массив с названиями всех объектов
all_objects = []

game_quit_sure = 0
#Меню

menu_access = 1


#Инвентарь

inv = 0
inv_type = 1

select_type = 2

inv_obj = 'Files/Textures/Objects/tree1.png'

inventory1 = Sprite(207,51,'Files/Textures/Inventory/Menu1.png',0,0,0)
inventory2 = Sprite(207,51,'Files/Textures/Inventory/Menu2.png',0,0,0)
inventory3 = Sprite(207,51,'Files/Textures/Inventory/Menu3.png',0,0,0)
inventory4 = Sprite(207,51,'Files/Textures/Inventory/Menu4.png',0,0,0)

#Иконки

select = Sprite(253,127,'Files/Textures/Inventory/Icons/select.png',0,0,0)

inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/tree1_icon.png',0,0,0)

#Сейчас меню или игра?
n = 1 #1 = Меню 0 = Игра

#Шрифт

#f2 = pygame.font.Font('Files/Font/GEO.ttf', 320)
#text2 = f2.render("World Мир", 1, (0, 180, 0))

f1 = pygame.font.Font('Files/Font/GEO.ttf', 36)
text1 = f1.render("Привет! Ты здесь впервые,", 1, (28, 112, 242))

f2 = pygame.font.Font('Files/Font/GEO.ttf', 36)
text2 = f2.render("позволишь мне объяснить", 1, (28, 112, 242))

f3 = pygame.font.Font('Files/Font/GEO.ttf', 36)
text3 = f3.render("как тут все устроено? :)", 1, (28, 112, 242))

#pygame.display.update()

#Инициализация меню

To_Mind_Palace = Sprite(200,120,'Files/Textures/Menu/To_Mind_Palace.png',0,0,0)
Learn = Sprite(780,15,'Files/Textures/Menu/Learn.png',0,0,0)
Profile = Sprite(190,308,'Files/Textures/Menu/Profile.png',0,0,0)
Settings = Sprite(390,306,'Files/Textures/Menu/Settings.png',0,0,0)
Exit = Sprite(583,308,'Files/Textures/Menu/Exit.png',0,0,0)

New_Mind_Palace = Sprite(80,120,'Files/Textures/Menu/New_Mind_Palace.png',0,0,0)
Continue_Mind_Palace = Sprite(80,120,'Files/Textures/Menu/Continue_Mind_Palace.png',0,0,0)
Tutorial = Sprite(80,120,'Files/Textures/Menu/Tutorial.png',0,0,0)
Quit_Menu2 = Sprite(88,120,'Files/Textures/Menu/Quit_Menu2.png',0,0,0)

dev = Sprite(100,-370,'Files/Textures/Menu/dev.png',0,0,0)
l = Sprite(100,-370,'Files/Textures/Menu/l.png',0,0,0)

sett = Sprite(80,-200,'Files/Textures/Menu/sett.png',0,0,0)

if sett_param[0] == 1:
    sett_1 = Sprite(80,-200,'Files/Textures/Menu/sett_1_on.png',0,0,0)
else:
    sett_1 = Sprite(80,-200,'Files/Textures/Menu/sett_1_off.png',0,0,0)

if sett_param[1] == 1:    
    sett_2 = Sprite(80,-200,'Files/Textures/Menu/sett_2_on.png',0,0,0)
else:
    sett_2 = Sprite(80,-200,'Files/Textures/Menu/sett_2_off.png',0,0,0)

if sett_param[2] == 1:    
    sett_3 = Sprite(80,-200,'Files/Textures/Menu/sett_3_on.png',0,0,0)
else:
    sett_3 = Sprite(80,-200,'Files/Textures/Menu/sett_3_off.png',0,0,0)

if sett_param[3] == 1:
    sett_4 = Sprite(80,-200,'Files/Textures/Menu/sett_4_on.png',0,0,0)
else:
    sett_4 = Sprite(80,-200,'Files/Textures/Menu/sett_4_off.png',0,0,0)

Game_Play = Sprite(80,120,'Files/Textures/Menu/game_play.png',0,0,0)
Game_Save = Sprite(80,120,'Files/Textures/Menu/game_save.png',0,0,0)
Game_Quit = Sprite(80,120,'Files/Textures/Menu/game_quit.png',0,0,0)

slot1 = Sprite(-390,-240,'Files/Textures/Menu/mslot1.png',0,0,0)
slot2 = Sprite(-390,-240,'Files/Textures/Menu/mslot2.png',0,0,0)
slot3 = Sprite(-390,-240,'Files/Textures/Menu/mslot3.png',0,0,0)
Quit_Slots = Sprite(-390,-240,'Files/Textures/Menu/mQuit_Slots.png',0,0,0)

background0 = Sprite(0,0,'Files/Textures/Menu/Background/0.png',0,0,0)
background1 = Sprite(5000,0,'Files/Textures/Menu/Background/1.png',0,0,0)
background2 = Sprite(5000,0,'Files/Textures/Menu/Background/2.png',0,0,0)
background3 = Sprite(5000,0,'Files/Textures/Menu/Background/3.png',0,0,0)
background4 = Sprite(5000,0,'Files/Textures/Menu/Background/4.png',0,0,0)
background5 = Sprite(5000,0,'Files/Textures/Menu/Background/5.png',0,0,0)
background6 = Sprite(5000,0,'Files/Textures/Menu/Background/6.png',0,0,0)

tutor = Sprite(0,400,'Files/Textures/Tutorial/tutor.png',0,0,0)#0,400
tutor2 = Sprite(0,400,'Files/Textures/Tutorial/tutor2.png',0,0,0)
tutor3 = Sprite(0,400,'Files/Textures/Tutorial/tutor3.png',0,0,0)
m1 = Sprite(10,10,'Files/Textures/Tutorial/m1.png',0,0,0)

menu_step = 0
ms = 6
ma = [0,ms,ms*2,ms*3,ms*4,ms*5,ms*6,ms*7]
def menu_anim():

    menu_music()
    #print(time.time())

    global menu_step
    global ma
    if menu_step>=ma[0] and menu_step<=ma[1]:
        background0.x = 0
        background1.x = 5000
        background2.x = 5000
        background3.x = 5000
        background4.x = 5000
        background5.x = 5000
        background6.x = 5000
    if menu_step>=ma[1] and menu_step<=ma[2]:
        background0.x = 5000
        background1.x = 0
        background2.x = 5000
        background3.x = 5000
        background4.x = 5000
        background5.x = 5000
        background6.x = 5000
    if menu_step>=ma[2] and menu_step<=ma[3]:
        background0.x = 5000
        background1.x = 5000
        background2.x = 0
        background3.x = 5000
        background4.x = 5000
        background5.x = 5000
        background6.x = 5000
    if menu_step>=ma[3] and menu_step<=ma[4]:
        background0.x = 5000
        background1.x = 5000
        background2.x = 5000
        background3.x = 0
        background4.x = 5000
        background5.x = 5000
        background6.x = 5000
    if menu_step>=ma[4] and menu_step<=ma[5]:
        background0.x = 5000
        background1.x = 5000
        background2.x = 5000
        background3.x = 5000
        background4.x = 0
        background5.x = 5000
        background6.x = 5000
    if menu_step>=ma[5] and menu_step<=ma[6]:
        background0.x = 5000
        background1.x = 5000
        background2.x = 5000
        background3.x = 5000
        background4.x = 5000
        background5.x = 0
        background6.x = 5000
    if menu_step>=ma[6] and menu_step<=ma[7]:
        background0.x = 5000
        background1.x = 5000
        background2.x = 5000
        background3.x = 5000
        background4.x = 5000
        background5.x = 5000
        background6.x = 0
    if menu_step>=ma[7]:
        menu_step = 0
    menu_step+=1

#Тип меню (1) главное, 2 - продолжить или начать новую

#Туториал
    '''
new = 1
save_file = open('Files/Saves/new.dat','wb')
pickle.dump(new, save_file)
save_file.close()'''

load_file = open('Files/Saves/new.dat', 'rb')
new = pickle.load(load_file)
load_file.close()

if new == 1:
    menu_type = 5 #5 - туториал
    tutor_step = 0
    tutor_on = 1 #1 включён
    text_x = 390
    tutor_begin = 0 #0 - загрузить
    new = 0
    save_file = open('Files/Saves/new.dat','wb')
    pickle.dump(new, save_file)
    save_file.close()
else:    
    menu_type = 1 #5 - туториал
    tutor_step = 0
    tutor_on = 0 #1 включён
    text_x = 390

    tutor_begin = 1 #0 - загрузить

def tutorial_text(t1,t2,t3):
        global f1
        global text1

        global f2
        global text2

        global f3
        global text3

        f1 = pygame.font.Font('Files/Font/GEO.ttf', 36)
        text1 = f1.render(t1, 1, (28, 112, 242))

        f2 = pygame.font.Font('Files/Font/GEO.ttf', 36)
        text2 = f2.render(t2, 1, (28, 112, 242))

        f3 = pygame.font.Font('Files/Font/GEO.ttf', 36)
        text3 = f3.render(t3, 1, (28, 112, 242))

def tutor_render():
        global To_Mind_Palace
        global Learn
        global Profile
        global Settings
        global Exit
        global tutor_step

        global New_Mind_Palace
        global Continue_Mind_Palace
        global Tutorial
        global Quit_Menu2

        global slot1
        
        if tutor_step == 1:
            m1.render()
            tutor.render()
            tutorial_text("Привет! Ты здесь впервые,","позволишь мне объяснить","как тут все устроено? :)")

        if tutor_step == 2:
            tutorial_text("","","")
            To_Mind_Palace.render()
            Learn.render()
            Profile.render()
            Settings.render()
            Exit.render()
            tutor2.render()

        if tutor_step == 3:
            To_Mind_Palace.render()
            Learn.render()  
            Profile.render()
            Settings.render()
            Exit.render()
            tutorial_text("","        Это главное меню.","")
            tutor.render()
        if tutor_step == 4:
            To_Mind_Palace = Sprite(200,120,'Files/Textures/Menu/To_Mind_Palace.png',0,0,0)
            Learn = Sprite(780,15,'Files/Textures/Menu/Learn.png',0,0,0)
            Profile = Sprite(190,308,'Files/Textures/Menu/Profile_Selected.png',0,0,0)
            Settings = Sprite(390,306,'Files/Textures/Menu/Settings_Selected.png',0,0,0)
            Exit = Sprite(583,308,'Files/Textures/Menu/Exit_Selected.png',0,0,0)
            tutor_step+=1
        if tutor_step == 5:
            tutorial_text("","","")
            tutor2.render()
            To_Mind_Palace.render()
            Learn.render()
            Profile.render()
            Settings.render()
            Exit.render()
        if tutor_step == 6:
            tutorial_text("Думаю эти кнопки","и так понятны :)","Потом посмотришь сам.")
            
            To_Mind_Palace.render()
            Learn.render()
            Profile.render()
            Settings.render()
            Exit.render()
            tutor.render()
        if tutor_step == 7:
            To_Mind_Palace = Sprite(200,120,'Files/Textures/Menu/To_Mind_Palace.png',0,0,0)
            Learn = Sprite(780,15,'Files/Textures/Menu/Learn_Selected.png',0,0,0)
            Profile = Sprite(190,308,'Files/Textures/Menu/Profile.png',0,0,0)
            Settings = Sprite(390,306,'Files/Textures/Menu/Settings.png',0,0,0)
            Exit = Sprite(583,308,'Files/Textures/Menu/Exit.png',0,0,0)
            tutor_step+=1
        if tutor_step == 8:
            tutorial_text("","","")
            To_Mind_Palace.render()
            Learn.render()
            Profile.render()
            Settings.render()
            Exit.render()
            tutor2.render()
        if tutor_step == 9:
            tutorial_text("Здесь ты можешь","узнать много нового!","Наука, языки и другое.")
            To_Mind_Palace.render()
            Learn.render()
            Profile.render()
            Settings.render()
            Exit.render()
            tutor.render()
        if tutor_step == 10:
            To_Mind_Palace = Sprite(200,120,'Files/Textures/Menu/To_Mind_Palace.png',0,0,0)
            Learn = Sprite(780,15,'Files/Textures/Menu/Learn.png',0,0,0)
            Profile = Sprite(190,308,'Files/Textures/Menu/Profile.png',0,0,0)
            Settings = Sprite(390,306,'Files/Textures/Menu/Settings.png',0,0,0)
            Exit = Sprite(583,308,'Files/Textures/Menu/Exit.png',0,0,0)
            tutor_step+=1
        if tutor_step == 11:
            tutorial_text("Теперь приступим","к созданию ", "Чертогов Разума!")
            To_Mind_Palace.render()
            Learn.render()
            Profile.render()
            Settings.render()
            Exit.render()
            tutor.render()
        if tutor_step == 12:
            To_Mind_Palace = Sprite(200,120,'Files/Textures/Menu/To_Mind_Palace_Selected.png',0,0,0)
            Learn = Sprite(780,15,'Files/Textures/Menu/Learn.png',0,0,0)
            Profile = Sprite(190,308,'Files/Textures/Menu/Profile.png',0,0,0)
            Settings = Sprite(390,306,'Files/Textures/Menu/Settings.png',0,0,0)
            Exit = Sprite(583,308,'Files/Textures/Menu/Exit.png',0,0,0)
            tutor_step+=1
        if tutor_step == 13:
            tutorial_text("","","")
            To_Mind_Palace.render()
            Learn.render()
            Profile.render()
            Settings.render()
            Exit.render()
            tutor2.render()
        if tutor_step == 14:
            New_Mind_Palace.render()
            Continue_Mind_Palace.render()
            Tutorial.render()
            Quit_Menu2.render()
            tutor2.render()
        if tutor_step == 15:
            New_Mind_Palace = Sprite(80,120,'Files/Textures/Menu/New_Mind_Palace_Selected.png',0,0,0)
            tutor_step+=1
        if tutor_step == 16:
            New_Mind_Palace.render()
            Continue_Mind_Palace.render()
            Tutorial.render()
            Quit_Menu2.render()
            tutor2.render()
        if tutor_step == 17:
            tutorial_text("Здесь можно создать","новые Чертоги Разума!","")
            New_Mind_Palace.render()
            Continue_Mind_Palace.render()
            Tutorial.render()
            Quit_Menu2.render()
            tutor.render()


        if tutor_step == 18:
            tutorial_text("","","")
            New_Mind_Palace = Sprite(80,120,'Files/Textures/Menu/New_Mind_Palace.png',0,0,0)
            Continue_Mind_Palace = Sprite(80,120,'Files/Textures/Menu/Continue_Mind_Palace.png',0,0,0)
            tutor_step+=1
        if tutor_step == 19:
            New_Mind_Palace.render()
            Continue_Mind_Palace.render()
            Tutorial.render()
            Quit_Menu2.render()
            tutor2.render()
        if tutor_step == 20:
            New_Mind_Palace = Sprite(80,120,'Files/Textures/Menu/New_Mind_Palace.png',0,0,0)
            Continue_Mind_Palace = Sprite(80,120,'Files/Textures/Menu/Continue_Mind_Palace_Selected.png',0,0,0)
            tutor_step+=1
        if tutor_step == 21:
            New_Mind_Palace.render()
            Continue_Mind_Palace.render()
            Tutorial.render()
            Quit_Menu2.render()
            tutor2.render()
        if tutor_step == 22:
            tutorial_text("Здесь ты можешь","продолжить строить","Чертоги разума.")
            New_Mind_Palace.render()
            Continue_Mind_Palace.render()
            Tutorial.render()
            Quit_Menu2.render()
            tutor.render()
        if tutor_step == 23:
            tutorial_text("","","")
            Continue_Mind_Palace = Sprite(80,120,'Files/Textures/Menu/Continue_Mind_Palace.png',0,0,0)
            tutor_step+=1
        if tutor_step == 24:
            New_Mind_Palace.render()
            Continue_Mind_Palace.render()
            Tutorial.render()
            Quit_Menu2.render()
            tutor2.render()

        if tutor_step == 25:
            Tutorial = Sprite(80,120,'Files/Textures/Menu/Tutorial_Selected.png',0,0,0)
            tutor_step+=1
        if tutor_step == 26:
            New_Mind_Palace.render()
            Continue_Mind_Palace.render()
            Tutorial.render()
            Quit_Menu2.render()
            tutor2.render()
        if tutor_step == 27:
            tutorial_text("Здесь можно посмотреть","это обучение если","что-то забудешь ;)")
            New_Mind_Palace.render()
            Continue_Mind_Palace.render()
            Tutorial.render()
            Quit_Menu2.render()
            tutor.render()

        if tutor_step == 28:
            Tutorial = Sprite(80,120,'Files/Textures/Menu/Tutorial.png',0,0,0)
            tutor_step+=1
        if tutor_step == 29:
            tutorial_text("","","")
            New_Mind_Palace.render()
            Continue_Mind_Palace.render()
            Tutorial.render()
            Quit_Menu2.render()
            tutor2.render()
        if tutor_step == 30:
            tutorial_text("Ну что,","готов узнать, как","помнить все?")
            New_Mind_Palace.render()
            Continue_Mind_Palace.render()
            Tutorial.render()
            Quit_Menu2.render()
            tutor.render()
        if tutor_step == 31:
            New_Mind_Palace = Sprite(80,120,'Files/Textures/Menu/New_Mind_Palace_Selected.png',0,0,0)
            tutor_step+=1
        if tutor_step == 32:
            tutorial_text("","               Поехали!", "")
            New_Mind_Palace.render()
            Continue_Mind_Palace.render()
            Tutorial.render()
            Quit_Menu2.render()
            tutor.render()
        if tutor_step == 33:
            tutorial_text("","", "")
            slot1.render()
            slot2.render()
            slot3.render()
            Quit_Slots.render()
            tutor2.render()
        if tutor_step == 34:
            tutorial_text("Создаем новые ","чертоги и сохраняем", "в 1 слоте.")
            slot1.render()
            slot2.render()
            slot3.render()
            Quit_Slots.render()
            tutor.render()
        if tutor_step == 35:
            tutorial_text("","","")
            slot1 = Sprite(-390,-240,'Files/Textures/Menu/mslot1_Selected.png',0,0,0)
            tutor_step+=1
        if tutor_step == 36:
            slot1.render()
            slot2.render()
            slot3.render()
            Quit_Slots.render()
            tutor2.render()
            
        if tutor_step == 37:
            tutor.render()
            global n
            n = 0
            main_theme_1.stop()
            main_theme_2.stop()
            tutor_step+=1

        if tutor_step == 38:
            global text_x
            tutorial_text("", "Вот мы и на месте!","")
            text_x = 120
            tutor3.render()
        if tutor_step == 39:
            tutorial_text("Управляй персонажем","с помощью","WASD.")
            tutor3.render()
        if tutor_step == 40:
            tutorial_text("Предлагаю осмотреться!", "Пройдись по тропе и", "запомни все по пути!")
            tutor3.render()
        if tutor_step == 41:
            tutorial_text("Когда закончишь, ", "Нажми ЛКМ и","мы продолжим.")
            tutor3.render()
        if tutor_step == 42:
            tutorial_text("","","")
        if tutor_step == 43:
            tutorial_text("Закончил осмотр?","Все запомнил?", ":)")
            tutor3.render()
        if tutor_step == 44:
            tutorial_text("Думаю это было легко", "запомнить, ведь это - ", "классическая история!")
            tutor3.render()
        if tutor_step == 45:
            tutorial_text("Рыцарь узнает о том", "что злой дракон заточил", "в замке принцессу.")
            tutor3.render()
        if tutor_step == 46:
            tutorial_text("По пути к принцессе","рыцарь преодолевает","испытания.")
            tutor3.render()
        if tutor_step == 47:
            tutorial_text("Они и есть - ", "наш ключ.", "")
            tutor3.render()
        if tutor_step == 48:
            tutorial_text("Давай возьмем образы", "из этого места чтобы", "запомнить любое число.")
            tutor3.render()
        if tutor_step == 49:
            tutorial_text("Все просто: ", "0 - рыцарь", "1 - его лощадь.")
            tutor3.render()
        if tutor_step == 50:
            tutorial_text("2 - таверна, где он взял", "еду в путь.","")
            tutor3.render()
        if tutor_step == 51:
            tutorial_text("3 - лавовое озеро", "на подступах к", "замку дракона!")
            tutor3.render()
        if tutor_step == 52:
            tutorial_text("","4 - сам дракон!","")
            tutor3.render()
        if tutor_step == 53:
            tutorial_text("","5 - его замок.","")
            tutor3.render()
        if tutor_step == 54:
            tutorial_text("","6 - принцесса.","")
            tutor3.render()
        if tutor_step == 55:
            tutorial_text("", "7 - золото дракона", "")
            tutor3.render()
        if tutor_step == 56:
            tutorial_text("", "8 - хвойный лес на", "обратном пути.")
            tutor3.render()
        if tutor_step == 57:
            tutorial_text("","9 - дом рыцаря","")
            tutor3.render()
        if tutor_step == 58:
            tutorial_text("","Вот и все!","")
            tutor3.render()
        if tutor_step == 59:
            tutorial_text("Теперь мы будем","запоминать не сухие","цифры, а")
            tutor3.render()
        if tutor_step == 60:
            tutorial_text("красочные образы","связанные друг с другом","крепкой связью.")
            tutor3.render()
        if tutor_step == 61:
            tutorial_text("Теперь расположи","образы в порядке","числа Пи.")
            tutor3.render()
        if tutor_step == 62:
            tutorial_text("","Или телефонного номера.","")
            tutor3.render()
        if tutor_step == 63:
            tutorial_text("","Или пароля.","")
            tutor3.render()
        if tutor_step == 64:
            tutorial_text("А ещё ключ может","представлять буквы!","Или целые слова!")
            tutor3.render()
        if tutor_step == 65:
            tutorial_text("","Простор неограничен!","")
            tutor3.render()
        if tutor_step == 66:
            tutorial_text("Строй свои","Чертоги Разума!","")
            tutor3.render()
        if tutor_step == 67:
            tutorial_text("А эта программа", "поможет тебе на","первых порах!")
            tutor3.render()
        if tutor_step == 68:
            tutorial_text("Располагай образы (ЛКМ)", "выбирая их из", "инвентаря (E)")
            tutor3.render()
            global inv
            inv = 1
        if tutor_step == 69:
            tutorial_text("Или удаляй (ПКМ)","","")
            tutor3.render()
            inv = 0
        if tutor_step == 70:
            tutorial_text("Не забывай", "сохранять чертоги!","")
            tutor3.render()
        if tutor_step == 71:
            tutorial_text("Ну вроде как все :)", "Помнить место - ", "помнить информацию.")
            tutor3.render()
        if tutor_step == 72:
            tutorial_text("","Приятного тебе","дня! Увидимся!")
            tutor3.render()
        if tutor_step == 73:
            tutorial_text("","","")
            n = 1
            global menu_type
            global tutor_on
            menu_type = 1
            tutor_step = 1
            tutor_on = 0
            tutor_begin = 1
            start_music()
            
def menu_render():
    background0.render()
    background1.render()
    background2.render()
    background3.render()
    background4.render()
    background5.render()
    background6.render()
    
    if menu_type == 1:
        To_Mind_Palace.render()
        Learn.render()
        Profile.render()
        Settings.render()
        Exit.render()
    if menu_type == 2:
        New_Mind_Palace.render()
        Continue_Mind_Palace.render()
        Tutorial.render()
        Quit_Menu2.render()
    if menu_type == 3:
        slot1.render()
        slot2.render()
        slot3.render()
        Quit_Slots.render()
    if menu_type == 4:
        slot1.render()
        slot2.render()
        slot3.render()
        Quit_Slots.render()
    if menu_type == 5:
        tutor_render()
    if menu_type == 6:
        dev.render()
    if menu_type == 7:
        l.render()
    if menu_type == 8:
        sett.render()
        sett_1.render()
        sett_2.render()
        sett_3.render()
        sett_4.render()
            
            
#Тут должно производиться считывание с файла и добавление объектов в RAM (массив)
pygame.key.set_repeat(1,1)

try:
    load_file = open('Files/Saves/new.dat', 'rb')
    new = pickle.load(load_file)
    load_file.close()
except:
    print('При считывании файла new.dat возникла ошибка.')
    print('Инициализирую повторное создание...')
    save_file = open('Files/Saves/new.dat','wb')
    new = 1
    pickle.dump(new, save_file)
    save_file.close()
    print('Файл new.dat был успешно восстановлен.')
    
try:
    load_file = open('Files/Saves/save1.dat', 'rb')
    all_objects = pickle.load(load_file)
    load_file.close()
except:
    print('При считывании файла сохранения №1 возникла ошибка.')
    print('Инициализирую повторное создание...')
    save_file = open('Files/Saves/save1.dat','wb')
    all_objects = []
    all_objects.append(['empty','0','0','Files/Textures/Objects/empty.png','0','0','0'])
    
    
    pickle.dump(all_objects, save_file)
    save_file.close()
    print('Файл #1 был успешно восстановлен.')
    all_objects = []

try:
    load_file = open('Files/Saves/save2.dat', 'rb')
    all_objects = pickle.load(load_file)
    load_file.close()
except:
    print('При считывании файла сохранения №2 возникла ошибка.')
    print('Инициализирую повторное создание...')
    save_file = open('Files/Saves/save2.dat','wb')
    all_objects = []
    all_objects.append(['empty','0','0','Files/Textures/Objects/empty.png','0','0','0'])
    
    
    pickle.dump(all_objects, save_file)
    save_file.close()
    print('Файл #2 был успешно восстановлен.')
    all_objects = []

try:
    load_file = open('Files/Saves/save3.dat', 'rb')
    all_objects = pickle.load(load_file)
    load_file.close()
except:
    print('При считывании файла сохранения №3 возникла ошибка.')
    print('Инициализирую повторное создание...')
    save_file = open('Files/Saves/save3.dat','wb')
    all_objects = []
    all_objects.append(['empty','0','0','Files/Textures/Objects/empty.png','0','0','0'])
    
    
    pickle.dump(all_objects, save_file)
    save_file.close()
    print('Файл #3 был успешно восстановлен.')
    all_objects = []

    
    #for i in range(0,len(all_objects)):
        #exec(all_objects[i][0] + '= Sprite(' + all_objects[i][1] + ',' + all_objects[i][2] + ',"' + all_objects[i][3] + '",' + all_objects[i][4] + ',' + all_objects[i][5] + ',' + all_objects[i][6] + ')')
#all_objects = []

#all_objects.append(['grass','-250','-250','Files/Textures/Objects/grass.png','0','0','0'])
#all_objects[0] = ['grass','-250','-250','Files/Textures/Objects/grass.png','320','320','0']

#tree1 = Sprite(350,120,'Files/Textures/tree1.png')

#Функция, выдающая самый ближайший сверху элемент (номер в массиве)
        

#Главный персонаж

hero_stay_down = Sprite(480,220,'Files/Textures/Hero/hero_stay_down.png',0,0,0)

hero_go1_down = Sprite(480,220,'Files/Textures/Hero/hero_go1_down.png',0,0,0)
hero_go2_down = Sprite(480,220,'Files/Textures/Hero/hero_go2_down.png',0,0,0)
hero_go3_down = Sprite(480,220,'Files/Textures/Hero/hero_go3_down.png',0,0,0)
hero_go4_down = Sprite(480,220,'Files/Textures/Hero/hero_go4_down.png',0,0,0)

hero_go1_down.y =5000
hero_go2_down.y =5000
hero_go3_down.y =5000
hero_go4_down.y =5000

#---

go_up_stay = Sprite(480,220,'Files/Textures/Hero/go_up_stay.png',0,0,0)

hero_go_up_1 = Sprite(480,220,'Files/Textures/Hero/go_up_1.png',0,0,0)
hero_go_up_2 = Sprite(480,220,'Files/Textures/Hero/go_up_2.png',0,0,0)
hero_go_up_3 = Sprite(480,220,'Files/Textures/Hero/go_up_3.png',0,0,0)
hero_go_up_4 = Sprite(480,220,'Files/Textures/Hero/go_up_4.png',0,0,0)

hero_go_up_1.y = 5000
hero_go_up_2.y = 5000
hero_go_up_3.y = 5000
hero_go_up_4.y = 5000

#---

hero_left_stay = Sprite(480,220,'Files/Textures/Hero/go_left_stay.png',0,0,0)

hero_go_left1 = Sprite(480,220,'Files/Textures/Hero/go_left1.png',0,0,0)
hero_go_left2 = Sprite(480,220,'Files/Textures/Hero/go_left2.png',0,0,0)

hero_go_left1.y = 5000
hero_go_left2.y = 5000


hero_right_stay = Sprite(480,220,'Files/Textures/Hero/go_right_stay.png',0,0,0)

hero_go_right1 = Sprite(480,220,'Files/Textures/Hero/go_right1.png',0,0,0)
hero_go_right2 = Sprite(480,220,'Files/Textures/Hero/go_right2.png',0,0,0)

hero_go_right1.y = 5000
hero_go_right2.y = 5000



step = 0
step_type = 'down'

def define_step():
    global hero_step

hs = 25
hero_step =[0,hs,hs*2,hs*3,hs*4]


def hero_anim():
    global step
    global step_type
    global hero_step
    hero_step =[0,hs,hs*2,hs*3,hs*4]
    if step_type == 'down':
        if step>hero_step[0] and step<hero_step[1]:
            hero_stay_down.y = 5000
            hero_go1_down.y =220
            hero_go2_down.y =5000
            hero_go3_down.y =5000
            hero_go4_down.y =5000
        if step>=hero_step[1] and step<hero_step[2]:
            hero_stay_down.y = 5000
            hero_go1_down.y =5000
            hero_go2_down.y =220
            hero_go3_down.y =5000
            hero_go4_down.y =5000
        if step>=hero_step[2] and step<hero_step[3]:
            hero_stay_down.y = 5000
            hero_go1_down.y =5000
            hero_go2_down.y =5000
            hero_go3_down.y =220
            hero_go4_down.y =5000
        if step>=hero_step[3] and step<hero_step[4]:
            hero_stay_down.y = 5000
            hero_go1_down.y =5000
            hero_go2_down.y =5000
            hero_go3_down.y =5000
            hero_go4_down.y =220
        if step>=hero_step[4]:
            step = 0

        ###
    if step_type == 'left':
        #print(step)
        if step>hero_step[0] and step<hero_step[1]:
            hero_left_stay.y = 5000
            hero_go_left1.y = 220
            hero_go_left2.y = 5000
        if step>hero_step[1] and step<hero_step[2]:
            hero_left_stay.y = 5000
            hero_go_left1.y = 5000
            hero_go_left2.y = 220
        if step>=hero_step[2]:
            step = 0    

    if step_type == 'right':
            #print(step)
            if step>hero_step[0] and step<hero_step[1]:
                hero_right_stay.y = 5000
                hero_go_right1.y = 220
                hero_go_right2.y = 5000
            if step>hero_step[1] and step<hero_step[2]:
                hero_right_stay.y = 5000
                hero_go_right1.y = 5000
                hero_go_right2.y = 220
            if step>=hero_step[2]:
                step = 0

    if step_type == 'up':
        if step>hero_step[0] and step<hero_step[1]:
            go_up_stay.y = 5000
            hero_go_up_1.y =220
            hero_go_up_2.y =5000
            hero_go_up_3.y =5000
            hero_go_up_4.y =5000
        if step>=hero_step[1] and step<hero_step[2]:
            go_up_stay.y = 5000
            hero_go_up_1.y =5000
            hero_go_up_2.y =220
            hero_go_up_3.y =5000
            hero_go_up_4.y =5000
        if step>=hero_step[2] and step<hero_step[3]:
            go_up_stay.y = 5000
            hero_go_up_1.y =5000
            hero_go_up_2.y =5000
            hero_go_up_3.y = 220
            hero_go_up_4.y =5000
        if step>=hero_step[3] and step<hero_step[4]:
            go_up_stay.y = 5000
            hero_go_up_1.y =5000
            hero_go_up_2.y =5000
            hero_go_up_3.y =5000
            hero_go_up_4.y =220
        if step>=hero_step[4]:
            step = 0

def hero_render():
    if step_type == 'down':
        hero_stay_down.render()
        hero_go1_down.render()
        hero_go2_down.render()
        hero_go3_down.render()
        hero_go4_down.render()
    if step_type == 'left':
        hero_left_stay.render()
        hero_go_left1.render()
        hero_go_left2.render()
    if step_type == 'right':
        hero_right_stay.render()
        hero_go_right1.render()
        hero_go_right2.render()
    if step_type == 'up':
            go_up_stay.render()
            hero_go_up_1.render()
            hero_go_up_2.render()
            hero_go_up_3.render()
            hero_go_up_4.render()
    ###

#Инициализирование (не добавление) всех объектов из массива (которые уже отсортированы)
#на игровое поле

#Спрайтинг
#for i in range(0,len(all_objects)):
    #exec(all_objects[i][0] + '= Sprite(' + all_objects[i][1] + ',' + all_objects[i][2] + ',"' + all_objects[i][3] + '",' + all_objects[i][4] + ',' + all_objects[i][5] + ',' + all_objects[i][6] + ')')

#def addnew():
   ## i = len(all_objects)
   # all_objects.append(('tree2','10','10','Files/Textures/tree1.png'))
   # exec(all_objects[i][0] + '= Sprite(' + all_objects[i][1] + ',' + all_objects[i][2] + ',"' + all_objects[i][3] + '")')

#addnew()
#Создание главного игрового цикла

Running = True

inv_step = 0
pygame.key.set_repeat(1,1)
#Функция для удаления объекта
def release(x,y,obj):
    if x>=obj.x and x<=(obj.x+obj.width) and y>=obj.y and y<=(obj.y + obj.height):
        return True
    else:
        return False

#Скорость персонажа
speed = 3

#Выход
quit_step = 0

#Красная
sure = 0

#Начать дворец
begin = 0

#
gamemenu_step = 0

#
Select_To_Mind_Palace = 0
Select_Profile = 0
Select_Settings = 0
Select_Learning = 0
Select_Quit = 0

New_Mind_Palace_Selected=0
Continue_Mind_Palace_Selected=0
Tutorial_Selected=0
Quit_Menu2_Selected=0

slot1_Selected=0
slot2_Selected=0
slot3_Selected = 0
Quit_Slots_Selected = 0
dev_Selected=0
l_Selected=0
Select_Learn = 0
sett_Selected = 0
Game_Quit_Selected=0
Game_Play_Selected = 0
Game_Save_Selected = 0

sure_save = 0

while Running:
    if n == 0:
        if play_background == 1:
            print('p')
            play_background=0
            Background.play(-1)
            print('PLAY')
    if n == 1:
        if play_background == 0:
            play_background=1
            print(time.time())
            Background.stop()
    
    if tutor_on == 1:
        if tutor_begin == 0:
            load_file = open('Files/Saves/tutorial.dat', 'rb')
                    
            all_objects = pickle.load(load_file)
            load_file.close()
            tutor_step+=1
            tutor_begin = 1
            for i in range(0,len(all_objects)):
                exec(all_objects[i][0] + '= Sprite(' + all_objects[i][1] + ',' + all_objects[i][2] + ',"' + all_objects[i][3] + '",' + all_objects[i][4] + ',' + all_objects[i][5] + ',' + all_objects[i][6] + ')')
   #if tutor_on == 1:
        ###tutor_render()

    if clock.get_fps()>=0 and clock.get_fps()<15:
        hs = 2
        speed = 12
    if clock.get_fps()>=15 and clock.get_fps()<25:
        hs = 4
        speed = 9      
    if clock.get_fps()>=25 and clock.get_fps()<35:
        hs = 6
        speed = 8
    if clock.get_fps()>=35 and clock.get_fps()<45:
        hs = 7
        speed = 6
    if clock.get_fps()>=45 and clock.get_fps()<55:
        hs = 10
        speed = 5   
    if clock.get_fps()>=55 and clock.get_fps()<65:
        hs = 10
        speed = 4 
    if clock.get_fps()>=65 and clock.get_fps()<75:
        hs = 13
        speed = 3
    if clock.get_fps()>=75 and clock.get_fps()<85:
        hs = 15
        speed = 3
    if clock.get_fps()>=85 and clock.get_fps()<95:
        hs = 17
        speed = 3
    if clock.get_fps()>=95 and clock.get_fps()<105:
        hs = 25
        speed = 2
    if clock.get_fps()>=105 and clock.get_fps()<125:
        hs = 20
        speed = 2
    if n==1:
        menu_anim()
    
    #pygame.display.set_caption("fps: " + str(clock.get_fps()))
    screen.fill((50,50,50))
    #Цикл событий
    for e in pygame.event.get():
        #Поиск среди событий клика на крестик выхода
        if e.type == pygame.QUIT:
            Running = False
        #if e.type==pygame.KEYDOWN:
            #if e.key==pygame.K_ESCAPE:
                #n = 1

        #Поиск среди всех событий движение мыши
        #Меню и мышка
        #if n == 0:
            #if e.type == pygame.MOUSEBUTTONDOWN:
                #if e.button == 1:
                    #print(pygame.mouse.get_pos())
                    #pygame.display.set_mode((1100,600),pygame.FULLSCREEN)

        
        if n==1:
            
            if menu_type == 1:
                ms = 6
                ma = [0,ms,ms*2,ms*3,ms*4,ms*5,ms*6,ms*7]
            if menu_type == 2:
                ms = 4
                ma = [0,ms,ms*2,ms*3,ms*4,ms*5,ms*6,ms*7]
            if menu_type == 3:
                ms = 3
                ma = [0,ms,ms*2,ms*3,ms*4,ms*5,ms*6,ms*7]
            if menu_type == 1:
                if e.type == pygame.MOUSEMOTION:
                    if pygame.mouse.get_pos()[0]>=233 and pygame.mouse.get_pos()[0]<=771 and pygame.mouse.get_pos()[1]>=135 and pygame.mouse.get_pos()[1]<=304:
                        Select_To_Mind_Palace += 1
                        if Select_To_Mind_Palace == 1:
                            To_Mind_Palace = Sprite(200,120,'Files/Textures/Menu/To_Mind_Palace_Selected.png',0,0,0)
                            Select_Sound.play()
                    else:
                        Select_To_Mind_Palace = 0
                        To_Mind_Palace = Sprite(200,120,'Files/Textures/Menu/To_Mind_Palace.png',0,0,0)
                    if pygame.mouse.get_pos()[0]>=232 and pygame.mouse.get_pos()[0]<=398 and pygame.mouse.get_pos()[1]>=326 and pygame.mouse.get_pos()[1]<=490:
                        Select_Profile +=1
                        if Select_Profile == 1:
                            Select_Sound.play()
                            Profile = Sprite(190,308,'Files/Textures/Menu/Profile_Selected.png',0,0,0)
                    else:
                        Select_Profile = 0
                        Profile = Sprite(190,308,'Files/Textures/Menu/Profile.png',0,0,0)

                    if pygame.mouse.get_pos()[0]>=418 and pygame.mouse.get_pos()[0]<=583 and pygame.mouse.get_pos()[1]>=324 and pygame.mouse.get_pos()[1]<=488:
                        Select_Settings+=1
                        if Select_Settings==1:
                            Select_Sound.play()
                            Settings = Sprite(390,306,'Files/Textures/Menu/Settings_Selected.png',0,0,0)
                    else:
                        Select_Settings=0
                        Settings = Sprite(390,306,'Files/Textures/Menu/Settings.png',0,0,0)
                        
                    if pygame.mouse.get_pos()[0]>=788 and pygame.mouse.get_pos()[0]<=971 and pygame.mouse.get_pos()[1]>=135 and pygame.mouse.get_pos()[1]<=488:
                        Select_Learn+=1
                        if Select_Learn==1:
                            Select_Sound.play()
                            Learn = Sprite(780,15,'Files/Textures/Menu/Learn_Selected.png',0,0,0)
                    else:
                        Select_Learn = 0
                        Learn = Sprite(780,15,'Files/Textures/Menu/Learn.png',0,0,0)

                    if pygame.mouse.get_pos()[0]>=603 and pygame.mouse.get_pos()[0]<=768 and pygame.mouse.get_pos()[1]>=326 and pygame.mouse.get_pos()[1]<=488:
                        Select_Quit +=1
                        if Select_Quit==1:
                            Select_Sound.play()
                        ###_HERE_###
                        if quit_step == 0:
                            Exit = Sprite(583,308,'Files/Textures/Menu/Exit_Selected.png',0,0,0)
                        if quit_step == 1:
                            Exit = Sprite(583,308,'Files/Textures/Menu/Exit_Sure.png',0,0,0)
                    else:
                        Select_Quit=0
                        Exit = Sprite(583,308,'Files/Textures/Menu/Exit.png',0,0,0)
                        quit_step = 0
                        
                if e.type == pygame.MOUSEBUTTONDOWN and menu_access == 1:
                    if pygame.mouse.get_pos()[0]>=233 and pygame.mouse.get_pos()[0]<=771 and pygame.mouse.get_pos()[1]>=135 and pygame.mouse.get_pos()[1]<=304:
                        Click_Sound.play()
                        menu_type = 2
                        menu_access-=1
                        #n = 0
                    if pygame.mouse.get_pos()[0]>=232 and pygame.mouse.get_pos()[0]<=398 and pygame.mouse.get_pos()[1]>=326 and pygame.mouse.get_pos()[1]<=490:
                        Click_Sound.play()
                        menu_type = 6
                        f1 = pygame.font.Font('Files/Font/GEO.ttf', 36)
                        text1 = f1.render('Автор', 1, (255, 255, 255))

                        f2 = pygame.font.Font('Files/Font/GEO.ttf', 36)
                        text2 = f2.render('Устименко Даниил Игоревич', 1, (255, 255, 255))

                        f3 = pygame.font.Font('Files/Font/GEO.ttf', 36)
                        text3 = f3.render('Связь со мной: +79631685941', 1, (255, 255,255))
                        
                        f4 = pygame.font.Font('Files/Font/GEO.ttf', 36)
                        text4 = f4.render('Почта: daniilustimencko@yandex.ru', 1, (255, 255,255))
                        f5 = pygame.font.Font('Files/Font/GEO.ttf', 36)
                        text5 = f5.render('Вконтакте: vk.com/mrriseyt', 1, (255, 255,255))

                        menu_access-=1
                    if pygame.mouse.get_pos()[0]>=603 and pygame.mouse.get_pos()[0]<=768 and pygame.mouse.get_pos()[1]>=326 and pygame.mouse.get_pos()[1]<=488:
                        Click_Sound.play()
                        quit_step+=1
                        Exit = Sprite(583,308,'Files/Textures/Menu/Exit_Sure.png',0,0,0)
                        if quit_step == 2:
                            Running = False

                    if pygame.mouse.get_pos()[0]>=788 and pygame.mouse.get_pos()[0]<=971 and pygame.mouse.get_pos()[1]>=135 and pygame.mouse.get_pos()[1]<=488:
                        Click_Sound.play()
                        menu_type = 7
                        menu_access-=1
                    if pygame.mouse.get_pos()[0]>=418 and pygame.mouse.get_pos()[0]<=583 and pygame.mouse.get_pos()[1]>=324 and pygame.mouse.get_pos()[1]<=488:
                        Click_Sound.play()
                        menu_type = 8
                        menu_access-=1



            if menu_type == 8:
                '''
                    (714, 42)
                    (917, 107)
                    (714, 143)
                    (916, 208)
                    (712, 242)
                    (916, 306)
                    (713, 344)
                    (915, 409)
                    (155, 449)
                    (970, 580)
                '''
                if e.type == pygame.MOUSEMOTION:
                    if pygame.mouse.get_pos()[0]>=155 and pygame.mouse.get_pos()[0]<=970 and pygame.mouse.get_pos()[1]>=450 and pygame.mouse.get_pos()[1]<=580:
                        sett_Selected+=1
                        if sett_Selected==1:
                            Select_Sound.play()
                            sett = Sprite(80,-200,'Files/Textures/Menu/sett_quit.png',0,0,0)
                    else:
                        sett_Selected = 0
                        sett = Sprite(80,-200,'Files/Textures/Menu/sett.png',0,0,0)
                        
                if e.type == pygame.MOUSEBUTTONDOWN and menu_access == 1:
                    if pygame.mouse.get_pos()[0]>=155 and pygame.mouse.get_pos()[0]<=970 and pygame.mouse.get_pos()[1]>=450 and pygame.mouse.get_pos()[1]<=580:
                        Click_Sound.play()
                        menu_type = 1
                        menu_access-=1
                        print('Сохранение параметров...')
                        save_file = open('Files/Saves/sett_param.dat','wb')
                        print(sett_param)
                        pickle.dump(sett_param, save_file)
                        print('Файл sett_param.dat был успешно сохранен.')
                        save_file.close()

                    if pygame.mouse.get_pos()[0]>=714 and pygame.mouse.get_pos()[0]<=815 and pygame.mouse.get_pos()[1]>=42 and pygame.mouse.get_pos()[1]<=107:
                        sett_param[0] = 0
                        Click_Sound = pygame.mixer.Sound('Files/Soundtrack/silent.ogg')
                        Click_Sound.set_volume(1)
                        Select_Sound = pygame.mixer.Sound('Files/Soundtrack/silent.ogg')
                        Select_Sound.set_volume(1)
                        sett_1 = Sprite(80,-200,'Files/Textures/Menu/sett_1_off.png',0,0,0)
                    if pygame.mouse.get_pos()[0]>=816 and pygame.mouse.get_pos()[0]<=917 and pygame.mouse.get_pos()[1]>=42 and pygame.mouse.get_pos()[1]<=107:
                        sett_param[0] = 1
                        Click_Sound = pygame.mixer.Sound('Files/Soundtrack/Click_Sound.ogg')
                        Click_Sound.set_volume(1)
                        Select_Sound = pygame.mixer.Sound('Files/Soundtrack/Select_Sound.ogg')
                        Select_Sound.set_volume(1)
                        sett_1 = Sprite(80,-200,'Files/Textures/Menu/sett_1_on.png',0,0,0)

                    if pygame.mouse.get_pos()[0]>=714 and pygame.mouse.get_pos()[0]<=815 and pygame.mouse.get_pos()[1]>=143 and pygame.mouse.get_pos()[1]<=208:
                        sett_param[1] = 0
                        main_theme_1.stop()
                        main_theme_2.stop()
                        main_theme_1 = pygame.mixer.Sound('Files/Soundtrack/silent.ogg')
                        main_theme_1.set_volume(0.5)

                        main_theme_2 = pygame.mixer.Sound('Files/Soundtrack/silent.ogg')
                        main_theme_2.set_volume(0.3)

                        

                        sett_2 = Sprite(80,-200,'Files/Textures/Menu/sett_2_off.png',0,0,0)
                    if pygame.mouse.get_pos()[0]>=816 and pygame.mouse.get_pos()[0]<=917 and pygame.mouse.get_pos()[1]>=143 and pygame.mouse.get_pos()[1]<=208:
                        sett_param[1] = 1
                        main_theme_1 = pygame.mixer.Sound('Files/Soundtrack/main_theme_1.ogg')
                        main_theme_1.set_volume(0.5)

                        main_theme_2 = pygame.mixer.Sound('Files/Soundtrack/main_theme_2.ogg')
                        main_theme_2.set_volume(0.3)

                        sett_2 = Sprite(80,-200,'Files/Textures/Menu/sett_2_on.png',0,0,0)

                        start_music()

                    
                    if pygame.mouse.get_pos()[0]>=714 and pygame.mouse.get_pos()[0]<=815 and pygame.mouse.get_pos()[1]>=242 and pygame.mouse.get_pos()[1]<=306:
                        sett_param[2] = 0
                        walk_sound = pygame.mixer.Sound('Files/Soundtrack/silent.ogg')
                        sett_3 = Sprite(80,-200,'Files/Textures/Menu/sett_3_off.png',0,0,0)
                    if pygame.mouse.get_pos()[0]>=816 and pygame.mouse.get_pos()[0]<=917 and pygame.mouse.get_pos()[1]>=242 and pygame.mouse.get_pos()[1]<=306:
                        sett_param[2] = 1
                        walk_sound = pygame.mixer.Sound('Files/Soundtrack/walk.ogg')
                        walk_sound.set_volume(1)
                        sett_3 = Sprite(80,-200,'Files/Textures/Menu/sett_3_on.png',0,0,0)


                    if pygame.mouse.get_pos()[0]>=714 and pygame.mouse.get_pos()[0]<=815 and pygame.mouse.get_pos()[1]>=344 and pygame.mouse.get_pos()[1]<=409:
                        sett_param[3] = 0
                        Background = pygame.mixer.Sound('Files/Soundtrack/silent.ogg')
                        Background.set_volume(1)
                        sett_4 = Sprite(80,-200,'Files/Textures/Menu/sett_4_off.png',0,0,0)                       
                        
                    if pygame.mouse.get_pos()[0]>=816 and pygame.mouse.get_pos()[0]<=917 and pygame.mouse.get_pos()[1]>=344 and pygame.mouse.get_pos()[1]<=409:
                        sett_param[3] = 1
                        Background = pygame.mixer.Sound('Files/Soundtrack/Background.ogg')
                        Background.set_volume(1)
                        sett_4 = Sprite(80,-200,'Files/Textures/Menu/sett_4_on.png',0,0,0) 
                        
                
            if menu_type == 6:
                if e.type == pygame.MOUSEMOTION:
                    if pygame.mouse.get_pos()[0]>=152 and pygame.mouse.get_pos()[0]<=968 and pygame.mouse.get_pos()[1]>=456 and pygame.mouse.get_pos()[1]<=583:
                            dev_Selected+=1
                            if dev_Selected==1:
                                Select_Sound.play()
                                dev = Sprite(100,-370,'Files/Textures/Menu/dev_Selected.png',0,0,0)
                    else:
                            dev_Selected=0
                            dev = Sprite(100,-370,'Files/Textures/Menu/dev.png',0,0,0)
                        
                if e.type == pygame.MOUSEBUTTONDOWN and menu_access == 1:
                    if pygame.mouse.get_pos()[0]>=152 and pygame.mouse.get_pos()[0]<=968 and pygame.mouse.get_pos()[1]>=456 and pygame.mouse.get_pos()[1]<=583:
                        Click_Sound.play()
                        menu_access-=1
                        menu_type = 1


            if menu_type == 7:
                if e.type == pygame.MOUSEMOTION:
                    if pygame.mouse.get_pos()[0]>=152 and pygame.mouse.get_pos()[0]<=968 and pygame.mouse.get_pos()[1]>=456 and pygame.mouse.get_pos()[1]<=583:
                            l_Selected+=1
                            if l_Selected==1:
                                Select_Sound.play()
                                l = Sprite(100,-370,'Files/Textures/Menu/l_selected.png',0,0,0)
                    else:
                            l_Selected=0
                            l = Sprite(100,-370,'Files/Textures/Menu/l.png',0,0,0)
                        
                if e.type == pygame.MOUSEBUTTONDOWN and menu_access == 1:
                    if pygame.mouse.get_pos()[0]>=152 and pygame.mouse.get_pos()[0]<=968 and pygame.mouse.get_pos()[1]>=456 and pygame.mouse.get_pos()[1]<=583:
                        Click_Sound.play()
                        menu_access-=1
                        menu_type = 1




                        
            if menu_type == 2:
                if pygame.mouse.get_pos()[0]>=274 and pygame.mouse.get_pos()[0]<=456 and pygame.mouse.get_pos()[1]>=146 and pygame.mouse.get_pos()[1]<=503:
                     New_Mind_Palace_Selected+=1
                     if New_Mind_Palace_Selected==1:
                         Select_Sound.play()
                         New_Mind_Palace = Sprite(80,120,'Files/Textures/Menu/New_Mind_Palace_Selected.png',0,0,0)
                else:
                    New_Mind_Palace_Selected = 0
                    New_Mind_Palace = Sprite(80,120,'Files/Textures/Menu/New_Mind_Palace.png',0,0,0)
                if e.type == pygame.MOUSEBUTTONDOWN and menu_access == 1:
                    if pygame.mouse.get_pos()[0]>=274 and pygame.mouse.get_pos()[0]<=456 and pygame.mouse.get_pos()[1]>=146 and pygame.mouse.get_pos()[1]<=503:
                        Click_Sound.play()
                        menu_type = 3
                        menu_access-=1
        
                if pygame.mouse.get_pos()[0]>=472 and pygame.mouse.get_pos()[0]<=822 and pygame.mouse.get_pos()[1]>=148 and pygame.mouse.get_pos()[1]<=315:
                    Continue_Mind_Palace_Selected+=1
                    if Continue_Mind_Palace_Selected==1:
                        Select_Sound.play()
                        Continue_Mind_Palace = Sprite(80,120,'Files/Textures/Menu/Continue_Mind_Palace_Selected.png',0,0,0)
                else:
                    Continue_Mind_Palace_Selected=0
                    Continue_Mind_Palace = Sprite(80,120,'Files/Textures/Menu/Continue_Mind_Palace.png',0,0,0)
                if pygame.mouse.get_pos()[0]>=659 and pygame.mouse.get_pos()[0]<=825 and pygame.mouse.get_pos()[1]>=339 and pygame.mouse.get_pos()[1]<=498:
                    Quit_Menu2_Selected+=1
                    if Quit_Menu2_Selected==1:
                        Select_Sound.play()
                        Quit_Menu2 = Sprite(88,120,'Files/Textures/Menu/Quit_Menu2_Selected.png',0,0,0)
                else:
                    Quit_Menu2_Selected = 0
                    Quit_Menu2 = Sprite(88,120,'Files/Textures/Menu/Quit_Menu2.png',0,0,0)

                if pygame.mouse.get_pos()[0]>=470 and pygame.mouse.get_pos()[0]<=633 and pygame.mouse.get_pos()[1]>=337 and pygame.mouse.get_pos()[1]<=498:
                    Tutorial_Selected+=1
                    if Tutorial_Selected==1:
                        Select_Sound.play()
                    Tutorial = Sprite(80,120,'Files/Textures/Menu/Tutorial_Selected.png',0,0,0)
                else:
                    Tutorial_Selected=0
                    Tutorial = Sprite(80,120,'Files/Textures/Menu/Tutorial.png',0,0,0)

                if e.type == pygame.MOUSEBUTTONDOWN and menu_access == 1:
                    print(pygame.mouse.get_pos())
                    if pygame.mouse.get_pos()[0]>=470 and pygame.mouse.get_pos()[0]<=633 and pygame.mouse.get_pos()[1]>=337 and pygame.mouse.get_pos()[1]<=498:
                        Click_Sound.play()
                        menu_access-=1
                        menu_type = 5
                        Tutorial = Sprite(80,120,'Files/Textures/Menu/Tutorial.png',0,0,0)
                        tutor_on = 1
                        tutor_step = 0
                        tutor_begin = 0###
                        text_x = 390
                    if pygame.mouse.get_pos()[0]>=274 and pygame.mouse.get_pos()[0]<=456 and pygame.mouse.get_pos()[1]>=146 and pygame.mouse.get_pos()[1]<=503:
                        Click_Sound.play()
                        n = 0#########################
                        menu_access-=1
                    if pygame.mouse.get_pos()[0]>=659 and pygame.mouse.get_pos()[0]<=825 and pygame.mouse.get_pos()[1]>=339 and pygame.mouse.get_pos()[1]<=498:
                        Click_Sound.play()
                        menu_type = 1
                        menu_access-=1
                    if pygame.mouse.get_pos()[0]>=472 and pygame.mouse.get_pos()[0]<=822 and pygame.mouse.get_pos()[1]>=148 and pygame.mouse.get_pos()[1]<=315:
                        Click_Sound.play()
                        menu_access-=1
                        menu_type = 4
            if menu_type == 5:
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        tutor_step+=1

                    if tutor_step==0:
                        tutor_step = 1
            if menu_type == 3:
                noone = True
                if pygame.mouse.get_pos()[0]>=681 and pygame.mouse.get_pos()[0]<=886 and pygame.mouse.get_pos()[1]>=92 and pygame.mouse.get_pos()[1]<=508:
                    Quit_Slots_Selected+=1
                    if Quit_Slots_Selected==1:
                        Select_Sound.play()
                        Quit_Slots = Sprite(-390,-240,'Files/Textures/Menu/mQuit_Slots_Selected.png',0,0,0)
                else:
                    Quit_Slots_Selected=0
                    Quit_Slots = Sprite(-390,-240,'Files/Textures/Menu/mQuit_Slots.png',0,0,0)
                    
                ##1
                if pygame.mouse.get_pos()[0]>=253 and pygame.mouse.get_pos()[0]<=662 and pygame.mouse.get_pos()[1]>=91 and pygame.mouse.get_pos()[1]<=220:
                    slot1_Selected+=1
                    if slot1_Selected==1:
                        Select_Sound.play()
                    noone = False
                    slot2 = Sprite(-390,-240,'Files/Textures/Menu/mslot2.png',0,0,0)
                    slot3 = Sprite(-390,-240,'Files/Textures/Menu/mslot3.png',0,0,0)
                    if sure == 0:
                        slot1 = Sprite(-390,-240,'Files/Textures/Menu/mslot1_Selected.png',0,0,0)
                    if sure == 1:
                        slot1 = Sprite(-390,-240,'Files/Textures/Menu/mslot1_Sure2.png',0,0,0)
                    if sure == 2:
                        slot1 = Sprite(-390,-240,'Files/Textures/Menu/mslot1_Sure1.png',0,0,0)
                ##2
                if pygame.mouse.get_pos()[0]>=253 and pygame.mouse.get_pos()[0]<=662 and pygame.mouse.get_pos()[1]>=238 and pygame.mouse.get_pos()[1]<=363:
                        slot2_Selected+=1
                        if slot2_Selected==1:
                            Select_Sound.play()
                        noone = False
                        slot1 = Sprite(-390,-240,'Files/Textures/Menu/mslot1.png',0,0,0)
                        slot3 = Sprite(-390,-240,'Files/Textures/Menu/mslot3.png',0,0,0)
                        if sure == 0:
                            slot2 = Sprite(-390,-240,'Files/Textures/Menu/mslot2_Selected.png',0,0,0)
                        if sure == 1:
                            slot2 = Sprite(-390,-240,'Files/Textures/Menu/mslot2_Sure2.png',0,0,0)
                        if sure == 2:
                            slot2 = Sprite(-390,-240,'Files/Textures/Menu/mslot2_Sure1.png',0,0,0)

                ##3
                if pygame.mouse.get_pos()[0]>=253 and pygame.mouse.get_pos()[0]<=662 and pygame.mouse.get_pos()[1]>=380 and pygame.mouse.get_pos()[1]<=509:
                        slot3_Selected+=1
                        if slot3_Selected==1:
                            Select_Sound.play()
                        noone = False
                        slot1 = Sprite(-390,-240,'Files/Textures/Menu/mslot1.png',0,0,0)
                        slot2 = Sprite(-390,-240,'Files/Textures/Menu/mslot2.png',0,0,0)
                        if sure == 0:
                            slot3 = Sprite(-390,-240,'Files/Textures/Menu/mslot3_Selected.png',0,0,0)
                        if sure == 1:
                            slot3 = Sprite(-390,-240,'Files/Textures/Menu/mslot3_Sure2.png',0,0,0)
                        if sure == 2:
                            slot3 = Sprite(-390,-240,'Files/Textures/Menu/mslot3_Sure1.png',0,0,0)
                        
                if noone:###
                    slot1_Selected = 0
                    slot2_Selected = 0
                    slot3_Selected = 0
                    slot1 = Sprite(-390,-240,'Files/Textures/Menu/mslot1.png',0,0,0)
                    slot2 = Sprite(-390,-240,'Files/Textures/Menu/mslot2.png',0,0,0)
                    slot3 = Sprite(-390,-240,'Files/Textures/Menu/mslot3.png',0,0,0)
                    sure = 0
                    begin = 0
                    
                if e.type == pygame.MOUSEBUTTONDOWN and menu_access == 1:
                    if pygame.mouse.get_pos()[0]>=681 and pygame.mouse.get_pos()[0]<=886 and pygame.mouse.get_pos()[1]>=92 and pygame.mouse.get_pos()[1]<=508:
                        Click_Sound.play()
                        menu_access-=1
                        menu_type = 2
                        begin = 0
                    ###___###1
                    if pygame.mouse.get_pos()[0]>=253 and pygame.mouse.get_pos()[0]<=662 and pygame.mouse.get_pos()[1]>=91 and pygame.mouse.get_pos()[1]<=220:
                        Click_Sound.play()
                        menu_access-=1

                        begin+=1
                        
                        load_file = open('Files/Saves/save1.dat', 'rb')
                        all_objects = pickle.load(load_file)
                        load_file.close()
                        empty_arr = []
                        empty_arr.append(['empty','0','0','Files/Textures/Objects/empty.png','0','0','0'])
                        empty = Sprite(0,0,'Files/Textures/Objects/empty.png',0,0,0)

                        if begin == 1:
                            if all_objects != empty_arr:
                                print('FULL')
                                slot1 = Sprite(-390,-240,'Files/Textures/Menu/mslot1_Sure2.png',0,0,0)
                                sure = 1
                            else:
                                print('EMPTY')
                                slot1 = Sprite(-390,-240,'Files/Textures/Menu/mslot1_Sure1.png',0,0,0)
                                sure = 2
                        if begin == 2:

                            current_slot = 1
                            all_objects = []
                            all_objects.append(['empty','0','0','Files/Textures/Objects/empty.png','0','0','0'])
                            n = 0
                            begin = 0
                            main_theme_1.stop()
                            main_theme_2.stop()
                    ###___###2
                    if pygame.mouse.get_pos()[0]>=253 and pygame.mouse.get_pos()[0]<=662 and pygame.mouse.get_pos()[1]>=238 and pygame.mouse.get_pos()[1]<=363:
                        Click_Sound.play()
                        menu_access-=1

                        begin+=1
                        
                        load_file = open('Files/Saves/save2.dat', 'rb')
                        all_objects = pickle.load(load_file)
                        load_file.close()
                        empty_arr = []
                        empty_arr.append(['empty','0','0','Files/Textures/Objects/empty.png','0','0','0'])
                        empty = Sprite(0,0,'Files/Textures/Objects/empty.png',0,0,0)

                        if begin == 1:
                            if all_objects != empty_arr:
                                print('FULL')
                                slot2 = Sprite(-390,-240,'Files/Textures/Menu/mslot2_Sure2.png',0,0,0)
                                sure = 1
                            else:
                                print('EMPTY')
                                slot2 = Sprite(-390,-240,'Files/Textures/Menu/mslot2_Sure1.png',0,0,0)
                                sure = 2
                        if begin == 2:
                            current_slot = 2
                            all_objects = []
                            all_objects.append(['empty','0','0','Files/Textures/Objects/empty.png','0','0','0'])
                            n = 0
                            begin = 0
                            main_theme_1.stop()
                            main_theme_2.stop()
                    ###___###3
                    if pygame.mouse.get_pos()[0]>=253 and pygame.mouse.get_pos()[0]<=662 and pygame.mouse.get_pos()[1]>=380 and pygame.mouse.get_pos()[1]<=509:
                        Click_Sound.play()
                        menu_access-=1

                        begin+=1
                        
                        load_file = open('Files/Saves/save3.dat', 'rb')
                        all_objects = pickle.load(load_file)
                        load_file.close()
                        empty_arr = []
                        empty_arr.append(['empty','0','0','Files/Textures/Objects/empty.png','0','0','0'])
                        empty = Sprite(0,0,'Files/Textures/Objects/empty.png',0,0,0)

                        if begin == 1:
                            if all_objects != empty_arr:
                                print('FULL3')
                                slot3 = Sprite(-390,-240,'Files/Textures/Menu/mslot3_Sure2.png',0,0,0)
                                sure = 1
                            else:
                                print('EMPTY333')
                                slot3 = Sprite(-390,-240,'Files/Textures/Menu/mslot3_Sure1.png',0,0,0)
                                sure = 2
                        if begin == 2:
                            current_slot = 3
                            all_objects = []
                            all_objects.append(['empty','0','0','Files/Textures/Objects/empty.png','0','0','0'])
                            n = 0
                            begin = 0
                            main_theme_1.stop()
                            main_theme_2.stop()    
                            
                    

            if menu_type == 4:
                noone = True
                if pygame.mouse.get_pos()[0]>=681 and pygame.mouse.get_pos()[0]<=886 and pygame.mouse.get_pos()[1]>=92 and pygame.mouse.get_pos()[1]<=508:
                    Quit_Slots_Selected+=1
                    if Quit_Slots_Selected==1:
                        Select_Sound.play()
                        Quit_Slots = Sprite(-390,-240,'Files/Textures/Menu/mQuit_Slots_Selected.png',0,0,0)
                else:
                    Quit_Slots_Selected = 0
                    Quit_Slots = Sprite(-390,-240,'Files/Textures/Menu/mQuit_Slots.png',0,0,0)
                    ###1
                if pygame.mouse.get_pos()[0]>=253 and pygame.mouse.get_pos()[0]<=662 and pygame.mouse.get_pos()[1]>=91 and pygame.mouse.get_pos()[1]<=220:
                    slot1_Selected+=1
                    if slot1_Selected==1:
                        Select_Sound.play()
                    noone = False
                    slot2 = Sprite(-390,-240,'Files/Textures/Menu/mslot2.png',0,0,0)
                    slot3 = Sprite(-390,-240,'Files/Textures/Menu/mslot3.png',0,0,0)
                    if sure == 0:
                        slot1 = Sprite(-390,-240,'Files/Textures/Menu/mslot1_Selected.png',0,0,0)
                    if sure == 1:
                        slot1 = Sprite(-390,-240,'Files/Textures/Menu/mslot1_Sure4.png',0,0,0)
                    if sure == 2:
                        slot1 = Sprite(-390,-240,'Files/Textures/Menu/mslot1_Sure3.png',0,0,0)

                   ###2 
                if pygame.mouse.get_pos()[0]>=254 and pygame.mouse.get_pos()[0]<=661 and pygame.mouse.get_pos()[1]>=238 and pygame.mouse.get_pos()[1]<=363:
                    slot2_Selected+=1
                    if slot2_Selected==1:
                        Select_Sound.play()
                    noone = False
                    slot1 = Sprite(-390,-240,'Files/Textures/Menu/mslot1.png',0,0,0)
                    slot3 = Sprite(-390,-240,'Files/Textures/Menu/mslot3.png',0,0,0)
                    if sure == 0:
                        slot2 = Sprite(-390,-240,'Files/Textures/Menu/mslot2_Selected.png',0,0,0)
                    if sure == 1:
                        slot2 = Sprite(-390,-240,'Files/Textures/Menu/mslot2_Sure4.png',0,0,0)
                    if sure == 2:
                        slot2 = Sprite(-390,-240,'Files/Textures/Menu/mslot2_Sure3.png',0,0,0)
                     ###3
                if pygame.mouse.get_pos()[0]>=252 and pygame.mouse.get_pos()[0]<=660 and pygame.mouse.get_pos()[1]>=380 and pygame.mouse.get_pos()[1]<=509:
                    slot3_Selected+=1
                    if slot3_Selected==1:
                        Select_Sound.play()
                    noone = False
                    slot2 = Sprite(-390,-240,'Files/Textures/Menu/mslot2.png',0,0,0)
                    slot1 = Sprite(-390,-240,'Files/Textures/Menu/mslot1.png',0,0,0)
                    if sure == 0:
                        slot3 = Sprite(-390,-240,'Files/Textures/Menu/mslot3_Selected.png',0,0,0)
                    if sure == 1:
                        slot3 = Sprite(-390,-240,'Files/Textures/Menu/mslot3_Sure4.png',0,0,0)
                    if sure == 2:
                        slot3 = Sprite(-390,-240,'Files/Textures/Menu/mslot3_Sure3.png',0,0,0)
                
                if noone:
                    slot1_Selected=0
                    slot2_Selected=0
                    slot3_Selected=0
                    slot1 = Sprite(-390,-240,'Files/Textures/Menu/mslot1.png',0,0,0)
                    slot2 = Sprite(-390,-240,'Files/Textures/Menu/mslot2.png',0,0,0)
                    slot3 = Sprite(-390,-240,'Files/Textures/Menu/mslot3.png',0,0,0)
                    sure = 0
                    begin = 0
                    

                if e.type == pygame.MOUSEBUTTONDOWN and menu_access == 1:
                     print(pygame.mouse.get_pos())
                     
                     if pygame.mouse.get_pos()[0]>=681 and pygame.mouse.get_pos()[0]<=886 and pygame.mouse.get_pos()[1]>=92 and pygame.mouse.get_pos()[1]<=508:
                         menu_access-=1
                         menu_type = 2
                         begin = 0
                         Click_Sound.play()
                         ###1
                     if pygame.mouse.get_pos()[0]>=253 and pygame.mouse.get_pos()[0]<=662 and pygame.mouse.get_pos()[1]>=91 and pygame.mouse.get_pos()[1]<=220:
                        Click_Sound.play()
                        menu_access-=1
                        begin+=1
                        load_file = open('Files/Saves/save1.dat', 'rb') 
                        all_objects = pickle.load(load_file)
                        load_file.close()
                        empty_arr = []
                        empty_arr.append(['empty','0','0','Files/Textures/Objects/empty.png','0','0','0'])
                        empty = Sprite(0,0,'Files/Textures/Objects/empty.png',0,0,0)
                        for i in range(0,len(all_objects)):
                            exec(all_objects[i][0] + '= Sprite(' + all_objects[i][1] + ',' + all_objects[i][2] + ',"' + all_objects[i][3] + '",' + all_objects[i][4] + ',' + all_objects[i][5] + ',' + all_objects[i][6] + ')')
                        
                        if begin == 1:
                            if all_objects != empty_arr:
                                print('FULL')
                                slot1 = Sprite(-390,-240,'Files/Textures/Menu/mslot1_Sure4.png',0,0,0)
                                sure = 1
                            else:
                                print('EMPTY')
                                slot1 = Sprite(-390,-240,'Files/Textures/Menu/mslot1_Sure3.png',0,0,0)
                                sure = 2
                        if begin == 2 and (all_objects != empty_arr):
                            current_slot = 1
                            n = 0
                            begin = 0
                            main_theme_1.stop()
                            main_theme_2.stop()
                        
                    ###2
                        
                        
                     if pygame.mouse.get_pos()[0]>=254 and pygame.mouse.get_pos()[0]<=661 and pygame.mouse.get_pos()[1]>=238 and pygame.mouse.get_pos()[1]<=363:
                        Click_Sound.play()
                        menu_access-=1
                        begin+=1
                        load_file = open('Files/Saves/save2.dat', 'rb') 
                        all_objects = pickle.load(load_file)
                        load_file.close()
                        empty_arr = []
                        empty_arr.append(['empty','0','0','Files/Textures/Objects/empty.png','0','0','0'])
                        empty = Sprite(0,0,'Files/Textures/Objects/empty.png',0,0,0)
                        for i in range(0,len(all_objects)):
                            exec(all_objects[i][0] + '= Sprite(' + all_objects[i][1] + ',' + all_objects[i][2] + ',"' + all_objects[i][3] + '",' + all_objects[i][4] + ',' + all_objects[i][5] + ',' + all_objects[i][6] + ')')
                        
                        if begin == 1:
                            if all_objects != empty_arr:
                                print('FULL2')
                                slot2 = Sprite(-390,-240,'Files/Textures/Menu/mslot2_Sure4.png',0,0,0)
                                sure = 1
                            else:
                                print('EMPTY2')
                                slot2 = Sprite(-390,-240,'Files/Textures/Menu/mslot2_Sure3.png',0,0,0)
                                sure = 2
                        if begin == 2 and (all_objects != empty_arr):
                            current_slot = 2
                            n = 0
                            begin = 0
                            main_theme_1.stop()
                            main_theme_2.stop()   
                    
                    ###3
                     if pygame.mouse.get_pos()[0]>=254 and pygame.mouse.get_pos()[0]<=661 and pygame.mouse.get_pos()[1]>=380 and pygame.mouse.get_pos()[1]<=509:
                        Click_Sound.play()
                        print("###3")
                        menu_access-=1
                        begin+=1
                        load_file = open('Files/Saves/save3.dat', 'rb') 
                        all_objects = pickle.load(load_file)
                        load_file.close()
                        empty_arr = []
                        empty_arr.append(['empty','0','0','Files/Textures/Objects/empty.png','0','0','0'])
                        empty = Sprite(0,0,'Files/Textures/Objects/empty.png',0,0,0)
                        for i in range(0,len(all_objects)):
                            exec(all_objects[i][0] + '= Sprite(' + all_objects[i][1] + ',' + all_objects[i][2] + ',"' + all_objects[i][3] + '",' + all_objects[i][4] + ',' + all_objects[i][5] + ',' + all_objects[i][6] + ')')
                        
                        if begin == 1:
                            if all_objects != empty_arr:
                                print('FULL3')
                                slot3 = Sprite(-390,-240,'Files/Textures/Menu/mslot3_Sure4.png',0,0,0)
                                sure = 1
                            else:
                                print('EMPTY3')
                                slot3 = Sprite(-390,-240,'Files/Textures/Menu/mslot3_Sure3.png',0,0,0)
                                sure = 2
                        if begin == 2 and (all_objects != empty_arr):
                            current_slot = 3
                            n = 0
                            begin = 0
                            main_theme_1.stop()
                            main_theme_2.stop()   
        #menu_access = 1    
        #Поиск среди всех событий нажатие на мышку
        #в игре
        if n == 0:
            '''
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 2:
                    print('Saving...')
                    for i in range(0,len(all_objects)):
                            exec('c = ' + str(all_objects[i][0]))
                            all_objects[i][1] = str(c.x)
                            all_objects[i][2] = str(c.y)
                    print(current_slot)
                    if current_slot == 1:
                        save_file = open('Files/Saves/save1.dat','wb')
                    if current_slot == 2:
                        save_file = open('Files/Saves/save2.dat','wb')
                    if current_slot == 3:
                        save_file = open('Files/Saves/save3.dat','wb')
                    pickle.dump(all_objects, save_file)
                    save_file.close()
                    print('Saving complete.')'''

            if e.type == pygame.MOUSEMOTION and menu_access == 1 and gamemenu_step == 1:
                if pygame.mouse.get_pos()[0]>=273 and pygame.mouse.get_pos()[0]<=605 and pygame.mouse.get_pos()[1]>=338 and pygame.mouse.get_pos()[1]<=503:
                    Game_Save_Selected+=1
                    if Game_Save_Selected==1:
                        Select_Sound.play()
                    if sure_save==0:
                        Game_Save = Sprite(80,120,'Files/Textures/Menu/game_save_Selected.png',0,0,0)
                    if sure_save == 1:
                        Game_Save = Sprite(80,120,'Files/Textures/Menu/game_save_Sure1.png',0,0,0)
                else:
                    sure_save = 0
                    Game_Save_Selected = 0
                    Game_Save = Sprite(80,120,'Files/Textures/Menu/game_save.png',0,0,0)
                if pygame.mouse.get_pos()[0]>=274 and pygame.mouse.get_pos()[0]<=813 and pygame.mouse.get_pos()[1]>=148 and pygame.mouse.get_pos()[1]<=317:
                    Game_Play_Selected+=1
                    if Game_Play_Selected==1:
                        Select_Sound.play()
                        Game_Play = Sprite(80,120,'Files/Textures/Menu/game_play_Selected.png',0,0,0)
                else:
                    
                    Game_Play_Selected = 0
                    Game_Play = Sprite(80,120,'Files/Textures/Menu/game_play.png',0,0,0)
                if pygame.mouse.get_pos()[0]>=648 and pygame.mouse.get_pos()[0]<=813 and pygame.mouse.get_pos()[1]>=338 and pygame.mouse.get_pos()[1]<=503:
                    
                    Game_Quit_Selected+=1
                    if Game_Quit_Selected==1:
                        Select_Sound.play()
                    if game_quit_sure == 0:
                        Game_Quit = Sprite(80,120,'Files/Textures/Menu/game_quit_Selected.png',0,0,0)
                    if game_quit_sure == 1:
                       Game_Quit = Sprite(80,120,'Files/Textures/Menu/game_quit_Sure1.png',0,0,0) 
                else:
                    game_quit_sure=0
                    Game_Quit_Selected=0
                    Game_Quit = Sprite(80,120,'Files/Textures/Menu/game_quit.png',0,0,0)
            
            if e.type == pygame.MOUSEBUTTONDOWN and menu_access == 1:
                '''
                (274, 148)
                (813, 317)
                (273, 339)
                (605, 503)
                '''
                if gamemenu_step == 1:
                    if e.button == 1:
                        print(pygame.mouse.get_pos())
                        if pygame.mouse.get_pos()[0]>=274 and pygame.mouse.get_pos()[0]<=813 and pygame.mouse.get_pos()[1]>=148 and pygame.mouse.get_pos()[1]<=317:
                            Click_Sound.play()
                            gamemenu_step = 0
                            pygame.key.set_repeat(1,1)
                            menu_access-=1
                        if pygame.mouse.get_pos()[0]>=648 and pygame.mouse.get_pos()[0]<=813 and pygame.mouse.get_pos()[1]>=338 and pygame.mouse.get_pos()[1]<=503:
                            Click_Sound.play()
                            game_quit_sure+=1
                            Game_Quit = Sprite(80,120,'Files/Textures/Menu/game_quit_Sure1.png',0,0,0)
                            if game_quit_sure == 2:
                                n = 1
                                gamemenu_step = 0
                                pygame.key.set_repeat(1,1)
                                tim = time.time()
                                print('WOW')
                                start_music()
                        if pygame.mouse.get_pos()[0]>=273 and pygame.mouse.get_pos()[0]<=605 and pygame.mouse.get_pos()[1]>=338 and pygame.mouse.get_pos()[1]<=503:
                             Click_Sound.play()
                             sure_save = 1
                             Game_Save = Sprite(80,120,'Files/Textures/Menu/game_save_Sure1.png',0,0,0)
                             print('Saving...')
                             for i in range(0,len(all_objects)):
                                        exec('c = ' + str(all_objects[i][0]))
                                        all_objects[i][1] = str(c.x)
                                        all_objects[i][2] = str(c.y)
                             print(current_slot)
                             if current_slot == 1:
                                    save_file = open('Files/Saves/save1.dat','wb')
                             if current_slot == 2:
                                    save_file = open('Files/Saves/save2.dat','wb')
                             if current_slot == 3:
                                    save_file = open('Files/Saves/save3.dat','wb')
                             pickle.dump(all_objects, save_file)
                             save_file.close()
                             print('Saving complete.')
                
                if inv == 1:
                    '''
                (511, 137)
                (612, 226)
                (637, 136)
                (738, 224)
                '''
                    if e.button == 1:
                        print(pygame.mouse.get_pos())
                        if pygame.mouse.get_pos()[0]>=222 and pygame.mouse.get_pos()[0]<=358 and pygame.mouse.get_pos()[1]>=69 and pygame.mouse.get_pos()[1]<=111:
                            inv_type = 1
                            
                        if pygame.mouse.get_pos()[0]>=360 and pygame.mouse.get_pos()[0]<=552 and pygame.mouse.get_pos()[1]>=67 and pygame.mouse.get_pos()[1]<=112:
                            inv_type = 2
                        if pygame.mouse.get_pos()[0]>=554 and pygame.mouse.get_pos()[0]<=744 and pygame.mouse.get_pos()[1]>=66 and pygame.mouse.get_pos()[1]<=114:
                            inv_type = 3
                        if pygame.mouse.get_pos()[0]>=746 and pygame.mouse.get_pos()[0]<=898 and pygame.mouse.get_pos()[1]>=66 and pygame.mouse.get_pos()[1]<=112:
                            inv_type = 4
                        if inv_type == 1:
                            if pygame.mouse.get_pos()[0]>=258 and pygame.mouse.get_pos()[0]<=357 and pygame.mouse.get_pos()[1]>=135 and pygame.mouse.get_pos()[1]<=223:    
                                inv_obj = 'Files/Textures/Objects/grass.png'
                                inv_cover_point = '0'
                                inv_x=0
                                inv_y=0
                                width = '320'
                                height = '320'
                                inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/grass_icon.png',0,0,0)
                                select_type = 1
                                select.x = 253
                                select.y=127
                            if pygame.mouse.get_pos()[0]>=382 and pygame.mouse.get_pos()[0]<=483 and pygame.mouse.get_pos()[1]>=137 and pygame.mouse.get_pos()[1]<=225:
                                inv_obj = 'Files/Textures/Objects/road1.png'
                                inv_cover_point = '400'
                                inv_x=0
                                inv_y=0
                                width = '64'
                                height = '64'
                                inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/road1_icon.png',0,0,0)
                                select_type = 1
                                #select.x = 253
                                select.x = 378
                                select.y=128
                            if pygame.mouse.get_pos()[0]>=511 and pygame.mouse.get_pos()[0]<=612 and pygame.mouse.get_pos()[1]>=137 and pygame.mouse.get_pos()[1]<=226:    
                                    inv_obj = 'Files/Textures/Objects/road2.png'
                                    inv_cover_point = '400'
                                    inv_x=0
                                    inv_y=0
                                    width = '64'
                                    height = '64'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/road2_icon.png',0,0,0)
                                    select_type = 1
                                    #select.x = 253
                                    select.x = 511-5
                                    select.y=137-9
                            if pygame.mouse.get_pos()[0]>=635 and pygame.mouse.get_pos()[0]<=746 and pygame.mouse.get_pos()[1]>=134 and pygame.mouse.get_pos()[1]<=225:    
                                    inv_obj = 'Files/Textures/Objects/lava.png'
                                    inv_cover_point = '500'
                                    inv_x=0
                                    inv_y=0
                                    width = '320'
                                    height = '274'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/lava_icon.png',0,0,0)
                                    select_type = 1
                                    #select.x = 253
                                    select.x = 635-2-1
                                    select.y=134-2-5
                            if pygame.mouse.get_pos()[0]>=765 and pygame.mouse.get_pos()[0]<=866 and pygame.mouse.get_pos()[1]>=133 and pygame.mouse.get_pos()[1]<=224:    
                                    inv_obj = 'Files/Textures/Objects/water.png'
                                    inv_cover_point = '500'
                                    inv_x=0
                                    inv_y=0
                                    width = '320'
                                    height = '274'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/water_icon.png',0,0,0)
                                    select_type = 1
                                    #select.x = 253
                                    select.x = 761
                                    select.y=126
                            if pygame.mouse.get_pos()[0]>=258 and pygame.mouse.get_pos()[0]<=358 and pygame.mouse.get_pos()[1]>=255 and pygame.mouse.get_pos()[1]<=344:    
                                    inv_obj = 'Files/Textures/Objects/sand.png'
                                    inv_cover_point = '500'
                                    inv_x=0
                                    inv_y=0
                                    width = '320'
                                    height = '274'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/sand_icon.png',0,0,0)
                                    select_type = 1
                                    #select.x = 253
                                    select.x = 253
                                    select.y=246


                        if inv_type == 2:
                            if pygame.mouse.get_pos()[0]>=258 and pygame.mouse.get_pos()[0]<=357 and pygame.mouse.get_pos()[1]>=135 and pygame.mouse.get_pos()[1]<=223:    
                                inv_obj = 'Files/Textures/Objects/tree1.png'
                                inv_cover_point = '80'
                                inv_x=180
                                inv_y=270
                                widht = '263'
                                height = '350'
                                inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/tree1_icon.png',0,0,0)
                                select_type = 2
                                select.x = 253
                                select.y=127
                            if pygame.mouse.get_pos()[0]>=382 and pygame.mouse.get_pos()[0]<=483 and pygame.mouse.get_pos()[1]>=137 and pygame.mouse.get_pos()[1]<=225:
                                inv_obj = 'Files/Textures/Objects/pine1.png'
                                inv_cover_point = '100'
                                inv_x=120
                                inv_y=220
                                width = '250'
                                height = '250'
                                inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/pine1_icon.png',0,0,0)
                                select_type = 2
                                #select.x = 253
                                select.x = 378
                                select.y=128

                            if pygame.mouse.get_pos()[0]>=511 and pygame.mouse.get_pos()[0]<=612 and pygame.mouse.get_pos()[1]>=137 and pygame.mouse.get_pos()[1]<=226:    
                                    inv_obj = 'Files/Textures/Objects/pine2.png'
                                    inv_cover_point = '100'
                                    inv_x=20
                                    inv_y=20
                                    width = '320'
                                    height = '320'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/pine2_icon.png',0,0,0)
                                    select_type = 2
                                    #select.x = 253
                                    select.x = 511-5
                                    select.y=137-9

                            if pygame.mouse.get_pos()[0]>=635 and pygame.mouse.get_pos()[0]<=746 and pygame.mouse.get_pos()[1]>=134 and pygame.mouse.get_pos()[1]<=225:    
                                    inv_obj = 'Files/Textures/Objects/log.png'
                                    inv_cover_point = '500'
                                    inv_x=20
                                    inv_y=20
                                    width = '220'
                                    height = '220'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/log_icon.png',0,0,0)
                                    select_type = 2
                                    #select.x = 253
                                    select.x = 635-2-1
                                    select.y=134-2-5

                            if pygame.mouse.get_pos()[0]>=765 and pygame.mouse.get_pos()[0]<=866 and pygame.mouse.get_pos()[1]>=133 and pygame.mouse.get_pos()[1]<=224:    
                                    inv_obj = 'Files/Textures/Objects/stump.png'
                                    inv_cover_point = '270'
                                    inv_x=0
                                    inv_y=0
                                    width = '70'
                                    height = '82'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/stump_icon.png',0,0,0)
                                    select_type = 2
                                    #select.x = 253
                                    select.x = 761
                                    select.y=126

                            if pygame.mouse.get_pos()[0]>=258 and pygame.mouse.get_pos()[0]<=358 and pygame.mouse.get_pos()[1]>=255 and pygame.mouse.get_pos()[1]<=344:    
                                    inv_obj = 'Files/Textures/Objects/bush.png'
                                    inv_cover_point = '240'
                                    inv_x=0
                                    inv_y=0
                                    width = '200'
                                    height = '100'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/bush_icon.png',0,0,0)
                                    select_type = 2
                                    #select.x = 253
                                    select.x = 253
                                    select.y=246

                            if pygame.mouse.get_pos()[0]>=382 and pygame.mouse.get_pos()[0]<=484 and pygame.mouse.get_pos()[1]>=255 and pygame.mouse.get_pos()[1]<=344:    
                                    inv_obj = 'Files/Textures/Objects/tree2.png'
                                    inv_cover_point = '0'
                                    inv_x=0
                                    inv_y=0
                                    width = '450'
                                    height = '450'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/tree2_icon.png',0,0,0)
                                    select_type = 2
                                    #select.x = 253
                                    select.x = 378
                                    select.y=247

                        if inv_type == 4:
                            if pygame.mouse.get_pos()[0]>=258 and pygame.mouse.get_pos()[0]<=357 and pygame.mouse.get_pos()[1]>=135 and pygame.mouse.get_pos()[1]<=223:    
                                inv_obj = 'Files/Textures/Objects/dragon.png'
                                inv_cover_point = '0'
                                inv_x=180
                                inv_y=270
                                width = '600'
                                height = '373'
                                inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/dragon_icon.png',0,0,0)
                                select_type = 4
                                select.x = 253
                                select.y=127
                            if pygame.mouse.get_pos()[0]>=382 and pygame.mouse.get_pos()[0]<=483 and pygame.mouse.get_pos()[1]>=137 and pygame.mouse.get_pos()[1]<=225:    
                                inv_obj = 'Files/Textures/Objects/princess.png'
                                inv_cover_point = '270'
                                inv_x=0
                                inv_y=0
                                width = '50'
                                height = '90'
                                inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/princess_icon.png',0,0,0)
                                select_type = 4
                                select.x = 378
                                select.y=128
                            if pygame.mouse.get_pos()[0]>=635 and pygame.mouse.get_pos()[0]<=746 and pygame.mouse.get_pos()[1]>=134 and pygame.mouse.get_pos()[1]<=225:    
                                    inv_obj = 'Files/Textures/Objects/horse.png'
                                    inv_cover_point = '500'
                                    inv_x=20
                                    inv_y=20
                                    width = '150'
                                    height = '100'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/horse_icon.png',0,0,0)
                                    select_type = 4
                                    #select.x = 253
                                    select.x = 635-2-1
                                    select.y=134-2-5
                            if pygame.mouse.get_pos()[0]>=765 and pygame.mouse.get_pos()[0]<=866 and pygame.mouse.get_pos()[1]>=133 and pygame.mouse.get_pos()[1]<=224:    
                                    inv_obj = 'Files/Textures/Objects/fox.png'
                                    inv_cover_point = '270'
                                    inv_x=0
                                    inv_y=0
                                    width = '70'
                                    height = '82'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/fox_icon.png',0,0,0)
                                    select_type = 4
                                    #select.x = 253
                                    select.x = 761
                                    select.y=126
                                
                            if pygame.mouse.get_pos()[0]>=511 and pygame.mouse.get_pos()[0]<=612 and pygame.mouse.get_pos()[1]>=137 and pygame.mouse.get_pos()[1]<=226:    
                                    inv_obj = 'Files/Textures/Objects/knight.png'
                                    inv_cover_point = '250'
                                    inv_x=20
                                    inv_y=20
                                    width = '90'
                                    height = '117'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/knight_icon.png',0,0,0)
                                    select_type = 4
                                    #select.x = 253
                                    select.x = 511-5
                                    select.y=137-9
                            if pygame.mouse.get_pos()[0]>=258 and pygame.mouse.get_pos()[0]<=358 and pygame.mouse.get_pos()[1]>=255 and pygame.mouse.get_pos()[1]<=344:    
                                    inv_obj = 'Files/Textures/Objects/ironman.png'
                                    inv_cover_point = '240'
                                    inv_x=0
                                    inv_y=0
                                    width = '60'
                                    height = '103'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/ironman_icon.png',0,0,0)
                                    select_type = 4
                                    #select.x = 253
                                    select.x = 253
                                    select.y=246

                            if pygame.mouse.get_pos()[0]>=382 and pygame.mouse.get_pos()[0]<=484 and pygame.mouse.get_pos()[1]>=255 and pygame.mouse.get_pos()[1]<=344:    
                                    inv_obj = 'Files/Textures/Objects/darthvador.png'
                                    inv_cover_point = '240'
                                    inv_x=0
                                    inv_y=0
                                    width = '60'
                                    height = '103'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/darthvador_icon.png',0,0,0)
                                    select_type = 4
                                    #select.x = 253
                                    select.x = 378
                                    select.y=247

                            if pygame.mouse.get_pos()[0]>=635 and pygame.mouse.get_pos()[0]<=746 and pygame.mouse.get_pos()[1]>=255 and pygame.mouse.get_pos()[1]<=344:    
                                    inv_obj = 'Files/Textures/Objects/wolf.png'
                                    inv_cover_point = '300'
                                    inv_x=0
                                    inv_y=0
                                    width = '60'
                                    height = '103'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/wolf_icon.png',0,0,0)
                                    select_type = 4
                                    #select.x = 253
                                    select.x = 632
                                    select.y=246

                            if pygame.mouse.get_pos()[0]>=765 and pygame.mouse.get_pos()[0]<=866 and pygame.mouse.get_pos()[1]>=255 and pygame.mouse.get_pos()[1]<=344:    
                                    inv_obj = 'Files/Textures/Objects/lion.png'
                                    inv_cover_point = '300'
                                    inv_x=0
                                    inv_y=0
                                    width = '60'
                                    height = '103'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/lion_icon.png',0,0,0)
                                    select_type = 4
                                    #select.x = 253
                                    select.x = 761
                                    select.y=245

                            if pygame.mouse.get_pos()[0]>=257 and pygame.mouse.get_pos()[0]<=358 and pygame.mouse.get_pos()[1]>=368 and pygame.mouse.get_pos()[1]<=457:    
                                    inv_obj = 'Files/Textures/Objects/sherlock.png'
                                    inv_cover_point = '300'
                                    inv_x=0
                                    inv_y=0
                                    width = '70'
                                    height = '154'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/sherlock_icon.png',0,0,0)
                                    select_type = 4
                                    #select.x = 253
                                    select.x = 253
                                    select.y=360
                        if inv_type == 3:
                             if pygame.mouse.get_pos()[0]>=258 and pygame.mouse.get_pos()[0]<=357 and pygame.mouse.get_pos()[1]>=135 and pygame.mouse.get_pos()[1]<=223:    
                                inv_obj = 'Files/Textures/Objects/house1.png'
                                inv_cover_point = '0'
                                inv_x=180
                                inv_y=270
                                width = '470'
                                height = '470'
                                inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/house1_icon.png',0,0,0)
                                select_type = 3
                                select.x = 253
                                select.y=127

                             if pygame.mouse.get_pos()[0]>=382 and pygame.mouse.get_pos()[0]<=483 and pygame.mouse.get_pos()[1]>=137 and pygame.mouse.get_pos()[1]<=225:    
                                    inv_obj = 'Files/Textures/Objects/castle.png'
                                    inv_cover_point = '-50'
                                    inv_x=120
                                    inv_y=220
                                    width = '580'
                                    height = '641'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/castle_icon.png',0,0,0)
                                    select_type = 3
                                    #select.x = 253
                                    select.x = 378
                                    select.y=128

                             if pygame.mouse.get_pos()[0]>=511 and pygame.mouse.get_pos()[0]<=612 and pygame.mouse.get_pos()[1]>=137 and pygame.mouse.get_pos()[1]<=226:    
                                    inv_obj = 'Files/Textures/Objects/tavern.png'
                                    inv_cover_point = '50'
                                    inv_x=20
                                    inv_y=20
                                    width = '900'
                                    height = '800'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/tavern_icon.png',0,0,0)
                                    select_type = 3
                                    #select.x = 253
                                    select.x = 511-5
                                    select.y=137-9
                             if pygame.mouse.get_pos()[0]>=635 and pygame.mouse.get_pos()[0]<=746 and pygame.mouse.get_pos()[1]>=134 and pygame.mouse.get_pos()[1]<=225:    
                                    inv_obj = 'Files/Textures/Objects/gold.png'
                                    inv_cover_point = '500'
                                    inv_x=20
                                    inv_y=20
                                    width = '100'
                                    height = '73'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/gold_icon.png',0,0,0)
                                    select_type = 3
                                    #select.x = 253
                                    select.x = 635-2-1
                                    select.y=134-2-5
                             if pygame.mouse.get_pos()[0]>=765 and pygame.mouse.get_pos()[0]<=866 and pygame.mouse.get_pos()[1]>=133 and pygame.mouse.get_pos()[1]<=224:    
                                    inv_obj = 'Files/Textures/Objects/car.png'
                                    inv_cover_point = '270'
                                    inv_x=0
                                    inv_y=0
                                    width = '260'
                                    height = '260'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/car_icon.png',0,0,0)
                                    select_type = 3
                                    #select.x = 253
                                    select.x = 761
                                    select.y=126

                             if pygame.mouse.get_pos()[0]>=258 and pygame.mouse.get_pos()[0]<=358 and pygame.mouse.get_pos()[1]>=255 and pygame.mouse.get_pos()[1]<=344:    
                                    inv_obj = 'Files/Textures/Objects/house2.png'
                                    inv_cover_point = '240'
                                    inv_x=0
                                    inv_y=0
                                    width = '400'
                                    height = '461'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/house2_icon.png',0,0,0)
                                    select_type = 3
                                    #select.x = 253
                                    select.x = 253
                                    select.y=246

                             if pygame.mouse.get_pos()[0]>=382 and pygame.mouse.get_pos()[0]<=484 and pygame.mouse.get_pos()[1]>=255 and pygame.mouse.get_pos()[1]<=344:    
                                    inv_obj = 'Files/Textures/Objects/helicopter.png'
                                    inv_cover_point = '240'
                                    inv_x=0
                                    inv_y=0
                                    width = '250'
                                    height = '202'
                                    inv_icon = Sprite(1015,520,'Files/Textures/Inventory/Icons/helicopter_icon.png',0,0,0)
                                    select_type = 3
                                    #select.x = 253
                                    select.x = 378
                                    select.y=247

                                    
            if e.type == pygame.MOUSEBUTTONDOWN and tutor_on == 1:
                tutor_step+=1
                #%%%%
            if inv == 0 and gamemenu_step == 0 and tutor_on == 0:                

                if e.type == pygame.MOUSEBUTTONDOWN and menu_access == 1:
                    #menu_access-=1
                    if e.button == 1:
                        i = len(all_objects)
                        text = 'a' + str(time.time())
                        text = text.replace('.','')
                        all_objects.append([text,str(pygame.mouse.get_pos()[0]-inv_x),str(pygame.mouse.get_pos()[1]-inv_y),inv_obj,width,height,inv_cover_point])
                        exec(all_objects[i][0] + '= Sprite(' + all_objects[i][1] + ',' + all_objects[i][2] + ',"' + all_objects[i][3] + '",' + all_objects[i][4] + ',' + all_objects[i][5] + ',' + all_objects[i][6] + ')')
                    if e.button == 3:
                        check = True
                        b = len(all_objects)-1
                        while check:
                            exec('c = ' + str(all_objects[b][0]))
                            if release(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],c):
                                del all_objects[b]
                                check = False
                            b-=1
                            if b==-1:
                                check = False
        menu_access = 1
        #if e.type == pygame.KEYDOWN:
           # if e.key == pygame.K_RETURN:
                # n = 0
                 #screen.fill((50,50,50))
        if n==0:    
            
            #Поиск среди всех событий нажатия на клавиатуру
            ###
            if e.type == pygame.KEYUP:
                step = 0
                walk_sound.stop()
                wtim = time.time()-5.5
                if step_type == 'down':
                    hero_stay_down.y = 220
                    hero_go1_down.y = 5000
                    hero_go2_down.y =5000
                    hero_go3_down.y =5000
                    hero_go4_down.y =5000
                if step_type == 'left':
                    hero_left_stay.y = 220
                    hero_go_left1.y = 5000
                    hero_go_left2.y =5000
                if step_type == 'right':
                    hero_right_stay.y = 220
                    hero_go_right1.y = 5000
                    hero_go_right2.y =5000
                if step_type == 'up':
                    go_up_stay.y = 220
                    hero_go_up_1.y =5000
                    hero_go_up_2.y =5000
                    hero_go_up_3.y =5000
                    hero_go_up_4.y =5000                

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_KP_PLUS:
                    Z+=1
                    print(Z)
                if e.key == pygame.K_KP_MINUS:
                    Z-=1
                    print(Z)
                if e.key == pygame.K_LEFT:
                    select.x-=Z
                    
                    print('X = ' + str(select.x) + 'Y = ' + str(select.y))
                if e.key == pygame.K_UP:
                    select.y-=Z
                    print('X = ' + str(select.x) + 'Y = ' + str(select.y))
                if e.key == pygame.K_DOWN:
                    select.y+=Z
                    print('X = ' + str(select.x) + 'Y = ' + str(select.y))
                if e.key == pygame.K_RIGHT:
                    select.x+=Z
                    print('X = ' + str(select.x) + 'Y = ' + str(select.y))
            if e.type == pygame.KEYDOWN:  
                if e.key == pygame.K_e and gamemenu_step == 0 and tutor_on == 0:
                    inv_step += 1
                if inv_step == 1:
                        #Для того, чтобы можно было зажимать клавиши
                        pygame.key.set_repeat(0,0)
                        inv = 1
                if inv_step == 2:
                        inv = 0
                        pygame.key.set_repeat(1,1)
                if inv_step == 2:
                    inv_step = 0      
                        
                if e.key == pygame.K_ESCAPE and inv_step == 0 and tutor_on == 0:
                    #n = 1
                    gamemenu_step += 1
                    pygame.key.set_repeat(0,0)
                if gamemenu_step == 2:
                    gamemenu_step = 0
                    pygame.key.set_repeat(1,1)
                    

                if inv == 0 and gamemenu_step == 0:
                    #Нажата клавиша S
                    ###
                    if e.key == pygame.K_s:
                       walk()
                       step_type = 'down'
                       step += 1
                       for i in range(0,len(all_objects)):
                            exec(all_objects[i][0] + '.y -= ' + str(speed))
                    #Нажата клавиша W
                    if e.key == pygame.K_w:
                       walk()
                       step_type = 'up'
                       step+=1
                       for i in range(0,len(all_objects)):
                            exec(all_objects[i][0] + '.y += ' + str(speed))
                    #Нажата клавиша A
                    if e.key == pygame.K_a:
                       walk()
                       step_type = 'left'
                       step+=1
                       for i in range(0,len(all_objects)):
                            exec(all_objects[i][0] + '.x += ' + str(speed))
                    #Нажата клавиша D
                    if e.key == pygame.K_d:
                        walk()
                        step_type = 'right'
                        step+=1
                        for i in range(0,len(all_objects)):
                            exec(all_objects[i][0] + '.x -= ' + str(speed))
                

#Рендеринг всех объектов из массива (которые уже отсортированы)

    if n==0:
        

            
        for i in range(0,len(all_objects)):
            exec(all_objects[i][0] + '.render()')
            hero_anim()

        for i in range(0,len(all_objects)):
            if all_objects[i][3] != 'Files/Textures/Objects/grass.png':
                exec('obj = ' + all_objects[i][0])
                if obj.y<obj.cover_point:
                    obj.render()
                    
        hero_render()
        
            
        for i in range(0,len(all_objects)):
            if all_objects[i][3] != 'Files/Textures/Objects/grass.png':
                exec('obj = ' + all_objects[i][0])
                if obj.y>=obj.cover_point:
                    obj.render()


        if gamemenu_step == 1:
            Game_Play.render()
            Game_Save.render()
            Game_Quit.render()
        if inv == 1:
            
            if inv_type == 1:
                inventory1.render()
            if inv_type == 2:     
                inventory2.render()
            if inv_type == 3:
                inventory3.render()
            if inv_type == 4:
                inventory4.render()
            if inv_type == select_type:
                select.render()
        inv_icon.render()
        if tutor_on == 1:
            tutor_render()

        
    if n==1:
        menu_render()

    
    window.blit(screen, (0,0))
    if menu_type == 5:
        window.blit(text1, (text_x, 450))#<>400,490
        window.blit(text2, (text_x, 490))
        window.blit(text3, (text_x, 530))
    if menu_type == 6:
        window.blit(text1, (450, 10+30))#<>400,490
        window.blit(text2, (160, 50+30+30))
        window.blit(text3, (160, 90+30+30))
        window.blit(text4, (160, 90+40+30+30))
        window.blit(text5, (160, 90+40+30+30+40))
    
    #pygame.display.flip()
    pygame.display.update()
    clock.tick(120)
    #pygame.event.wait()
    #Шрифт
        

    
    

pygame.quit()
