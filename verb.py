import nltk


class Verb:
    def __init__(self, text):
        self.text = text
        self.filepath = "gutenberg/{}".format(self.text)
        self.string = ""
        self.tokens = []
        self.tokens_with_pos = []
        self.num_of_will_and_going = 0
        self.num_of_will = 0
        self.num_of_going = 0
        self.list_will_or_going_and_index = []
        self.ratio_dict = {}

   # Read the textfile
    def read_textfile(self):
        with open(self.filepath, "r", encoding='utf-8', errors="ignore") as f:
            string = f.read()
        self.string = string

    # Assign the POS tags for each word
    def convert_string_to_tokens(self):
        self.tokens = nltk.word_tokenize(self.string)
        self.tokens_with_pos = nltk.pos_tag(self.tokens)

    # Find "will" and "going-to" and return 
    def get_will_or_going_and_index(self):
        list_will_or_going_and_index = []
        for index, word in enumerate(self.tokens):
            word_lowercase = word.lower()
            if word_lowercase == "will":
                list_will_or_going_and_index.append(tuple(("will", index)))
            elif word_lowercase == "going" and self.tokens[index + 1].lower() == "to":
                list_will_or_going_and_index.append(tuple(("going-to", index + 1)))
        self.list_will_or_going_and_index = list_will_or_going_and_index

    # Returns a word if it is a verb
    def get_ratio(self):
        for will_or_going_and_index in self.list_will_or_going_and_index:
            index = will_or_going_and_index[1]
            if self.tokens_with_pos[index + 1][1] != "VB":
                continue

            if will_or_going_and_index[0] == "will":
                self.num_of_will += 1
            elif will_or_going_and_index[0] == "going-to":
                self.num_of_going += 1

            self.num_of_will_and_going += 1

        if self.num_of_will_and_going != 0:
            self.ratio_dict["will"] = (self.num_of_will / self.num_of_will_and_going) * 100
            self.ratio_dict["going-to"] = (self.num_of_going / self.num_of_will_and_going) * 100
        else:
            self.ratio_dict["will"] = 0
            self.ratio_dict["going-to"] = 0
