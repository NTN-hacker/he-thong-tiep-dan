from chatterbot import languages
import string
class VietnameseTager(object):
    def __init__(self):
        import underthesea
        import numpy as np

        self.language = languages.VIE

        self.punctuation_table = str.maketrans(dict.fromkeys(string.punctuation))

        self.nlp = underthesea.pos_tag

        self.tag_remove = ('CH', 'Np', 'C', 'Cc', 'M')
       
        with open('chatbot/vietnamese_stopwords.txt', 'r', encoding="utf8") as f:
            self.stopwords = np.array(f.read().split('\n'))

    def get_text_index_string(self, text):
        """
        Return a string of text containing part-of-speech, lemma pairs.
        """
        bigram_pairs = []

        if len(text) <= 2:
            text_without_punctuation = text.translate(self.punctuation_table)
            if len(text_without_punctuation) >= 1:
                text = text_without_punctuation

        document = self.nlp(text)

        for token in document:
            word = token[0].lower()
            tag = token[1]
            if word not in self.stopwords and tag not in self.tag_remove:
                bigram_pairs.append('{}:{}'.format(
                        tag,
                        word
                    ))

        if not bigram_pairs:
            for token in document:
                word = token[0].lower()
                tag = token[1]
                if tag not in self.tag_remove:
                    bigram_pairs.append('{}:{}'.format(
                            tag,
                            word
                        ))

        return ' '.join(bigram_pairs)