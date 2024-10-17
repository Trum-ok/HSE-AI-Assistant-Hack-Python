import io
import sys

from typing import Optional

def exec_code(code: str, inputs: str) -> Optional[str]:
    original_stdin = sys.stdin
    original_stdout = sys.stdout

    if "; " in inputs:
        sys.stdin = io.StringIO(inputs.replace("; ", "\n"))
    else:
        sys.stdin = io.StringIO(inputs)

    output_buffer = io.StringIO()
    sys.stdout = output_buffer

    local_scope = {}

    try:
        exec(code, {}, local_scope)

        if 'output' in local_scope:
            return_value = local_scope['output']
        elif 'result' in local_scope:
            return_value = local_scope['result']
        else:
            return_value = output_buffer.getvalue().strip()

        return return_value or ''

    except Exception as e:
        return f"Ошибка: {str(e)}"

    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout
