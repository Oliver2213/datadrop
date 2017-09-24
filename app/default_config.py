# app configuration

DATADROP_URLSTRING_LENGTH = 5 # url strings will be 5 characters long
DATADROP_DEFAULT_LISTED = True # drops will be publicly listed by default
DATADROP_DEFAULT_EXPIRES = False # drops don't expire by default
DATADROP_MIN_EXPIRE_TIME = 30 # drops can't be set to expire less than 30 seconds after they were created
DATADROP_MAX_EXPIRE_TIME = 1209600 # drops can't be set to expire more than 2 weeks after they were created
DATADROP_DEFAULT_EXPIRES_IN = DATADROP_MIN_EXPIRE_TIME + DATADROP_MAX_EXPIRE_TIME/2
DATADROP_DEFAULT_SELF_DESTRUCTS = False # drops don't automatically delete themselves after a certain number of 'GET' requests
DATADROP_DEFAULT_SELF_DESTRUCT_GETS = 2 # when set to self-destruct, and a specific number of gets isn't provided, that drop will be deleted after 2
DATADROP_MAX_DROP_KEYS_PER_DROP = 3 # each drop can only be associated with a max of 3 drop keys
