import unittest


class TestUser(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

  def test_user_creation(self):
    user = User("Tractor Ryan", "tryan")
    self.assertEqual("Tractor Ryan", user.full_name)
    self.assertEqual("tryan", user.screen_name)
    self.assertIsNotNone(user.user_id)
    self.assertIsInstance(user, User)
    pass



if __name__ == '__main__':
    unittest.main()