import pandas as pd
import logging


def import_csv(csv_path):
    df = pd.read_csv(csv_path)
    print(df)
    return df


def loadfile(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    logging.info(lines)
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


def extract_lins(lines, dim_start_line, dim_end_line):
    dim_lines = []
    for line in lines[dim_start_line:dim_end_line]:
        dim_lines.append(line)

    # print(dim_lines)
    return dim_lines


def extract(dims_list, csv_path, dims):
    for dim_name in dims_list:
        csv_lines = loadfile(csv_path)

        dim = split_csv_dim_indexes(csv_lines, dim_name)
        logging.info(dim_name)
        logging.info(dim)

        dim_lines = extract_lins(csv_lines, dim[0], dim[2])
        dims[dim_name] = dim_lines
    return dims


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)

    csv_path = './data/84710ENG_metadata.csv'
    # dim_name = 'TravelMotives'
    dims_list = ['Margins', 'Periods', 'Population', 'RegionCharacteristics', 'TableInfos', 'TravelModes',
                 'TravelMotives']
    dims = dict()

    extract(dims_list, csv_path, dims)
    logging.info(dims)

# TODO Extract: metadata to DF;  load csv in DF, split DF
# TODO Transform: data validation and cleansing: /n, trim
# TODO Load: load the data in the database according to relational consistency,
#  giving due consideration to idempotency issues.
