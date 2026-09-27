import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        size = int(self.headers.get("Content-Length", "0"))
        request = json.loads(self.rfile.read(size))
        if self.headers.get("Authorization") != "Bearer local-fixture-key" or request.get("model") != "local-model":
            self.send_error(400)
            return
        if self.path == "/v1/responses" and request.get("input") == "Greet Norm":
            body = json.dumps({
                "id": "resp_local",
                "status": "completed",
                "output": [{"type": "message", "content": [
                    {"type": "output_text", "text": "Hello, Norm"}
                ]}],
                "usage": {"input_tokens": 3, "output_tokens": 2, "total_tokens": 5},
            }).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if self.path != "/v1/chat/completions" or request.get("stream") is not True:
            self.send_error(400)
            return
        tools = request.get("tools", [])
        if len(tools) != 1 or tools[0].get("function", {}).get("name") != "deposit":
            self.send_error(400)
            return
        messages = request.get("messages", [])
        if len(messages) == 1 and messages[0].get("content") == "Add five credits":
            deltas = [
                {"id": "r1", "choices": [{"index": 0, "delta": {"role": "assistant", "tool_calls": [
                    {"index": 0, "id": "call1", "function": {"name": "deposit", "arguments": "{\"credits\":5}"}}
                ]}, "finish_reason": None}]},
                {"id": "r1", "choices": [{"index": 0, "delta": {}, "finish_reason": "tool_calls"}]},
            ]
        elif messages and messages[-1].get("role") == "tool" and messages[-1].get("content") == "5":
            deltas = [
                {"id": "r2", "choices": [{"index": 0, "delta": {"role": "assistant", "content": "Balance: 5"}, "finish_reason": None}]},
                {"id": "r2", "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}]},
            ]
        else:
            self.send_error(400)
            return
        body = "".join(f"data: {json.dumps(delta)}\n\n" for delta in deltas) + "data: [DONE]\n\n"
        encoded = body.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)


HTTPServer(("127.0.0.1", 18766), Handler).serve_forever()
