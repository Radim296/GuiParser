from tkinter import *
import webbrowser
import clipboard
import config as cf
#print(clipboard.paste())

palitrs = {
    "blue" : "#1240AB	#2A4480	#06266F	#4671D5	#6C8CD5",
    "green" : "#74E600	#6CAC2B	#4B9500	#98F23D	#B0F26D",
    "yellow" : "#FFAA00	#BF8F30	#A66F00	#FFBF40	#FFD073",
    "gold" : "#AE8349	#836A4A	#714B18	#D7AF79	#D7B992",
    "red" : "#B88484	#AF7F7F	#AB6E6E	#BF8B8B	#BF8E8E",
    "pink" : "#A400FF	#8C30BF	#6B00A6	#BB40FF	#CD73FF",
    "emerald" : "#00B454	#228751	#007536	#36DA82	#62DA9A",
    "grey" : "#4C4C4C	#5B5B5B	#323232	#797979	#9D9D9D",
    "greyWhite" : "#4C4C4C	#5A5A5A	#272727	#A6A6A6	#EDEDED"
}
palitr = palitrs[cf.COLORTHEME].split()
class colors():
    one = palitr[0]
    two = palitr[1]
    three = palitr[2]
    four = palitr[3]
    five = palitr[4]
class config():
    # Конфигурация окна
    wind_name = "Парсер" #Имя окна
    wind_geometry = "585x130" #Размеры окна 
    wind_background = colors.five #Фоновый цвет окна 
    wind_icon = "files\icon.ico"#Путь к иконки
    # Конфигурация кнопок
    buttons_bg = colors.four
    buttons_fg = "black"#colors.three 
    buttons_height = 2
    buttons_width = 10

class gui():
    def __init__(self):
        self.root = Tk()
        self.message = StringVar()
        self.root.title(config.wind_name)
        self.x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2.85
        self.y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2.85
        self.root.wm_geometry("+%d+%d" % (self.x, self.y))
        self.root.geometry(config.wind_geometry)
        self.root["bg"] = config.wind_background 
        self.root.iconbitmap(config.wind_icon)
        self.root.resizable(False, False) # hello
        self.makeMenu()
        self.makewidgets()
        self.root.config(menu = self.mainmenu)
    def makewidgets(self):
        self.entry = Entry(self.root, bg = config.buttons_bg, fg = config.buttons_fg, width = 39, textvariable = self.message, font = ("Helvetica", 20, "bold"))
        if cf.pasteFromClipboard:
            self.entry.insert(0, clipboard.paste())
        self.entry.place(x = 0, y = 0)
        #self.noText = Label(self.root, text = " ", bg = colors.four).grid(row = 2, column = 0)
        self.pasteButton = Button(self.root, text = "Вставить", bg =  config.buttons_bg, height = config.buttons_height, width = config.buttons_width,
                    fg =  config.buttons_fg, command = lambda a = 0: self.entry.insert(0, clipboard.paste()), activebackground = config.buttons_bg, activeforeground = config.buttons_fg)
        self.pasteButton.place(x = 10, y = 40)
        self.deleteButton = Button(self.root, text = "Очистить", bg =  config.buttons_bg, height = config.buttons_height, width = config.buttons_width,
                    fg =  config.buttons_fg, command = lambda a = 0: self.entry.delete(0, len(self.entry.get())), activebackground = config.buttons_bg, activeforeground = config.buttons_fg)
        self.deleteButton.place(x = 95, y = 40)
        self.parseButton = Button(self.root, text = "Спарсить", bg = config.buttons_bg, height = config.buttons_height,width = config.buttons_width,
                    fg =  config.buttons_fg, command = lambda a = 0: self.entry.delete(0, len(self.entry.get())), activebackground = config.buttons_bg, activeforeground = config.buttons_fg)
        self.parseButton.place(x = 180, y = 40)
        self.sendButton = Button(self.root, text = "Отправить данные", bg = config.buttons_bg, height = config.buttons_height,width = config.buttons_width * 2,
                    fg =  config.buttons_fg, command = lambda a = 0: self.entry.delete(0, len(self.entry.get())), activebackground = config.buttons_bg, activeforeground = config.buttons_fg)
        self.sendButton.place(x = 266, y = 40)
        self.writeButton = Button(self.root, text = "Записать в файл", bg = config.buttons_bg, height = config.buttons_height,width = config.buttons_width * 2,
                    fg =  config.buttons_fg, command = lambda a = 0: self.entry.delete(0, len(self.entry.get())), activebackground = config.buttons_bg, activeforeground = config.buttons_fg)
        self.writeButton.place(x = 422, y = 40)
        self.text = Button(self.root, bg = config.wind_background, relief = "flat", fg = "black", text = "Открыть гугл-таблицы", command = lambda a = 0: webbrowser.open(cf.SheetsLink, 2))
        self.text.place(x = 10, y = 85)
    def makeMenu(self):
        self.mainmenu = Menu(self.root, background = colors.five, foreground = colors.three)
        self.filemenu = Menu(self.mainmenu, tearoff=0, background = colors.five, foreground = colors.three)
        # Filemenu
        self.filemenu.add_command(label="Справка", command = lambda a = 1:help(), background = colors.five, foreground = colors.three)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Закрыть программу", command = exit, background = colors.five, foreground = colors.three)
        # Инициализация элементов меню
        self.mainmenu.add_cascade(menu=self.filemenu, label ="Файл")

def main():
    window = gui()
    window.root.mainloop()

if __name__ == "__main__":
    main()