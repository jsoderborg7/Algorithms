#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # n is the number of rounds
  # keep the combos played
  results = []
  # there are 3 possible options for play
  options = ['rock', 'paper', 'scissors']

  def play(options_chosen, rounds_left):
    # if there are no rounds left, add the option chosen to the results array, otherwise, it will just keep going
    if rounds_left == 0:
      results.append(options_chosen)
      return
    for i in options:
      play(options_chosen + [i], rounds_left - 1)
    
  play([],n)
  return results
    


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')