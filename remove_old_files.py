import yaml
import os
import re
import datetime
import logging
from pathlib import Path
from dateutil import relativedelta


config_path = os.path.join(os.getcwd(), 'config.yml')
with open(config_path, 'r') as stream:
    yaml_data = yaml.safe_load(stream)

yaml_keys = list(yaml_data.keys())

current_date = datetime.date.today()
log_name = 'removed_files' + current_date.strftime('%Y_%m_%d') + '.log'
log_path = os.path.join(os.getcwd(), 'logs')
log_file_path = os.path.join(log_path, log_name)
Path(log_path).mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename=log_file_path, level=logging.INFO
                    , format='%(asctime)s %(levelname)-8s %(message)s'
                    , datefmt='%Y-%m-%d %H:%M:%S')
logging.info('Run started')
for key in yaml_keys:
    date_add_list = [relativedelta.relativedelta(days=yaml_data[key]['days_back']),
                     relativedelta.relativedelta(weeks=yaml_data[key]['weeks_back']),
                     relativedelta.relativedelta(months=yaml_data[key]['months_back']),
                     relativedelta.relativedelta(years=yaml_data[key]['years_back'])]
    max_date = current_date - date_add_list[0] - date_add_list[1] - date_add_list[2] - date_add_list[3]
    path = yaml_data[key]['path']
    file_regex = yaml_data[key]['file_regex']
    file_list = [f for f in os.listdir(path) if re.search(file_regex, f)]
    path_file_list = [os.path.join(path, f) for f in file_list]
    stat_file_list = [(pf, datetime.datetime.utcfromtimestamp(os.path.getmtime(pf)).date())
                      for pf in path_file_list if os.path.isfile(pf)]
    for f in stat_file_list:
        if f[1] < max_date:
            os.remove(f[0])
            logging.info(key + ' ' + f[1].strftime('%Y-%m-%d') + ' ' + f[0])

logging.info('Run finished')
