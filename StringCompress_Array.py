#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 19:54:15 2020

@author: Hank.Da
"""

"""

String Compression

Problem

    Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

    The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

"""

import collections

def compress(s):
    
    if s:
    
        # Using default dict to avoid key errors
        d=collections.defaultdict(int) 

        #using dictionary to record each character and counts
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1

        items = d.items() 
        string_res = ""
        
        #join key and value to a string
        for item in items:
            string_res += (item[0]+str(item[1]))

        return string_res
    
    else: 
        return ""
    
    
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress)