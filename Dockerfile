FROM  python:3.7-slim-buster

RUN apt-get update && apt-get install
RUN apt-get install unixodbc -y
RUN apt-get install unixodbc-dev -y
RUN apt-get install freetds-dev -y
RUN apt-get install freetds-bin -y
RUN apt-get install tdsodbc -y
RUN apt-get install --reinstall build-essential -y
RUN apt-get install curl -y
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN pip install --upgrade pip
RUN ACCEPT_EULA=Y apt-get install msodbcsql17 -y
RUN apt-get clean && apt-get update

# ssh
ENV SSH_PASSWD "root:Docker!"
RUN apt-get update \
        && apt-get install -y --no-install-recommends dialog \
        && apt-get update \
	&& apt-get install -y --no-install-recommends openssh-server \
	&& echo "$SSH_PASSWD" | chpasswd

COPY sshd_config /etc/ssh/
COPY init.sh /usr/local/bin/
RUN chmod u+x /usr/local/bin/init.sh

COPY requirements.txt .
COPY wait-for-it.sh /usr/wait-for-it.sh
RUN chmod +x /usr/wait-for-it.sh

RUN pip install -r requirements.txt

COPY . .

RUN chmod u+x ./api.sh

ENV SSH_PORT 2222

EXPOSE 2222

#CMD ["python", "./main.py"]