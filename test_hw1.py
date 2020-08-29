# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import mock
import pytest
import os

import Prob2
from newspeak import negate, intensify, reinforce

def numcheck(num, ans, tol=0.02):
    return (ans*(1-tol) < num < ans*(1+tol))

class Test_WrittenWork:
    def test_pdf_present(self):
        assert os.path.isfile('HW1.pdf') == True, "You are missing the written pdf or have given it a different name!"

class Test_Problem2:
    def test_0_length(self):
        submission = Prob2.distance(0,0)
        assert numcheck(submission, 0), "Points at the origin should be returning a length of 0."

    def test_2_positive(self):
        submission = Prob2.distance(3,4)
        assert numcheck(submission, 5), "A point located at (3,4) should be a distance 5 away."

    def test_1_pos_1_neg(self):
        submission = Prob2.distance(-3, 6)
        assert numcheck(submission, 6.7082), "The point located at (-3,6) should be 6.7082 away."

    def test_2_negative(self):
        submission = Prob2.distance(-5, -12)
        assert numcheck(submission, 13), "A point located at (-5, -12) should be a distance 13 away."


class Test_Newspeak:
    words = ['cold', 'good', 'bright']

    def test_negate(self):
        sols = ['uncold', 'ungood', 'unbright']
        for word,sol in zip(self.words, sols):
            sub = negate(word)
            assert sub.lower() == sol, f"The negation of {word} should be {sol}, but instead is {sub}."

    def test_intensify(self):
        sols = ['pluscold', 'plusgood', 'plusbright']
        for word,sol in zip(self.words, sols):
            sub = intensify(word)
            assert sub.lower() == sol, f"The intensifying of {word} should be {sol}, but instead is {sub}."

    def test_reinforce(self):
        sols = ['doublecold', 'doublegood', 'doublebright']
        for word,sol in zip(self.words, sols):
            sub = reinforce(word)
            assert sub.lower() == sol, f"The reinforcing of {word} should be {sol}, but instead is {sub}."

    def test_multi_modifiers(self):
        assert reinforce(intensify("bright")).lower() == "doubleplusbright"
        assert intensify(negate("bad")).lower() == "plusunbad"
        assert reinforce(intensify(negate("fair"))) == "doubleplusunfair"

