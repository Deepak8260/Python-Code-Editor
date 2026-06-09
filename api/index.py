import json
import subprocess
import sys


def handler(request):
    payload = {}

    if hasattr(request, "json"):
        try:
            payload = request.json or {}
        except Exception:
            payload = {}
    elif hasattr(request, "get_json"):
        try:
            payload = request.get_json(silent=True) or {}
        except Exception:
            payload = {}
    else:
        try:
            body = request.body
            if isinstance(body, bytes):
                body = body.decode("utf-8")
            payload = json.loads(body or "{}")
        except Exception:
            payload = {}

    code = str(payload.get("code", "")).strip()
    user_input = str(payload.get("user_input", ""))

    if not code:
        return {"output": "Error: No Python code was submitted."}

    try:
        process = subprocess.Popen(
            [sys.executable, "-u", "-c", code],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        output, error = process.communicate(input=user_input, timeout=10)
        output = output.strip() or error.strip() or "Program finished with no output."
    except subprocess.TimeoutExpired:
        process.kill()
        output = "Error: Execution timed out after 10 seconds."
    except Exception as exc:
        output = f"Error: {exc}"

    return {"output": output}


app = handler
application = handler
