# -*-coding:utf-8-*-
# @Time : 2019/6/21 上午7:39
# @Author : pyz
# @Project : wiki
# @File : wiki.py
# @Software: PyCharm


from app import create_app

#log
# import logging
#
# logging.basicConfig(filename='app.log', format='%(asctime)s - %(name)s - %(levelname)s '
#                                                '%(filename)s - %(module)s - %(funcName)s -%(lineno)d'
#                                                '%(message)s')

# 引起工厂应用模式 实例化

if __name__ == '__main__':
    app = create_app('config_name')
    app.run(host='0.0.0.0', port=8080, debug=True)
    # 此处配置已失效