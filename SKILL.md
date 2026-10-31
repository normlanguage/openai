# openai Skill

Use this skill to work with Norm module `openai` version 5. Use only declarations listed below.

## `openai`

Source: `client.norm`

### `ResponseStatus`

```norm
enum ResponseStatus
```

#### `Completed`

```norm
Completed
```

#### `Incomplete`

```norm
Incomplete
```

#### `Failed`

```norm
Failed
```

#### `Cancelled`

```norm
Cancelled
```

#### `Queued`

```norm
Queued
```

#### `InProgress`

```norm
InProgress
```

### `OpenAiException`

```norm
class OpenAiException extends Exception
```

#### `code`

```norm
String code
```

Type: `String`

#### `httpStatus`

```norm
Integer? httpStatus
```

Type: `Integer?`

#### `requestId`

```norm
String? requestId
```

Type: `String?`

#### `OpenAiException`

```norm
OpenAiException(String code, String message, Integer? httpStatus, String? requestId)
```

Parameters:

- `code`: `String`
- `message`: `String`
- `httpStatus`: `Integer?`
- `requestId`: `String?`

### `StructuredOutputMode`

```norm
enum StructuredOutputMode
```

#### `JsonSchema`

```norm
JsonSchema
```

#### `JsonObject`

```norm
JsonObject
```

### `StructuredOutput`

```norm
value StructuredOutput
```

#### `name`

```norm
String name
```

Type: `String`

#### `schema`

```norm
JsonValue schema
```

Type: `JsonValue`

#### `mode`

```norm
StructuredOutputMode mode
```

Type: `StructuredOutputMode`

### `structuredOutput`

```norm
StructuredOutput structuredOutput<T>(String name, StructuredOutputMode mode)
```

Type parameters:

- `T`

Parameters:

- `name`: `String`
- `mode`: `StructuredOutputMode`

Returns: `StructuredOutput`

### `ResponseInput`

```norm
enum ResponseInput
```

#### `Text`

```norm
Text(String value)
```

Parameters:

- `value`: `String`

#### `Items`

```norm
Items(List<JsonValue> values)
```

Parameters:

- `values`: `List<JsonValue>`

### `ToolDefinition`

```norm
value ToolDefinition
```

#### `name`

```norm
String name
```

Type: `String`

#### `description`

```norm
String description
```

Type: `String`

#### `parameters`

```norm
JsonValue parameters
```

Type: `JsonValue`

#### `strict`

```norm
Boolean strict
```

Type: `Boolean`

### `ToolCall`

```norm
value ToolCall
```

#### `callId`

```norm
String callId
```

Type: `String`

#### `name`

```norm
String name
```

Type: `String`

#### `arguments`

```norm
String arguments
```

Type: `String`

### `ResponseRequest`

```norm
value ResponseRequest
```

#### `model`

```norm
String model
```

Type: `String`

#### `input`

```norm
ResponseInput input
```

Type: `ResponseInput`

#### `instructions`

```norm
String? instructions
```

Type: `String?`

#### `format`

```norm
StructuredOutput? format
```

Type: `StructuredOutput?`

#### `maximumOutputTokens`

```norm
Integer? maximumOutputTokens
```

Type: `Integer?`

#### `tools`

```norm
List<ToolDefinition> tools
```

Type: `List<ToolDefinition>`

### `Usage`

```norm
value Usage
```

#### `inputTokens`

```norm
Long inputTokens
```

Type: `Long`

#### `outputTokens`

```norm
Long outputTokens
```

Type: `Long`

#### `totalTokens`

```norm
Long totalTokens
```

Type: `Long`

### `Response`

```norm
value Response
```

#### `id`

```norm
String id
```

Type: `String`

#### `status`

```norm
ResponseStatus status
```

Type: `ResponseStatus`

#### `text`

```norm
String text
```

Type: `String`

#### `refusal`

```norm
String? refusal
```

Type: `String?`

#### `incompleteReason`

```norm
String? incompleteReason
```

Type: `String?`

#### `usage`

```norm
Usage? usage
```

Type: `Usage?`

#### `errorCode`

```norm
String? errorCode
```

Type: `String?`

#### `errorMessage`

```norm
String? errorMessage
```

Type: `String?`

#### `requestId`

```norm
String? requestId
```

Type: `String?`

#### `output`

```norm
List<JsonValue> output
```

Type: `List<JsonValue>`

#### `calls`

```norm
List<ToolCall> calls
```

Type: `List<ToolCall>`

#### `decode`

```norm
T decode<T>()
```

Type parameters:

- `T`

Returns: `T`

### `Client`

Public API declaration Client.

```norm
class Client
```

#### `Client`

Creates an OpenAI protocol client.

```norm
Client(String apiKey, String model, String endpoint, HttpClient transport, Duration timeout, Integer maximumResponseBytes, HeaderMap headers)
```

