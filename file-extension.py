import os, argparse

def rename(workingDirectory, oldExt, newExt):

    # lists the files in the directory path (or current directory if no arg)
    for file in os.listdir(workingDirectory):
        # splits the file name into a list with name and extension
        fileName, fileExt = os.path.splitext(file)
        if oldExt == fileExt:
            os.rename(
                os.path.join(workingDirectory, file),
                os.path.join(workingDirectory, fileName+newExt)
            )

def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('workingDirectory', type=str, nargs=1, help='the directory where to change extension')
    parser.add_argument('oldExt', type=str, nargs=1, help='old extension')
    parser.add_argument('newExt', type=str, nargs=1, help='new extension')
    return parser

def main():
    parser = get_parser()
    # vars returns a dictionary with ordered pairs, containing inputted values
    # as first items of pairs
    args = vars(parser.parse_args())

    workingDirectory = args['workingDirectory'][0]
    oldExt = args['oldExt'][0]
    newExt = args['newExt'][0]

    rename(workingDirectory, oldExt, newExt)


if __name__ == '__main__':
    main()
