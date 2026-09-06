import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """ Class for storing data about students """
    name: str
    surname: str
    id: str = field(init=False, default_factory=generate_id)
    active: bool = field(init=False, default=True)
    login: str = field(init=False)

    def __post_init__(self):
        self.login = self.name[0] + self.surname


def main():
    student = Student(name="Edward", surname="agle")
    print(student)
    print("---")
    try:
        Student(name="Edward", surname="agle", id="toto")
        Student(name="Edward", surname="agle", login="user_vip")
    except TypeError as error:
        print(f"TypeError: {error}")
    return


if __name__ == "__main__":
    main()
