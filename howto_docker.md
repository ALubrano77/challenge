sudo service docker status
sudo service docker start
sudo docker run -d --rm     -p 25432:5432     --name csv2pg-test     -e POSTGRES_DB=test     -e POSTGRES_USER=test     -e POSTGRES_PASSWORD=test postgres
docker ps
