class Person:
    def __init__(self) -> None:
        self._idPerson = None
        self._nationality = None

    @property
    def idPerson(self):
        return self._idPerson

    @idPerson.setter
    def idPerson(self, value):
        self._idPerson = value

    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        self._nationality = value