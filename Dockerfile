from python:3.12

ADD main.py .
RUN pip install pandas csv2pg

CMD ls
CMD python3 ./main.py

