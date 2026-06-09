import json
import subprocess
import sys
from vercel import Response


def handler(request):
    payload = {}

    if hasattr(request, "get_json"):
        try:
            payload = request.get_json(silent=True) or {}
        except Exception:
            payload = {}
    elif hasattr(request, "json"):
        try:
            payload = request.json or {}
        except Exception:
            payload = {}
    else:
        try:
            payload = json.loads(request.body or b"{}")
        except Exception:
            payload = {}

    code = str(payload.get("code", "")).strip()
    user_input = str(payload.get("user_input", ""))

    if not code:
        return Response(json.dumps({"output": "Error: No Python code was submitted."}), status=400, headers={"Content-Type": "application/json"})

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

    return Response(json.dumps({"output": output}), headers={"Content-Type": "application/json"})


app = handler
application = handler
