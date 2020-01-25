# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import mock
import pytest
import os

import Prob3
import Prob4

def numcheck(num, ans, tol=0.02):
    return (ans*(1-tol) < num < ans*(1+tol))

class Test_WrittenWork:
    def test_pdf_present(self):
        assert os.path.isfile('HW1.pdf') == True


class Test_Prob4:
    def test_B_big_d_zero(self, capsys):
        Prob4.find_area(2,3,0)
        captured = capsys.readouterr()
        assert numcheck(float(captured.out.rstrip()),13)

    def test_B_big_d_halfA(self, capsys):
        Prob4.find_area(2,3,1)
        captured = capsys.readouterr()
        assert numcheck(float(captured.out.rstrip()), 11)

    def test_B_big_d_A(self, capsys):
        Prob4.find_area(3,5,3)
        captured = capsys.readouterr()
        assert numcheck(float(captured.out.rstrip()), 25)

    def test_A_big_d_zero(self, capsys):
        Prob4.find_area(6,3,0)
        captured = capsys.readouterr()
        assert numcheck(float(captured.out.rstrip()),45)

    def test_A_big_d_halfB(self, capsys):
        Prob4.find_area(2,1,0.5)
        captured = capsys.readouterr()
        assert numcheck(float(captured.out.rstrip()), 4.5)

    def test_A_big_d_B(self, capsys):
        Prob4.find_area(10,5,5)
        captured = capsys.readouterr()
        assert numcheck(float(captured.out.rstrip()), 100)

class Test_Prob3:
    def test_all_evens(self, capsys):
        inputs = ['6', '-6', '18']
        with mock.patch('builtins.input', side_effect=inputs):
            Prob3.big_odd_finder()
            cap = capsys.readouterr()
            assert cap.out == 'No odd numbers found.\n'

    def test_all_odds(self, capsys):
        inputs = [
                ['3', '-7', '1'],
                ['1', '-3', '7'],
                ['-1', '5', '3']
                ]
        sols = ['3', '7', '5']

        for _input,sol in zip(inputs,sols):
            with mock.patch('builtins.input', side_effect=_input):
                Prob3.big_odd_finder()
                cap = capsys.readouterr()
                assert cap.out.rstrip() == sol

    def test_one_odd(self, capsys):
        inputs = [
                ['-2', '-7', '8'],
                ['7', '8', '-4'],
                ['4', '8', '11']
                ]
        sols = ['-7', '7', '11']
        for _input, sol in zip(inputs,sols):
            with mock.patch('builtins.input', side_effect=_input):
                Prob3.big_odd_finder()
                cap = capsys.readouterr()
                assert cap.out.rstrip() == sol

    def test_two_odd(self, capsys):
        inputs = [
                ['11', '7', '8'],
                ['3', '9', '2'],
                ['20', '3', '13'],
                ]
        sols = ['11', '9', '13']
        for _input, sol in zip(inputs,sols):
            with mock.patch('builtins.input', side_effect=_input):
                Prob3.big_odd_finder()
                cap = capsys.readouterr()
                assert cap.out.rstrip() == sol
