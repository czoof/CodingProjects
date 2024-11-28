#Practice leetcode algorithms and problems

#Use this when you need both the index and the value of each element.
nums = [6, 5, 4, 8]
for i, num in enumerate(nums):
    print(f"Index: {i}, Value: {num}")

#Use this when you only need the value of each element and don't care about the index.
nums = [6, 5, 4, 8]
for num in nums:
    print(f"Value: {num}")


#Use this when you only need the index or if you want both the index and the value but prefer manual indexing.
nums = [6, 5, 4, 8]
for i in range(len(nums)):
    print(f"Index: {i}, Value: {nums[i]}")


#two sum practice
nums = [1, 2, 3, 4]
target = 5

for i in range(len(nums)):##finding the index in the range of the length of the numbers
        ##which means i is the index, and nums[i] is the value pair

    for j in range(i+1, len(nums)): #j is the index of i+1. We use i+1 instead of just i because when we are comparing the nums, we need to compare
        #the value of i to the next number in the list. Ex: if we had just i, then 1 is being compared to itself. The problem with this is 
        #we are only trying to see if 2 separate indicies add up to the target, aka 1,2 or 2,3. If we just put i instead of i+1 and the target
        #happened to be 4, then element 2 would compare to itself because 2+2 = 4, and we would end up with an output of [1,1] which is not what we want

        if nums[i] + nums[j] == target: #asking if the values of i and the values of j add up to the target.
            print(f"Indices: {i}, {j}")
            break
        #if you need access to the index's of a list, or change the list, or modify the list, then you use for i in (len(nums)). if you only need access to the values of a list
        #then use for i in nums
#end of two sum

#list practice
nums = [6, 5, 4, 8] ##program that takes a list of nums, and outputs how many numbers in that list are less than each number. Ex: in this list right here,
#numbers 5 and 4 are both less than 6 therefore the output for 6 would be 2 because 2 numbers(5 and 4) are less than 6. Same thing for number 5, the only
#number less than 5 is 4 in the list, so the output for 5 would be 1.

output = []#create empty list in which we append the outputs to later

for i, num in enumerate(nums): ##for the index, in the range of the length of our number list. we use two for loops here because we have to check if each 
    #number is less than the other. if we only had one, we would only had one for loop, we would only be able to check if that value is < itself which
    #we would never be true. 
    count = 0  #set out to 0
    for j, num in enumerate(nums): 
        if j != i and nums[j] < nums[i]:  #check if index j is not the same number as index i. If it is not, then we check if the values of those indexes
            #are less than the other. the way nested for loops works is, the inner loop iterates all of the values and compares them with the outside loop
            #value. once the inner loop reaches the end of the nums list, we go back to the outside loop. The outside loop now goes to the second number
            #which is 5, and the inner loop restarts the process of comparing 5 to each value in nums. Then once again after it compares each value, then
            #the outer loop will go to 4, etc. Once the outer loop iterates over the entire list, the program ends.

            count += 1   #if they are, we add one to count
    output.append(count) #add the number count to the list. if 6 has 2 numbers less than it, then 2 will be outputted in the index where 6 is. This works
    #because the list is empty, so since we are starting from left to right when iterating over the list, the append lines up properly with each index 
    #and value that is in the list. Ex: we start with 6, and 2 numbers are less than 6. Therefore, '2' will be added to the list. After the loop ends,
    #we switch to 5, and since 5 has 1 number less than it, it gets appended into the list. Every addition to the empty list aligns with the proper index
    #and value of the nums list because we are doing everything in order
print(nums)
print(output)
#end of list practice



#start of palindrome leetcode program
x = 2112 #can use any number to test if its a palindrome

original_nums = str(x)  #convert the nums to a string
reverse_nums = original_nums[::-1]  #reverse the nums 
if original_nums == reverse_nums: #check if the original numbers equal the reverse numbers
    print(f"{x} is a palindrome")
else:
    print(f"{x} is not a palindrome")
#end of palindrome assignment


#Start of leetcode longest common prefix assignment
class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 1: #if the length of the list only = 1, then we return an empty string because their are no prefixs to check
            return strs[0] 
        
        prefix = strs[0]  #set prefix to the first index of the first list
        count = 1  #initialize the count variable and set it to 1
        
        while count <= len(prefix): #main loop, while the count variable is less than or equal to the lenght of the 
            common_prefix = prefix[:count] #takes the characters only in the first count characters of the first string in strs
            for i in range(1, len(strs)):  #for loop to get the range of 1, to the lenght of the strings
                if not strs[i].startswith(common_prefix): #if the value of every string after the first one does not start with the first prefix of 
                    #the first string inside the list, then we return the prefix up to count - 1
                    return prefix[:count-1] if count > 1 else ""#if count is 1 or less, then we return an empty string indicating no common prefix exists
            count += 1  #increment count after the loop to keep the loop going
        
        return strs

