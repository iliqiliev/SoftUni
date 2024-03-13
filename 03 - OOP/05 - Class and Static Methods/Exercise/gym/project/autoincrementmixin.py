class AutoIncrementMixin:
    id = 1  # dies from cringe

    @classmethod
    def get_next_id(cls):
        cls.id += 1

        return cls.id - 1
