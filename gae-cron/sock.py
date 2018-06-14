from _ssl import \
    RAND_add, \
    RAND_status, \
    SSL_ERROR_ZERO_RETURN, \
    SSL_ERROR_WANT_READ, \
    SSL_ERROR_WANT_WRITE, \
    SSL_ERROR_WANT_X509_LOOKUP, \
    SSL_ERROR_SYSCALL, \
    SSL_ERROR_SSL, \
    SSL_ERROR_WANT_CONNECT, \
    SSL_ERROR_EOF, \
    SSL_ERROR_INVALID_ERROR_CODE
try:
    from _ssl import RAND_egd
except ImportError:
    # LibreSSL does not provide RAND_egd
    pass