# Test the function with a specific input
solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  # Expected: ["flower", "flow", "flight"]
#end of leetcode longest common prefix assignment

#start of valid parentheses program
#this is a program in which you have three options: ( ) [ ] { }. our job is to determine if they are in proper order for example () is true
#[] is true ([) is false because the one in the middle doesnt finish before the outside parenthesis closes. ()[]{} is true )( is false [} is false
#{[]} is true because they are in a proper order 
class Solution:
    def isValid(self, s:str) -> bool:

        stack = [] #initialize the stack for the program, we use this to track the outputs of parenthesis

        for i in s:  #for the value inside of the input 
            if i not in ')]}': #if i is not either )]}, then we append i to the stack because it means that i has to eaqual either ([{.
                stack.append(i)
            
            elif stack:   #if i does equal )]}, then we pop out the last value inside of the stack. This is because say we so far have ([, because the next
                #input is either )]} given how we are here in the first place, then we assign the last value in the stack which is [ to x. from here,
                #because we have x = [, we can now check if x = '[' and i != ']'. This is saying if x = [ which it is, if the next input is NOT ], then
                #we are done with the program. Ex so far we has ([, if the next input is either ) or }, then we are done, because [ never properly ends with ]
                x = stack.pop()
                if (x == '(' and i != ')') or (x == '[' and i != ']') or (x == '{' and i != '}'):
                    return False
                
            else:
                return False
            
        return False if stack else True
#end of valid parenthesis program


#start of largest odd number sequence program 
#program to find the largest odd number sequence from input ex: 321fgw6543rrr1234 the largest odd number sequence would be 6543
word = input("Enter a string: ")

reversed_word = word[::-1]
odd_numbers = []
current_number = ""

for char in reversed_word: #for the value inside the reversed
    if char.isdigit(): #if the character is a diget then
        current_number = char + current_number  #assign current_number = the value in the reversed list + the current_number. NOTE SINCE THE WORD IS A STRING TO BEGIN WITH,
        #DOING CURRENT_NUMBER = CHAR + CURRENT_NUMBER MEANS YOU ARE CONCATINATING THE STRING AND NOT ADDING THE NUMBERS. THEREFORE IT THE CURRENT NUMBER IS 1, AND THE CHAR IS 2,
        #IT WOULD CONCATINATE 1 AND 2 MAKING IT 12
    else:  #if the value in the reversed list is not a digit then
        if current_number:  #if their is a new current number, then
            if int(current_number) % 2 == 1:  #we check if the entire number sequence is odd
                odd_numbers.append(int(current_number)) #if it is odd, then we add it to the odd numbers list
            current_number = ""  #set current_number back to an empty string so we can repeat the loop

if current_number and int(current_number) % 2 == 1: #checks the final number sequence. when you reach the end of the for loop. if the input string ends with digits, then we need that
    #factored in our program. without this line, the final number sequence would not be checked or added to the odd_numbers list as it wouldnt be followed by a non-digit character to 
    #trigger the else condition
    odd_numbers.append(int(current_number)) #if the above line is true, then again we add the current number to the list

if odd_numbers:  #checks if their are any odd numbers inside the list
    largest_odd_number = max(odd_numbers)  #assigning the largest odd number sequence inside the list to the biggest number to get proper output for the program
    print("Largest odd number sequence:", largest_odd_number)  
else:
    print("No odd number sequences found.")
#end of largest odd number sequence program

#start of leetcode remove duplicates from sorted array
#in the sorted array, find the unique numbers so that we get a list of non repeated numbers. ex in the list [0,0,1,1,1,1,1,1,2,3,4,5,6,6] the output should be [0,1,2,3,4,5,6]
#brute force
#iterate through the array and point out each unique number
#append the number to a new list
#if that number is not in the new list then we append it to the list
class Solution(object):
    def removeDuplicates(self, nums):

        list1 = [] #initialize a list to use later
        count = 0 #initialize count variable and set it to 0
        for i in range(len(nums)):  #for loop taking the range of the length of the nums 
            if nums[i] not in list1:  #if each value inside of nums is not in the list
                list1.append(nums[i]) #then we append that value. For example if we have a list [0,0,0,1,2,3] then we check first if 0 is in the list, since it is not, we append it to the list
                #then after that we go through the loop again and check if the next value is inside the list which is 0. Since 0 is already in the list, we skip this value.
                nums[count] = nums[i] #initialises nums[count] with nums[i]. By doing this, you are able to retain the unique elements in the lists initial positions up to count.
                count+=1 #if we do append a number to the list, then the count variable increases.

        return count
