import os

BASE_DIR = "./my_files"


def get_file_path(filename: str):
    return BASE_DIR + "/" + filename


def get_file_info(filename):
    filepath = get_file_path(filename)
    if os.path.isdir(BASE_DIR) and os.path.exists(filepath):
        return True
    return False


def read_file(filename: str):
    try:
        if get_file_info(filename):
            filepath = get_file_path(filename)
            with open(filepath, "r+") as f:
                return f.read()
    except FileNotFoundError:
        return f"{filename} file not found.Please make sure {filename} file exists or not."


def write_file(filename, content=""):
    filepath = get_file_path(filename)
    with open(filepath, "w") as f:
        f.write(content)


def search_file_char(filename: str, search_char: str):
    try:
        filepath = get_file_path(filename)

        with open(filepath) as f:
            data = f.read()

            if search_char.lower() in data.lower():
                return True
            else:
                return False

    except Exception as e:
        print("Error::", e)
    pass


def replace_file_char(filename: str, search_char: str, new_char: str):
    try:
        filepath = get_file_path(filename)

        with open(filepath, "r+") as f:
            data = f.read()
            data = data.replace(search_char, new_char)

        # IMP -> data variable can be access here.
        with open(filepath, "w+") as f:
            f.write(data)

        print("\n text replaced.")

    except Exception as e:
        print("Error::", e)
    pass


def get_user_input():
    print("Enter the content that you want to write in file (type save on a new line to save and exist):: ")
    lines = []
    while True:
        line = input()
        if line.upper() == "SAVE":
            break

        lines.append(line)

    return "\n".join(lines)


print(search_file_char("words.txt", "hulk"))


def main():
    file = input("Enter the filename to open or create: ").strip()
    try:
        if get_file_info(file):
            print(read_file(file))
        else:
            write_file(file)

            content = get_user_input()
            write_file(file, content)
            print(f"{file} saved successfully.")
            quit()
    except Exception as e:
        print("this is error::", e)


if __name__ == "__main__":
    # main()
    pass
