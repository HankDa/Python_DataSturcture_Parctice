#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 22:42:36 2020

@author: Hank.Da
"""

"""

Find the Missing Element

Problem

Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:

5 is the missing number

"""
import collections

def finder(arr1,arr2):

    for i in arr2:
        if i in arr1:
            arr1.remove(i) 
    return arr1[0]


#using dictionary to solve this problem
def finder2(arr1,arr2):
    
    d=collections.defaultdict(int) 
    
    for num in arr2:
        d[num] += 1
        
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -=1
            
    return None

#Using XOR to find a missing number serise of number, if the numbers are pair in serise after XOR the result should be 0
#Otherwise, it should be the value of number because it hasn't pair
def finder3(arr1, arr2): 
    result=0 
   
    # Perform an XOR between the numbers in the arrays
    for num in arr1+arr2: 
        result^=num 
        print(result)
        
    return result 

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestFinder(object):
    
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print('ALL TEST CASES PASSED')

# Run test
t = TestFinder()
t.test(finder2)
