# 📊 SYD - Show Your Data

**Web Programming Assignment: Effortless Data Visualization**

SYD(Show Your Data)는 복잡한 로그인 과정 없이 **CSV 파일 업로드만으로 데이터의 통계 그래프를 즉시 생성**해주는 웹 서비스입니다.

---

## 🚀 Quick Start (Installation)

이 프로젝트는 Docker를 통해 환경에 구애받지 않고 즉시 실행할 수 있습니다.

```bash
# 레포지토리 클론
git clone https://github.com/your-repo/syd.git
cd syd

# 서비스 실행
docker-compose up
# 혹은
cmake

```

실행 후 브라우저에서 `localhost` (또는 설정된 포트)로 접속하세요.

---

## ✨ Key Features (Current Progress)

현재 구현된 주요 기능들은 다음과 같습니다.

### 🔹 Backend (Django REST Framework)

* **Architecture**: 헥사고날/Layered 아키텍처를 고려한 유연한 프로젝트 구조 설계
* **Environment**: `django-environ`을 통한 환경 변수 관리 및 `local/prod` 설정 분리
* **API**:
* Django REST Framework 기반의 데이터 통신 규격 수립
* CORS 설정 완료 (Frontend-Backend 통신 최적화)


* **Data Processing**:
* CSV 파일 업로드 및 관리를 위한 `CSVFile` 모델/시리얼라이저 구현
* `BinaryStringGenerator` 인터페이스를 통한 데이터 프레임 처리 로직 구축



### 🔹 Frontend (React with Vite)

* **Modern Stack**: Vite를 사용한 빠른 번들링 환경 및 ESLint/Prettier 코드 컨벤션 적용
* **UI/UX**:
* React-Bootstrap 기반의 반응형 웹 디자인
* 메인 레이아웃(Header, Body, Footer) 및 모달 컴포넌트 구현


* **Visualization**:
* `Plot` 컴포넌트를 통한 데이터 시각화 블록 구현
* 드래그 앤 드롭 또는 클릭을 통한 `CSVUpload` 컴포넌트 구축



---

## 🛠 Tech Stack

| Category | Tech Stack |
| --- | --- |
| **Backend** | Django & Django REST Framework (DRF) |
| **Frontend** |  React (with Vite)  |
| **DevOps** |  Docker  |

> React-bootstrap-icons used

---

## 📂 Project Structure

```text
.
├── BACK.md
├── FRONT.md
├── LICENSE
├── Makefile
├── README.md
├── back
│   ├── Dockerfile.prod
│   ├── api
│   │   ├── __init__.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── utils
│   │   └── views.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── django
│   │   ├── env.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   ├── manage.py
│   └── requirements.txt
├── docker-compose.yml
├── front
│   ├── Dockerfile.prod
│   ├── dist
│   │   ├── assets
│   │   └── index.html
│   ├── nginx.conf
│   ├── package.json
│   └── vite.config.js
└── scripts
    └── get_secret_key.sh
```

---

## 📜 License

[MIT License](./LICENSE)

Copyright (c) 2024 Park Seonghun