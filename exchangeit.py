"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Brantley G. Gusler
Date: 1/19/2022
"""

import currency

a = input('3-letter code for original currency: ')
src = str(a)
b = input('3-letter code for the new currency: ')
dst = str(b)
c = input('Amount of the original currency: ')
amt = float(c)
result = round(currency.exchange(src, dst, amt),3)
print('You can exchange '+str(amt)+' '+str(src)+' for '+str(result)+' '+str(dst)+'.')
