# 1 Use the Python OnBuild
FROM python:3.6-slim

# 2 Force stdin, stdout and stderr to be totally unbuffered and don´t write .pyc or .pyo files
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

# 4 Install all the dependencies except libcairo2 from jessie, then install libcairo2 from stretch


RUN apt-get -y update\
    && apt-get install -y \
        python-dev \
        python-pip \
        python-setuptools \
        python-wheel \
        python-cffi \
        libcairo2>=1.14.2 \
        libpango-1.0-0 \
        libpangocairo-1.0-0 \
        libgdk-pixbuf2.0-0 \
        libffi-dev \
        shared-mime-info\
    && apt-get -y clean


# 5 Set the rights to access the files
RUN groupadd -r pdf && useradd -r -g pdf pdf


# 6 Copy the App
COPY . /pdf

# 7 Give access to user
RUN chown -R pdf /pdf

# 8 Requirements have to be pulled and installed here, otherwise caching won't work
COPY requirements.txt requirements.txt

# 9 Update PIP and install the local requirements
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt


# 12 Add django to the sudo group
RUN echo "pdf:pdf" | chpasswd && adduser pdf sudo

#13 Set the working dir
USER pdf
WORKDIR /pdf

EXPOSE 8200

# 14 Start the server
CMD ["python", "manage.py", "collectstatic",  "--noimput"]

CMD ["gunicorn",  "pdf.wsgi", "-w 4", "-b 0.0.0.0:8200",  "--chdir=.", "--reload"]

HEALTHCHECK CMD curl --fail http://localhost:8200/health/ || exit 1
