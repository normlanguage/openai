# OpenAI for Norm

[English](README.md) | [简体中文](README.zh-CN.md)

适用于 [Norm](https://github.com/normlanguage/Norm) 的 OpenAI 兼容 Responses 和 Chat Completions 客户端，支持流式输出与函数工具。

软件包由[模块声明](openai/module.norm)定义。[示例](samples/README.zh-CN.md)声明各自的依赖，并提供本地兼容 OpenAI 协议的 HTTP 模拟服务。

## 可选输出 token 上限

对于拒绝输出 token 上限参数的兼容网关，可以在 `ResponseRequest`、`Client.generate` 的两个重载或 `Agent` 中显式传入 `maximumOutputTokens: null`：

```norm
var answer = client.exchange(stream: false,
  request: ResponseRequest(model: client.defaultModel(),
    input: ResponseInput.Text(value: "你好，Norm"), maximumOutputTokens: null))
```

此时 Responses 请求省略 `max_output_tokens`，Chat Completions 请求省略 `max_completion_tokens`，不会发送 JSON `null`。输出上限由服务端决定。请求和生成方法的默认值仍为 1024，Agent 默认值仍为 8192；显式数值必须大于零。库不会自动重试或静默移除调用者指定的上限。

运行离线协议回归测试：`norm test openai`。

源码位于 [`openai/`](openai)。该模块最初在 [normlanguage/Norm](https://github.com/normlanguage/Norm/tree/main/norm/libraries/openai) 中开发，采用 [MPL-2.0](LICENSE) 许可。
