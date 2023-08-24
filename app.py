from flask import Flask
from datetime import datetime as dt
from importlib import import_module
from blueprints import all_blueprints

def create_app():
    app = Flask(__name__)
    # app.config.from_object('config.Config')

    for blueprint in all_blueprints:
        import_module(blueprint.import_name)
        app.register_blueprint(blueprint)

    return app

app = create_app()

# @app.template_filter('strftime')
# def _jinja2_filter_datetime(data, fmt=None):
#     dateformat = dt.strptime(data,'%Y-%m-%d %H:%M:%S.%f')
#     return dt.strftime(dateformat,'%Y/%m/%d %H:%M')
    
# @app.template_filter('stuats')
# def _jinja2_filter_status(data, fmt=None):
#     try:
#         status_dict = {
#         'RECEIVE':'未処理',
#         'DENY':'否認',
#         'ACCEPT':'承認済（登録・削除待ち）',
#         'SUCCESS':'エラーなし',
#         'FAIL':'エラーあり'
#         }
#         return status_dict[data]
#     except:
#         return '未処理'
    