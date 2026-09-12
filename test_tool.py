import unittest
from tool import breaking,compare
class VersionTests(unittest.TestCase):
 def test_signature_changes(self):
  result=compare({'version':'1','features':{'x':'float','y':'str'}},{'version':'2','features':{'x':'int','z':'str'}});self.assertEqual(result['removed_features'],['y']);self.assertEqual(result['changed_features'],['x']);self.assertTrue(breaking(result))
if __name__=='__main__':unittest.main()
