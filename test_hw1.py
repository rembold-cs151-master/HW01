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
    def test_d_is_zero(self, capsys):
        Prob4.find_area(10,5,0)
        captured = capsys.readouterr()
        assert numcheck(float(captured.out.rstrip()),50)

    def test_d_is_A(self, capsys):
        Prob4.find_area(10,5,10)
        captured = capsys.readouterr()
        assert numcheck(float(captured.out.rstrip()), 37.5)

    def test_d_is_halfA(self, capsys):
        Prob4.find_area(10,5,5)
        captured = capsys.readouterr()
        assert numcheck(float(captured.out.rstrip()), 34.375)


class Test_Prob3:
    def test_all_evens(self, capsys):
        inputs = ['6', '-6', '18']
        with mock.patch('builtins.input', side_effect=inputs):
            Prob3.big_odd_finder()
            cap = capsys.readouterr()
            assert cap.out == 'No odd numbers found.\n'

    def test_all_odds(self, capsys):
        inputs = ['3', '-7', '1']
        with mock.patch('builtins.input', side_effect=inputs):
            Prob3.big_odd_finder()
            cap = capsys.readouterr()
            assert cap.out == '3\n'

    def test_one_odd(self, capsys):
        inputs = ['-2', '-7', '8']
        with mock.patch('builtins.input', side_effect=inputs):
            Prob3.big_odd_finder()
            cap = capsys.readouterr()
            assert cap.out == '-7\n'

    def test_two_odd(self, capsys):
        inputs = ['11', '7', '8']
        with mock.patch('builtins.input', side_effect=inputs):
            Prob3.big_odd_finder()
            cap = capsys.readouterr()
            assert cap.out == '11\n'
