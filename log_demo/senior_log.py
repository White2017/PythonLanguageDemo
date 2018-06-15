# coding:utf-8  fxb_qzyx@163.com
"""
   logging模块的使用：使用字典配置log参数(dictConfig())
   参考资料：http://yshblog.com/blog/125
"""

import os
import logging.config

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 生产环境:True, 开发环境：False
DEBUG = True


# 给过滤器使用的判断
class RequireDebugTrue(logging.Filter):
    # 重写filter方法
    def filter(self, record):
        return DEBUG


LOGGING = {
    # 基本设置
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用现有的记录器

    # 日志管理器集合
    'loggers': {
        # 管理器
        'mylog': {
            'handlers': ['console', 'log'],  # 处理器
            'level': 'DEBUG',  # 日志级别
            'propagate': True,  # 是否传递给父记录器
        },
    },

    # 日志格式集合
    'formatters': {
        # 标准输出格式
        'standard': {
            'format': '[%(asctime)s]-[Line:%(lineno)s]-%(levelname)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'  # 时间格式化输出
        }
    },

    # 过滤器
    'filters': {
        'require_debug_true': {
            '()': RequireDebugTrue,
        }
    },

    # 处理器集合
    'handlers': {

        # 输出到控制台
        'console': {
            'level': 'DEBUG',  # 输出信息的最低级别
            'class': 'logging.StreamHandler',
            'formatter': 'standard',  # 使用standard格式
            'filters': ['require_debug_true', ],  # 仅当 DEBUG = True 该处理器才生效
        },

        # 输出到文件
        'log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(BASE_DIR, 'debug.log'),  # log日志的保存位置
            'maxBytes': 1024 * 1024 * 5,  # 文件大小 5M
            'backupCount': 5,  # 备份份数
            'encoding': 'utf8',  # 文件编码
        },
    },

}

if __name__ == "__main__":
    # 加载log配置
    logging.config.dictConfig(LOGGING)
    # 获取名为mylog的日志管理器
    logger = logging.getLogger('mylog')
    # 打印不同级别的log日志
    logger.debug("python debug test")
    logger.warn("python warn test")
    logger.info("python info test")
