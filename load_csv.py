import pandas as pd


def import_csv(csv_path):
    df = pd.read_csv(csv_path)
    print(df)
    return df


def loadfile(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    print(lines)
    return lines


def split_csv_dim_indexes(lines, dim_name):
    dim_start_line = -1
    dim_nrows = -1
    dim_end_line = -1
    csv_separator = ';'
    rec_found = False

    for row in lines:

        if dim_start_line > 0:
            if row.find(csv_separator) != -1 and rec_found:
                dim_nrows = dim_nrows + 1
                rec_found = True
            else:
                break

        if row.find('"' + dim_name + '"\n') != -1:
            dim_start_line = lines.index(row) + 1
            dim_nrows = 0
            rec_found = True

    if dim_nrows > 0:
        dim_end_line = dim_start_line + dim_nrows

    return dim_start_line, dim_nrows, dim_end_line


def extract_dim(csv_path, dim_name, dim_start_line, dim_end_line):
    with open(csv_path, 'r') as fp:
        lines = fp.readlines()
        for line in lines[dim_start_line:dim_end_line]:
            print(line)


if __name__ == '__main__':
    csv_path = './data/84710ENG_metadata.csv'
    dim_name = 'TravelMotives'

    # find dim
    # print('TableInfos', split_dim_csv_indexes(csv_path, 'TableInfos'))
    # print('TravelMotives', split_dim_csv_indexes(csv_path, 'TravelMotives'))
    # print('Population', split_dim_csv_indexes(csv_path, 'Population'))
    # print('TravelModes', split_dim_csv_indexes(csv_path, 'TravelModes'))
    # print('test', split_dim_csv_indexes(csv_path, 'test'))

    csv_lines = loadfile(csv_path)

    dim = split_csv_dim_indexes(csv_lines, dim_name)
    print(dim_name, ': ', dim)
    extract_dim(csv_path, dim_name, dim[0], dim[2])
    # extract dim


# TODO Extract: metadata to DF;  load csv in DF, split DF
# TODO Transform: data validation and cleansing: /n, trim
# TODO Load: load the data in the database according to relational consistency,
#  giving due consideration to idempotency issues.
