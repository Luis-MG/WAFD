FROM python:3.8
ENV DATABASE_URL="mysql+pymysql://db_user:M4ster123@db/wafd"
COPY . /usr/src/app
RUN python3 -m pip install Flask flask_sqlalchemy flask_marshmallow flask_cors marshmallow-sqlalchemy pymysql requests
WORKDIR /usr/src/app
EXPOSE 5000
CMD ["python3","app.py"]