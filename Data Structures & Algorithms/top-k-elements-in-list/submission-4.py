class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lis = {}
        maxed = []

        for i in nums:
            lis[i] = lis.get(i, 0)+1

        for j in range(k):
            x = max(lis, key=lis.get)
            maxed.append(x)
            lis.pop(x)

        return maxed