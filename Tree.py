#!/usr/bin/env python3

# Made by: flaszlo2000 2021.04.22

from dataclasses import dataclass, field


@dataclass
class Tree:
    # some complex stuff going on here
    name: str
    connections: list = field(default_factory=list)

    def __str__(self) -> str:
        result = self.name

        for connection in self.connections:
            result += f"\n-{connection.name}"

            if len(connection.connections) > 0:
                recursive_result = str(connection).split("\n")[1:] # cut down the first line because it was recursive so it got the connection.name
                recursive_result = map(lambda line: '-' + line, recursive_result) # magic
                #> (add one - sign every iteration, because it's recursive, it builds up pretty well)


                result_line = '\n' + '\n'.join(recursive_result) # assign every line with \n to make a nice output (we need to add one more \n because the program cut down after the first line)
                result += result_line # add the current iteration for the result
        
        return result


if __name__ == "__main__":
    test_tree = Tree("base", [
        Tree("a", [
            Tree("1", [
                Tree("i1", [
                    Tree("ii1")
                ])
            ]),
            Tree("2")
        ]),
        Tree("b", [
            Tree("3"),
            Tree("4")
        ])
    ])

    print(test_tree)
