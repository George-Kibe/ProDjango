SECRET_KEY = "django-insecure-6&-=rwy^_xt+dc6rcynclae3n$#i$sp+j+y)_=gojo45t%0s(f"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

LOGGING['formatters']['colored'] = {  # type: ignore
    '()': 'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
}
LOGGING['loggers']['core']['level'] = 'DEBUG'  # type: ignore
LOGGING['handlers']['console']['level'] = 'DEBUG'  # type: ignore
LOGGING['handlers']['console']['formatter'] = 'colored'  # type: ignore
