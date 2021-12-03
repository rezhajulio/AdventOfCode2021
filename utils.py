def read_map(file_path, function):
    with open(file_path, "r") as f:
        return list(map(function, f.readlines()))