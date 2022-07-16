class Solution:
    def fillCups(self, amount: List[int]) -> int:
        time = 0
        amount.sort(reverse=True)
        while(amount[0]):
            if amount[1]:
                amount[0], amount[1] = amount[0] - 1, amount[1] - 1
            else:
                time += amount[0]
                break
            amount.sort(reverse=True)
            time += 1
        return time