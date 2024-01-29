![Logi](https://raw.githubusercontent.com/mr-sami-x/sami_ai/main/logo.png)

# SAMI AI V0.5

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/release)
[![GitHub issues](https://img.shields.io/github/issues/mr-sami-x/sami_ai)](https://github.com/mr-sami-x/sami_ai/issues)
[![GitHub stars](https://img.shields.io/github/stars/mr-sami-x/sami_ai)](https://github.com/mr-sami-x/sami_ai/stargazers)

## Overview

sami_ai is an advanced artificial intelligence library designed to assist with the development of sophisticated and efficient software solutions.

## Features

- Powerful AI capabilities
- Fast and efficient algorithms
- Easy-to-use interface
- The reply settings feature has become available
## Installation

You can install sami-ai using pip:

```
pip install sami-ai
```

## Example:
```
from sami_ai import sami_ai


user_input = input("Enter Your Msg: ")
key_openai = input("Enter Your key OpenAi: ")
setting = input("Enter Your setting response: ")
result = sami_ai(user_input,key_openai,setting)
print(result["response"])

```
