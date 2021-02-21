import config 
import gspread
import termcolor

themes = []
for i in config.palitrs:
    themes.append(i)
    
palitr = palitrs[config.COLORTHEME if config.COLORTHEME != "" else open(config.colorthemeFile).read() if open(config.colorthemeFile).read() in themes else "white"].split()
class colors():
    one = palitr[0]
    two = palitr[1]
    three = palitr[2]
    four = palitr[3]
    five = palitr[4]

try:
    inf = open(config.colorthemeFile).read()
    inf = inf if inf != "" else "gold"
    palitr = list(palitrs[inf].split())
except:
    file = open(config.colorthemeFile, "w",encoding="utf-8")
    file.write("gold")
    file.close()
    palitr = list(palitrs[open(config.colorthemeFile, encoding="utf-8").read()].split())

class tables():
    def __init__(self):
        self.gc = gspread.service_account(filename=config.ApiKey)
        self.sh = self.gc.open_by_url(config.SheetsLink)
        self.sheets = {}
        for i in self.sh.worksheets(): self.sheets[i.title] = i
        self.curx = 0
        self.cury = 0
    def makemaket(self, colorscheme):
        

google = tables()
print(google.sheets)