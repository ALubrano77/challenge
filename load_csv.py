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


def extract_lines(lines, dim_start_line, dim_end_line):
    dim_lines = []
    for line in lines[dim_start_line:dim_end_line]:
        dim_lines.append(line)

    # print(dim_lines)
    return dim_lines



def extract(dims_list, csv_path):
    dims = dict()
    csv_lines = loadfile(csv_path)

    for dim_name in dims_list:
        logging.info(dim_name)
        dim_idx = split_csv_dim_indexes(csv_lines, dim_name)
        logging.info(dim_idx)
        dim_lines = extract_lines(csv_lines, dim_idx[0], dim_idx[2])
        dims[dim_name] = dim_lines
    return dims

def transform(dims):
    dims_trans = dict()
    for dim_name, dim_list in dims.items():
        logging.info(dim_name)
        logging.info(dim_list)
        dim_list_trans = list()
        for row in dim_list:
            row = row.replace("\n", "").strip()
            dim_list_trans.append(row)

        dims_trans[dim_name] = dim_list_trans
    return dims_trans

def dim_list_load():
    dim_list = []
    DataProperties_dict = extract(['DataProperties'], csv_path)
    DataProperties_dict = transform(DataProperties_dict)
    DataProperties_list = DataProperties_dict['DataProperties']

    for row in DataProperties_list:
        row_list = row.split(";")
        if row_list[3] == "\"Dimension\"" :
            dim_list.append(row_list[4])

    return dim_list


if __name__ == '__main__':
    # logging.getLogger().setLevel(logging.INFO)

    csv_path = './data/84710ENG_metadata.csv'

    dim_list = dim_list_load()

    # dim_name = 'TravelMotives'
    # dims_list = ['Margins', 'Periods', 'Population', 'RegionCharacteristics', 'TableInfos', 'TravelModes', 'TravelMotives']
    dims_list = ['RegionCharacteristics']
    dims = extract(dims_list, csv_path)
    # logging.info(dims)

    dims = transform(dims)
    logging.info(dims)

# TODO Extract: metadata to DF;  load csv in DF, split DF
# TODO Transform: data validation and cleansing: /n, trim
# TODO Load: load the data in the database according to relational consistency,
#  giving due consideration to idempotency issues.
