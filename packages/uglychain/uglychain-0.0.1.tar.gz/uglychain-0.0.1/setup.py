# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['uglychain',
 'uglychain.chains',
 'uglychain.chains.llm',
 'uglychain.examples',
 'uglychain.llm',
 'uglychain.provider',
 'uglychain.retrievers',
 'uglychain.utils']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.7.2,<0.8.0',
 'openai>=1.10.0,<2.0.0',
 'pathos>=0.3.1,<0.4.0',
 'pydantic>=2.5.3,<3.0.0',
 'requests>=2.31.0,<3.0.0',
 'tenacity>=8.2.3,<9.0.0']

setup_kwargs = {
    'name': 'uglychain',
    'version': '0.0.1',
    'description': 'UglyChain：更好用的 LLM 应用构建工具',
    'long_description': '# UglyChain\n⚡ UglyChain：更好用的 LLM 应用构建工具 ⚡\n\n## Features\n- 📦 对大模型接口进行封装，提供对工程化更加直观易懂的交互方式，而不是传统的对话式交互。\n  - 可以参数化 Prompt，更加方便地进行批量调用\n  - 可以对 Prompt 进行结构化返回，方便后续处理\n  - 可以对 Prompt 进行角色设置，方便模型进行角色扮演（这个过程无需操控 Message）\n- 🔗 对大模型的高级调用进行封装，提供更加方便的交互方式\n  - 提供了类似于 MapReduce 的功能，可以通过 MapChain 对多个 Prompt 进行并行调用，也可以用 ReduceChain 对多个 Prompt 进行串行调用\n  - 大模型最优质的能力之一就是拥有 ReAct 能力。我们提供了 ReActChain 便捷的实现这种能力。\n- 💾 提供了搜索引擎的封装，可以方便地进行搜索引擎的调用。\n  - 注意我们只封装了搜索过程的调用，而没有提供搜索引擎的搭建。如果要构建基于 RAG 的应用，需要利用其他的工具完成资料库的建立，而我们只提供对资料库搜索功能的封装。\n\n## Setup\n\n\n## Example usage\n### LLM\n\n> 这是最基础的模型调用类，其他的高级类也都继承和使用了这个类的基本功能。\n\n快速使用：\n\n```python\nfrom uglychain import LLM, Model\nllm = LLM()\nprint(llm("你是谁？")) # 与模型对话，返回字符串的回答\n```\n\n调整基础配置选项：\n\n```python\nllm = LLM(model = Model.YI) # 可以选择更多的模型，如 Model.GPT3_TURBO、Model.GPT4 等等\nllm = LLM(system_prompt = "我想让你担任职业顾问。我将为您提供一个在职业生涯中寻求指导的人，您的任务是帮助他们根据自己的技能、兴趣和经验确定最适合的职业。您还应该对可用的各种选项进行研究，解释不同行业的就业市场趋势，并就哪些资格对追求特定领域有益提出建议。") # 可以对模型设置角色，这样模型就会以这个角色的视角来回答问题。设置的内容保存在 System Message 中。\n```\n\n参数化 prompt：\n\n```python\nllm = LLM(prompt_template = "{object}的{position}是谁？")\nprint(llm(object = "《红楼梦》", position = "作者"))\nprint(llm(object = "上海市", position = "市长"))\n```\n\n对于 prompt 中只有一个参数的情况，可以直接传入参数：\n\n```python\nllm = LLM("介绍一下{object}")\nprint(llm("Transformer"))\n```\n\n结构化返回结果：\n\n```python\nclass UserDetail(BaseModel):\n    name: str\n    age: int\n\nllm = LLM(response_model=UserDetail)\nprint(llm("Extract Jason is 25 years old")) # UserDetail(name=\'Jason\', age=25)\n```\n\n### MapChain\n\n> 这是一个可以并行对同类型 Prompt 进行调用的类，可以大大提高调用效率。\n\n快速使用：\n\n```python\nllm = MapChain()\nprint(llm([\n        {"input": "How old are you?"},\n        {"input": "What is the meaning of life?"},\n        {"input": "What is the hottest day of the year?"},\n    ]))\n``````\n类似于 LLM，也可以对 MapChain 进行更高阶的使用：\n\n```python\nclass AUTHOR(BaseModel):\n    name: str = Field(..., description="姓名")\n    introduction: str = Field(..., description="简介")\n\nllm = MapChain(prompt_template="{book}的{position}是谁？", response_model=AUTHOR, map_keys=["book",])\ninput = [\n    "《红楼梦》",\n    "《西游记》",\n    "《三国演义》",\n    "《水浒传》",\n]\nprint(llm(book=input, position="作者"))',
    'author': 'uglyboy',
    'author_email': 'uglyboy@uglyboy.cn',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
