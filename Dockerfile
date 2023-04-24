# Build the app image
FROM python:3.10

# Create directory for the app user
RUN mkdir -p /home/app

# Create the app user
RUN groupadd app && useradd -g app app

# Create the home directory
ENV APP_HOME=/home/app
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# install
COPY . $APP_HOME
RUN pip install -r requirements.txt
RUN pip install -e .

RUN chown -R app:app $APP_HOME
USER app

CMD ["python3","manage.py","runserver", "0.0.0.0:8000"]