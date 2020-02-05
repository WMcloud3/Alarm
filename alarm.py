def main():
    fileName = "Script3.csv"

    old_file = open(fileName, "r")

    new_file = open("TempFile.csv", "w")

    line = old_file.readline()

    # part 1: print name, FavoriteFridge1
    while line != "":
        field = line.split(',')
        new_file.write(field[0] + "," + (field[4]).rstrip('\n') + "," + field[2] + "," + field[3] + "," + field[4])
        line = old_file.readline()
    new_file.close()

    # Part 2 New data from tempfile into original

    with open("TempFile.csv") as f:
        with open(fileName, "w") as f1:
            for line in f:
                f1.write(line)


main()
