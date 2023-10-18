class InterpeterExceptions:
    def __init__(self) -> None:
        pass

    @staticmethod
    def CantIncrementPointer():
        raise Exception("pointer cannot be incremented any more")

    @staticmethod
    def CantDecrementPointer():
        raise Exception("pointer cannot be decremented any more")

    @staticmethod
    def BraceMismatch():
        raise Exception("braces are mismatched")
