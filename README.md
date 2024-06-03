# SYD - Show Your Data
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
  - [✓] Add SASS compile command in `Makefile`
  - [✓] Add react-bootstrap and react-bootstrap-icons for design


- [✓] Initialize others (config files, folders, ...)
  - [✓] Setup test api for communication in djangorestframework
  - [✓] Add `app/back/api/models.py` for testing
  - [✓] Add `app/back/api/serializers.py` for testing
  - [✓] Add axios package and setup communication in react
  - [✓] Add django-cors-headers module and setup communication in django
  - [✓] Modify wrong proxy with proxy for Vite
  - [✓] Initialize all unnecessary settings for pre-test


- [✓] Backend - Create Models & Serializers or Others
  - [✓] Create `CSVFile` Model for request, `CSVFileSerializer` Serializer and `CSVFileAPIView` APIView class

  - [✓] Implement transferring binary strings to the frontend server
    - [✓] Implement `BinaryStringGenerator` Pseudo-Interface
      - [✓] Define `get_binary_strings()` abstract method
    
    - [✓] Implement `Frame` class which is inherted `BinaryStringGenerator` interface
      - [✓] Make `get_binary_strings()` function
  
  - [✓] Remove temp file `test.csv` and reduce class (removing `Graph`)
  - [ ] Modify `frame.py` to add more graph types
  - [ ] Add title in graph

- [✓] Frontend - Implements Components & Features and Design Layout in App
  - [✓] Styling initial page
    - [✓] Create `CSVUpload.jsx`, `Body.jsx`, `Footer.jsx`, `Header.jsx`
    - [✓] Create `CSVUpload.scss`, `Body.scss`, `Footer.scss`, `Header.jsx`
    - [✓] Implement Drag & Drop in `CSVUpload.jsx` component
  
  - [✓] Styling Block component
    - [✓] Create `DownloadButton.jsx`, `Plot.jsx`, `Block.jsx` and `Loading.jsx` components
    - [✓] Create `DownloadButton.scss`, `Plot.scss`, `Block.scss`, `Loading.scss`
    - [✓] Implement visualizing graphs with response
    - [✓] With modal window technique
      - [✓] Implement loading screen in `Modal.jsx`
    - [✓] Implement download function

  - [ ] Styling responsive web design
    - [ ] Create a `RadialMenu.scss` and `RadialMenu.jsx` component

- [ ] Validate Unit Test
- [ ] Validate Integrated Test
- [ ] Refactoring and Find Lazy Loading
- [ ] Import Guidelines and Documents for Project