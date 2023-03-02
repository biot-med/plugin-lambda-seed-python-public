from interceptor_post import index as INTERCEPTOR_POST
from interceptor_post_entity import index as INTERCEPTOR_POST_ENTITY
from interceptor_pre import  index as INTERCEPTOR_PRE
from nonspecific import index as NONSPECIFIC
from notification import index as NOTIFICATION

from utils.index import *

from constants import *

functions_mapper = {
    "INTERCEPTOR_POST": INTERCEPTOR_POST,
    "INTERCEPTOR_POST_ENTITY": INTERCEPTOR_POST_ENTITY,
    "INTERCEPTOR_PRE": INTERCEPTOR_PRE,
    "NONSPECIFIC": NONSPECIFIC,
    "NOTIFICATION": NOTIFICATION
}