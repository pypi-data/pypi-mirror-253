### 一个全局拦截日志并转为loguru日志的插件

<a href="https://pypi.org/project/usepy-plugin-logger" target="_blank">
    <img src="https://img.shields.io/pypi/v/usepy-plugin-logger.svg" alt="Package version">
</a>

<a href="https://pypi.org/project/usepy-plugin-logger" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/usepy-plugin-logger.svg" alt="Supported Python versions">
</a>

#### 安装

> pip install use-logger

#### 使用

- 直接使用

```python
from use_logger import useLogger

useLogger()  # 使用默认配置
```

- 如果你是usepy用户

```python
from usepy.plugin import useLogger

useLogger()  # 使用默认配置

```

如果你自身项目正在使用`loguru`，这一切似乎感觉毫无变化。因为默认的配置只是修改了一点输出样式。

如果想要感受它带来的“魔法”，需要稍微配置一下。

```python
from usepy.plugin import useLogger

useLogger(packages=["scrapy", "django", "usepy"])

```

##### Logstash/Filebeat

日志的更重要能力是将日志记录发送到`Logstash`/`Filebeat`，这样就可以将日志记录存储到`Elasticsearch`
中，方便进行日志分析。所以统一日志的最终输出格式是非常重要的。

`useLogger`内置一个`logstash_handler`统一化输出格式。

```python
from loguru import logger
from usepy.plugin import useLogger, useLoggerHandlers

useLogger(
    handlers=[
        useLoggerHandlers.logstash_handler(level="DEBUG", extra={"app_name": "spider"})
    ],
    packages=["usepy"],  # hook拦截 usepy 的日志
    extra={"project_name": "usepy"}
)
logger.warning("test warning")
logger.info("test info")
logger.debug("test debug")

```

##### Uvicorn/FastAPI

使用 `uvicorn` 作为 `FastAPI` 的服务器，那么你可以使用 `useLogger` 来拦截 `uvicorn` 的日志。
(如果使用的是 `gunicorn`， 那么只要指定 `class` 为 `uvicorn.workers.UvicornWorker` 即可)

```python

fr

```