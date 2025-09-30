def read_data(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    processed_data = []
    for line in lines:
        name, age = line.split(",")
        processed_data.append((name, int(age)))
    return processed_data

