# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-1vmv^+s%u1fw#a*imqg=*cj3x#%ao@vsy7da%-h8q11$#b+z$x"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

LOGGING['formatters']['colored'] = {  # type: ignore
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
}
LOGGING['loggers']['core']['level'] = 'DEBUG'  # type: ignore
LOGGING['handlers']['console']['level'] = 'DEBUG'  # type: ignore
LOGGING['handlers']['console']['formatter'] = 'colored'  # type: ignore