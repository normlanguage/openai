# OpenAI 客户端示例

[English](README.md) | [简体中文](README.zh-CN.md)

[hello.norm](hello.norm) 通过兼容 OpenAI 协议的 `Client` 向仓库内的[本地模拟服务](local_server.py)发送真实 HTTP 请求，然后读取解析后的响应与用量。模拟服务核对请求路径、Bearer 请求头、模型和输入。它不访问 OpenAI，也不需要外部 API 密钥。

[tools.norm](tools.norm) 定义两个带注解的函数，通过 `ToolRegistry` 公开工具定义、把 JSON 参数分派给绑定的 Norm 方法，并拒绝未知工具。它验证本地工具调用，不声称模型实际请求了这些调用。

[agent.norm](agent.norm) 使用同一本地模拟服务的 Chat Completions 端点，处理两轮流式响应。第一轮请求带注解的工具；第二轮接收工具结果并返回文本。回调核对请求和工具完成次数。这验证的是本地协议模拟服务，而非外部模型。

在仓库根目录使用 Python 3 启动模拟服务，再在另一个终端运行独立消费者：

```sh
python samples/local_server.py
```

```sh
norm run samples/hello.norm
```

预期输出：

```text
Hello, Norm
5
```

按 Ctrl+C 停止模拟服务。它只监听 `127.0.0.1:18766`。[module.norm](../openai/module.norm) 定义软件包。模拟服务验证的是本地协议行为，不代表外部服务互操作已经验收。

无需服务即可运行工具示例：

```sh
norm run samples/tools.norm
```

示例输出两次 `15`：第一次来自存入操作，第二次来自余额查询。

保持模拟服务运行，再执行流式 Agent 示例：

```sh
norm run samples/agent.norm
```

它输出 `Balance: 5` 和 `5`。模拟服务核对每次请求，并返回确定的流式事件。尚未验收云端服务。
