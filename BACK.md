
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

- [✓] Upload API
  - [✓] `File` Model
  - [✓] `FileSerializer` Serializer
  - [✓] `FileAPIView` APIView class

- Services
  - Visualizing API
    - [✓] Board
      - Member Variables
        - fig, axs, graphs, source_table, numerical_variables, categorical_variables, datetime_variables
      
      - Methods
        - [✓] choose(): choose plot type in various plot types
        - [✓] draw(): show all graphs
        - [✓] set(): setting variables of specific graph
        - [✓] resize(): adjust the board size

- Utils
  - [ ] Graph
    - Member Variables
      - axis, plot_type

    - Methods
      - [ ] show(): show graph(
        [✓] bar, [ ]hist, [ ]scatter, [ ]line
      )
