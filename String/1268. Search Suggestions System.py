"""
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
 

Constraints:

1 <= products.length <= 1000
There are no repeated elements in products.
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.
"""

# The solution that I came up with, however I think the time complexity is too high
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        def checkMatch(products, keyword):
            res = []
            len_key = len(keyword)
            for product in products:
                if keyword == product[:len_key]:
                    res.append(product)
            res.sort()
            return res if len(res) <= 3 else res[:3]
        
        for i in range(1, len(searchWord)+1):
            res.append(checkMatch(products, searchWord[:i]))
        return res

# A better solution uses sorting and binary search
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    	# Sort the product list first
        products.sort()
        searchWord_len = len(searchWord)
        res = [[] for _ in range(searchWord_len)]
        
        curr = ""
        
        for char in searchWord:
            curr += char

            # Find the index of insertion using binary search. This makes looking a bit faster
            indexOfInsertion = self.binarySearch(products, curr)
            for i in range(indexOfInsertion, min(len(products), indexOfInsertion+3)):
                product = products[i]
                array_pos = len(curr)-1
                if len(res[array_pos]) < 3 and product.startswith(curr):
                    res[array_pos].append(product)
        return res
    
    
    def binarySearch(self, array, target):
        lo = 0
        hi = len(array)
        
        while lo < hi:
            mid = (lo+hi)//2
            if array[mid] < target:
                lo = mid+1
            else:
                hi = mid
        return lo