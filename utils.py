def read_map(file_path, function):
    with open(file_path, "r") as f:
        return list(map(function, f.readlines()))


def chunks(a_list, n):
    """Yield successive n-sized chunks from list."""
    for i in range(0, len(a_list), n):
        yield a_list[i:i + n]
