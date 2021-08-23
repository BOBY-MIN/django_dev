# base 이미지
FROM python:3.9.4

ENV PYTHONUNBUFFERED 1

# 이미지 내 작업디렉토리 생성 및 이동
RUN mkdir /web
WORKDIR /web
# 모든 디렉토리 및 파일 복사
COPY . /web

# 필요 패키지 설치
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
