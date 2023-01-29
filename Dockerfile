FROM python:3.9-alpine

RUN mkdir /code

WORKDIR /code

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "chess_canvas.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8080"]
