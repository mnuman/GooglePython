import ex9_7
import unittest

class TestEX97UnitTest(unittest.TestCase):
  def test_TooShortAWord(self):
    r = ex9_7.hasTripleDouble('AABBC')
    self.assertFalse(r)

  def test_MatchingWord(self):
    r = ex9_7.hasTripleDouble('AABBCC')
    self.assertTrue(r)

  def test_FinalMatchingWord(self):
    r = ex9_7.hasTripleDouble('XYZAABBCC')
    self.assertTrue(r)

  def test_FinalNonMatchingWord(self):
    r = ex9_7.hasTripleDouble('XYZAABCC')
    self.assertFalse(r)

if __name__ == '__main__':
  unittest.main()
