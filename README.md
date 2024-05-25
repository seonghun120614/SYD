# MyBlog
Web Programming Assignment &amp; Usage of Data Visualization

# 🧑🏼‍💻 Requirements
- [✓] Initialize Django with Django REST framework
  - [✓] Create Django Project
  - [✓] Revise file structures for my project
  - [✓] Revise `app/back/config/django/base.py`
  - [✓] Create `app/back/config/env.py` for environment variables
  - [✓] Devide configuration for local environment to add `app/back/config/django/local.py`
  - [✓] Revise `app/back/config/asgi.py` and `app/back/config/wsgi.py`
  - [✓] Create `Makefile` for managing and building Django project
  - [✓] Install djangorestframework and import

- [✓] Initialize React
  - [✓] Create React App & Modify `.gitignore`
  - [✓] Clean unnecessary files or codes
  - [✓] Modify file structure
  - [✓] Add ESLint and Prettier packages
  - [✓] Ready for imigrate CRA to Vite
  - [✓] Remove CRA project and rename folders and files for division in back
  - [✓] Add codes `Makefile` for managing and building Vite project

- [✓] Initialize others (config files, folders, ...)
  - [✓] Setup test api for communication in djangorestframework
  - [✓] Add `app/back/api/models.py` for testing
  - [✓] Add `app/back/api/serializers.py` for testing
  - [✓] Add axios package and setup communication in react
  - [✓] Add django-cors-headers module and setup communication in django
  - [✓] Modify wrong proxy with proxy for Vite
  - [✓] Initialize all unnecessary settings for pre-test

- [✓] Backend - Create Models & Serializers or Others
  - [✓] Create `CSVFile` Models for request
  - [✓] Create `CSVFileSerializer` Serializers
  - [✓] Create `CSVFileAPIView` APIView class
  - [✓] Create "api/" urlpattern and binding to `CSVFileAPIView`
  - [✓] Add brief comments for every codes

- [ ] Frontend - Implements Components & Features and Design Layout in App
  - [✓] Create a `CSVUpload.jsx` component
  - [✓] Create a `DownloadButton.jsx` component
  - [✓] Create a `Plot.jsx` component
  - [✓] Create a `Block.jsx` component & add comments
  - [✓] Create a `Loading.jsx` component
  - [✓] Create a `Header.jsx` layout
  - [✓] Create a `Body.jsx` layout
  - [✓] Create a `Footer.jsx` layout
  - [✓] Modify code style about whole functions
  - [ ] Create a `RadialMenu.jsx` component

- [ ] Frontend - Styling with Sass & Bootstrap
  - [✓] Add SASS compile command in `Makefile`
  - [✓] Add react-bootstrap and react-bootstrap-icons for design
  - [✓] Create a `CSVUpload.css`
  - [✓] Styling a `DownloadButton.jsx` component with bootstrap
  - [✓] Styling size of `Plot.jsx` for long width graph (It must be implemented with horizontal scroll)
  - [✓] Styling `Block.jsx` with all components
  - [✓] Create a `Loading.css`
  - [✓] Styling a `Header.jsx` with main component `Block.jsx`
  - [✓] Create a `Body.css` & Modify all components' size
  - [✓] Create a `Footer.css`
  - [✓] Modify a `Body.jsx` layout for testing communication with back server
    - [✓] Implement Drag & Drop in `CSVUpload` component
  - [ ] Create a `RadialMenu.css`

- [ ] Validate Unit Test
- [ ] Validate Integrated Test
- [ ] Refactoring and Find Lazy Loading
- [ ] Import Guidelines and Documents for Project