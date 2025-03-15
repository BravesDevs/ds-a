class Solution:
    def suggestedProducts(self,products, searchWord):
        products.sort()
        res = []
        for i in range(1,len(searchWord)+1):
            products = list(filter(lambda x: x.startswith(searchWord[:i]), products))
            res.append(products[:3])
        return res
            
            
sln = Solution()
print(sln.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))