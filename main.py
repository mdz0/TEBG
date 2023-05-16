import os.path
from settings_control.stg_ctrl import createConfig
from bot.body import botBody

if __name__ == '__main__':
    if os.path.isfile('settings.ini'):
        botBody()
    else:
        createConfig()
        print('Api_key missing. '
              'The settings.ini file has been created in the directory. '
              'Please paste your api_key there')
