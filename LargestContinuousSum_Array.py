#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 17:36:26 2020

@author: Hank.Da
"""
"""
Largest Continuous Sum

Problem

Given an array of integers (positive and negative) find the largest continuous sum.

Solution

Fill out your solution below:
"""

def large_cont_sum(arr): 

    sum_max = 0
    sum_current = arr[0]

    for num in arr[1:]:

        # if sum_current less than current number which means that sum_current is negative, then upadate sum_current to 
        # current number, in other words change the start point of continuous sum.
        sum_current = max(sum_current+num,num)
        sum_max = max(sum_current, sum_max)

    return sum_max


from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print("ALL TEST CASES PASSED")
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum)
