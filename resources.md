https://pypi.org/project/csv2pg/

sudo service docker start

docker run -d --rm \
    -p 25432:5432 \
    --name csv2pg-test \
    -e POSTGRES_DB=test \
    -e POSTGRES_USER=test \
    -e POSTGRES_PASSWORD=test \
postgres



import csv2pg

HOST = "localhost"
PORT = 25432
DBNAME = "test"
USER = "test"
PASSWORD = "test"

csv2pg.copy_to(HOST, PORT, DBNAME, USER, PASSWORD, "public.data", "./simple.csv", verbose=True)