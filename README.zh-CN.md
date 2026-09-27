# OpenAI for Norm

[English](README.md) | [简体中文](README.zh-CN.md)

适用于 [Norm](https://github.com/normlanguage/Norm) 的 OpenAI 兼容 Responses 和 Chat Completions 客户端，支持流式输出与函数工具。

在 `module.norm` 中添加已发布的模块：

```norm
dependency(repository: "github", name: "openai", version: 1)
```

该包以 `openai-1.nar` 发布于 [`v1` Release](https://github.com/normlanguage/openai/releases/tag/v1)。它需要包含 `v0.24.0` 之后引入的标准库 API 的 Norm 编译器；已使用从 Norm 提交 `6c3e1c5` 构建的编译器验证。

源码位于 [`openai/`](openai)。该模块最初在 [normlanguage/Norm](https://github.com/normlanguage/Norm/tree/main/norm/libraries/openai) 中开发，采用 [MPL-2.0](LICENSE) 许可。
