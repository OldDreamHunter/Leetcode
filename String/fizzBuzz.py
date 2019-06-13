# coding=utf-8
# -*- coding:utf-8 -*-
"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

"""

class solution(object):
    def fizzBuzz(self, n):
        """
        3 multiples fizz
        5 multiples buzz
        3 and 5 multiples fizzbuzz
        :return:
        """
        return ['fizz' * (not i%3) + 'buzz' * (not i%5) or str(i) for i in range(1,n+1)]


if __name__ == '__main__':
    calcSolution = solution()
    print calcSolution.fizzBuzz(10)
