class Trainer:
    _id = 0

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()


    @staticmethod
    def get_next_id():
        return Trainer._id + 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"










