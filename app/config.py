import os
DEBUG = True
# INSECURE KEY - only for testing
PRIVATE_KEY_PATH = os.getenv("PRIVATE_KEY", "private.pem")
PUBLIC_KEY_PATH = os.getenv("PUBLIC_KEY", "public.pem")
