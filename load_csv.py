import pandas as pd
import logging



def import_csv(csv_path):
    df = pd.read_csv(csv_path)
    # print(df)
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



def extract(dim_list, csv_path):
    dims_rows = dict()
    csv_lines = loadfile(csv_path)

    for dim_name in dim_list:
        logging.info(dim_name)
        dim_idx = split_csv_dim_indexes(csv_lines, dim_name)
        # print(csv_lines)
        logging.info(dim_idx)
        dim_lines = extract_lines(csv_lines, dim_idx[0], dim_idx[2])
        dims_rows[dim_name] = dim_lines

    return dims_rows

def transform(dims):
    dims_trans = dict()
    row_split = []
    for dim_name, dim_list in dims.items():
        logging.info(dim_name)
        logging.info(dim_list)
        dim_list_trans = list()
        for row in dim_list:
            row = row.replace("\n", "").strip()
            row_split = row.split( ";")
            #print(row_split)
            dim_list_trans.append(row_split)

        dims_trans[dim_name] = dim_list_trans
    return dims_trans

def dim_list_load():
    dim_list = []
    DataProperties_dict = extract(['DataProperties'], csv_path)
    DataProperties_dict = transform(DataProperties_dict)
    DataProperties_list = DataProperties_dict['DataProperties']
    print(DataProperties_list)

    for row in DataProperties_list:
        if row[3] == "\"Dimension\"" :
            dim_list.append(row[4].replace("\"", ""))

    return dim_list


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    logger = logging.getLogger(__name__)

    csv_path = './data/84710ENG_metadata.csv'

    dim_list = dim_list_load()
    logging.info("dim_list")
    logging.info(dim_list)

    # dim_list = ['Margins', 'Periods', 'Population', 'RegionCharacteristics', 'TableInfos', 'TravelModes', 'TravelMotives']
    # dim_list = ['Margins']
    dims_rows = extract(dim_list, csv_path)
    print(dims_rows)

    dims_dictlist = transform(dims_rows)

    logging.info("dims transformed")
    logging.info(dims_dictlist)

    print('dims_dict ', dims_dictlist)

    dims_dictdf = {}
    for dim_tab, dim_cells in dims_dictlist.items():
        print('dim_tab ', dim_tab)
        print('dim_cells ', dim_cells)
        dims_dictdf[dim_tab] = pd.DataFrame(dim_cells, columns = dim_cells[0])

    print("TEST")
    print(dims_dictdf["Population"])

    #print("")
    #print (dims_dictlist['Margins'])
    #df = pd.DataFrame(dims_dictlist['Margins'], columns = dims_dictlist['Margins'][0])
    #print(df)

# TODO Extract: metadata to DF;  load csv in DF, split DF
# TODO Transform: data validation and cleansing: /n, trim
# TODO Load: load the data in the database according to relational consistency,
#  giving due consideration to idempotency issues.
