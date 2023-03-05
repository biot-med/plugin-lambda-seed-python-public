import src.interceptor_post.index as INTERCEPTOR_POST
import src.interceptor_post_entity.index as INTERCEPTOR_POST_ENTITY
import src.interceptor_pre.index as INTERCEPTOR_PRE
import src.nonspecific.index as NONSPECIFIC
import src.notification.index as NOTIFICATION

from src.utils.index import *

from src.constants import *

functions_mapper = {
    "INTERCEPTOR_POST": INTERCEPTOR_POST,
    "INTERCEPTOR_POST_ENTITY": INTERCEPTOR_POST_ENTITY,
    "INTERCEPTOR_PRE": INTERCEPTOR_PRE,
    "NONSPECIFIC": NONSPECIFIC,
    "NOTIFICATION": NOTIFICATION
}