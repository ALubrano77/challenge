import pandas as pd

def import_csv(csv_path):
    df = pd.read_csv(csv_path)
    print(df)

def split_dim_TableInfos(csv_path, dim_name):
    dim_start_line = -1
    dim_nrows = -1
    dim_end_line = -1
    csv_separator=';'
    rec_found = False

    with open(csv_path, 'r') as fp:

        lines = fp.readlines()
        for row in lines:

            if dim_start_line > 0:
                if row.find(csv_separator) != -1 and rec_found:
                    dim_nrows = dim_nrows + 1
                    rec_found = True
                else:
                    break

            if row.find('"'+dim_name+'"\n') != -1:
                dim_start_line = lines.index(row) +1
                dim_nrows = 0
                rec_found = True

        if dim_nrows >0 :
            dim_end_line = dim_start_line + dim_nrows

        return dim_start_line, dim_nrows, dim_end_line

def extract_dim(csv_path, dim_name, dim_start_line, dim_end_line):
    with open(csv_path, 'r') as fp:
        lines = fp.readlines()
        for line in lines[dim_start_line:dim_end_line]:
            print(line)


if __name__ == '__main__':
    csv_path='./data/84710ENG_metadata.csv'

    # find dim
    print('TableInfos',split_dim_TableInfos(csv_path, 'TableInfos') )
    print('TravelMotives',split_dim_TableInfos(csv_path, 'TravelMotives'))
    print('Population', split_dim_TableInfos(csv_path, 'Population'))
    print('TravelModes', split_dim_TableInfos(csv_path, 'TravelModes'))
    print('test', split_dim_TableInfos(csv_path, 'test'))

    dim = split_dim_TableInfos(csv_path, 'TravelMotives')
    print(dim[1])
    extract_dim(csv_path,'TravelMotives', dim[0], dim[2])
    # extract dim