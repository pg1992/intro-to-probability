FROM python:3.10
WORKDIR /usr/src/app
RUN pip install --no-cache-dir pipenv
COPY Pipfile* ./
RUN pipenv install --system --deploy --ignore-pipfile
COPY . .
CMD ["python", "ch01/sec01/CoinTosses.py", "2"]