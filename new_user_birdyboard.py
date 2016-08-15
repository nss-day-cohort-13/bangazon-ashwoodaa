import uuid


class User:
  '''
    Takes name and screen_name attributes
    gets uuid for user
  '''

  def __init__(self, name, screen_name):
          self.name = name
          self.screen_name = screen_name
          self.user_uuid = uuid.uuid4()

if __name__ == '__main__':
  u = User()
