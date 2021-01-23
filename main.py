import csv
from os import readlink, write
from constants import lineEnd, parcel_id_next


def main():
    with open("data.csv", "w") as data_to_csv:
        writer = csv.writer(data_to_csv)
        row = [
            "Name A",
            "Name B",
            "Name C",
            "Mailing Address",
            "City",
            "State",
            "Zip",
            "Parcel ID",
            "Property Address",
            "City",
            "State",
            "Zip",
            "Serial Number",
            "Property Class",
        ]
        print(row)
        writer.writerow(row)
        stats = 2
        with open("data.txt", "r") as data:
            j = 1
            line = data.readline()
            # while line:
            for i in range(0, 61614):
                # print(len(lineEnd))
                if line == lineEnd:
                    j = 0
                    row = []
                    r = 0
                    line = data.readline()
                    k = 0
                    r = columns_1_4(line, k, row, data, r)
                    r = column_5_7(data, row, r)
                    r = column_8_9(data, row, r)
                    r = column_10_12(row, r)

                    r = column_13_14(row, data, r)
                    writer.writerow(row)
                    print(row, r)

                line = data.readline()


def column_13_14(row, data, r):
    for i in range(0, 2):
        row.append(data.readline().split(": ")[1].strip("\n"))
        r = r + 1
    return r


def column_10_12(row, r):
    if row[8] in row[3]:
        for i in range(4, 7):
            row.append(row[i])
            r = r + 1
    else:
        for i in range(4, 7):
            row.append("")
            r = r + 1
    return r


def column_8_9(data, row, r):
    while not parcel_id_next == data.readline():
        pass
    line = data.readline()
    row.append(line.strip("\n"))
    r = r + 1
    row.append(data.readline().strip("\n"))
    r = r + 1
    return r


def column_5_7(data, row, r):
    line = data.readline()
    if line[0].isdigit():
        row[3] = row[3] + " Or \n" + line
        line = data.readline()
    address = list(line.split(" "))
    if len(address) == 4:
        address = [address[0] + " " + address[1], address[2], address[3]]

    for i in range(0, 3):
        try:
            row.append(address[i].strip("\n"))
        except:
            row.append("")
        r = r + 1
    return r


def add_row(line, data, row, writer):
    for i in range(0, 61614):
        # print(len(lineEnd))
        if line == lineEnd:
            j = 0
            row = []
            r = 0
            line = data.readline()
            k = 0
            r = columns_1_4(line, k, row, data, r)
            r = column_5_7(data, row, r)
            while not parcel_id_next == data.readline():
                pass
            line = data.readline()
            row.append(line.strip("\n"))
            r = r + 1
            row.append(data.readline().strip("\n"))

            if row[8] in row[3]:
                for i in range(4, 7):
                    row.append(row[i])
            else:
                for i in range(4, 7):
                    row.append("")

            r = column_13_14(row, data, r)
            writer.writerow(row)
            print(row, r)


def columns_1_4(line, k, row, data, r):
    while (
        not line[0].isdigit()
        and not "PO BOX" == line[0:6]
        and k < 3
        and not line == "ONE AIRPORT WAY\n"
    ):
        row.append(line.strip("\n"))
        line = data.readline()
        r = r + 1
        k = k + 1
    while r < 3:
        row.append("")
        r = r + 1

    if line[0].isdigit() or "PO BOX" == line[0:6] or line == "ONE AIRPORT WAY\n":
        row.append(line.strip("\n"))
    else:
        row.append("")
    r = r + 1
    return r


main()
