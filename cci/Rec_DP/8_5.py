def multiply(a, b):
    if a > b:
        n, m = a, b
    else:
        n, m = b, a
    product = 0
    #ループの度に倍にしている
    while m:
        bit = m & -m
        print('m', bin(m))
        print('-m', bin(-m))
        print('bit', bin(bit))
        #1の部分を消している
        m ^= bit
        exponent = bit.bit_length()-1
        product += n << exponent
    return product

import unittest

class Test(unittest.TestCase):
  def test_multiply(self):
    #self.assertEqual(multiply(2, 2), 4)
    #self.assertEqual(multiply(1, 125), 125)
    self.assertEqual(multiply(7, 11), 77)
    #self.assertEqual(multiply(10000000010, 21), 210000000210)

if __name__ == "__main__":
  unittest.main()

