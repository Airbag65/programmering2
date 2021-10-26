import random

INTX = 10
INTY = 10

def get_board_size() -> None:
    global INTX, INTY
    print("\nAnge x och y koordinater för brädet enligt \"X Y\": ")
    input_board = str(input(""))
    print("\nDitt bräde ser ser ut som följande: ")
    coords = input_board.split(" ")
    for idx, coord in enumerate(coords):
        coords[idx] = int(coord)
    INTY = coords[1]
    INTX = coords[0] 


def gen_board(x: int, y: int):
    plane = []
    for i in range(y):
        plane.append([None] * x)
        for j in range(x):
            plane[i][j] = random.randrange(2)
    return plane
    

def flood_fill(x: int, y: int) -> None:
    old_list = []
    old_list.append([x,y])

    while(old_list != []):
        new_list = []
        for point in old_list:
            print("Hello")


get_board_size()
board = gen_board(INTX, INTY)
for array in board:
    print(array)
