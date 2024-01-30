<h1 align="center">Gpt-Client</h1>

## Author
👤 Anybodyy

* Github: [@Anybodyy](https://github.com/anybodyy)
* Telegram: [@User_With_Username](t.me/User_With_Username)

Thanks to the [@xtekky](https://github.com/xtekky). I was inspired by his project(gpt free)

## Description
This is a powerful script to communicate with big text AI models like gpt4 or OpenChat for free

## Installing
You can load this lib using pip:
```sh
pip install Gpt-Client
```

## Docs
To communicate with AI, you can use this code:
```python
from Gpt_Client import Completion

async for response_chunk in Completion.create(messages=[{"role": "system", "message": "hello world!"):
    print(response_chunk, flush=True, end='')
```

## License
This project is licensed under the [MIT License](LICENSE).
