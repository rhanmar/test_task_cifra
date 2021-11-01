## Test Task Cifra-k

### News Web-App

#### Endpoints
* Articles (List, Retrieve, Update, Partial Update, Delete)
* Article Types (List, Retrieve, Update, Partial Update, Delete)
* Articles Extended List with information about Article Type: name, color (List)

#### Endpoint filters
* Articles: *type*
* Articles Types: *name, color*
* Articles Extended List: *type_name, type_color*

#### Usage

* Clone from github https://github.com/rhanmar/test_task_cifra
* Start app
  * Via docker  
    * ```docker build --tag cifra . ```  
    * ```docker run -p 8000:8000 cifra```  
    * Open http://localhost:8000/ in browser
    * if you need to save your data after stopping the server use ```docker run -v news_data:/app/data -p 8000:8000 cifra```
  * Via manage.py
    * create virtual environment
    * ```python manage.py migrate```
    * ```python manage.py runserver```
