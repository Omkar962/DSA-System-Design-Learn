# 1. Right-Angled Triangle of Stars

# n = 4

# *
# **
# ***
# ****

class Solution:
    def rightAngledTriangle(self, n: int) -> list[str]:
        ans=[]

        for i in range(1,n+1):
            ans.append("*"*i)
        return ans

# Time & Space Complexity

# Time complexity: O(n^2) Because creating each string of length i takes O(i), and the total work is 1 + 2 + ... + n = O(n^2).

# Space complexity: O(n^2)  The output itself contains all stars across all rows, so this is optimal for returning the full triangle.


# 2. Inverted Right-Angled Triangle

# n = 4

# ****
# ***
# **
# *

class Solution:
    def invertedTriangle(self, n: int) -> list[str]:
        ans=[]
        for i in range(n,0,-1):
            ans.append("*"*i)
        return ans

# Time & Space Complexity
# Time: O(n^2) You generate n strings, and the total number of stars created is n + (n-1) + ... + 1, which is quadratic.

# Space: O(n^2) The output itself stores all rows, so this is optimal for returning the full triangle.


# 3. Pyramid of Stars


# n = 3

#   *
#  ***
# *****

class Solution:
    def pyramidOfStars(self, n: int) -> list[str]:
        ans=[]
        for i in range(1,n+1):
            ans.append((n-i)*" "+(2*i-1)*"*")
        return ans

# Time & Space Complexity

# Time: O(n^2) Each of the n rows constructs a string of length up to 2n - 1, so total work is quadratic.

# Space: O(n^2) The returned list stores all rows, and the total output size is proportional to the pyramid size.


# 4. Inverted Pyramid 

# n = 3

# *****
#  ***
#   *


class Solution:
    def invertedPyramid(self, n: int) -> list[str]:
        ans=[]
        for i in range(n,0,-1):
            ans.append((n-i)*" " +(2*i-1)*"*")
        return ans


# Time & Space Complexity

# Time: O(n^2) You build n strings, and each row can be up to O(n) characters long.

# Space: O(n^2) The output itself contains n rows with total size proportional to the number of characters printed.


# 5. Hollow Square

# n = 4

# ****
# *  *
# *  *
# ****


class Solution:
    def hollowSquare(self, n: int) -> list[str]:
        ans=[]
        for i in range(1,n+1):
            if i==1 or i==n:
                ans.append(n*"*")
            else:
                ans.append("*"+(n-2)*" "+"*")
        return ans


# Time & Space Complexity

# Time: O(n^2) You build n strings, each of length n.

# Space: O(n^2) The output itself contains n strings of length n.


# 6. Hollow Triangle

# *
# **
# * *
# *  *
# *****


class Solution:
    def hollowTriangle(self, n: int) -> list[str]:
        ans=[]
        for i in range(1,n+1):
            if i==1 or i==n:
                ans.append("*"*i)
            else:
                ans.append("*"+" "*(i-2)+"*")
        return ans


# Time & Space Complexity

# Time: O(n^2) because the total number of characters across all rows is 1 + 2 + ... + n.
# Space: O(n^2) for storing the output strings.


# 7. Diamond Pattern

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

class Solution:
    def diamondPattern(self, n: int) -> list[str]:
        ans=[]
        for i in range(1,n+1):
            ans.append(" "*(n-i)+"*"*(2*i-1))

        for i in range(n-1,0,-1):
            ans.append(" "*(n-i)+"*"*(2*i-1))

        return ans


# Time & Space Complexity

# Time: O(n^2) Each of the 2n-1 rows is built using string multiplication proportional to n.
# Space: O(n^2) The output itself contains 2n-1 strings, each up to length 2n-1.



# 8. Floyd's Triangle

# n = 3

# Row 1:  1
# Row 2:  2  3
# Row 3:  4  5  6

class Solution:
    def floydsTriangle(self, n: int) -> list[list[int]]:
        ans=[]
        j=1
        for i in range(1,n+1):
            row=[]
            for _ in range(i):
                row.append(j)
                j+=1
            ans.append(row)
        return ans

# Time & Space Complexity

# Time: O(n^2) — you generate a total of 1 + 2 + ... + n = n(n+1)/2 numbers.
# Space: O(n^2) — the output triangle stores all generated numbers.
  

# 9. Mirror Pattern

# n = 3

# Row 1:  1
# Row 2:  121
# Row 3:  12321


class Solution:
    def mirrorNumberPattern(self, n: int) -> list[str]:
        ans=[]
        for i in range(1,n+1):
            row=""
            for j in range(1,i+1):
                row+=str(j)
            for j in range(i-1,0,-1):
                row+=str(j)
            ans.append(row)
        return ans

# Time & Space Complexity

# Time Complexity: O(n^2) Each row can be up to length 2i - 1, and you build n rows.
# Space Complexity: O(n^2) The output itself stores all rows, which is necessary.


# 10. Butterfly Pattern

# *    *
# **  **
# ******
# **  **
# *    *

class Solution:
    def butterflyPattern(self, n: int) -> list[str]:
        ans=[]
        for i in range(1,n+1):
            ans.append("*"*i+" "*(2*(n-i))+"*"*i)
        
        for i in range(n-1,0,-1):
            ans.append("*"*i+" "*(2*(n-i))+"*"*i)
        return ans


# Time & Space Complexity

# Time complexity: O(n^2) Each row is built in O(n) time, and there are O(n) rows.
# Space complexity: O(n^2) The output itself stores 2n - 1 strings, each of length 2n.



# 11. HourGlass Pattern

# *****
#  ***
#   *
#  ***
# *****

class Solution:
    def hourglassPattern(self, n: int) -> list[str]:
        ans=[]
        for i in range(n,0,-1):
            ans.append(" "*(n-i)+"*"*(2*i-1))
        for i in range(2,n+1):
            ans.append(" "*(n-i)+"*"*(2*i-1))

        return ans

# Time & Space Complexity

# Time: O(n^2) You generate 2n - 1 strings, and each string can be up to O(n) long.
# Space: O(n^2) The output itself dominates space usage, which is optimal since you must return all rows.



# 12. Spiral Number Pattern

# 1 2 3
# 8 9 4
# 7 6 5

# Input: n = 3

# Output: [[1,2,3],[8,9,4],[7,6,5]]


class Solution:
    def spiralNumberPattern(self, n: int) -> list[list[int]]:
        grid=[[0]*n for _ in range(n) ]
        top,bottom,left,right=0,n-1,0,n-1
        num=1

        while top<=bottom and left<=right :
            for c in range(left,right+1):
                grid[top][c]=num
                num+=1
            top+=1

            for r in range(top,bottom+1):
                grid[r][right]=num
                num+=1
            right-=1

            if top<=bottom:
                for c in range(right,left-1,-1):
                    grid[bottom][c]=num
                    num+=1
                bottom-=1

            if left<=right:
                for r in range(bottom,top-1,-1):
                    grid[r][left]=num
                    num+=1
                left+=1
        return grid 


# Time & Space Complexity
# Time Complexity: O(n^2) Every cell is filled exactly once.
# Space Complexity: O(n^2) The output grid requires n^2 space, which is optimal since the problem asks you to return the full matrix.