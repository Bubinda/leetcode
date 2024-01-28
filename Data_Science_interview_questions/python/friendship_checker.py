#  Write a function to list the pairs of friends with their corresponding timestamps of the friendship beginning and the timestamp of the friendship ending.

# For this Facebook data science interview question, you’re given two lists of dictionaries representing friendship beginnings and endings: friends_added and friends_removed. Each dictionary contains the user_ids and created_at time of the friendship beginning /ending.

# Input:

# friends_added = [
#     {'user_ids': [1, 2], 'created_at': '2020-01-01'},
#     {'user_ids': [3, 2], 'created_at': '2020-01-02'},
#     {'user_ids': [2, 1], 'created_at': '2020-02-02'},
#     {'user_ids': [4, 1], 'created_at': '2020-02-02'}]

# friends_removed = [
#     {'user_ids': [2, 1], 'created_at': '2020-01-03'},
#     {'user_ids': [2, 3], 'created_at': '2020-01-05'},
#     {'user_ids': [1, 2], 'created_at': '2020-02-05'}]
# Output:

# friendships = [{
#     'user_ids': [1, 2],
#     'start_date': '2020-01-01',
#     'end_date': '2020-01-03'
#   },
#   {
#     'user_ids': [1, 2],
#     'start_date': '2020-02-02',
#     'end_date': '2020-02-05'
#   },
#   {
#     'user_ids': [2, 3],
#     'start_date': '2020-01-02',
#     'end_date': '2020-01-05'
#   },
# ]


from collections import defaultdict
from pprint import pprint

def list_friendships(friends_added, friends_removed):
    # Create a defaultdict to store friendship information
    friendships_dict = defaultdict(list)

    # Process friends_added list
    for added in friends_added:
        key = tuple(sorted(added['user_ids']))
        friendships_dict[key].append({'date': added['created_at'], 'event': 'start'})

    # Process friends_removed list
    for removed in friends_removed:
        key = tuple(sorted(removed['user_ids']))
        friendships_dict[key].append({'date': removed['created_at'], 'event': 'end'})

    # Create the final list of friendships
    friendships = []
    for key, events in friendships_dict.items():
        events.sort(key=lambda x: x['date'])

        for i in range(0, len(events), 2):
            friendship = {
                'user_ids': list(key),
                'start_date': events[i]['date'],
                'end_date': events[i + 1]['date'] if i + 1 < len(events) else None
            }
            friendships.append(friendship)

    return friendships

# Example usage:
friends_added = [
    {'user_ids': [1, 2], 'created_at': '2020-01-01'},
    {'user_ids': [3, 2], 'created_at': '2020-01-02'},
    {'user_ids': [2, 1], 'created_at': '2020-02-02'},
    {'user_ids': [4, 1], 'created_at': '2020-02-02'}]

friends_removed = [
    {'user_ids': [2, 1], 'created_at': '2020-01-03'},
    {'user_ids': [2, 3], 'created_at': '2020-01-05'},
    {'user_ids': [1, 2], 'created_at': '2020-02-05'}]

friendships = list_friendships(friends_added, friends_removed)
pprint(friendships)
