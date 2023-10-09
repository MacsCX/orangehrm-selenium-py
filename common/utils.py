def draw_tree(height: int, character: str = "@") -> str:
    width = 2 * height - 1  # number of characters in the last line
    result = ""
    for x in range(1, height + 1):
        num_of_stars = 2 * x - 1
        margin = " " * int((width - num_of_stars) / 2)
        result += f"{margin}{character * num_of_stars}\n"

    return result[:-1]
