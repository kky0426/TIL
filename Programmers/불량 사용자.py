from itertools import product

def compare(user,ban):
    if len(user)!=len(ban):
        return False
    for i in range(len(ban)):
        if ban[i] == '*':
            continue
        if ban[i] != user[i]:
            return False
    return True



def solution(user_id, banned_id):
    answer = []
    ban_user = []
    N = len(banned_id)
    for ban in banned_id:
        temp = []
        for user in user_id:
            if compare(user,ban):
                temp.append(user)
        ban_user.append(temp)
    ban_user = [x for x in ban_user]
    result = list(product(*ban_user))
    for item in result:
        item = set(item)
        if len(item) == N and item not in answer:
            answer.append(item)

    return len(answer)