#end of leetcode remove duplicates from sorted array

#Start of Remove element program
#given an array nums for example [0,1,2,2,3,0,4,2] and a val = 2, we need to return all values in nums that do not equal 2
#for example the output of this solution would be 5 with the numbers equaling [0,1,3,0,4,2]
#another example nums = [3,2,2,3] with a value=3. Output would be 2, nums=[2,2]
#brute force
#create a new list
#iterate over the array and check if that specific value is equal to the target value
#for example if the example is [0,1,2,2,3,0,4,2] and a val = 2. I need to check each item in the array and if it does not equal 2, I will add it to a new list.
#then count each index that is in the new list, so with [0,1,3,0,4,2] the values would output as 6
#WE ONLY CARE ABOUT THE NUMBER OF ELEMENTS THAT DO NOT EQUAL THE VAL WHICH IS WHY WE OUTPUT COUNT AND DONT CARE ABOUT THE ACTUAL NUMBERS IN THE LIST
class Solution(object):
    def removeElement(self, nums, val): 

        count = 0 #initialize count to 0 
        for i in range(len(nums)): #for loop iterating over the array of numbers
            if nums[i] != val: #if each value in nums does not equal the value,
                nums[count] = nums[i] #we then assign nums at index count to the value of which ever number in nums is not equal to val
                count+=1 #we then increment count + 1

        return count
#end of remove element program

#start of Find the Index of the First Occurrence in a String program
#needle is a substring of haystack for example if haystack = "sadbusted" and needle = "sad", then we return the first occurance of needle in haystack which would be at index 0
#another example if haystack = "leetcode" and needle = "leeto", then we return -1 because leeto is not in leecode
#brute force 
#we need to first implement if their is no substring in haystack
#we next need to check if the complete substring word is actually inside of the main word
class Solution(object):
    def strStr(self, haystack, needle):
        
        if needle not in haystack: #if the needle string is not in the haystack string
            return -1 #then we return -1
        else:
            x = (haystack.index(needle)) #if the string is inside the haystack string, then we assign x with the index of the needle string inside haystack
            return x
#end of Find the Index of the First Occurrence in a String program        

#start of search insert position leetcode
#given an array of sorted integers with a target value, return the index if the target is found. If the target is not found, then return the index of where that targer would be inside the list
#for example if I have a list [1,3,5,6] and the target = 5, we would output 2, because that is the index of where 5 is inside of the list
#another example if I have a list [1,3,5,6] and the target = 2, the output would be 1 because that is where 2 would be in the list

#brute force
class Solution(object):
    def searchInsert(self, nums, target):
        
        for i in range(len(nums)): #for loop iterating over the numbers inside of nums
            if nums[i] == target: #if the value inside the loop is equal to the target we are assigned
                return i #then we return the index where the value is
        
        nums.append(target) #if the target doesnt exist inside of the array nums, then as shown here, we append the target to the array nums
        x = sorted(nums)  #then we sort out the array so we get the numbers in nums to be in order
        y = x.index(target)  #then we get the index of the target so we can find where it would be if it was placed inside of the array
        return(y)
#end of insert position leetcode program

#start of plus one program
class Solution(object):
    def plusOne(self, digits):
        
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        # When all elements were 9, we add 1 at the beginning of the array
        return [1] + digits

#Start of sqrt leetcode problem
#given a positive integer x, return the square root of x roundded down to the nearest integer. The returned integer should be positive as well. 
#ex if I have an input x that is equal to 4, the output would be 2 because the square root of 4 = 2.
#another ex if I have an input x that is equal to 8, the square root is 2.82842 therefore the output is 2
import math
class Solution(object):
    def mySqrt(self, x):
        
        result = math.sqrt(x) #we use math.sqrt to find the square root of the number that we are given
        result = math.floor(result) #we then use math.floor to floor the result that we are given
        result = int(result) #then we convert the result into an integer and return it
        return result 

#you are climbing a staircase, it takes n steps to reach the top. You can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#ex n = 2. The output would be 2 because there are 2 ways of climbing to the top. 1 step + 1 step, or 2 steps
#So if we had n = 4, the ways to climb would be 1:step+step+step+step, 2:2steps+2steps. 3:2steps+1step+1step 4:1step+1step+2steps
#So if we had n=5, their would be 8 ways to climb
#if we had n=6, their would be 13 ways to climb
#if we had n=7, their would be 21 ways to climb 
#from this, we can see that each sequence is the sum of the prev 2 terms
#ex 2+1=3, 3+2=5, 5+3=8, 8+5=13, 21+13=34
