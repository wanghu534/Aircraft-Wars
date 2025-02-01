import maliang
from other import wx_GUI

def maliang_gui():
    global difficulty, gameControl
    size = 570, 460
    title = "游戏设置"
    window = maliang.Tk(size, title=title)
    window.resizable(width=False,height=False)
    window.center()

    cv = maliang.Canvas(master=window, bg="white")
    cv.place(width=570, height=460)

    ok = maliang.Button(cv,size=(100, 40),position=(235, 350), text="开始游戏", command=lambda: window.destroy())
    
    statictext_1 = maliang.Text(cv, text='请选择游戏难度：', position=(50, 50))
    statictext_2 = maliang.Text(cv, text='请选择控制方式：', position=(50, 100))

    box_1 = ("简单", "一般", "困难")
    box_2 = ("键盘", "鼠标")

    comboBox_1 = maliang.ComboBox(cv, size=(90, 28), position=(220, 50), text=box_1)
    comboBox_2 = maliang.ComboBox(cv, size=(90, 28), position=(220, 100), text=box_2)

    window.mainloop()
    if comboBox_1.get() == None:
        difficulty = "简单"
    else:
        difficulty = box_1[comboBox_1.get()]
    if comboBox_2.get() == None:
        gameControl = "键盘"
    else:
        gameControl = box_2[comboBox_2.get()]

def main():
    global difficulty, gameControl

    maliang_gui()
    p = wx_GUI.difficultToChoose(difficulty, gameControl)
    return p

