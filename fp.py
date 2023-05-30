import numpy as np
import sys
import marker
import verb
import nltk
import matplotlib.pyplot as plt

# Threshold value for each marker (These values should be considered carefully)
THRESHOLD_IN = 0.85
THRESHOLD_VB = 0.1
THRESHOLD_JJR = 2
THRESHOLD_JJS = 2
THRESHOLD_RB = 0.85
THRESHOLD_VBD = 0.2
THRESHOLD_UH = 6
THRESHOLD_FW = 20
THRESHOLD_WILL_GOING = 10

THRESHOLD_LIST = [THRESHOLD_IN, THRESHOLD_VB, THRESHOLD_JJR, THRESHOLD_JJS, 
                THRESHOLD_RB, THRESHOLD_VBD, THRESHOLD_UH, THRESHOLD_FW, THRESHOLD_WILL_GOING]

THRESHOLD_FOR_VERLIFICATION = 8


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def find_most_likely_text(known_text_1, known_text_2, questioned_text):

    try:
        with open("gutenberg/{}".format(known_text_1), errors="ignore", encoding="utf-8") as f:
            known_text_1_string = f.read()
        with open("gutenberg/{}".format(known_text_2), errors="ignore", encoding="utf-8") as f:
            known_text_2_string = f.read()
        with open("gutenberg/{}".format(questioned_text), errors="ignore", encoding="utf-8") as f:
            questioned_text_string = f.read()

    except:
        print("Warning: The given text name are not found in the data set.")
        sys.exit()


    state = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
             "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    char2id_dict = {}
    for index, char in enumerate(state):
        char2id_dict[char] = index

    def create_transition_matrix(text):
        transition_matrix = np.zeros((27, 27))
        
        for i in range(len(text)-1):
            current_char = text[i].lower()
            next_char = text[i+1].lower()
            
            if (current_char in state) & (next_char in state):
                current_char_id = char2id_dict[current_char]
                next_char_id = char2id_dict[next_char]
                transition_matrix[current_char_id][next_char_id] = transition_matrix[current_char_id][next_char_id] + 1
                sum_of_each_row_all  = np.sum(transition_matrix, 1)
        
        for i in range (27):
            single_row_sum = sum_of_each_row_all[i]
            if (sum_of_each_row_all [i] == 0):
                single_row_sum = 1
                
            transition_matrix[ i,: ] =  transition_matrix[ i,: ] / single_row_sum

        return transition_matrix


    TM_known_text_1 = create_transition_matrix(known_text_1_string)
    TM_known_text_2 = create_transition_matrix(known_text_2_string)

    log_likelihood_known_text_1 = 0
    log_likelihood_known_text_2 = 0

    for i in range(len(questioned_text_string)-1):
        current_char = questioned_text_string[i].lower()
        next_char = questioned_text_string[i+1].lower()

        if (current_char in state) & (next_char in state):
            current_char_id = char2id_dict[current_char]
            next_char_id = char2id_dict[next_char]

            if TM_known_text_1[current_char_id][next_char_id] != 0 and TM_known_text_2[current_char_id][next_char_id] != 0:
                log_likelihood_known_text_1 += np.log(TM_known_text_1[current_char_id][next_char_id])
                log_likelihood_known_text_2 += np.log(TM_known_text_2[current_char_id][next_char_id])
    

    if log_likelihood_known_text_1 > log_likelihood_known_text_2:
        log_likelihood_larger = known_text_1
    else:
        log_likelihood_larger = known_text_2

    # Print most likely text to the command line
    print("The most likely text is {}.".format(log_likelihood_larger))
    return log_likelihood_larger


def get_ratio_difference(known_text: object, questioned_text: object):
    ratio_diff = 0
    for preposition, ratio in questioned_text.ratio_dict.items(): 
        if preposition in known_text.ratio_dict:
            ratio_diff += abs(float(ratio) - float(known_text.ratio_dict[preposition]))
        else:
            ratio_diff += float(ratio)
    length = len(questioned_text.ratio_dict)
    if length != 0:
        ave_ratio_diff = ratio_diff / length
    else:
        ave_ratio_diff = 0
    return ave_ratio_diff

