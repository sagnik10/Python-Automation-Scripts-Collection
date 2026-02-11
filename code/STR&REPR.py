class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"

p = Person("Sawjanya", 25)
print(str(p))
print(repr(p))