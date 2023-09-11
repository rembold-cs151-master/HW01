# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!

import Prob2

class Test_Prob2:
    
    def test_prints_something(self, capsys):
        Prob2.divisible_by_six_or_seven(6,100)
        captured = capsys.readouterr().out.rstrip()
        assert len(captured) > 0, "Is your code actually printing out anything from inside the function? It should be!"

    def test_multiples_of_six_or_seven(self, capsys):
        Prob2.divisible_by_six_or_seven(6,60)
        captured = capsys.readouterr().out.rstrip()
        values = [int(n) for n in captured.split('\n')]
        for num in values:
            assert num % 6 == 0 or num % 7 == 0, f"The number {num} was printed to the screen but that is not divisible by either 6 or 7."

    def test_multiples_of_six_and_seven(self,capsys):
        Prob2.divisible_by_six_or_seven(6,60)
        captured = capsys.readouterr().out.rstrip()
        values = [int(n) for n in captured.split('\n')]
        for num in values:
            assert not (num % 6 == 0 and num % 7 == 0), f"The number {num} was printed to the screen, but it is divisible by both 6 AND 7, and thus should not be printed."
        
    def test_within_thresholds(self, capsys):
        Prob2.divisible_by_six_or_seven(6,60)
        captured = capsys.readouterr().out.rstrip()
        values = [int(n) for n in captured.split('\n')]
        for num in values:
            assert 6 <= num and num <= 60, f"With inputs of 6 and 60, you should only have numbers in the list between 6 and 60, but you currently have the number {num} in the list."

    def test_no_duplicates(self, capsys):
        Prob2.divisible_by_six_or_seven(6,60)
        captured = capsys.readouterr().out.rstrip()
        values = [int(n) for n in captured.split('\n')]
        assert len(values) == len(set(values)), "You seem to be printing out some duplicate values to the screen? Each number should only appear once."

    def test_returns_something(self):
        sol = Prob2.divisible_by_six_or_seven(1,100)
        assert isinstance(sol, int), "Is your code returning an integer type object? It should be!"

    def test_returns_correct_count(self):
        ranges = [(40,60), (6, 60), (7,100), (13,63)]
        counts = [5, 16, 25, 14]
        for r,c in zip(ranges, counts):
            sol = Prob2.divisible_by_six_or_seven(*r)
            assert sol == c, f"For a range from {r[0]} to {r[1]}, your function should have printed out {c} numbers and returned a value of {c}. But it is instead returning {sol}."

