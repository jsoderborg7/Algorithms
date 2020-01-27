#!/usr/bin/python

import argparse

def find_max_profit(prices):

  # Stock price math flow using the readme example
  # example [1050, 270, 1540, 3800, 2]
  # function should iterate through numbers like this
  # 1050 Buy (no profit)
  # 270 Buy (no profit)
  # subtract previous number(s) from current number
  # 270-1050 = -780
  # 1540-270, 1540-1050 (profit on both)
  # 3800-1540, 3800-270, 3800-1050 (profit on all, largest so far)
  # 2-any previous number (no profit)

# start with first index
  current_min_price = prices[0]
# profit starts at 0
  max_profit = 0
# loop through all prices
  for i in range(len(prices)):
# current price listed
    current_price = prices[i] 
# check for lowest price, reassign
    if current_price < current_min_price:
      if max_profit <= 0:
        max_profit = current_price - current_min_price
# reassign min price
      current_min_price = current_price
# find current max profit
    elif current_price - current_min_price > max_profit:
      max_profit = current_price - current_min_price
  return max_profit



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))