# OpenAI for Norm

OpenAI-compatible Responses and Chat Completions client for [Norm](https://github.com/normlanguage/Norm), with streaming output and function tools.

Add the published module to `module.norm`:

```norm
dependency(repository: "github", name: "openai", version: 1)
```

The package is published as `openai-1.nar` in the [`v1` release](https://github.com/normlanguage/openai/releases/tag/v1). It requires a Norm compiler with the standard-library APIs introduced after `v0.24.0`; it was verified with the compiler built from Norm commit `6c3e1c5`.

The source is in [`openai/`](openai). This module was originally developed in [normlanguage/Norm](https://github.com/normlanguage/Norm/tree/main/norm/libraries/openai). It is licensed under [MPL-2.0](LICENSE).
