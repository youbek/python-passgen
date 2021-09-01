from os import getcwd, path


def save_password(password):
    file = open(path.join(getcwd(), "./passwords.txt"), 'a')
    file.write(f"{password}\n")
