# Tested 2016-06-08 22:07

def make_bricks(small, big, goal):
    if (big*5 + small < goal) or (small < goal%5):
        return False
    return True
