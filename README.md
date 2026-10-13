# OpenAI for Norm

[English](README.md) | [简体中文](README.zh-CN.md)

OpenAI-compatible Responses and Chat Completions client for [Norm](https://github.com/normlanguage/Norm), with streaming output and function tools.

The [module declaration](openai/module.norm) defines the package. The [samples](samples/README.md) declare their dependencies and include a local OpenAI-compatible HTTP fixture.

## Optional output token limit

For compatible gateways that reject output token limits, explicitly pass `maximumOutputTokens: null` to `ResponseRequest`, either `Client.generate` overload, or `Agent`:

```norm
var answer = client.exchange(stream: false,
  request: ResponseRequest(model: client.defaultModel(),
    input: ResponseInput.Text(value: "Hello, Norm"), maximumOutputTokens: null))
```

This omits `max_output_tokens` for Responses and `max_completion_tokens` for Chat Completions; it does not send JSON `null`. The provider controls the output limit in this mode. Defaults remain 1024 for requests/generation and 8192 for agents. Explicit numeric limits must be positive. There is no automatic retry or fallback that silently removes a requested limit.

Run the offline protocol regression tests with `norm test openai`.

The source is in [`openai/`](openai). This module was originally developed in [normlanguage/Norm](https://github.com/normlanguage/Norm/tree/main/norm/libraries/openai). It is licensed under [MPL-2.0](LICENSE).
