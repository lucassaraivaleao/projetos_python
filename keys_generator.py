# import lib for random keys
from random import sample as sp
# defining letters and numbers to compose the password
keys = 'abcdefghijklmnopqrstuvxywz'
keys_upper = keys.upper()
numbers_symbols = '0123456789[]{}*;/,_-'
# junction of letters and numbers
all_keys = (keys+keys_upper+numbers_symbols)
# defining lenght of password
key_lenght = 18
# defining password
password = "".join(sp(all_keys, key_lenght))
# Show full password
print(password)
