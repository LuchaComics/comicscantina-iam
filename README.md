pip install django                        # Our MVC Framework
pip install django-environ                # Environment Variables with 12factorization
pip install Pillow                        # Req: ImageField
pip install django-cors-headers           # Enable CORS in Headers
pip install gunicorn                      # Web-Server Helper
pip install djangorestframework           # RESTful API Endpoint Generator
pip install django-starterkit             # Django starter kit
pip install django_filter                 # Filter querysets dynamically
#pip install djangorestframework-msgpack   # MessagePack support for Django REST framework
#pip install djangorestframework-jwt       # JSON Web Token Authentication support for Django REST Framework
pip install django-oauth-toolkit


# Step 1 - Read
http://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/getting_started.html

# Step 2 - Create super user and login
python manage.py createsuperuser


# Step 3 - Create
Name: IAM API endpoints Access
Client ID: jFjWI9lRbPKCrQfZnliJElEz4QWbTsTiOalFDN5j
Client secret: JBfIbsbSvgHuu1W1PsDU3UjbHii9RUaMBU8IJyAnMr1XLxYu9SnEerOCF3Nwip76HsPXJWMHFKFrUJ8IMEJ3DwpDQXNAJjMzaWbbNXGiJhch1pMgM62eUuGadnKL2eJB
Client type: Confidential
Authorization grant type: Resource owner password-based


# Step 3 - Run
curl -X POST -d "grant_type=password&username=bmika@icloud.com&password=123password" -u"<client_id>:<client_secret>" http://127.0.0.1:8000/o/token/


# Step 4 - JSON output
{
    "access_token": "eHTvXwfztswmrxAQCGEykUY75hJDvD",
    "expires_in": 36000,
    "token_type": "Bearer",
    "scope": "read write groups",
    "refresh_token": "HadQyAUKNNA4VpaZcgAC1367Ie4uWu"
}


# Step 5 - Run

# Retrieve users
curl -H "Authorization: Bearer eHTvXwfztswmrxAQCGEykUY75hJDvD" http://127.0.0.1:8000/users/


# Step 6 - Refresh
curl -X POST -d "grant_type=refresh_token&client_id=<your_client_id>&client_secret=<your_client_secret>&refresh_token=<your_refresh_token>" http://localhost:8000/o/token/
