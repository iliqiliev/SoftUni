class Weapon:

    def __init__(self, bullets: int) -> None:
        self.bullets = bullets

    def shoot(self) -> str:
        if self.bullets:
            self.bullets -= 1
            return "shooting..."

        else:
            return "no bullets left"

    def __str__(self) -> str:
        return f"Remaining bullets: {self.bullets}"
