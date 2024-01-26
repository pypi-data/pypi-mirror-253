# wttch 的 AI 训练工具包

## 一、消息通知

### 1.1 钉钉 webhook 通知

[钉钉 webhook 机器人API](https://open.dingtalk.com/document/orgapp/robot-message-types-and-data-format#title-z74-8to-i7e)

```python
from wttch.train.notification import DingtalkNotification

# 钉钉机器人 webhook 的链接
webhook_url = ''
# 消息签名的密钥
secret = ''

notification = DingtalkNotification(webhook_url, secret)

# 发送文本通知
notification.send_text("")
# 发送markdown
notification.send_markdown('')
```

### 1.2 企业微信 webhook 通知

[企业微信机器人API](https://developer.work.weixin.qq.com/document/path/91770)

```python
from wttch.train.notification import WechatNotification

# 企业微信机器人 webhook 的链接
webhook_url = ''
notification = WechatNotification(webhook_url)

# 发送文本通知
notification.send_text("")
# 发送markdown
notification.send_markdown('')
```

## 二、训练工具包

### 2.1 缓存工具

> 不需要修改太多代码就可以帮助你缓存数据到指定的缓存文件去。
>
> (1). 添加 cache_wrapper;
> (2). 正常调用你的函数。

```python
from wttch.train.utils import cache_wrapper

# 缓存的文件名字前缀，函数的参数会被添加到该名字后面
prefix = 'dataset'
# 缓存的文件夹位置
save_path = './dataset_cache'


@cache_wrapper(prefix=prefix, save_path=save_path)
def you_load_dataset_function():
    return {'a': 1, 'b': 2}


you_load_dataset_function()
```

### 2.2 计时器

```python
from wttch.train.utils import StopWatch

stopwatch = StopWatch()
stopwatch.start("job 1")
# 费时操作
stopwatch.stop()
stopwatch.start("job 2")
# 费时操作
stopwatch.stop()

# 格式化打印
stopwatch.display()
```

## 2.3 进度条
> 简单包装了 `tqdm` 工具。

```python
from wttch.train.utils.progress import Progress

with Progress(total=1000) as progress:
    for i in range(1000):
        # 在这里训练

        # 进度条末尾显示训练结果
        progress.train_result(loss=0.01, acc=0.02)
```

## 三、torch 工具包

### 3.1 方便设备获取

> (1). 将使用的设备写入 thread local;
> (2). 从 thread local 中获取设备数据;
> (3). 训练。

```python
from wttch.train.torch.utils import try_gpu, get_device_local, set_device_local

# 尝试获取 gpu 并写入 thread local
set_device_local(try_gpu(device_no=0))

# 从 thread local 读取设备
device = get_device_local()

```