# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "dbizs"
app_title = "Digital BizSolution"
app_publisher = "vinhnguyen.t090@gmail.com"
app_description = "Digital BizSolution"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "vinhnguyen.t090@gmail.com"
app_license = "MIT"

website_context = {
	"favicon": 	"/assets/dbizs/images/dbizs-ico-32.png",
	"splash_image": "/assets/dbizs/images/logo_dbizs.png"
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/dbizs/css/dbizs.css"
# app_include_js = "/assets/dbizs/js/dbizs.js"

app_include_css = "/assets/dbizs/css/custom.css"

app_include_js = [
    "/assets/dbizs/js/custom.js",
    "/assets/js/dbizs-template.min.js",
]

# include js, css files in header of web template
# web_include_css = "/assets/dbizs/css/dbizs.css"
# web_include_js = "/assets/dbizs/js/dbizs.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "dbizs.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "dbizs.install.before_install"
# after_install = "dbizs.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dbizs.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"dbizs.tasks.all"
# 	],
# 	"daily": [
# 		"dbizs.tasks.daily"
# 	],
# 	"hourly": [
# 		"dbizs.tasks.hourly"
# 	],
# 	"weekly": [
# 		"dbizs.tasks.weekly"
# 	]
# 	"monthly": [
# 		"dbizs.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "dbizs.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "dbizs.event.get_events"
# }

