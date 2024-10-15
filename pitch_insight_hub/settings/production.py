from .base import *

DEBUG = False

ALLOWED_HOSTS = ['your-domain.com']  # Replace with your actual domain

# Add any production-specific settings here, such as:
# - Database configurations
# - Static file serving
# - Security settings (HTTPS, HSTS, etc.)
# - Logging configurations
# - Caching settings

# Example:
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True