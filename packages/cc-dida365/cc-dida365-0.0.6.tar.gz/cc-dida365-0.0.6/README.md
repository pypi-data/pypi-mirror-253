## 概览

滴答清单的 Python SDK

## 如何安装

```sh
pip3 install cc-dida365
```

## 如何使用

### 引入模块
```python
from cc_dida365.client import Client
dida = Client(cookie='')
```

## Test

直接在根目录执行 `pytest` 即可，会读取 pytest.ini 的配置，并进行测试