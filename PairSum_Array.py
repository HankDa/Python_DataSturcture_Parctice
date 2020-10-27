#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 21:55:52 2020

@author: Hank.Da
"""

"""
Array Pair Sum

Problem

Given an integer array, output all the * *unique ** pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)
would return 2 pairs:

 (1,3)
 (2,2)
"""

def pair_sum(arr,k):
    
    if len(arr)<2:
        return 0
    # using characteristic of set to keep pair unique. 
    lookup = set()
    answer = set()
    
    for i in arr: 
        if k-i in lookup: 
            # even though there are same pair will be automatically filtered by set. 
            answer.add((i,k-i))
            print('answer', answer)
        else:
            # if not pair put it into lookup to wait pair
            lookup.add(i)
            print('lookup',lookup)
        
    
    return len(answer)


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestPair(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print ('ALL TEST CASES PASSED')
        
#Run tests
t = TestPair()
t.test(pair_sum)