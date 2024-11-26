# GLORY BE TO GOD,
# TESTING FILE
# BY ISRAEL MAFABI EMMANUEL

from functions import greet_programmer, greet, greet_with_default, add, halve

import io
import sys
# import re

# class TestAppPy:
#     app_path:str = "lib/app.py"
#     def test_app_py_exists(self):
#         # app.py exists in the lib directory
#         assert(path.exists(self.app_path))
    
#     def test_app_py_run(self):
#         # app.py runs efficiently and as should
#         runpy.run_path(self.app_path)

#     def test_app_py_prints_message(self):
#         output:str = io.StringIO()
#         sys.stdout = output
#         runpy.run_path(self.app_path)
#         sys.stdout = sys.__stdout__

#         # let's match the output
#         # assert(output.getvalue() == "Hello World!, greetings from Emmanuel!!!\n")
#         assert re.match(r"Hello World!, greetings from .+!!!\n", output.getvalue())

class TestGreetProgrammer:
    # for the greet_programmer function
    def test_greet_programmer(self):
        # prints the message: hello, programmer!
        output:str = io.StringIO()
        sys.stdout = output
        greet_programmer()
        sys.stdout = sys.__stdout__
        assert(output.getvalue() == "Hello, Programmer!\n")

class TestGreet:
    # for the greet() function
    def test_greet_programmer(self):
        output = io.StringIO()
        sys.stdout = output
        greet("Emmanuel")
        sys.stdout = sys.__stdout__
        assert(output.getvalue() == "Hello, Emmanuel!\n")

class TestGreetWithDefault:
    # for the function greet_with_default
    def test_greet_with_default(self):
        output = io.StringIO()
        sys.stdout = output
        greet_with_default()
        sys.stdout = sys.__stdout__
        assert(output.getvalue() == "Hello, Emmanuel!\n")

    def test_greet_with_default_with_param(self):
        output = io.StringIO()
        sys.stdout = output
        greet_with_default("Wendy")
        sys.stdout = sys.__stdout__
        assert(output.getvalue() == "Hello, Wendy!\n")


class TestAdd:
    # for the add() function
    def test_add(self):
        assert(add(45, 55) == 100)

class TestHalve:
    # for the halve() function
    def test_halve_int(self):
        assert(halve(100) == 50)

    def test_halve_float(self):
        assert(halve(99.0) == 49.5)