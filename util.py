def read_txt(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [line.strip().split() for line in lines]
    
def read_txt2(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [line for line in lines]