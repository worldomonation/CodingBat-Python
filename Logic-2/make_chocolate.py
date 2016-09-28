def make_chocolate(small, big, goal):
    if goal == 0:
        return -1
    elif goal < 5:
        return -1 if small < goal else goal
    else:
        if goal - (big * 5) == 0:
            return 0
        else:
            while goal > 4 and big != 0:
                goal = goal - 5
                big = big - 1
            if small >= goal:
                return goal
            else:
                return -1
