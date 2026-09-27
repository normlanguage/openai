# OpenAI client samples

[English](README.md) | [简体中文](README.zh-CN.md)

[hello.norm](hello.norm) sends a real HTTP request through the OpenAI-compatible `Client` to the included [local fixture](local_server.py), then reads the parsed response and usage. The fixture verifies the request path, bearer header, model, and input. It does not contact OpenAI or require an external API key.

[tools.norm](tools.norm) defines two annotated functions, exposes their definitions through `ToolRegistry`, dispatches JSON arguments to bound Norm methods, and rejects an unknown tool. It exercises local tool invocation; it does not claim a model requested those calls.

[agent.norm](agent.norm) uses the same local fixture's Chat Completions endpoint for two streamed response rounds. The first round requests an annotated tool; the second receives its result and completes with text. Callbacks verify the request and tool completion counts. This tests a local protocol fixture, not an external model.

From the repository root, start the fixture with Python 3, then run the standalone consumer in another terminal:

```sh
python samples/local_server.py
```

```sh
norm run samples/hello.norm
```

Expected output:

```text
Hello, Norm
5
```

Stop the fixture with Ctrl+C. It only listens on `127.0.0.1:18766`. [module.norm](../openai/module.norm) defines the package. The fixture validates local protocol behavior, not external service interoperability.

Run the tool sample without a server:

```sh
norm run samples/tools.norm
```

It prints `15` twice: once from the deposit call and once from the current balance.

With the fixture running, execute the streamed agent sample:

```sh
norm run samples/agent.norm
```

It prints `Balance: 5` and `5`. The fixture validates each request and returns deterministic streamed events. No cloud service was exercised.
