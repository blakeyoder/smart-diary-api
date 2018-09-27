import os
from application.factories import create_app

stage = os.environ.get('STAGE', 'dev')
dotted_config_path = 'application.config.{}.Config'.format(stage)
app_name = os.environ.get('APP', 'Smart-Diary-API')

app = create_app(app_name, dotted_config_path=dotted_config_path)
