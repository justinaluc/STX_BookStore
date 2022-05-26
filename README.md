# STX BookStore APP
*** 
Created as a recruitment task for **Django Developer in STX Next** company;
Django app to manage books in store (create, show, update, delete)
using Google API to import books to the database


## Technologies
* Python
* data type: json
* framework: Django, Django Rest Framework
* Google Books API
* database: PostgreSQL 

## Technical requirements
```
pip install -r requirements.txt
```

## Launch
Deployment of the application using a publicly available server
[link](###)

## Detailed functionalities
1. get info about API: 
```
[GET]      http://.../api_spec
```
2. get the list of **all books** from the database or **filtered**
```
[GET]      http://.../books
[GET]      http://.../books?author="Tolkien"&from=2003&to=2022&acquired=false
```
3. get details of single book
```
[GET]      http://.../books/7
```
4. add new book to collection (database)
```
[POST]     http://.../books
```
5. update details of single book
```
[PATCH]    http://.../books/77
```
6. delete a book
```
[DELETE]   http://.../books
```
7. import books from Google Books API for requested author
```
[POST]     http://.../import
```
*** 

## Created by
Justyna Łuczak _@justinaluc_

find me on [github](https://github.com/justinaluc)
or [linkedin](https://www.linkedin.com/in/justyna-%C5%82uczak-9535ab8b/)
*** 
