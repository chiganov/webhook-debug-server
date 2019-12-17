from python:3.7

RUN pip install Flask

COPY main.py ./

CMD ["python", "main.py", "5000"]
