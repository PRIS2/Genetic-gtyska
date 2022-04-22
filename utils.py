
def get_next_index(index: int, list_length: int) -> int:
    if index >= list_length - 1:
        index = 0
    else:
        index += 1
    return index
