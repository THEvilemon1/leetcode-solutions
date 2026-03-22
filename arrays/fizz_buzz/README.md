# FizzBuzz problem

## Problem Description
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

Constraints:

1 <= n <= 104

## Approach



-first thing came to mind was how to create the array filled with the right and fitting values, i thought about handling each value from the smallest to the biggest, one by one in other words: beginning from the first index i=0 going upwards to i=n and running all the tests that i created in my if-else if conditions and after that inserting each answer to the array right after identifing it.


---

## Solution Explanation

1. Step 1: creating a loop that runs across all n values 
2. Step 2: running if-else if conditions if(index value is divided by 3 and 5 append FizzBuzz to the array) ..etc
3. Step 3: returning the array as an output

my approach works because it runs on each index and runs all tests required in order to ensure what exactly we should insert that block socket of array (4 possible outcomes including all cases) running this tests for each index in the array to ensure right insertions in each step and at the end of the loop we return the new array that we built along the way.

---

## Complexity Analysis

running a loop across all n values(indexes) therefore:
- Time Complexity: O(n)

creating an empty array and appending certain values n times according to the loop therefore:
- Space Complexity: O(n)



---

## Example

Input: n=6

Output: ["1","2","Fizz","4","Buzz","Fizz"]


---

## Key Takeaways

i learned how to create custom arrays according to the conditions that i want to set making an array that submits to your rules and works exactly how we want it to work depending the need and neccessity of that "new product" - custom array 
one insight that came to mind: that we can create this own made arrays to help us in solving a bigger problems that we want to behave with certain indexes or values in a different way from other ones

---