'''
def ratio_plot(ratio_dict: dict, marker_name):
    x = [marker for marker, _ in ratio_dict.items()]
    x_ = x[:10]
    xi = list(range(len(x)))
    xi_ = xi[:10]
    y = [ratio for _, ratio in ratio_dict.items()]
    y_ = y[:10]
    # plot the index for the x-values
    plt.plot(xi_, y_, marker='o', linestyle='--', color='r', label='Square') 
    plt.xlabel('{}'.format(marker_name))
    plt.ylabel('Ratio') 
    plt.xticks(xi_, x_)
    plt.title('Ratio - {}'.format(marker_name))
    plt.legend() 
    plt.show()
'''

if __name__ == '__main__':

    known_text_1 = sys.argv[1]
    known_text_2 = sys.argv[2]
    questioned_text = sys.argv[3]

    most_likely_known_text = find_most_likely_text(known_text_1, known_text_2, questioned_text)

    tags = ["IN", "VB", "JJR", "JJS", "RB", "VBD", "UH", "FW"]
    ratio_diff_list = []

    marker_known_text = marker.Marker(most_likely_known_text)
    marker_questioned_text = marker.Marker(questioned_text)

    marker_known_text.read_textfile(); marker_questioned_text.read_textfile()
    marker_known_text.convert_string_to_tokens(); marker_questioned_text.convert_string_to_tokens()

    for tag in tags:
        marker_known_text.set_tag(tag); marker_questioned_text.set_tag(tag)
        marker_known_text.get_list_of_markers(); marker_questioned_text.get_list_of_markers()
        marker_known_text.count_each_marker(); marker_questioned_text.count_each_marker()
        marker_known_text.get_ratio(); marker_questioned_text.get_ratio()

        marker_ratio_diff = get_ratio_difference(marker_known_text, marker_questioned_text)
        ratio_diff_list.append(marker_ratio_diff)

        marker_known_text.clear_data(); marker_questioned_text.clear_data()

        print("The ratio difference of {} is {} %.".format(tag, str(marker_ratio_diff)))

    verb_known_text = verb.Verb(most_likely_known_text)
    verb_questioned_text = verb.Verb(questioned_text)

    verb_known_text.read_textfile(); verb_questioned_text.read_textfile()
    verb_known_text.convert_string_to_tokens(); verb_questioned_text.convert_string_to_tokens()
    verb_known_text.get_will_or_going_and_index(); verb_questioned_text.get_will_or_going_and_index()

    verb_known_text.get_ratio(); verb_questioned_text.get_ratio()

    will_going_ratio_diff = get_ratio_difference(verb_known_text, verb_questioned_text)
    ratio_diff_list.append(will_going_ratio_diff)

    print("The ratio difference of Will and Going is {} %.".format(will_going_ratio_diff))


    # Verlification process
    num_of_satisfied_condition = 0
    for i, th in enumerate(THRESHOLD_LIST):
        ratio_diff = ratio_diff_list[i]
        if th > ratio_diff:
            num_of_satisfied_condition += 1
    
    if num_of_satisfied_condition >= THRESHOLD_FOR_VERLIFICATION:
        if sys.argv[4] == "RUN":
            print("The questioned text \"{}\" is considered as written by the author of the text \"{}\".".format(questioned_text, most_likely_known_text))
        # For Test
        if sys.argv[4] == "TEST":
            print(most_likely_known_text)
            print("1")
    else:
        if sys.argv[4] == "RUN":
            print("The text \"{}\" is NOT considered as written by the author of the text \"{}\".".format(questioned_text, most_likely_known_text))
        # For Test
        if sys.argv[4] == "TEST":
            print(most_likely_known_text)
            print("2")
