import os.path

from scrapy.cmdline import execute

import sys


def run_spider(spider_dir: str, spider_name: str, **kwargs):
    sys.path.append(spider_dir)
    tmp_cwd = os.getcwd()
    os.chdir(spider_dir)
    cmd_list = ['scrapy', 'crawl', spider_name]
    if kwargs:
        for arg_name, arg_value in kwargs.items():
            cmd_list.append('-a')
            cmd_list.append(f'{arg_name}={arg_value}')
    execute(cmd_list)
    os.chdir(tmp_cwd)


if __name__ == '__main__':
    spider_path = os.path.dirname(os.path.abspath(__file__))
    run_spider(spider_path, 'quotes')
