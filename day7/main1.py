from typing import List, Tuple
from collections import Counter

RANKS = {
    'fivekind': 6,
    'fourkind': 5,
    'fullhouse': 4,
    'threekind': 3,
    '2pair': 2,
    '1pair': 1,
    'high': 0,
}

CARDS = { 'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8,
         '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, 'J': 0 }

def handType(cards: str) -> str | None:
    counts = Counter(cards)
    topFreq = counts.most_common()[0][1]
    uniqCount = len(set(cards))

    if uniqCount == 1: return 'fivekind'
    if uniqCount == 2 and topFreq == 4: return 'fourkind'
    if uniqCount == 2 and topFreq == 3: return 'fullhouse'
    if uniqCount == 3 and topFreq == 3: return 'threekind'
    if uniqCount == 3 and topFreq == 2: return '2pair'
    if uniqCount == 4 and topFreq == 2: return '1pair'
    if uniqCount == len(cards): return 'high'

    return None

def sortHands(hands):
    swaps = True
    while swaps:
        swaps = False
        for i in range(len(hands) - 1):
            a = hands[i][0]
            b = hands[i+1][0]
            for j in range(5):
                if CARDS[a[j]] > CARDS[b[j]]:
                    hands[i], hands[i+1] = hands[i+1], hands[i]
                    swaps = True
                    break
                elif CARDS[a[j]] < CARDS[b[j]]:
                    break
    return hands

total = 0
groupedHands: List[List[Tuple[str, int]]] = [[] for _ in range(len(RANKS))]

with open('input.txt', 'r') as f:
    for line in f:
        cards, bid = line.split()
        t = handType(cards)
        if t is not None:
            groupedHands[RANKS[t]].append((cards, int(bid)))

actualRank = 1
for rank, hands in enumerate(groupedHands):

    if len(hands) == 1:
        total += actualRank * hands[0][1]
        actualRank += 1
    else:
        sortHands(hands)
        for hand in hands:
            total += actualRank * hand[1]
            actualRank += 1

print(total)
