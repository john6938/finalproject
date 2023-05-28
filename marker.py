import nltk


class Marker:
    # Initialize
    def __init__(self, text, tag=""):
        self.text = text
        self.filepath = "gutenberg/{}".format(self.text)
        self.string = ""
        self.tokens = []
        self.list_of_markers = []
        self.dict_of_markers = {}
        self.num_of_marker = 0
        self.ratio_dict = {}
        self.tag = tag

    def clear_data(self):
        self.list_of_markers = []
        self.dict_of_markers = {}
        self.num_of_marker = 0
        self.ratio_dict = {}

    # Set POS tag
    def set_tag(self, tag):
        self.tag = tag

    # Read the textfile
    def read_textfile(self):
        with open(self.filepath, "r", encoding='utf-8', errors="ignore") as f:
            string = f.read()
        self.string = string
        self.length = len(self.string)

    # Assign the POS tags for each word
    def convert_string_to_tokens(self):
        tokens = nltk.word_tokenize(self.string)
        self.tokens = nltk.pos_tag(tokens)

    # Find the prepositions using POS tag
    def get_list_of_markers(self):
        list_of_markers = []
        for word, tag in self.tokens:
            if tag == self.tag:
                list_of_markers.append(word)
                self.num_of_marker += 1
        self.list_of_markers = list_of_markers

    # Count the number of each preposition
    def count_each_marker(self):
        dict_of_markers = {}
        for preposition in self.list_of_markers:
            if preposition in dict_of_markers:
                dict_of_markers[preposition] += 1
            else:
                dict_of_markers[preposition] = 1
        self.dict_of_markers = dict_of_markers

    # Get the ratio of each preposition
    def get_ratio(self):
        sorted_dict = sorted(self.dict_of_markers.items(), key=lambda x:x[1], reverse=True)
        ratio_dict = {}
        for preposition, count in sorted_dict:
            ratio = (count / self.num_of_marker) * 100
            ratio_dict[preposition] = round(ratio, 5)
        self.ratio_dict = ratio_dict
