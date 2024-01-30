def text_pos(position: str, linedata: str) -> str:
    """Grabs text on position in linedata and returns the result.

    ``position`` can be a single number "1" or a range "10-22"

    returns string
    """
    from_pos = -1
    to_pos = -1
    pos = -1
    if "-" in position:
        from_pos, to_pos = position.split("-")
        from_pos = int(from_pos)
        to_pos = int(to_pos)
        return linedata[from_pos - 1 : to_pos].rstrip(" ")
    else:
        pos = int(position)
        return linedata[pos - 1]


def left_align(text: str, col_width: int, fill_char=" ") -> str:
    """Left align text in a string.

    Fills the space with ``fill_char`` to the desiered length ``col_width``.

    """
    fill_text = ""
    if len(text) > col_width:
        text = text[:col_width]
    for _ in range(0, col_width - len(text)):
        fill_text += fill_char
    return text + fill_text


def right_align(text: str, col_width: int, fill_char=" ") -> str:
    """Right align text in a string.

    Fills the space with ``fill_char`` to the desiered length ``col_width``.

    """
    fill_text = ""
    if len(text) > col_width:
        text = text[-col_width:]
    for _ in range(0, col_width - len(text)):
        fill_text += fill_char
    return fill_text + text
