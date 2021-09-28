FROM python:3
COPY . /usr/src/app
RUN python3 -m pip install Flask flask_sqlalchemy flask_marshmallow flask_cors marshmallow-sqlalchemy pymysql
WORKDIR /usr/src/app
EXPOSE 5000
ENV DATABASE_URL="mysql+pymysql://db_user:M@ster123@db/wafd"
CMD ["python3","app.py"]