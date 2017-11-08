#!/usr/bin/env python

from BowlingGame import BowlingGame
from Assert import Assert

def testZero():
    game = BowlingGame()
    Assert.Equal(0, game.score())

def testGutterGame():
    game = BowlingGame()
    for i in range(20):
        game.bowl(0)
    Assert.Equal(0, game.score())


tests = {
        "Can report zero score on init": testZero,
        "Can report a gutter game as 0": testGutterGame
        }

for eachTest in tests:
    testName = eachTest
    testResult = "\033[32m\u2713\033[0m"
    try:
        tests[eachTest]()
    except:
        testResult = "\033[31m\u2717\033[0m"

    print("{} - {}".format(testResult, testName))
