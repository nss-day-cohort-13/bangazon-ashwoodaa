# from birdyboard_menu import *
# from birdyboard_new_user import *
# from birdyboard_view_chirps import *
# from birdyboard_public_chirp import *
# from birdyboard_private_chirp import *

import unittest
import CoversationSingleton


class TestChirp(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

# ******************* PUBLIC CHIRP ****************************
  def test_new_public_chirp_creation(self):
    source = User("Gemma Stone", "GemStone")
    chirp = Chirp(
                  message="This is my new public chirp.",
                  user=source.user_id,
                  private=False
                  )

    it_exists = CoversationSingleton.chirp_exists_in_conversation(chirp)

    self.assertTrue(it_exists)
    self.assertEqual(chirp.message, "This is my new public chirp.")
    self.assertEqual(chirp.user_id, source.user_id)
    self.assertEqual(chirp.private, False)
    self.assertIsInstance(chirp, Chirp)
    self.assertIsNotNone(chirp.chirp_id)

# ******************* REPLY TO PUBLIC CHIRP *******************
  def test_reply_public_chirp_creation(self):
    source = User("Gemma Stone", "GemStone")
    target = #this should be the id of the public chirp/ or id of the conversation/ or id of the user and just reply publicly?

    chirp = Chirp(
                  message="This is my public response to your public message.",
                  user=source.user_id,
                  private=False
                  )

    it_exists = CoversationSingleton.chirp_exists_in_conversation(chirp)

    self.assertTrue(it_exists)
    self.assertEqual(chirp.message, "This is my public response to your public message.")
    self.assertEqual(chirp.user_id, source.user_id)
    self.assertEqual(chirp.private, False)
    self.assertIsInstance(chirp, Chirp)
    self.assertIsNotNone(chirp.chirp_id)

# ******************* PRIVATE CHIRP *******************
  def test_new_private_chirp_creation(self):
    source = User("Gemma Stone", "GemStone")
    target = User("George Lucas", "hahajarjar")
    chirp = Chirp(
                  message="This is my new private chirp.",
                  user=source.user_id,
                  private=True,
                  receiver=target.user_id #does this need a receiver?
                  )

    it_exists = CoversationSingleton.chirp_exists_in_conversation(chirp)


    self.assertTrue(it_exists)
    self.assertEqual(chirp.message, "This is my new private chirp.")
    self.assertEqual(chirp.user_id, source.user_id)
    self.assertEqual(chirp.private, True)
    self.assertIsInstance(chirp, Chirp)
    self.assertIsNotNone(chirp.chirp_id)



# ******************* REPLY TO PRIVATE CHIRP *******************
  def test_reply_private_chirp_creation(self):
    source = User("Gemma Stone", "GemStone")
    target = User("George Lucas", "hahajarjar")

    chirp = Chirp(
                  message="This is my private response to your private message.",
                  user=source.user_id,
                  private=False
                  receiver=target.user_id #this def needs a target id. right?
                  )

    it_exists = CoversationSingleton.chirp_exists_in_conversation(chirp)

    self.assertTrue(it_exists)
    self.assertEqual(chirp.message, "This is my private response to your private message.")
    self.assertEqual(chirp.user_id, source.user_id)
    self.assertEqual(chirp.private, True)
    self.assertIsInstance(chirp, Chirp)
    self.assertIsNotNone(chirp.chirp_id)







if __name__ == '__main__':
    unittest.main()