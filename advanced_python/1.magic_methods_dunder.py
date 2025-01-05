from typing import Any


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Object is being deconstructed")

    def __call__(self):
        pass
    def __len__(self):
        pass
    def __repr__(self) -> str:
        pass

    def __instancecheck__(self, instance: Any) -> bool:
        pass

p = Person("Mike",25)
