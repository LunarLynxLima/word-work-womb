import re, collections
from tqdm import tqdm


class VocabularyGenerator:
    def __init__(self, file_path, iterations):
        self.file_path = file_path
        self.iterations = iterations
        self.corpus = self.read_file()
        self.vocabulary = None
        self.merge_rules = None


    def read_file(self):
        with open(self.file_path, 'r') as file:
            return file.read()
        

    '''
    returns a list of words is the corpus with a $ at the end of 
    each word and in each word characters are separated by a -
    '''
    def get_words(self):
        words = re.findall('[a-z]+', self.corpus.lower())
        words = [word + '$' for word in words]
        words = [list(word) for word in words]
        words = ['-'.join(x) for x in words]
        return words

    '''
    return a dictionary with the count of each pair of characters in the words
    '''
    def count_pairs(self, words):
        pair_counts = {}
        for word in words:
            temp = re.split('-', word)
            for i in range(len(temp)-1):
                pair = temp[i]+','+temp[i+1]
                if pair not in pair_counts:
                    pair_counts[pair] = 1
                else:
                    pair_counts[pair] += 1

        return pair_counts

    '''
    return the pair with the highest count
    '''
    def get_max_pair(self, pair_counts):
        return collections.Counter(pair_counts).most_common(1)[0][0]

    '''
    combine the pair of characters in the words with the highest count
    '''
    def combine_letters(self, pair, words):
        temp_pair = '-'.join(list(pair))
        for i,word in enumerate(words):
            words[i] = re.sub(temp_pair, pair, word)
        
        return words

            
    '''
    learn the vocabulary from the corpus and return the vocabulary, and merge rules
    '''
    def learn_vocabulary(self):
        print("--------------------------------------------------------")
        print("                Learning Vocabulary")
        print("--------------------------------------------------------")
        vocabulary = ['$']

        for letter in 'abcdefghijklmnopqrstuvwxyz':
            vocabulary.append(letter)

        merge_rules = []
        words = self.get_words()
        pairs = None

        for _ in tqdm(range(self.iterations)):
            pairs = self.count_pairs(words)
            # print(pairs)
            max_pair = self.get_max_pair(pairs)
            pair = "".join(max_pair.split(','))
            while pair in vocabulary:
                if len(pairs) == 0:
                    break
                pairs.pop(max_pair)
                max_pair = self.get_max_pair(pairs)
                pair = "".join(max_pair.split(','))
            
            merge_rules.append(max_pair)
            vocabulary.append(pair)

            words = self.combine_letters(pair, words)

        print("--------------------------------------------------------")
        print("                Vocabulary Learned")
        print("--------------------------------------------------------")

        return vocabulary, merge_rules
    

class Tokenizer:
    def __init__(self, merge_rules):
        self.merge_rules = merge_rules

    def break_word(self, word):
        # tokens = []
        # print(word)
        # print(list(word))
        word = ",".join(list(word))
        # print(word)
        for rule in self.merge_rules:
            merged_rule = "".join(rule.split(','))
            word = word.replace(rule, merged_rule)
        tokens = word.split(',')
        return tokens

    def tokenize(self, scentence):
        words = re.findall('[a-z]+', scentence.lower())
        words = [word + '$' for word in words]

        tokens = []
        for i,word in enumerate(words):
            
            tokens.extend(self.break_word(word))


        return tokens
    

if __name__ == "__main__":
    file_path = 'corpus.txt'
    iterations = 1000
    vg = VocabularyGenerator(file_path, iterations)
    vocabulary, merge_rules = vg.learn_vocabulary()
    # print(merge_rules)

    with open('merge_rules.txt', 'w') as file:
        for rule in merge_rules:
            file.write(rule + '\n')

    with open('tokens.txt', 'w') as file:
        for word in vocabulary:
            file.write(word + '\n')

    tokenizer = Tokenizer(merge_rules)
    
    with open('test.txt', 'r') as in_file:

        text = in_file.read()
        text = text.split('\n')
        out_file = open('output.txt', 'w')

        for line in text:
            tokens = tokenizer.tokenize(line)
            out_file.write(','.join(tokens) + '\n')

        out_file.close()
