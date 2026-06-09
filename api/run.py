import subprocess
import sys
from vercel import Response


def handler(request):
    try:
        payload = request.get_json() or {}
    except Exception:
        payload = {}

    code = payload.get("code", "").strip()
    user_input = payload.get("user_input", "")

    if not code:
        return Response({"output": "Error: No Python code was submitted."}, status=400)

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

    return Response({"output": output})
