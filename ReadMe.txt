This is a Virtual Library Management System Project mainly focused on Back-end side, written in Python & Django.
For database I use PostgreSQL and Front-end is done via HTML, CSS & JavaScript.


*********** Important Information ***********

For Safety purposes I remove the setting.py file of this project from repositories, but for your convenience
I added Instrustions below for setting.py file which you have to complete in your setting.py file before running
the server.


********* Instructioins **********
 
# we need to configure our apps (need, accounts, first) for migrations in INSTALLED_APPS list

INSTALLED_APPS = [
    'need.apps.NeedConfig',
    'accounts.apps.AccountsConfig',
    'first.apps.FirstConfig', 
]


# add path of our templates in the TEMPLATES list

'DIRS': [os.path.join(BASE_DIR, 'templates')],


# we are using Postres as a backend so we change default database setting

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': Your Database Name (in string),
        'USER': Username of your Database (in string),
        'PASSWORD': Your Password (in string),
        'HOST': 'localhost'
    }
}


# add path of your static files(images etc) from static folder

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]



******** Contact ********

Aseem Ranjan
+91-9982054542
aseemranjan10@gmail.com