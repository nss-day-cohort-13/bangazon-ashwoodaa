import unittest
from new_user_birdyboard import *


class TestUser(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

# ******************* NEW USER ****************************
  def test_new_user_creation(self):
    user = User(
              name = "Gemma Stone",
              screen_name = "Gemstone"
              )

    self.assertEqual(user.name, "Gemma Stone")
    self.assertEqual(user.screen_name, "Gemstone")
    self.assertIsInstance(user, User)
    self.assertIsNotNone(user.user_uuid)

if __name__ == '__main__':
  unittest.main()