Parameters:

- `apiKey`: `String`
The API key.

- `model`: `String`
The model name.

- `endpoint`: `String`
The endpoint URL.

- `transport`: `HttpClient`
The HTTP transport.

- `timeout`: `Duration`
The request timeout.

- `maximumResponseBytes`: `Integer`
The response byte limit.

- `headers`: `HeaderMap`
Additional HTTP headers; Authorization and Content-Type are managed by the client.


#### `Client`

Creates an OpenAI protocol client.

```norm
Client(String apiKey, String model, Array<String> headers, String endpoint, HttpClient transport, Duration timeout, Integer maximumResponseBytes)
```

Parameters:

- `apiKey`: `String`
The API key.

- `model`: `String`
The model name.

- `headers`: `Array<String>`
Additional HTTP headers; Authorization and Content-Type are managed by the client.

- `endpoint`: `String`
The endpoint URL.

- `transport`: `HttpClient`
The HTTP transport.

- `timeout`: `Duration`
The request timeout.

- `maximumResponseBytes`: `Integer`
The response byte limit.


#### `defaultModel`

```norm
String defaultModel()
```

Returns: `String`

#### `generate`

```norm
Response generate(String input, String? instructions, List<Function<?>> tools, Integer? maximumOutputTokens, Function<Void(String)>? onResponseStarted, Function<Void(String)>? onMessageStarted, Function<Void(String)>? onText, Function<Void(Message)>? onMessageCompleted, Function<Void(ToolCall)>? onToolCallReceived, Function<Void(Response)>? onResponseCompleted, Function<Void(Exception)>? onFailed, Function<Void(GenerationEvent)>? onEvent)
```

Parameters:

- `input`: `String`
- `instructions`: `String?`
- `tools`: `List<Function<?>>`
- `maximumOutputTokens`: `Integer?`
- `onResponseStarted`: `Function<Void(String)>?`
- `onMessageStarted`: `Function<Void(String)>?`
- `onText`: `Function<Void(String)>?`
- `onMessageCompleted`: `Function<Void(Message)>?`
- `onToolCallReceived`: `Function<Void(ToolCall)>?`
- `onResponseCompleted`: `Function<Void(Response)>?`
- `onFailed`: `Function<Void(Exception)>?`
- `onEvent`: `Function<Void(GenerationEvent)>?`

Returns: `Response`

#### `generate`

```norm
Response generate<T>(String input, String? instructions, Integer? maximumOutputTokens, StructuredOutputMode mode, Function<Void(String)>? onResponseStarted, Function<Void(String)>? onMessageStarted, Function<Void(String)>? onText, Function<Void(Message)>? onMessageCompleted, Function<Void(ToolCall)>? onToolCallReceived, Function<Void(Response)>? onResponseCompleted, Function<Void(Exception)>? onFailed, Function<Void(GenerationEvent)>? onEvent)
```

Type parameters:

- `T`

Parameters:

- `input`: `String`
- `instructions`: `String?`
- `maximumOutputTokens`: `Integer?`
- `mode`: `StructuredOutputMode`
- `onResponseStarted`: `Function<Void(String)>?`
- `onMessageStarted`: `Function<Void(String)>?`
- `onText`: `Function<Void(String)>?`
- `onMessageCompleted`: `Function<Void(Message)>?`
- `onToolCallReceived`: `Function<Void(ToolCall)>?`
- `onResponseCompleted`: `Function<Void(Response)>?`
- `onFailed`: `Function<Void(Exception)>?`
- `onEvent`: `Function<Void(GenerationEvent)>?`

Returns: `Response`

#### `exchange`

```norm
Response exchange(ResponseRequest request, GenerationCallbacks callbacks, Boolean stream)
```

Parameters:

- `request`: `ResponseRequest`
- `callbacks`: `GenerationCallbacks`
- `stream`: `Boolean`

Returns: `Response`

## `openai`

Source: `events.norm`

### `Message`

```norm
value Message
```

#### `id`

```norm
String id
```

Type: `String`

#### `text`

```norm
String text
```

Type: `String`

#### `refusal`

```norm
String? refusal
```

Type: `String?`

### `ToolResult`

```norm
value ToolResult
```

#### `call`

```norm
ToolCall call
```

Type: `ToolCall`

#### `output`

```norm
String output
```

Type: `String`

### `ToolFailure`

```norm
value ToolFailure
```

#### `call`

```norm
ToolCall call
```

Type: `ToolCall`

#### `error`

```norm
Exception error
```

Type: `Exception`

### `GenerationEvent`

```norm
enum GenerationEvent
```

#### `ResponseStarted`

```norm
ResponseStarted(String id)
```

Parameters:

- `id`: `String`

#### `MessageStarted`

```norm
MessageStarted(String id)
```

Parameters:

- `id`: `String`

