import runpy
import sys

sys.argv = ["langchain_azure_ai.agents.hosting.run", "--protocol", "responses"]
runpy.run_module("langchain_azure_ai.agents.hosting.run", run_name="__main__", alter_sys=True)