#!/usr/bin/env python

from BowlingGame import BowlingGame
from Assert import Assert

def testZero():
    game = BowlingGame()
    Assert.Equal(0, game.score())

testZero()
