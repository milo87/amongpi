from dataclasses import dataclass
from typing import List, Union


FROM_CACHE = True


class Sprite:
    def __init__(self, data: List[List[Union[str, int]]]) -> None:
        self.data = data
        self.width = len(data[0])
        self.height = len(data)

    def render(self, padding=2):
        for row in self.data:
            print(int(padding) * " ", end="")
            print("".join(str(c) for c in row))

    def __repr__(self) -> str:
        return "".join(str(column) for row in self.data for column in row)

    def __eq__(self, __o: object) -> bool:
        return self.__repr__() == __o.__repr__()


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


def main():
    if FROM_CACHE:
        with open("pi_million.txt", "r") as f:
            pi = [int(c) for c in f.read()]
    else:
        from cache_pi import pi_digits, DIGITS

        pi = [n for n in list(pi_digits(DIGITS + 1))]

    pi.pop(0)

    binary_pi = "".join([bin(d).lstrip("0b") for d in pi])
    print(f"Finding Amongi in {len(pi)} digits of Pi...\n")

    amongi_sprite = Sprite([[0, 1, 1, 1], [1, 1, 0, 0], [1, 1, 1, 1], [0, 1, 0, 1]])

    for index, _ in enumerate(binary_pi[: -amongi_sprite.width]):
        row = [int(binary_pi[index + i]) for i in range(amongi_sprite.width)]
        if row == amongi_sprite.data[0]:
            candidate_sprite = Sprite(
                [
                    r
                    for r in chunks(
                        binary_pi[
                            index : index + amongi_sprite.height * amongi_sprite.height
                        ],
                        4,
                    )
                ]
            )

            if candidate_sprite == amongi_sprite:
                print(f"Found one! Index {index} is sus...")
                Sprite(
                    [r for r in chunks(binary_pi[index - 2 * 4 : index + 6 * 4], 4)]
                ).render()

                # candidate_sprite.render()


if __name__ == "__main__":
    main()
