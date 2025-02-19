# count = 0
# ans = 0

# nums = [6, 8, 10, 12, 13, 14]

# for i in range(2, len(nums)):
#     a=nums[i]
#     b=nums[i-1]
#     c=nums[i-2]
#     if a - b == b - c:
#         count += 1
#     else:
#         print("end number")
#         print(b)
#         ans += (count * (count + 1)) // 2
#         count = 0
# if count:
#     ans += (count * (count + 1)) // 2

# ordered = [5, 7, 8, 9, 10, 11, 13]

# # Straight requires at least five different ranks
# if len(ordered) >= 5:
#     straight = [ordered[0]]  # Initial value for straight

#     for i in range(1, len(ordered)):
#         print(i)
#         a = ordered[i]
#         b = ordered[i-1]
#         if a-b==1:
#             straight.append(a)
#         else:
#             # Straight already detected
#             if len(straight) >= 5:
#                 print(straight)
#                 break
#             else:
#                 straight = [ordered[i]]
#                 print(straight)
#         print("in for")
#     print("out of for")

import random
import copy

class Card():
    def __init__(self) -> None:
        self.suit = None
        self.rank = None

deck = {
    "Spades":[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 
    "Clubs":[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    "Hearts":[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 
    "Diamonds":[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
}

cards = []
for suit in deck:
    for val in deck[suit]:
        new = Card()
        new.suit=suit
        new.rank=val
        cards.append(new)

total = 6
pulls = random.sample(list(cards), total)

for x in pulls:
    print((x.rank, x.suit))