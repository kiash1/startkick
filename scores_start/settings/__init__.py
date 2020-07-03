
from .base import *

from .urls_paths import *

from .apps import *

from .logging import *

from .email import *

from .system_settings import *



########### SERVER OVERRIDE ###########

from scores_start.configs.config import *

from .thirdparty import *

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

import pymysql
pymysql.install_as_MySQLdb()