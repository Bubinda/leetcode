user_ids = [103, 105, 105, 107, 106, 103, 102, 108, 107, 103, 102]
tips = [2, 5, 1, 0, 2, 1, 1, 0, 0, 2, 2]

def most_tips(user_ids, tips):
    user_tips = {}

    for user, tip in zip(user_ids,tips):
        if user not in user_tips:
            user_tips[user] = tip
        else:
            user_tips[user] += tip
    most_tip = [x[0] for x in sorted(user_tips.items(),key=lambda x:x[1], reverse=True)]
    return most_tip[0]




def most_tips_2(user_ids, tips):
    user_tips = {}

    for user, tip in zip(user_ids, tips):
        if user not in user_tips:
            user_tips[user] = tip
        else:
            user_tips[user] += tip

    # Find the user with the maximum tip using the max function
    most_tip_user = max(user_tips.items(), key=lambda x: x[1])

    return most_tip_user[0]


print(most_tips_2(user_ids,tips))
print(most_tips(user_ids,tips))

