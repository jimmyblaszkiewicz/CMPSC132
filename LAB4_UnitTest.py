import unittest 
from LAB4 import *

class EncryptTestCase(unittest.TestCase):
	"""Tests for 'LAB4.py'"""

	def test_uppercase(self):
		#test if uppercase letters stay uppercase
		self.assertEqual(encrypt("the quick brown fox jumped over the lazy dog", 8), "bpm ycqks jzwev nwf rcuxml wdmz bpm tihg lwo")

	def test_lowercase(self):
		#test if lowercase letters stay lowercase
		self.assertEqual(encrypt("THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG", 8), "BPM YCQKS JZWEV NWF RCUXML WDMZ BPM TIHG LWO")

	def test_mixed(self):
		#test mixed cases
		self.assertEqual(encrypt("tHis SenteNcE has MiXeD caSes", 8), "bPqa AmvbmVkM pia UqFmL kiAma")

	def test_wrapping(self):
		#test if z and Z + 8 (arbitrary number) wrap to h and H etc.
		self.assertEqual(encrypt("ZxqwZZZZZZ ZZzzzZzZZzZZz", 8), "HfyeHHHHHH HHhhhHhHHhHHh")

	def test_bad_message(self):
		#test to see if bad str input handles properly
		self.assertEqual(encrypt(1.232341, 4), "Invalid input")

	def test_bad_key(self):
		#test to see if bad int input handles properly
		self.assertEqual(encrypt("This is a string", 1.2), "Invalid input")

	def test_punctuation(self):
		#test to see if punctuation stays the same
		self.assertEqual(encrypt("This can change but this -> !@#$!@%#@^#%$.... will not", 5), "Ymnx hfs hmfslj gzy ymnx -> !@#$!@%#@^#%$.... bnqq sty")

	def test_bigKey(self):
		#test to see if a large (>26) key will be handled properly
		self.assertEqual(encrypt("This one has a big key", 30), "Xlmw sri lew e fmk oic")

	def test_decrypt(self):
		#test if decrypt sets the new key properly (it decrypts correctly)
		self.assertEqual(decrypt("bPqa AmvbmVkM pia UqFmL kiAma", 8), "tHis SenteNcE has MiXeD caSes")

	def test_bad_decrypt_message(self):
		#test to see if bad str input handles properly
		self.assertEqual(decrypt(1.232341, 4), "Invalid input")

	def test_bad_decrypt_key(self):
		#test to see if bad int input handles properly
		self.assertEqual(decrypt("This is a string", 1.2), "Invalid input")



if __name__ == '__main__':unittest.main(exit=False)