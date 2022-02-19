
#### 장고 프레임워크 연습

CRUD 연습  


* django 3.2
* python 3.9.4
* mysql 8.0.18
* 이클립스 pyDev


#### 가상환경 구성

```
-- devenv 가상환경 만들기
-- 명령어를 수행한 디렉토리 하위로 생성
D:\devPy> python -m venv devenv
 
-- 가상환경 실행하기
D:\devPy> devenv\Scripts\activate
 
-- 가상환경 종료하기
D:\devPy> devenv\Scripts\deactivate
 
 
-- 가상환경 내 pip upgrade
(devenv) D:\devPy> python -m pip install --upgrade pip
 
-- 가상환경 내 필요모듈 설치
(devenv) D:\projectRoot>pip install -r requirements.txt 
 
```

* 이클립스 pyDev 인터프리터에 위에서 생성한 가상환경 설정


#### docker 환경파일 추가

* docker-compose.yml
* Dockerfile
* requirements.txt

* docker 이미지 생성

```
$ docker build --tag bobypoby123/python .
```

* docker 컨테이너 생성

```
$ docker create --name testpython -p 8000:8000 bobypoby123/python python manage.py runserver 0.0.0.0:8000
```

* docker 실행

```
$ docker start 컨테이너이름
```


#### celery 실행 모음

```
-- celery worker 수동실행
-- project root 경로/src 에서 진행
$ (가상환경)> celery -A projectName worker -l INFO
 
-- 윈도우의 경우 celery 4.0 부터 지원되지 않으므로 아래 패키지 설치 후 실행
$ (가상환경)> pip install gevent
-- project root 경로/src 에서 진행
$ (가상환경)> celery -A projectName worker -l info -P gevent
 
-- 테스트
$ (가상환경)> python ./manage.py shell
>>> from celerytest.tasks import add, mul, xsum
>>> res = add.delay(2,3)
>>> res.get()
5
```

* celery 테스트하려면 로컬에 rabbitMQ 설치되어 있어야 함.
* rabbitMQ 관련 정보는 프로젝트/settings.py, celery.py 에 기재되어 있음.
* rabbitMQ 설치 또는 celery 설정은 development-guide 내 문서 참고