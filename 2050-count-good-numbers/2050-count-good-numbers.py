class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = pow(10, 9) + 7
        even_indices = (n + 1) // 2
        odd_indices = n // 2
        
        return (pow(5, even_indices, mod) * pow(4, odd_indices, mod) )% mod