#### `Text`

```norm
Text(String text)
```

Parameters:

- `text`: `String`

#### `MessageCompleted`

```norm
MessageCompleted(Message message)
```

Parameters:

- `message`: `Message`

#### `ToolCallReceived`

```norm
ToolCallReceived(ToolCall call)
```

Parameters:

- `call`: `ToolCall`

#### `ToolStarted`

```norm
ToolStarted(ToolCall call)
```

Parameters:

- `call`: `ToolCall`

#### `ToolCompleted`

```norm
ToolCompleted(ToolResult result)
```

Parameters:

- `result`: `ToolResult`

#### `ToolFailed`

```norm
ToolFailed(ToolFailure failure)
```

Parameters:

- `failure`: `ToolFailure`

#### `ResponseCompleted`

```norm
ResponseCompleted(Response response)
```

Parameters:

- `response`: `Response`

#### `Failed`

```norm
Failed(Exception error)
```

Parameters:

- `error`: `Exception`

#### `RunStarted`

```norm
RunStarted(String input)
```

Parameters:

- `input`: `String`

#### `RunCompleted`

```norm
RunCompleted(Response response)
```

Parameters:

- `response`: `Response`

### `GenerationCallbacks`

```norm
class GenerationCallbacks
```

#### `onResponseStarted`

```norm
Function<Void(String)>? onResponseStarted
```

Type: `Function<Void(String)>?`

#### `onMessageStarted`

```norm
Function<Void(String)>? onMessageStarted
```

Type: `Function<Void(String)>?`

#### `onText`

```norm
Function<Void(String)>? onText
```

Type: `Function<Void(String)>?`

#### `onMessageCompleted`

```norm
Function<Void(Message)>? onMessageCompleted
```

Type: `Function<Void(Message)>?`

#### `onToolCallReceived`

```norm
Function<Void(ToolCall)>? onToolCallReceived
```

Type: `Function<Void(ToolCall)>?`

#### `onToolStarted`

```norm
Function<Void(ToolCall)>? onToolStarted
```

Type: `Function<Void(ToolCall)>?`

#### `onToolCompleted`

```norm
Function<Void(ToolResult)>? onToolCompleted
```

Type: `Function<Void(ToolResult)>?`

#### `onToolFailed`

```norm
Function<Void(ToolFailure)>? onToolFailed
```

Type: `Function<Void(ToolFailure)>?`

#### `onResponseCompleted`

```norm
Function<Void(Response)>? onResponseCompleted
```

Type: `Function<Void(Response)>?`

#### `onFailed`

```norm
Function<Void(Exception)>? onFailed
```

Type: `Function<Void(Exception)>?`

#### `onRunStarted`

```norm
Function<Void(String)>? onRunStarted
```

Type: `Function<Void(String)>?`

#### `onRunCompleted`

```norm
Function<Void(Response)>? onRunCompleted
```

Type: `Function<Void(Response)>?`

#### `onEvent`

```norm
Function<Void(GenerationEvent)>? onEvent
```

Type: `Function<Void(GenerationEvent)>?`

#### `emit`

```norm
Void emit(GenerationEvent event)
```

Parameters:

- `event`: `GenerationEvent`

Returns: `Void`

## `openai`

Source: `tools.norm`

### `Tool`

Public API declaration Tool.

```norm
annotation Tool implements FunctionTarget, RuntimeRetention
```

#### `description`

The tool or parameter description.

```norm
String description
```

Type: `String`

#### `name`

The optional exposed tool name.

```norm
String? name
```

Type: `String?`

### `ToolParameter`

Public API declaration ToolParameter.

```norm
annotation ToolParameter implements ParameterTarget, RuntimeRetention
```

#### `description`

The tool or parameter description.

```norm
String description
```

Type: `String`

### `ToolCatalog`

Public API declaration ToolCatalog.

```norm
class ToolCatalog
```

#### `refresh`

Public API declaration refresh.

```norm
ToolRegistry refresh(List<Function<?>> tools)
```

Parameters:

- `tools`: `List<Function<?>>`
The tool functions.


Returns: `ToolRegistry`

#### `rejection`

Public API declaration rejection.

```norm
String? rejection()
```

Returns: `String?`

### `ToolRegistry`

Public API declaration ToolRegistry.

```norm
class ToolRegistry
```

#### `ToolRegistry`

Creates a tool registry.

```norm
ToolRegistry(List<Function<?>> tools)
```

Parameters:

- `tools`: `List<Function<?>>`
The tool functions.


#### `definitions`

Public API declaration definitions.

```norm
List<ToolDefinition> definitions()
```

Returns: `List<ToolDefinition>`

#### `invoke`

Public API declaration invoke.

```norm
String invoke(ToolCall call)
```

Parameters:

- `call`: `ToolCall`
The tool call.


Returns: `String`

