
# Requirements

- [✓] Initialize Django with Django REST framework
  - [✓] Create Django Project
  - [✓] Revise file structures for my project
  - [✓] Revise `app/back/config/django/base.py`
  - [✓] Create `app/back/config/env.py` for environment variables
  - [✓] Devide configuration for local environment to add `app/back/config/django/local.py`
  - [✓] Revise `app/back/config/asgi.py` and `app/back/config/wsgi.py`
  - [✓] Create `Makefile` for managing and building Django project
  - [✓] Install djangorestframework and import
  - [✓] Setup test api for communication in djangorestframework
  - [✓] Add `app/back/api/models.py` for testing
  - [✓] Add `app/back/api/serializers.py` for testing
  - [✓] Add django-cors-headers module and setup communication in django

- [✓] Create Models & Serializers or Others
  - [✓] Create `CSVFile` Model for request, `CSVFileSerializer` Serializer and `CSVFileAPIView` APIView class
  - [✓] Implement transferring binary strings to the frontend server
    - [✓] Implement `BinaryStringGenerator` Pseudo-Interface
      - [✓] Define `get_binary_strings()` abstract method
    - [✓] Implement `Frame` class which is inherted `BinaryStringGenerator` interface
      - [✓] Make `get_binary_strings()` function