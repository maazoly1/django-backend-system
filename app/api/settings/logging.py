LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'filters': []
        }
    },
    'loggers': {
        logger_name : {
            'level': 'WARNING',
            'propogate': True
        } for logger_name in ('django', 'django_request', 'django.db.backends', 'django_template', 'core')
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'] 
    }
}