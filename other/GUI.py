from wx import *

class w(Frame):
    def __init__(self):
        global difficulty, x_1, x_2, x_3, difficulty_l, gameControl_l, gameControl, numberofplayers, numberofplayers_l, w_2
        difficulty = "简单"
        gameControl = "键盘"
        numberofplayers = 1
        difficulty_l = ["简单", "一般", "困难"]
        x_1 = 0
        gameControl_l = ["键盘", "鼠标"]
        x_2 = 0
        numberofplayers_l = ["1", "2", "3"]
        x_3 = 0

        super().__init__(None, title='游戏设置',
                         size=(285, 230), pos=(800, 400),
                         style=DEFAULT_FRAME_STYLE & ~MAXIMIZE_BOX & ~RESIZE_BORDER)
        p = Panel(parent=self)
        ok = Button(p, label='完成', pos=(100, 150))
        self.Bind(EVT_BUTTON, self.OK_EXIT, ok)

        self.statictext_1 = StaticText(p, label='请选择游戏难度：', pos=(10, 10))
        self.statictext_11 = StaticText(p, label="简单", pos=(110, 10))
        next_1 = Button(p, label="下一个", size=(40, 19), pos=(145, 8))
        self.Bind(EVT_BUTTON, self.click_1, next_1)

        self.statictext_2 = StaticText(p, label="请选择控制方式：", pos=(10, 30))
        self.statictext_21 = StaticText(p, label="键盘", pos=(110, 30))
        next_2 = Button(p, label="下一个", size=(40, 19), pos=(145, 28))
        self.Bind(EVT_BUTTON, self.click_2, next_2)

        # self.statictext_3 = StaticText(p, label="请选择玩家人数：", pos=(10, 50))
        # self.statictext_31 = StaticText(p, label="1", pos=(110, 50))
        # next_3 = Button(p, label="下一个", size=(40, 19), pos=(145, 50))
        # self.Bind(EVT_BUTTON, self.click_3, next_3)
        self.Show()

        # w_2 = Frame(self, title='多玩家人数设置',
        #             size=(285, 230), pos=(800, 450),
        #             style=MINIMIZE_BOX | SYSTEM_MENU | CLOSE_BOX | CLIP_CHILDREN | CAPTION)
        # p_2 = Panel(parent=w_2)

    def click_1(self, event):
        global x_1, difficulty, difficulty_l
        x_1 += 1
        if x_1 == 3:
            x_1 = 0
        x_2 = difficulty_l[x_1]
        difficulty = x_2
        self.statictext_11.SetLabelText(x_2)

    def click_2(self, event):
        global gameControl, x_2, gameControl_l
        x_2 += 1
        if x_2 == 2:
            x_2 = 0
        x_4 = gameControl_l[x_2]
        gameControl = x_4
        self.statictext_21.SetLabelText(x_4)

    # def click_3(self, event):
    #     global numberofplayers, x_3, numberofplayers_l, w_2
    #     x_3 += 1
    #     if x_3 == 3:
    #         x_3 = 0
    #     x_6 = numberofplayers_l[x_3]
    #     numberofplayers = x_6
    #     self.statictext_31.SetLabelText(x_6)
    #     if x_6 >= "2":
    #         w_2.Show()
    #     else:
    #         w_2.Hide()

    def OK_EXIT(self, event):
        self.Hide()
        app.ExitMainLoop()


def wx_gui():
    global difficulty, app
    app = App()
    w_1 = w()
    app.MainLoop()


def difficultToChoose():
    global difficulty, r_1, r_2, speed, gameControl, numberofplayers,n
    wx_gui()
    match(difficulty, gameControl):
        case "简单", "键盘":
            r_1 = 3
            r_2 = 6
            speed = 1.78
            growthOfLifeValueRatio = 0.7
            reduceLifeValueRatio = 0.315
        case "简单", "鼠标":
            r_1 = 5
            r_2 = 8
            speed = 2
            growthOfLifeValueRatio = 0.5
            reduceLifeValueRatio = 0.36
        case "一般", "键盘":
            r_1 = 5
            r_2 = 8
            speed = 2
            growthOfLifeValueRatio = 0.5
            reduceLifeValueRatio = 0.345
        case "一般", "鼠标":
            r_1 = 9
            r_2 = 12
            speed = 3.25
            growthOfLifeValueRatio = 0.3
            reduceLifeValueRatio = 0.39
        case "困难", "键盘":
            r_1 = 9
            r_2 = 12
            speed = 3.25
            growthOfLifeValueRatio = 0.245
            reduceLifeValueRatio = 0.375
        case "困难", "鼠标":
            r_1 = 12
            r_2 = 15
            speed = 3.50
            growthOfLifeValueRatio = 0.215
            reduceLifeValueRatio = 0.458

    p = [difficulty, gameControl, r_1, r_2, speed, int(
        numberofplayers), growthOfLifeValueRatio, reduceLifeValueRatio]
    return p


# difficultToChoose()
