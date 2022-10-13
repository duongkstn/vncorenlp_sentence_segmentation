# VnCoreNLP for sentence segmentation (Python Version, not java)


Python code for sentence segmentation using [VnCoreNLP](https://github.com/vncorenlp/VnCoreNLP)  and Python

## Table Of Contents
  * [Why using this code?](#why-using-this-code)
  * [Installation](#installation)
  * [Example Usage](#example-usage)
  * [License](#license)


## Why using this code ?
Some Engineers want to use a sentence segmentation tool from VnCoreNLP without loading whole Java model in VnCoreNLP's official repo and do not want to look at Java code.


## Installation


```
$ pip install regex
```


## Example Usage

A simple example of how to use this tool:

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
from tokenizer import Tokenizer
s = "Ông Nguyễn Khắc Chúc  đang làm việc tại Đại học Quốc gia Hà Nội. Bà Lan, vợ ông Chúc, cũng làm việc tại đây."
print(Tokenizer.joinSentences(Tokenizer.tokenize(s)))
```

And here is the output:

```
['Ông   Nguyễn   Khắc   Chúc   đang   làm   việc   tại   Đại   học   Quốc   gia   Hà   Nội   .', 'Bà   Lan   ,   vợ   ông   Chúc   ,   cũng   làm   việc   tại   đây   .']
```

## License

MIT