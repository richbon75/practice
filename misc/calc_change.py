
def calc_change(amount, change=None, remaining_amount=None, remaining_coins=None):
    '''print all the ways the change can be made'''
    coins = [25, 10, 5, 1]

    # initialize values, if necessary
    if change is None:
        change = dict()
    if remaining_amount is None:
        remaining_amount = amount
    if remaining_coins is None:
        remaining_coins = coins

    if len(remaining_coins) == 0:
        if remaining_amount == 0:
            print(change)
        return

    coin = remaining_coins[0]
    max_coins = remaining_amount // coin
    for use_coins in range(max_coins+1):
            change[coin] = use_coins
            calc_change(amount = amount,
                        change = change,
                        remaining_amount = remaining_amount-coin*use_coins,
                        remaining_coins = remaining_coins[1:])
            change.pop(coin)
 
        
