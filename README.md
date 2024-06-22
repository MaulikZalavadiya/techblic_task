# techblic_task

### Run the following commands to get started:
```
git clone https://github.com/MaulikZalavadiya/techblic_task.git techblic_task
python3 -m venv venv
```

#### Activate the virtual environment

Mac OS / Windows
```source env/bin/activate```

Linux
```.\env\Scripts\activate```

```
cd techblic_task
pip install -r requirements.txt
```


# Overview

This project is a Language Traslate App.
It was built using Django and contains the following:

* Allows new accounts registration, login and logout change-password, forgot-password.
* token-based authentication system.


* [Authentication](#auth)
  * Signup ```http://127.0.0.1:8000/api/accounts/register/```
  * Login ```http://127.0.0.1:8000/api/accounts/login/```
  * change-password ```http://127.0.0.1:8000/api/accounts/change-password/```
  * forgot-password ```http://127.0.0.1:8000/api/accounts/forgot-password/```
  * logout ```http://127.0.0.1:8000/api/accounts/token/refresh/```


* [Message](#CRUD)
  * Get-recipe ```http://127.0.0.1:8000/api/messages/```
  * Post-recipe ```http://127.0.0.1:8000/api/messages/```
