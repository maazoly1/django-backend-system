if IN_DOCKER: # type: ignore
    print("RUNNING IN DOCKER MODE")
    assert MIDDLEWARE[:1] == [ # type: ignore
        'django.middleware.security.SecurityMiddleware',
    ]