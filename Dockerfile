FROM python:3.10
WORKDIR /usr/src/rt_solar
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY requirements_actual.txt ./
RUN pip install -r requirements_actual.txt
COPY . .