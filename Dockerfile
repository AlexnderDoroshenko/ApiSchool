FROM python:3.10.11

LABEL Has been created by Doroshenko A.D. for the UPItec school.

RUN mkdir -p /usr/src/Api/
WORKDIR /usr/src/Api/

COPY . /usr/src/Api/
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "/usr/src/Api/manage.py", "runserver", "0.0.0.0:55501"]
