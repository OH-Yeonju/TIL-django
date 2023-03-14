# django

-----

###### 프로젝트 생성하기

**가상환경 생성하기**

python -m venv venv

source venv/Scripts/activate

**가상환경에 장고 설치, 프로젝트 생성**

pip list  > 확인용도

pip installl django==3.2.18

django-admin startproject 프로젝트이름 . > 점이 있으면 폴더생성안함

*점 없이 만들었을 경우*

cd 프로젝트이름 > 으로 폴더안으로

**앱 생성하기**

python manage.py startapp 앱이름(복수형권장)

**해줄것**

settings에 앱 추가

urls에 url 추가

views에 함수 추가

앱 폴더 내 templates 추가해서 html파일 생성