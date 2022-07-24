FROM python:3.8
WORKDIR /usr/src/app/
COPY . /usr/src/app/
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"
RUN poetry install
CMD ["poetry","run", "python","/usr/src/app/currencyconverterbelbot/bot.py","-t","TOKEN"]
