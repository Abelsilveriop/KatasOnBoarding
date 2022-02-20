def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesysten under heavy load, cant complete reading configuration file")
        


if __name__ == '__main__':
    main()
