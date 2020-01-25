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
        assert os.path.isfile('HW1.pdf') == True, "You are missing the written pdf or have given it a different name!"


class Test_Prob4:
    def report(self, args, sol, usersol):
        return f"\n When run with parameters of {args}, problem should print a value of {sol} but is instead printing {usersol}."

    def test_B_big_d_zero(self, capsys):
        Prob4.find_area(2,3,0)
        captured = capsys.readouterr()
        assert numcheck(float(captured.out.rstrip()),13), self.report([2,3,0],13, captured.out.rstrip())

    def test_B_big_d_halfA(self, capsys):
        Prob4.find_area(2,3,1)
        captured = capsys.readouterr()
        assert numcheck(float(captured.out.rstrip()), 11), self.report([2,3,1],11, captured.out.rstrip())


    def test_B_big_d_A(self, capsys):
        Prob4.find_area(3,5,3)
        captured = capsys.readouterr()
        assert numcheck(float(captured.out.rstrip()), 25), self.report([3,5,3],25, captured.out.rstrip())


    def test_A_big_d_zero(self, capsys):
        Prob4.find_area(6,3,0)
        captured = capsys.readouterr()
        assert numcheck(float(captured.out.rstrip()),45), self.report([6,3,0],45, captured.out.rstrip())


    def test_A_big_d_halfB(self, capsys):
        Prob4.find_area(2,1,0.5)
        captured = capsys.readouterr()
        assert numcheck(float(captured.out.rstrip()), 4.5), self.report([2,1,0.5],4.5, captured.out.rstrip())


    def test_A_big_d_B(self, capsys):
        Prob4.find_area(10,5,5)
        captured = capsys.readouterr()
        assert numcheck(float(captured.out.rstrip()), 100), self.report([10,5,5],100, captured.out.rstrip())


class Test_Prob3:
    def report(self, numbers, sol, usersol):
        return f"The numbers {numbers} were entered of which {sol} should have been printed. But instead {usersol} was printed."

    def test_all_evens(self, capsys):
        inputs = [['6', '-6', '18'],
                ['2', '8', '100'],
                ['-4', '-6', '-8']
                ]
        for _input in inputs:
            with mock.patch('builtins.input', side_effect=_input):
                Prob3.big_odd_finder()
                cap = capsys.readouterr()
                usersol = cap.out.rstrip()
                assert usersol == 'No odd numbers found.', self.report(_input, "No odd numbers found.", usersol)

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
                usersol = cap.out.rstrip()
                assert usersol == sol, self.report(_input, sol, usersol)

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
                usersol = cap.out.rstrip()
                assert usersol == sol, self.report(_input, sol, usersol)

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
                usersol = cap.out.rstrip()
                assert usersol == sol, self.report(_input, sol, usersol)
