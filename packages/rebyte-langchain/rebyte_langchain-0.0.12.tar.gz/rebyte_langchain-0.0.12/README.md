# rebyte-langchain

[![Static Badge](https://img.shields.io/badge/discord-Join_Chat-blue?&color=blue)](https://rebyte.ai/join-discord)
[![PyPI](https://img.shields.io/pypi/v/rebyte-langchain.svg)](https://pypi.python.org/pypi/rebyte-langchain)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/rebyte-langchain)](https://pypi.python.org/pypi/rebyte-langchain)
[![GitHub issues](https://img.shields.io/github/issues/ReByteAI/bug-tracker)](https://rebyte.ai/feedback)
[![readthedocs](https://img.shields.io/badge/docs-stable-brightgreen.svg?style=flat)](https://rebyte-ai.gitbook.io/rebyte/)
[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)


rebyte-langchain is a Python library to access the ReByte Agent REST API. This library enables you to use rebyte in a langchain-like style.

## Features

1. Generate streaming or non-streaming output.
2. Use async or sync method.
3. Compatiable with langchain callback functions.
4. Support stateful agent memory with session_id.

## Install
```shell
pip install rebyte-langchain
```

## Prerequisites

### ReByte API Key
To get your ReByte API key, follow these steps:

1. Go to the [ReByte website](https://rebyte.ai/) and sign up for an account if you haven't already.
2. Once you're logged in, go to Settings > API Keys.
3. Generate a new API key by clicking on the "Generate" button.
4. Prepare to use it during configuration.

### ReByte Agent Creation

1. You can follow the tutorial in the webpage [ReByte Quick Start](https://rebyte-ai.gitbook.io/rbyte/agents/quick-start) to create your own agent. Or you can use agents in ReByte Community. Open an agent and clone to your personal project.

2. Deploy the agent and get the project_id and agent_id in the following format: https://rebyte.ai/api/sdk/p/{project_id}/a/{agent_id}/r.

## Simple Demo

```python
# import packages
from rebyte_langchain.rebyte_langchain import RebyteEndpoint
import os
import asyncio
from langchain.schema.messages import HumanMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# required keys & config
# You can set REBYTE_API_KEY as an environment variable 
os.environ['REBYTE_API_KEY'] = "<rebyte_api_key>"
# Or pass it as an argument to the RebyteEndpoint constructor
test_rebyte_api_key:str = "<rebyte_api_key>"

# create an agent on rebyte platform and get the project_id and agent_id
# https://rebyte.ai/api/sdk/p/{test_project_id}/a/{test_agent_id}/r
# An example agent for Mark Zuckerberg: https://rebyte.ai/p/d4e521a67bb8189c2189/callable/a38ec8c60c3925696385/editor
test_project_id:str = "d4e521a67bb8189c2189"
test_agent_id:str = "a38ec8c60c3925696385"

# You may use any string as session_id and try to avoid duplicate session_ids
# Note that you must set session_id if you want to enable stateful actions, such as threads (aka, memory), in your agent.
# Or you can leave it as None when the agent has no stateful actions.
test_session_id:str = None

# test input
human_messages = [HumanMessage(content="Who are you")]

def generate(stream = False):
  model = RebyteEndpoint(
    rebyte_api_key=test_rebyte_api_key,
    project_id=test_project_id,
    agent_id=test_agent_id,
    session_id=test_session_id,
    streaming=stream
  )
  response = model.generate([human_messages],
                            callbacks=[StreamingStdOutCallbackHandler()]
                            )
  return response

async def agenerate(stream = False):
  model = RebyteEndpoint(
    rebyte_api_key=test_rebyte_api_key,
    project_id=test_project_id,
    agent_id=test_agent_id,
    session_id=test_session_id,
    streaming=stream
  )
  response = await model.agenerate(messages=
                                   [human_messages],
                                   callbacks=[StreamingStdOutCallbackHandler()]
                                   )
  return response

if __name__ == "__main__":
  print("\n\nTEST GENERATE\n\n")
  response = generate(stream=True)

  print("\n\nTEST AGENERATE\n\n")
  loop = asyncio.get_event_loop()
  loop.run_until_complete(agenerate(stream=True))
```

Please see more examples in main.py and example.ipynb.

## Documentation

More information can be found on the [ReByte Documentation Site](https://rebyte-ai.gitbook.io/rebyte/).
