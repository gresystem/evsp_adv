# evsp_adv
## environment & activation
![image](https://user-images.githubusercontent.com/109661376/182842181-ba6afd4d-c701-4544-8589-50f2f34dc08b.png)
1. Download ZIP을 선택하여 프로젝트 폴더에 놓고 Unzip 한다.
2. 다음과 같이 프로젝트 폴더로 이동한다.
```
$ pwd
~/Documents/projects/evsp_adv-master
$ ls
evsp_adv-master/
```
3. 프로젝트 폴더에서 가상환경을 구성하고 가상환경에서 django framework을 설치한다.
```
$ virtualenv venv
created virtual environment CPython3.10.6.final.0-64 in 3734ms
  creator Venv(dest=C:\Users\jeongsooh\Documents\projects\python\evsp_adv-master\venv, clear=False, no_vcs_ignore=False, global=False, describe=CPython3Windows)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\jeongsooh\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\Local\pypa\virtualenv)
    added seed packages: pip==22.1.2, setuptools==63.1.0, wheel==0.37.1
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

$ ls
evsp_adv-master/  venv/
$ source venv/scripts/activate
(venv)
$ pip install django
Collecting django
  Downloading Django-4.1-py3-none-any.whl (8.1 MB)
     ---------------------------------------- 8.1/8.1 MB 5.3 MB/s eta 0:00:00
Collecting asgiref<4,>=3.5.2
  Using cached asgiref-3.5.2-py3-none-any.whl (22 kB)
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.2-py3-none-any.whl (42 kB)
Collecting tzdata
  Using cached tzdata-2022.1-py2.py3-none-any.whl (339 kB)
Installing collected packages: tzdata, sqlparse, asgiref, django
Successfully installed asgiref-3.5.2 django-4.1 sqlparse-0.4.2 tzdata-2022.1

[notice] A new release of pip available: 22.1.2 -> 22.2.2
[notice] To update, run: python.exe -m pip install --upgrade pip
(venv)
$
```
4. 기본적인 환경구성은 완료. 현재 폴더에서 VS Code 구동해서 테스트 실행
5. VS Code에서 터미날을 열고 아래와 같이 테스트 실행
```
$ ls
evsp_adv-master/  venv/

$ source venv/scripts/activate
(venv)
$ ls
evsp_adv-master/  venv/
(venv)
$ source venv/scripts/activate
(venv) 
```
6. 추가로 설치해야 할 것들 아래와 같이 설치 수행
```
$ pip install channels
$ pip install djangorestframework
$ pip install mysqlclient
$ pip install pillow
```
