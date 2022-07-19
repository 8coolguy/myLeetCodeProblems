#i need to start doing some medioums on codesignal and need to start the hackerRank practice
def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    if max(yourLeft,yourRight) == max(friendsLeft,friendsRight) and min(friendsLeft,friendsRight)==min(yourLeft,yourRight):
        return True
    else:
        return False

