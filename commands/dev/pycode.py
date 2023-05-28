import io
import sys
import traceback


def pycode(code):
    try:
    
        code = code.replace("```py&```python&```","")
        code = code.replace("^\s","")
        print(type(code))
        exec(str(
            str(code)
            +
            "\nglobal result = str(io.StringIO())\nsys.stdout = result\noutput = str(result.getvalue())\nprint(str(output)"
        ))
        return result
    except(Exception):
        return "An error occured:\n" + "\`" + str(sys.exc_info() + "\`")

pycode("print('e')")