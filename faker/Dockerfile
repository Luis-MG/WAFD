FROM python:3.8
COPY . /usr/src/app
RUN python3 -m pip install Flask faker
WORKDIR /usr/src/app
EXPOSE 5001
CMD ["python3","faker-service.py"]