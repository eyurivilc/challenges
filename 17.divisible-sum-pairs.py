n = 6
k = 3
arr = [1, 3, 2, 6, 1, 2]


def divisibleSumPairs(n, k, ar):
    counter = 0
    for i, num in enumerate(ar):
        for j in range(1, n):
            if i < j:
                print(f"i={i}  arr[i]={ar[i]}  arr[j]={ar[j]}")
                pairs_sum = ar[i] + ar[j]
                print(f"Sum of pairs= {pairs_sum}")

                if pairs_sum % k == 0:
                    counter += 1

    print(counter)


divisibleSumPairs(n, k, arr)
