import os


def read_data_to_file(filename):
    try:
        with open(f"{filename}", "r+") as f:
            # print("this is readlines::\n", type(f.read()))
            return f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError


def write_data_to_file(filename, data: str):
    with open(f"{filename}", "a+") as f:
        f.writelines(data)


def delete_data_to_file(filename, index):
    f = open(filename, "r+")
    data = f.readlines()
    data.pop(index - 1)
    f.writelines(data)
    f.close()

    # def read():
    #     with open(filename) as f:
    #         data = f.readlines()
    #         data.pop(index - 1)
    #         return data
    #
    # def write_file():
    #     data = read()
    #     f = open(filename, "w")
    #     f.writelines(data)
    #     f.close()

    # write_file()


def update_data_to_file():
    pass


def clear_data_to_file(filename):
    with open(filename, "w") as f:
        return f.write("")


def create_dir(dir_name: str):
    """
    :param dir_name: Directory name that you want to create.
    :type dir_name: str
    :return: Bool
    :rtype:
    This function create a directory into current working directory.If Directory not exist then it will create a
    directory.
    """
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        return True
    else:
        raise FileExistsError
