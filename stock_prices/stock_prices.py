#!/usr/bin/python

import argparse

def find_max_profit(prices):
    # make sure the list has enough items to iterate over
    if len(prices) < 2:
        return 'Insufficient stock price data'
    else:
        # counter for buy; ignores last item (needs to be bought AND sold)
        for i in range(0, len(prices) - 2):
            # counter for sell; will iterate one less after each buy loop
            for j in range(i + 1, len(prices) - 1):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
        return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))