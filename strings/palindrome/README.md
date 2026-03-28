# palindrome problem

## Problem Description
Given an integer x, return true if x is a palindrome, and false otherwise.

 


 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?

## Approach

first instinct was solving the problem where x is a string, thinking about this problem led me to think about iteratiing across all the string placeholders one from the beginning and one sstarting from the last character moving 
each step towards the middle until checking every two characters that are on the opposite sides together.

after that i ttried solving it as x is integer where i thought about the base case where negative numbers can't be part of a palindrome at all since putting the negative sign "minus" only from the left side of the number, and i tried thinking about a mathmatical way to be able to extract the opposite number from the original number.

---

## Solution Explanation

1. Step 1: creating original variable that holds the value of x, and variable reversed_num which i will be adding the original digit's to the reversed one in a reverse manner_
2. Step 2: if condition negative numbers return False
3. Step 3: while original number is not 0 keep going 
	4. Step 3.1: dig variable holds the units digit of the original number
	5. Step 3.2:  we multiply the reversed number by 10 to move all digits one place to the left and add a new unit value (digit)
	6. Steo 3.3:  we cut the units digit out from the original number to move on to the next digit
7. Step 4: we check if the reversed number equals the x(original number)
	8. Step 4.1: if yes return True
	9. Step 4.2: if not return False
	
my approach was talking the original number and flipping it from the end to the beginning in the numbers order and re-checking it with the original number because a palindrome number can be checked from both sides and shohuld be the same number read form both sides

---

## Complexity Analysis

running across all x digits:
- Time Complexity: O(n)
making other mathmatical calculations: O(1), inside the loop: O(n)
therefore total of time complexity is: O(n)

using variables without any strings/arrays building from scratch:
therefore space complexity is: O(1)

---

## Example

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.



---
								of ar	
## Key Takeaways

i was familiar with the problem before and solved it in the past, i do refreshed my memory about all kinds of ways that can be used in this question to solve this problem, it's very important to alwasy remember that thier is a lot of ways to solve any kind of problem that we encounter it dosen't matter where, i solved this problem first in a version where i assumed that x is a string showing that also by using string "arrays" and checking every 2 opposite digits can also give us a good solution for the problem even creating an array where it is not needed because of the structure of the strings in python we gave up this way for a good and optimal solution, in the end thinking about it where x is an integer can be more of a challenge because you need to think in a different matter where you need to do mathmatical manipulations in order to solve your problem correctly.

---
