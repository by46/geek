"""Design a Simple Automaton (Finite State Machine)

https://www.codewars.com/kata/5268acac0d3f019add000203

Create a finite automaton that has three states. Finite automatons are the same as finite state machines for our purposes.

Our simple automaton, accepts the language of A, defined as {0, 1} and should have three states,
q1, q2, and q3.

q1 is our start state. We begin reading commands from here.
q2 is our accept state. We return true if this is our last state.

q1 moves to q2 when given a 1, and stays at q1 when given a 0.
q2 moves to q3 when given a 0, and stays at q2 when given a 1.
q3 moves to q2 when given a 0 or 1.

Our automaton should return whether we end in our accepted state, or not (true/false.)

Here's an example.

a = Automaton()
# Do anything you need to set up this automaton's states.
is_accepted = a.read_commands(["1", "0", "0", "1", "0"])
We make these transitions based on the input of ["1", "0", "0", "1", "0"],

1 q1 -> q2
0 q2 -> q3
0 q3 -> q2
1 q2 -> q2
0 q2 -> q3
We end in q3, which is not our accept state, so return false.

The input of ["1", "0", "0", "1", "0"] would cause us to return false, as we would end in q3.

I have started you off with the bare bones of the Automaton object.

class Automaton(object):

    def __init__(self):
        self.states = []

    def read_commands(self, commands):
        # Return True if we end in our accept state, False otherwise

my_automaton = Automaton()

# Do anything necessary to set up your automaton's states, q1, q2, and q3.
You will have to design your state objects, and how your Automaton handles transitions.
Also make sure you set up the three states, q1, q2, and q3, for the myAutomaton instance.
The test fixtures will be calling against myAutomaton.

As an aside, the automaton accepts an array of strings, rather than just numbers,
or a number represented as a string, because the language an automaton can
accept isn't confined to just numbers. An automaton should be able to accept any 'symbol.'

Here are some resources on DFAs (the automaton this Kata asks you to create.)

http://www.cs.odu.edu/~toida/nerzic/390teched/regular/fa/dfa-definitions.html

http://en.wikipedia.org/wiki/Deterministic_finite_automaton

http://www.cse.chalmers.se/~coquand/AUTOMATA/o2.pdf


"""
Q1 = 'q1'
Q2 = 'q2'
Q3 = 'q3'


class Automaton(object):
    """

    Basic Example:
    >>> automation = Automaton()
    >>> automation.read_commands(["1", "0", "0", "1", "0"])
    False

    """

    def __init__(self):
        self.states = []

    def read_commands(self, commands):
        # Return True if we end in our accept state, False otherwise
        current_state = Q1
        self.states.append(current_state)
        for command in commands:
            if current_state is Q1:
                if command == '1':
                    current_state = Q2
            elif current_state is Q2:
                if command == '0':
                    current_state = Q3
            else:
                current_state = Q2
            self.states.append(current_state)

        return current_state == Q2


if __name__ == '__main__':
    import doctest

    doctest.testmod()
