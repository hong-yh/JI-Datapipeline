"""Insta485 development configuration."""

import os

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Database file is var/jidp2.sqlite3
DATABASE_FILENAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'jidp2.sqlite3'
)

# Email service
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'jidpalert@gmail.com'
MAIL_PASSWORD = 've450dp22'
MAIL_USE_TLS = False
MAIL_USE_SSL = True