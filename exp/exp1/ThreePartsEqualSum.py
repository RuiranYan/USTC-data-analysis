# 给定一个整数数组 A，只有我们可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
#
# 形式上，如果我们可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。
a = [0,2,1,-6,6,-7,9,1,2,0,1]
class Solution:
    def canThreePartsEqualSum(self, A: list[int]) -> bool:
        for i in range(len(A)):
            s1 = 0
            for k in range(i+1):
                s1 = s1 + A[k]
            for j in range(i + 1, len(A)):
                s2 = 0
                s3 = 0
                for k in range(i + 1, j):
                    s2 = s2 + A[k]
                for k in range(j, len(A)):
                    s3 = s3 + A[k]
                if (s1 == s2 & s2 == s3):
                    return True
        return False
print(Solution.canThreePartsEqualSum(Solution,a))