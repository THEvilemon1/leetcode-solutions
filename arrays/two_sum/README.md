# TwoSum problem

## Problem Description
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

## Approach

my approach was first looking at the easiest way to solve the problem which looking at the complement of each number in each socket in the array nums and trying to find it in the array in order to find two pieces of the puzzle that sums up to the target value

---

## Solution Explanation

Step 1: creating an empty hashmap dictionary 
Step 2: creating a loop that runs on all the values and indexes of the array nums
Step 3: calculating complement number per iteration
Step 4: check if the complement found in the hashmap
	4.1: if yes: return the the value of the key that was found with the index i as "[value, i]"
	4.2: if no: save the last num value of the array as a key with value i in the hashmap and keep iterating in the loop
Step 5:return [] beacue no two numbers sums up to the target value

in my approach you can clearly see the structure works block by block where we find out the complement number first after that check if it exists in our hashmap if it does that means we found the two numbers we are searching for that sums up to the target and return them in the correct manner otherwise we save the last checked number in our hashmap as a key with his index value which gives us a strong foundation to search correctly across all the values that were given in the array

---

## Complexity Analysis

i choose to write my code to answer the follow up question in the description in the first place to find a better time complexity for my program

running a loop across all n values of nums therefore:
- Time Complexity: O(n)
searching in hashmap where the values are known is time complexty of O(1)
- therfore total time Complexity of: O(n)

creating an empty hashmap and appending keys and values n times according to the loop therefore:
- Space Complexity: O(n)



---

## Example

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]



---

## Key Takeaways

today i learned 2 very useful tools that considered as fundamentals in order to work with python
i learned how to create dictionaries in python, i was familiar with hasmaps from Data Structers course that i took a year ago in my academic persuit
i learned how to iterate across indexes and values simultaneously in a loop and utilizee this ability to create dictionaries that are very helpful and needed in this very solution

---