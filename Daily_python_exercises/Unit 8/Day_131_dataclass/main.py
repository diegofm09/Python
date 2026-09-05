from dataclasses import dataclass

@dataclass
class Usuario:
    username: str
    email: str
    es_admin: bool = False

    def __post_init__(self):
        self.username = self.username.strip()

        if not self.username:
            raise ValueError("The username mustnt be empty")

        if "@" not in self.email:
            raise ValueError("The email must have an @")

