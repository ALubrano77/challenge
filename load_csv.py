import pandas as pd

def import_csv(csv_path):
    df = pd.read_csv(csv_path)
    print(df)

def split_dim_TableInfos(csv_path):
    dim_start_line = dict()
    dim_nrows = dict()
    dim_name = 'TravelMotives'
    csv_separator=';'
    dim_rows = 0
    rec_found = False

    with open(csv_path, 'r') as fp:

        lines = fp.readlines()
        for row in lines:

            if dim_name in dim_start_line :
                if row.find(csv_separator) != -1 and rec_found:
                    dim_nrows[dim_name]=dim_nrows[dim_name]+1
                    rec_found = True
                else:
                    break


            # print(row.find(dim_name))
            # find() method returns -1 if the value is not found,
            # if found it returns index of the first occurrence of the substring
            if row.find('"'+dim_name+'"\n') != -1:
                dim_start_line[dim_name] = lines.index(row)
                dim_nrows[dim_name] = 0
                rec_found = True


        print('dim_start_line', dim_start_line)
        print('dim_nrows:', dim_nrows)







        # content = fp.read()
        # if '"TravelMotives"' in content:
        #     print('string exist')
        # else:
        #    print('string does not exist')

        # lines = fp.readlines()

        # for line in lines[0:10]:
        #     print(line)

    #with open(csv_path, 'w') as file:
    #    for line in lines[0:10]:
    #        file.write(line)


if __name__ == '__main__':
    csv_path='./data/84710ENG_metadata_xs.csv'
    split_dim_TableInfos(csv_path)