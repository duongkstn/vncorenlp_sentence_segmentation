from Tokenizer import Tokenizer
from WordSegmenter import WordSegmenter



if __name__ == "__main__":
    wordSegmenter = WordSegmenter()
    s = 'VTV đồng ý chia sẻ bản quyền World Cup 2018 cho HTV để khai thác. Nhưng cả hai nhà đài đều phải chờ sự đồng ý của FIFA mới thực hiện được điều này.'
    
    print('tokenize: ', wordSegmenter.tokenize(s))
    print('sentence_tokenize: ', Tokenizer.sentence_tokenize(s))

            
