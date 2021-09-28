FROM python:3.8
COPY . /usr/src/app
RUN python3 -m pip install Flask
WORKDIR /usr/src/app
EXPOSE 80
CMD ["python3","app.py"]