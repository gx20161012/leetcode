class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_length = len(a)
        b_length = len(b)
        c_list = list()
        carry = 0
        n = int(a[a_length-1]) + int(b[b_length-1])
        if n <= 1:
            c_list.append(n)
            carry = 0
        else:
            c_list.append(n-2)
            carry = 1
        i = a_length - 2
        j = b_length - 2
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                m = int(a[i]) + int(b[j]) + carry
                if m <= 1:
                    c_list.append(m)
                    carry = 0
                    i -= 1
                    j -= 1
                else:
                    c_list.append(m-2)
                    carry = 1
                    i -= 1
                    j -= 1
            elif i >= 0 and j < 0:
                m = int(a[i]) + carry
                if m <= 1:
                    c_list.append(m)
                    carry = 0
                    i -= 1
                else:
                    c_list.append(m-2)
                    carry = 1
                    i -= 1
            elif i < 0 and j >= 0:
                m = int(b[j]) + carry
                if m <= 1:
                    c_list.append(m)
                    carry = 0
                    j -= 1
                else:
                    c_list.append(m-2)
                    carry = 1
                    j -= 1
        if carry == 1:
            c_list.append(1)
        return "".join([str(x) for x in c_list[::-1]])
s = Solution()
a = "1111"
b = "1111"
print(s.addBinary(a, b))
