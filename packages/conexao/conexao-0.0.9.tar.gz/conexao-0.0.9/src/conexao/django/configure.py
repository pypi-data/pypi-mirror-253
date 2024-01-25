import os

import django

from conexao.config import config
from conexao.ssh import start_forward


def configure(profile_name: str):
    '''Configures a Django project to use its ORM.'''
    profile = config['profiles'][profile_name]

    if ssh := profile.get('ssh'):
        start_forward(ssh['host'], ssh['forwards'])

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', profile['django']['settings'])

    django.setup()
