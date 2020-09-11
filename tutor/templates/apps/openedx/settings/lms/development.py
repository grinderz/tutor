# -*- coding: utf-8 -*-
import os
from lms.envs.devstack import *

{% include "apps/openedx/settings/partials/common_lms.py" %}

# Setup correct webpack configuration file for development
WEBPACK_CONFIG_PATH = "webpack.dev.config.js"

SESSION_COOKIE_DOMAIN = ".{{ LMS_HOST|common_domain(CMS_HOST) }}"

LMS_BASE = "{{ LMS_HOST}}:8000"
LMS_ROOT_URL = "http://{}".format(LMS_BASE)
LMS_INTERNAL_ROOT_URL = LMS_ROOT_URL
SITE_NAME = LMS_BASE
CMS_BASE = "{{ CMS_HOST}}:8001"
CMS_ROOT_URL = "http://{}".format(CMS_BASE)
LOGIN_REDIRECT_WHITELIST.append(CMS_BASE)

FEATURES['ENABLE_COURSEWARE_MICROFRONTEND'] = False
COMMENTS_SERVICE_URL = "http://{{ FORUM_HOST }}:4567"

LOGGING["loggers"]["oauth2_provider"] = {
    "handlers": ["console"],
    "level": "DEBUG"
}

{% if ACTIVATE_HTTPS %}
# Properly set the "secure" attribute on session/csrf cookies. This is required in
# Chrome to support samesite=none cookies.
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
DCS_SESSION_COOKIE_SAMESITE = "None"
{% else %}
# When we cannot provide secure session/csrf cookies, we must disable samesite=none
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
DCS_SESSION_COOKIE_SAMESITE = "Lax"
{% endif %}

# Required to display all courses on start page
SEARCH_SKIP_ENROLLMENT_START_DATE_FILTERING = True

{{ patch("openedx-development-settings") }}
{{ patch("openedx-lms-development-settings") }}
