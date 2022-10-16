def make_bricks(small,big,goal):
    return goal - (big * 5) <= small >= goal % 5
make_bricks(3,1,8)