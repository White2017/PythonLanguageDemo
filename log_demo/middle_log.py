# coding:utf-8  fxb_qzyx@163.com
"""
   logging模块的使用：使用basicConfig()方法进行配置
"""

import logging

log_path = "D:/middle_log.log"

# 指定log日志的输出格式
format = '[%(asctime)s]-[Line:%(lineno)s]-%(levelname)s: %(message)s'

# 配置文件log日志
logging.basicConfig(level=logging.DEBUG,
                    format=format,
                    filename=log_path,
                    datefmt='%Y-%m-%d %H:%M:%S'  # 时间格式化输出
                    )

# 设置控制台日志处理器
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(format))
console_handler.setLevel(logging.DEBUG)

# 添加控制台打印处理器
logger = logging.getLogger("MyLog")
logger.addHandler(console_handler)

# 调用不同日志级别，输出log信息
logger.debug("python debug test")
logger.info("python info test")
logger.warn("python warn test")

if __name__ == "__main__":
    pass
