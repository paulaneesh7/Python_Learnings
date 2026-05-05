

class AddString:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, AddString):
            return AddString(self.value + other.value)
        return NotImplemented

    def __str__(self):
        return self.value


# Example usage
a = AddString('xyz')
b = AddString('abc')
c = a + b
print(c)  # Prints xyzabc
