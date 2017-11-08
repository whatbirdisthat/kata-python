# Python Bowling Game Kata

## A variant on the Bowling Game Kata on python

As the journey is important, a decision here is to keep
the project free from depencies.

This means our tests are themselves written from the ground up,
there are no "how do I write unit tests in python?" stuff,
it is all - "I need to do <this>"

## The journey is important.

# Running the tests

To reduce the amount of pollution on your laptop, a container
is provided with some convenience scripts to start the environment
and run the tests.

The construction of these is part of the kata. I found that 
building a container for each kata was great for developing a deep
knowledge of containerisation in general.

To start the container:

```bash
  ./start-container.sh
```

To run the tests:

```bash
  ./run-tests.sh
```

