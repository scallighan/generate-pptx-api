FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY backend/ /code/app

CMD ["fastapi", "run", "app/server.py", "--port", "80"]