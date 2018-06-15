# coding:utf-8  fxb_qzyx@163.com
"""
   logging模块的使用：最一般的写法
"""
import logging

# 获取logger实例，默认为root
logger = logging.getLogger('MyLog')

# 指定log日志的输出格式
formatter = logging.Formatter('[%(asctime)s]-[Line:%(lineno)s]-%(levelname)s: %(message)s')

log_path = "D:/base_log.log"
# 设置文件日志处理器
file_handler = logging.FileHandler(log_path)
file_handler.setFormatter(formatter)

# 设置控制台日志处理器
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# 给logger对象添加处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 设置日志级别：DEBUG模式
logger.setLevel(logging.DEBUG)

# 调用不同日志级别，输出log信息
logger.info("python info test")
logger.debug("python debug test")
logger.warn("python warn test")


if __name__ == "__main__":
    pass
