from collections import Counter

def sortKey(hand: str):
    hand = hand.replace('T', chr(ord('9') + 1))
    hand = hand.replace('J', chr(ord('2') - 1))
    hand = hand.replace('Q', chr(ord('9') + 3))
    hand = hand.replace('K', chr(ord('9') + 4))
    hand = hand.replace('A', chr(ord('9') + 5))

    counter = Counter(hand)

    # find most common card that isn't J and replace all J's with it
    target = list(counter.keys())[0]

    for card in counter:
        if card != '1':
            if counter[card] > counter[target] or target == '1':
                target = card

    if '1' in counter and target != '1':
        counter[target] += counter['1']
        del counter['1']

    sv = sorted(counter.values())
    if sv == [5]: return (7, hand)
    if sv == [1,4]: return (6, hand)
    if sv == [2,3]: return (5, hand)
    if sv == [1,1,3]: return (4, hand)
    if sv == [1,2,2]: return (3, hand)
    if sv == [1,1,1,2]: return (2, hand)
    if sv == [1,1,1,1,1]: return (1, hand)

hands = []

with open('input.txt', 'r') as f:
    for line in f:
        hand, bid = line.split()
        hands.append((hand, bid))

total = 0
hands = sorted(hands, key = lambda h: sortKey(h[0]))

for i, hand in enumerate(hands):
    total += (i+1) * int(hand[1])

print(total)
