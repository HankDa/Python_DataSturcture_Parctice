#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 18:32:51 2020

@author: Hank.Da
"""

"""
Sentence Reversal

Problem

Given a string of words, reverse all the words. For example:

Given:

'This is the best'

Return:

'best the is This'

As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

'  space here'  and 'space here      '

both become:

'here space'

"""
def rev_word(s):
    
    ls_str = s.split(" ")

    ls_str = [i for i in ls_str if i] 
    ls_str_new =[]

    for i in range(1,len(ls_str)+1):
        ls_str_new.append(ls_str[-1*i])

    res = " ".join(ls_str_new)
    return res


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print("ALL TEST CASES PASSED")
        
# Run and test
t = ReversalTest()
t.test(rev_word)