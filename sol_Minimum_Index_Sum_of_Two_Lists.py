
class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d1 = dict()
        d2 = dict()

        for i, k in enumerate(list1):
            d1[k] = i

        for i, k in enumerate(list2):
            d2[k] = i

        keys1 = set(list(d1.keys()))
        keys2 = set(list(d2.keys()))

        mn = 2000
        res = list()

        for k in keys1 & keys2:
            mn = min(d1[k] + d2[k], mn)

        for k in keys1 & keys2:
            if d1[k] + d2[k] == mn:
                res.append(k)

        return res


args = (["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"], )
sol = Solution()
res = sol.findRestaurant(*args)
print(res)


