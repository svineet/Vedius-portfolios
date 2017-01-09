# Vedius-portfolios
Django application which allows multiple users (students) to share their projects and create their online portfolio.

Using Social Accounts validation (allauth - Google, Facebook and local accounts), CKEditor for modyfing projects content and more.

## Requirements

pip:

* django-allauth
* django-ckeditor
* django-wysiwyg
* html5lib
* oauthlib
* olefile
* Pillow
* python-openid
* pytidylib
* requests
* requests-oauthlib
* webencodings==0.5

## Configuration

To configure Facebook and Google authentication generate ID's and secret keys.

* Google - <https://developers.google.com/identity/sign-in/web/devconsole-project>
* Facebook - <http://developers.facebook.com>


Admin panel

* Sites - remove example, add your site
* Social Applications - add social ID's, Key's and relate to site


## What we are using

* Django allauth <https://github.com/pennersr/django-allauth>
* Django ckeditor <https://github.com/django-ckeditor/django-ckeditor>