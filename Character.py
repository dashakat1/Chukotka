from tkinter import *
from collections import deque


def OUT():
    global canv
    if Q:
        line = Q.popleft()
        canv.configure(height=canv.winfo_height() + 20)
        line.pack(anchor='nw')


def tell(line):
    Q.append(Label(f, fg='grey', font=20, wraplength=500, justify=LEFT, text=line))


class Character:
    def __init__(self, name: str):
        self.name = name
        self.color = 'green'
        # battle
        self.friendship_with_player = 0
        self.hp = 10
        self.defence = 0
        # knowledge
        self.phon = 0
        self.morph = 0
        self.synth = 0

    # for all
    def utter(self, line):
        lab = Label(f, fg=self.color, font=20, wraplength=500, justify=LEFT, text=self.name + ': ' + line)
        Q.append(lab)

    # npc only - unique for all
    def tell_skill_details(self):
        pass

    # unique for all
    def use_skill(self):
        pass

    def rise_friendship(self):
        self.friendship_with_player += 1


class Player:
    # inherited from all npc
    skills = []


# _________________________________________________BEGINNING>________________________________________________________
root = Tk()
root.geometry('800x600')
root.resizable(False, False)
root.title('имя позже придумаем')

frm1 = LabelFrame(root, width=800, height=500)

canv = Canvas(frm1,width=800, height=500)
canv.pack(fill="both", expand=True)

scrlbar = Scrollbar(canv ,orient="vertical", command=canv.yview)
scrlbar.pack(side="right", fill="y")

canv.configure(yscrollcommand=scrlbar.set)

canv.bind('<Configure>', lambda e: canv.configure(scrollregion=canv.bbox('all')))

f = Frame(canv, width=800, height=500)
canv.create_window((0, 0), window=f, anchor='nw')

frm2 = Frame(root, width=800, height=70)
btn = Button(frm2, text='Продолжить', bg='PaleGreen', fg='ForestGreen', command=OUT)

Q = deque()


# ______________________________________________window for choice_____________________________________________________

def dialogue(event):
    def first_button():
        MASHA.rise_friendship()
        dial.destroy()

    def second_button():
        MASHA.tell_skill_details()
        dial.destroy()

    dial = Toplevel(root)
    dial['bg'] = 'LightCyan'
    dial.title('Что будем делать?')
    dial.geometry('300x150+500+100')
    dial.grab_set()
    dial.resizable(False, False)
    question = Label(dial, text = '???', bg = 'LightCyan', fg = 'SteelBlue', font = ('Times New Roman', 18))
    question.pack(padx = 95, pady = 30)
    frame = Frame(dial, width = 300, height = 50, bg = 'LightCyan')
    frame.pack()
    btn1 = Button(frame, text = 'Подружимся!', bg = 'Orchid', fg = 'purple', command = first_button)
    btn1.pack(side = LEFT, padx = 10)
    btn2 = Button(frame, text = 'Узнаем скиллы!', bg = 'SlateBlue', fg = 'Navy', command = second_button)
    btn2.pack(side = RIGHT, padx = 10)

root.bind('<Return>', dialogue)

# _________________________________________________<BEGINNING________________________________________________________

MASHA = Character('Masha')
tell('story')
for i in range(10):
    tell('this is a story - jhyghwehb jkfjidhjbew nmdflgjhejwnmfd lkjihebwenmfsmdjkb hnemf ,ekjhfbnmkvjhfvb '
         'nmnvkjhfjmr kmsjbvfrmkjs bhvffnmrks fjrmv')
    MASHA.utter('I am Masha. I like iuhgyhjbjnk flfbhnksvjih ufjenkvfbhenk nvjsfkmcnfd jre grejk gewrug erukg '
                'erkugerwuguiewrg er ugre gu egue')

# ___________________________________________________END>_____________________________________________________________
frm1.pack(fill="both", expand=True)
frm2.pack(anchor='s')
btn.pack(anchor='ne', padx=10, pady=10)
root.mainloop()
# ___________________________________________________<END_____________________________________________________________
