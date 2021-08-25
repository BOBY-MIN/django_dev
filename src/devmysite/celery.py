'''
Created on 2021. 8. 25.

@author: 이상민
'''

import os

from celery import Celery

# django 환경파일로 등록
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devmysite.settings')

app = Celery('devmysite')

# django 설정 모듈 Celery의 구성 소스로 추가
# namespace 명으로 celery 구성 옵션 지정 가능
# 지정한 이름을 이용한 환경변수를 가져오며, 관용적으로 CELERY 형식을 유지할 필요가 있음.
app.config_from_object('django.conf:settings', namespace='CELERY')

# 각 패키지 내 tasks.py 를 자동으로 검색
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
        print(f'Request: {self.request!r}')
        