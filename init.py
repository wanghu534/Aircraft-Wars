from other.GUI import difficultToChoose  # 游戏初始化
def main():
    l = difficultToChoose()
    print(l)
    gameControl, r_1, r_2, speed, numberofplayers, growthOfLifeValueRatio, reduceLifeValueRatio = l[
        1], l[2], l[3], l[4], l[5], l[6], l[7]
    speedIncrease = speed


if __name__ == "__main__":
    main()
