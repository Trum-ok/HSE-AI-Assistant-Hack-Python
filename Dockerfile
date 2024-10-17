FROM 3.11.9-alpine3.20

WORKDIR /app

RUN pip install poetry

# 

COPY . /app

RUN mkdir -p /app/data/complete /app/data/processed /app/data/raw/test /app/data/raw/train

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["poetry", "run", "python", "main.py"]