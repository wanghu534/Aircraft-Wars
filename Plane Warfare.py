from init import *
from cpgzh import *
from random import randint
TITLE = '飞机大战'  # 设置标题
WIDTH = 640  # 设置宽度
HEIGHT = 720  # 设置高度
game_state = 'start'
diamond = Actor('diamond.png', [randint(0, WIDTH), randint(-500, -250)])
bg = Actor('background.png', [WIDTH / 2, HEIGHT])
bg1 = Actor('background1.png', [WIDTH / 2, bg.y - HEIGHT])
player = Actor('player' + str(randint(1, 2)) + '.png', [320, 650])
player_centre_point = Actor('player_centre_point', [player.x, player.y])
player_lifeValue = Actor('lifevalue_full.png', [player.x - 64, player.y])
n = False
isInjured = False


class my_rock(Actor):

    def __init__(self):
        super().__init__(  # 继承父类Actor的初始化方法
            'rock' + str(randint(0, 4)) + '.png',
            [randint(0, WIDTH), randint(-250, -100)])

    def rock():
        global rockFormation, r_1, r_2, time, speedIncrease, rocks
        rockFormation = True
        if game_state == "play":
            for i in range(randint(r_1 // 2, r_2 // 2)):  # 产生随机岩石
                rock = my_rock()
                rocks.append(rock)
            time += 0.5
            speedIncrease += 0.03

    def rockDetection():
        global score, game_state, rocks, bullets, n, isInjured, lifeValue, growthOfLifeValueRatio, reduceLifeValueRatio
        for rock in rocks:  # 通过遍历列表来检测岩石是否与子弹、玩家发生碰撞
            for bullet in bullets:
                if rock.collidepoint([bullet.x, bullet.y - 27]) and bullet.y > -10:
                    sounds.expl.play()
                    score += 0.25 * speedIncrease * 0.3
                    if lifeValue < 45:
                        lifeValue += speedIncrease * growthOfLifeValueRatio
                    rock.image = 'rock_expl.png'
                    n = True
                    bullets.remove(bullet)
            if rock.collidepoint([player_centre_point.x, player_centre_point.y]):
                score -= speedIncrease * 0.135
                if score < 0:
                    score = 0
                if rock.image != "rock_expl.png":
                    m = list(rock.image)
                    # print(m)
                    k = int(m[4]) + 3
                    # print(k)
                else:
                    k = randint(2, 5)
                lifeValue -= k * speedIncrease * reduceLifeValueRatio
                rock.image = 'rock_expl.png'
                clock.schedule(injured, 0.57)
                isInjured = True
                n = True
            if n:
                rocks.remove(rock)
                n = False
        if lifeValue < 10:
            lifeValue += 0.015
        elif lifeValue < 15:
            lifeValue += 0.008
        elif lifeValue < 20:
            lifeValue += 0.005
        elif lifeValue < 25:
            lifeValue += 0.001


def draw():
    global game_state, score, rocks, time, bulletNumber, bullets, speedIncrease, isInjured, lifeValue, rockFormation
    screen.clear()
    if game_state == 'start':
        screen.blit(  # 绘制玩法和标题
            'background.png', (0, 0))
        screen.draw.text('飞机大战', (170, 150), fontname='font_1.ttf',
                         color=("yellow"), fontsize=70)
        screen.draw.text('按下空格键开始!', (170, 270),
                         fontname='font_1.ttf', color=('red'), fontsize=40)
        screen.draw.text('游戏玩法:', (225, 495),
                         fontname='font_1.ttf', color=('green'), fontsize=43)
        screen.draw.text('按WASD或上下左右键移动,', (155, 550), fontname='font_1.ttf', color=('green'),
                         fontsize=25)
        screen.draw.text('得到钻石和击碎岩石,', (190, 580), fontname='font_1.ttf', color=('green'),
                         fontsize=25)
        screen.draw.text('来获得分数!', (245, 610),
                         fontname='font_1.ttf', color=('green'), fontsize=25)
        screen.draw.text('v0.5.0', (0, HEIGHT - 25),
                         fontname='font.ttf', fontsize=25)
        if keyboard.space:  # 按下空格键开始游戏
            rocks = []  # 创建一个列表来存储岩石变量
            bullets = []  # 创建一个列表来存储岩石变量
            lifeValue = 30
            score = 0  # 初始化得分
            time = 0  # 初始化时间
            rockFormation = False
            game_state = 'play'
            music.play('bg.mp3')

    elif game_state == 'play':
        bg.draw()  # 游戏中绘制角色
        bg1.draw()
        diamond.draw()
        for bullet in bullets:
            bullet.draw()
        player.draw()
        player_lifeValue.draw()
        player_centre_point.draw()
        if rockFormation:
            for rock in rocks:
                if rock.y < HEIGHT + 100 and rock.image != 'rock_expl.png':
                    rock.draw()
                    rock.y += speedIncrease * 1.5
        if isInjured:
            c = "red"
        else:
            c = "yellow"
        screen.draw.text('分数:' + str(round(score, 1)), (5, 0), fontname='font_1.ttf', color=(c),
                         fontsize=27)
        screen.draw.text('所坚持的时间:' + str(time), (3.5, 30), fontname='font_1.ttf', color=('green'),
                         fontsize=25)

    elif game_state == 'over':
        music.stop()  # 停止音乐
        screen.blit(  # 绘制图像
            'background.png', (0, 0))
        player.draw()
        screen.draw.text('游戏结束!', (190, 170),
                         fontname='font_1.ttf', color=('red'), fontsize=60)
        if score < 0:
            score = 0
        screen.draw.text('你的分数是:' + str(round(score, 1)), (205, 420), fontname='font_1.ttf', color=('green'),
                         fontsize=35)
        screen.draw.text('所坚持的时间:' + str(round(time, 1)), (205, 470), fontname='font_1.ttf', color=('green'),
                         fontsize=35)
        screen.draw.text('按下空格键重新开始!', (125, 560), fontname='font_1.ttf', color=('purple'),
                         fontsize=40)
        if keyboard.space:  # 按下空格键重新初始化并开始
            time = 0
            score = 0
            lifeValue = 30
            bullets = []
            player.x = 320
            player.y = 650
            player.image = 'player' + str(randint(1, 2)) + '.png'
            rocks = []
            bulletNumber = 0
            isInjured = False
            game_state = 'play'
            music.play('bg.mp3')


def update():
    global game_state, score, gameControl, bulletNumber, isInjured, lifeValue
    if game_state == 'play':
        if gameControl == "键盘":
            if keyboard[keys.A] or keyboard.left:  # 键盘WASD或上下左右控制飞船移动
                if keyboard[keys.A] and keyboard[
                        keys.W] or keyboard.left and keyboard.up:
                    player.y -= speed * 1.3
                    player.x -= speed * 1.3
                elif keyboard[keys.A] and keyboard[
                        keys.S] or keyboard.left and keyboard.down:
                    player.y += speed * 1.3
                    player.x -= speed * 1.3
                else:
                    player.x -= speed * 1.3
            elif keyboard[keys.D] or keyboard.right:
                if keyboard[keys.D] and keyboard[
                        keys.W] or keyboard.right and keyboard.up:
                    player.y -= speed * 1.3
                    player.x += speed * 1.3
                elif keyboard[keys.D] and keyboard[
                        keys.S] or keyboard.right and keyboard.down:
                    player.y += speed * 1.3
                    player.x += speed * 1.3
                else:
                    player.x += speed * 1.3
            elif keyboard[keys.W] or keyboard.up:
                player.y -= speed * 1.3
            elif keyboard[keys.S] or keyboard.down:
                player.y += speed * 1.3

        for bullet in bullets:
            bullet.y -= 6
            if bullet.y < -20:
                bullets.remove(bullet)

        if player.x < 0:  # 让玩家无法飞出屏幕
            player.x = 0
        elif player.x > WIDTH:
            player.x = WIDTH
        diamond.y += 1.25  # 钻石角色的移动
        if diamond.collidepoint([player.x, player.y]):  # 检测钻石是否与玩家碰撞
            diamond.x = randint(0, WIDTH)
            diamond.y = randint(-500, -250)
            score += 2

        bg.y += speedIncrease  # 设置背景持续滚动
        bg1.y += speedIncrease
        if bg.y > HEIGHT + HEIGHT / 2:
            bg.y = bg1.y - HEIGHT
        if bg1.y > HEIGHT + HEIGHT / 2:
            bg1.y = bg.y - HEIGHT

        if lifeValue < 0:  # 检测得分是否小于0，如果则GAME OVER
            game_state = 'over'
            player.image = "player_expl.png"
            music.stop()
            sounds.player_expl.play()
        if rockFormation:  # 检测岩石与子弹、玩家的碰撞
            my_rock.rockDetection()

        if keyboard[keys.K]:
            game_state = 'over'
            player.image = "player_expl.png"
            music.stop()
            sounds.player_expl.play()

        player_centre_point.x = player.x
        player_centre_point.y = player.y
        player_lifeValue.x = player.x + 64
        player_lifeValue.y = player.y

        if lifeValue <= 30 * 0.8:
            player_lifeValue.image = "lifevalue_80%.png"
        if lifeValue <= 30 * 0.6:
            player_lifeValue.image = "lifevalue_60%.png"
        if lifeValue <= 30 * 0.4:
            player_lifeValue.image = "lifevalue_40%.png"
        if lifeValue <= 30 * 0.2:
            player_lifeValue.image = "lifevalue_20%.png"
        if lifeValue >= 30 * 1.25:
            player_lifeValue.image = "lifevalue_125%.png"
        if lifeValue >= 30 * 1.5:
            player_lifeValue.image = "lifevalue_150%.png"
        if lifeValue == 30:
            player_lifeValue.image = "lifevalue_full.png"


def on_mouse_move(pos):  # 鼠标控制
    global game_state, gameControl
    if game_state == "play" and gameControl == "鼠标":
        player.x = pos[0]
        player.y = pos[1]


def bulletGenerated():
    global bullets
    if game_state == "play":
        bullet = Actor("bullet.png", [player.x, player.y])
        bullets.append(bullet)


def injured():
    global isInjured
    isInjured = False


clock.schedule_interval(my_rock.rock, 0.5)  # 设置每0.5秒生成岩石
clock.schedule_interval(bulletGenerated, 0.4)  # 设置每0.4秒生成子弹

go()
