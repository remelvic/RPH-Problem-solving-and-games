import os
import utils
import re
 
 
class MyFilter:
    def __init__(self):
        self.spamWords = ['join', 'millions', 'dollars', 'mainframe', 'free', 'new', 'replay', 'spam', 'buy', 'win',
                          'go here', 'gift']
        self.classification = ''  # There SPAM or OK
 
    def train(self, train_corpus_dir):  # !truth.txt
        spam_words = {}
        ok_words = {}
        tokens = []
        tokens = utils.read_classification_from_file(train_corpus_dir + "/!truth.txt")
        for (dirpath, dirname, files) in os.walk(train_corpus_dir):
            for name in files:
                if not name[0] == '!':
                    if tokens[name] == 'SPAM':
                        f_read = open(os.path.join(train_corpus_dir + '/' + name), 'r', encoding="utf-8")
                        spam_text = f_read.read()
                        spam_data = spam_text.split()
                        spam_data = re.findall(r'[A-Za-z]{4,}', spam_text)  # Leave words at
                        # least 4 characters long
                        spam_data_words_without_copy = list(set(spam_data))
                        for word in spam_data_words_without_copy:
                            spam_words[word] = spam_words.get(word, 0) + 1
                        f_read.close()
                    if tokens[name] == 'OK':
                        f_read = open(os.path.join(train_corpus_dir + '/' + name), 'r', encoding="utf-8")
                        ok_text = f_read.read()
                        ok_data = ok_text.split()
                        for word in ok_data:
                            ok_words[word] = ok_words.get(word, 0) + 1
                        f_read.close()
 
        words = []
        for word in spam_words:
            if spam_words[word] > 150:
                words.append(word)
        for spam in words:
            for ok in ok_words:
                if spam == ok:
                    words.remove(spam)
        words.append(self.spamWords)
        self.spamWords = words
 
    def test(self, test_corpus_dir):  # !truth.txt
        # create !prediction.txt
        f = open(os.path.join(test_corpus_dir, "!prediction.txt"), 'w', encoding="utf-8")
        for (dirpath, dirname, files) in os.walk(test_corpus_dir):
            for name in files:  # for each file in directory
                f_read = open(os.path.join(test_corpus_dir + '/' + name), 'r', encoding="utf-8")
                data = f_read.read()
                if any(word in data for word in str(self.spamWords)):
                    self.classification = ' SPAM'
                else:
                    self.classification = ' OK'
                if not name[0] == '!':
                    f.write(name + self.classification + '\n')
                f_read.close()
        f.close()
