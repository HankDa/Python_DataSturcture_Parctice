#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 20:55:15 2020

@author: Hank.Da
"""


"""
Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".
"""
from nose.tools import assert_equal

#solution 1 : O(n**2)
def anagram(s1,s2):
    # remove space and ignore capitalization
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    
    if len(s1) != len(s2):
        return False
    else:
        for let1 in s1:
            for let2 in s2:
                if let1 == let2:
                    s1 = s1.replace(let1,"")
                    s2 = s2.replace(let2,"")
                    print(s1,s2)
        
        if len(s1)>0 or len(s2)>0: 
            return False
       
        else: 
            return True  

#solution 2 : comparing two sorted string
def anagram2(s1,s2):
    # remove space and ignore capitalization
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    
    if len(s1) != len(s2):
        return False
    else:
        return sorted(s1) == sorted(s2)
    
#solution 3 : dictionary
def anagram3(s1,s2):    
    # remove space and ignore capitalization
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    
    if len(s1) != len(s2):
        return False
    else:
        counter={}
        
        for i in s1:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
                
        for j in s2:
            if j in counter:
                counter[j] -=1
            else:
                return False
            
        for value in counter.values():
            if value >0 : return False
            else: return True
    
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""


class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print("ALL TEST CASES PASSED")

# Run Tests
t = AnagramTest()
#t.test(anagram)
t.test(anagram3)