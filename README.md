# VnCoreNLP for sentence/word segmentation (Python Version, not java)


Python code for sentence/word segmentation using [VnCoreNLP](https://github.com/vncorenlp/VnCoreNLP)  and Python

## Table Of Contents
  * [Why using this code?](#why-using-this-code)
  * [Installation](#installation)
  * [Example Usage](#example-usage)
  * [License](#license)


## Why using this code ?
Some Engineers want to use a sentence/word segmentation tool from VnCoreNLP without loading whole Java model in VnCoreNLP's official repo and do not want to look at Java code.


## Installation


```
$ pip install regex
```


## Example Usage

A simple example of how to use this tool:

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tokenizer import Tokenizer
from WordSegmenter import WordSegmenter

wordSegmenter = WordSegmenter()
s = 'VTV đồng ý chia sẻ bản quyền World Cup 2018 cho HTV để khai thác. Nhưng cả hai nhà đài đều phải chờ sự đồng ý của FIFA mới thực hiện được điều này.'
    
print('tokenize: ', wordSegmenter.tokenize(s))
print('sentence_tokenize: ', Tokenizer.sentence_tokenize(s))

```

And here is the output:

```
tokenize:  [['VTV', 'đồng_ý', 'chia_sẻ', 'bản_quyền', 'World_Cup', '2018', 'cho', 'HTV', 'để', 'khai_thác', '.'], ['Nhưng', 'cả', 'hai', 'nhà', 'đài', 'đều', 'phải', 'chờ', 'sự', 'đồng_ý', 'của', 'FIFA', 'mới', 'thực_hiện', 'được', 'điều', 'này', '.']]
sentence_tokenize:  ['VTV đồng ý chia sẻ bản quyền World Cup 2018 cho HTV để khai thác .', 'Nhưng cả hai nhà đài đều phải chờ sự đồng ý của FIFA mới thực hiện được điều này .']
```


##DISCLAIMER

The speed performance of this code is much slower than the official Java code. The purpose of creating this repos is understanding VnCoreNLP by converting it to python programming language. Besides, many Vietnamese NLP tasks just require a sentence and word tokenizer solution, so I decide not to rewrite the NER, Pos Tagging parts of the original codebase.

## License

MIT
