from flask import Blueprint
import os

all_list = []
main = Blueprint('main', import_name='apps.main.index', url_prefix='/')
all_list.append(main)
# if os.path.exists(os.getcwd ()+"/apps/main"):
#     main = Blueprint('main', import_name='apps.main.index', url_prefix='/')
#     all_list.append(main)

all_blueprints = tuple(all_list)