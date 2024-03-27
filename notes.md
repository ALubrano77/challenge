

# content = fp.read()
# if '"TravelMotives"' in content:
#     print('string exist')
# else:
#    print('string does not exist')

# lines = fp.readlines()

# for line in lines[0:10]:
#     print(line)

# with open(csv_path, 'w') as file:
#    for line in lines[0:10]:
#        file.write(line)

he “Extraction” component will be mainly responsible for extracting dimensions from the metadata.
The “Transform” component will be mainly responsible for data validation and cleansing, as appropriate.
The “Load” component will be minimal: just load the data in the database according to relational consistency,
giving due consideration to idempotency issues.

## Extract
import_csv(csv_path)
I can not load the csv, it is NOT a csv, it is a text file made of several csv appended  

so:
read the file in a list
have a list of dimensions to look for
find indexes, ciclying the list of Dims
split the list in several lists or in a list of lists



