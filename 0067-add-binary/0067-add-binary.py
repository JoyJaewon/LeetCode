class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry: 
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            carry, digit = divmod(digit_a + digit_b + carry, 2)
            result.append(str(digit))

            i -= 1
            j -= 1

        return ''.join(result[::-1])
