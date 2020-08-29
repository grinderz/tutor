# -*- coding: utf-8 -*-
import os
from cms.envs.devstack import *

LMS_BASE = "{{ LMS_HOST }}:8000"
LMS_ROOT_URL = "http://" + LMS_BASE
FEATURES["PREVIEW_LMS_BASE"] = "preview." + LMS_BASE

{% include "apps/openedx/settings/partials/common_cms.py" %}

# Setup correct webpack configuration file for development
WEBPACK_CONFIG_PATH = "webpack.dev.config.js"

MIDDLEWARE.insert(0, "whitenoise.middleware.WhiteNoiseMiddleware")

{{ patch("openedx-development-settings") }}
{{ patch("openedx-cms-development-settings") }}
