import uuid


class User:
  '''
    Takes name and screen_name attributes
    gets uuid for user
  '''

  def __init__(self, full_name, screen_name):
          self.full_name = full_name
          self.screen_name = screen_name
          self.user_uuid = uuid.uuid4()

if __name__ == '__main__':
  u = User()
