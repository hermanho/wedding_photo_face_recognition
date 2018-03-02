import logging
import logging.config


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s - (%(name)s)[%(levelname)s] - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'logFile': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'verbose',
            'when': 'D',
            'interval': 1,
            'backupCount': 7,
            'filename': 'wedding_photo_face_recognition.log',
            'encoding': 'utf-8'
        }
    },
    'loggers': {
        'wedding_photo_face_recognition': {
            'handlers': ['console', 'logFile'],
            'propagate': False,
            'level': 'INFO',
        }
    }
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger('wedding_photo_face_recognition')
