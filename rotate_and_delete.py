# As usual Babul is again back with his problem and now with numbers. He thought of an array of numbers in which he does two types of operation that is rotation and deletion. His process of doing these 2 operations are that he first rotates the array in a clockwise direction then delete the last element. In short he rotates the array nth times and then deletes the nth last element. If the nth last element does not exists then he deletes the first element present in the array. So your task is to find out which is the last element that he deletes from the array so that the array becomes empty after removing it.

# For example
# A = {1,2,3,4,5,6}.

# He rotates the array clockwise i.e. after rotation the array A = {6,1,2,3,4,5} and delete the last element that is {5} so A = {6,1,2,3,4}. Again he rotates the array for the second time and deletes the second last element that is {2} so A = {4,6,1,3}, doing these steps when he reaches 4th time, 4th last element does not exists so he deletes 1st element ie {1} so A={3,6}. So continuing this procedure the last element in A is {3}, so o/p will be 3.
 

# Input:
# The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains two lines. The first line of each test case contains an integer N. Then in the next line are N space separated values of the array A.
 

# Output:
# For each test case in a new line print the required result.
 

# Constraints:
# 1<=T<=200
# 1<=N<=100
# 1<=A[i]<=10^7
 

# Example:
# Input
# 2
# 4
# 1 2 3 4
# 6
# 1 2 3 4 5 6

# Output:
# 2
# 3

#code
t = int(input())
for i in range(t):
    n = int(input())
    l = n
    arr = input().split(' ')
    arr = [int(i) for i in arr if i.isdigit()]
    for j in range(n):
        k = l-1
        last = arr[k]
        while(k>0):
            arr[k] = arr[k-1]
            k = k-1
        arr[0] = last
        if (len(arr)>=(j+1)):
            del arr[-(j+1)]
        else:
            del arr[0]
        l = l-1
        if len(arr)==1:
            print(arr[0])
