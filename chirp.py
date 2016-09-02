import uuid


class Chirp:


    def __init__(self, chirp_text):
            self.chirp_text = chirp_text
            self.chirp_uuid = uuid.uuid4()


if __name__ == '__main__':
  chirp = Chirp()
