FROM python:3.12.7
#LABEL authors="jusu-in"

#work dir
WORKDIR /code

# project dependency file requirements.txt copy
COPY requirements.txt /code/

#dependency setup
RUN pip install -r requirements.txt

#mod project file container copy
COPY . /code/

# 포트 8000을 오픈 (Django 웹 서버)
EXPOSE 8000

# Celery worker execution command (worker)
#CMD ["celery","-A","AssetsMgrToyProjectInternal","worker","--loglevel=info"]

#Celery beat execution command (beat)
#CMD ["celery", "-A", "AssetsMgrToyProjectInternal", "beat", "--loglevel=info"]

#ENTRYPOINT ["top", "-b"]