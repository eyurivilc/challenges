
# 9
a = [10, 5, 20, 20, 4, 5, 2, 25, 1]  # output 2 4


def breakingRecords(scores):
    n = len(scores)
    highestCounter, lowestCounter = 0, 0
    highestScore = scores[0]
    lowestScore = scores[0]

    if n >= 1 and n <= 1000:
        for i in range(n):
            if scores[i] >= 0 and scores[i] <= pow(10, 8):

                if highestScore < scores[i]:
                    highestScore = scores[i]
                    highestCounter += 1

                if lowestScore > scores[i]:
                    lowestScore = scores[i]
                    lowestCounter += 1

    print(f"H: {highestCounter}  L: {lowestCounter}")


breakingRecords(a)
