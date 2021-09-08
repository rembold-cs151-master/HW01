# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import pytest

import Prob2
import Prob3


def numcheck(num, ans, tol=0.02):
    return ((ans-tol) < num < (ans+tol))


class Test_Prob2:
    words = ['cold', 'good', 'bright']

    def test_negate_exists(self):
        assert "negate" in dir(Prob2), "No function called negate found. Did you name it correctly?"
    
    def test_intensify_exists(self):
        assert "intensify" in dir(Prob2), "No function called intensify found. Did you name it correctly?"
   
    def test_reinforce_exists(self):
        assert "reinforce" in dir(Prob2), "No function called reinforce found. Did you name it correctly?"

    def test_negate(self):
        sols = ['uncold', 'ungood', 'unbright']
        for word,sol in zip(self.words, sols):
            sub = Prob2.negate(word)
            assert sub.lower() == sol, f"The negation of {word} should be {sol}, but instead is {sub}."

    def test_intensify(self):
        sols = ['pluscold', 'plusgood', 'plusbright']
        for word,sol in zip(self.words, sols):
            sub = Prob2.intensify(word)
            assert sub.lower() == sol, f"The intensifying of {word} should be {sol}, but instead is {sub}."

    def test_reinforce(self):
        sols = ['doublecold', 'doublegood', 'doublebright']
        for word,sol in zip(self.words, sols):
            sub = Prob2.reinforce(word)
            assert sub.lower() == sol, f"The reinforcing of {word} should be {sol}, but instead is {sub}."

    def test_multi_modifiers(self):
        assert Prob2.reinforce(Prob2.intensify("bright")).lower() == "doubleplusbright"
        assert Prob2.intensify(Prob2.negate("bad")).lower() == "plusunbad"
        assert Prob2.reinforce(Prob2.intensify(Prob2.negate("fair"))).lower() == "doubleplusunfair"

class Test_Prob3:
    
    def test_prints_something(self, capsys):
        Prob3.print_multiples()
        captured = capsys.readouterr().out.rstrip()
        assert len(captured) > 0, "Is your code actually printing out anything from inside the function? It should be!"

    def test_multiples_of_six_or_seven(self, capsys):
        Prob3.print_multiples()
        captured = capsys.readouterr().out.rstrip()
        values = [int(n) for n in captured.split('\n')]
        for num in values:
            assert num % 6 == 0 or num % 7 == 0, f"The number {num} was printed to the screen but that is not divisible by either 6 or 7."

    def test_multiples_of_six_and_seven(self,capsys):
        Prob3.print_multiples()
        captured = capsys.readouterr().out.rstrip()
        values = [int(n) for n in captured.split('\n')]
        for num in values:
            assert not (num % 6 == 0 and num % 7 == 0), f"The number {num} was printed to the screen, but it is divisible by both 6 AND 7, and thus should not be printed."
        
