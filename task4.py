def is_valid_username(username1, username2):
    return username1 == username2


def main():
    username1 = input("Enter the user name: ")
    username2 = input("Reenter the user name: ")

    if is_valid_username(username1, username2):
        print("User name is Valid")
    else:
        print("User name is Invalid")


if __name__ == "__main__":
    main()
