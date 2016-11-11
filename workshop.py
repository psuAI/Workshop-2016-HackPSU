############################################################
#
#
# Artificial Intelligence Association Workshop at HackPSU
#
#
# We are so happy that you are participating!
#
# If you want to hear more about our events,
# please send your name and email to ljj5099@psu.edu for all the future notifications
#
# President: Jason Tu (jasontu@psu.edu)
# VP: Rodney Wells
#
############################################################

############################################################
# Imports
############################################################

# All the imports are just suggestion for our demo, please feel free to change or check them out.
import email
import collections
import math
import os.path

############################################################
# Section 1: Spam Filter
############################################################

# resever for the unknown word, please do not change the value of unknown in your program
unknown = "<UNK>"
trainingDataSpam = "data/spam"
trainingDataHam = "data/ham"

# load all the content from a give file, the path is relative from the location of your program
# It returns a list of all the words in the file
def load_tokens(email_path):
    contents = []
    message = email.message_from_file(open(email_path, 'r'))
    for lines in email.iterators.body_line_iterator(message):
        for words in lines.split():
            contents.append(words)
    return contents

class SpamFilter(object):

    def __init__(self, smoothing):
        # all the class variables are declared right here

        # step 1: count through the file
        self.spam_counter = collections.Counter()   # number of each words in spam
        self.ham_counter = collections.Counter()    # number of each words in ham

        # step 2: calculate the possibility and the log of it
        # the possibility need to be in log form or it may cause underflow. we use the function "math.log()"
        self.spam_log = {}                          # the log of possibility for each word in spam
        self.ham_log = {}                           # the log of possibility for each word in ham
        self.total_spam = 0                         # the total number of words in spam
        self.total_ham = 0                          # the total number of words in ham

        # most calculation should go here
        spam_contents = []        # spam_contents is a list of all the file contents from spam folder
        ham_contents = []        # ham_contents is a list of all the file contents from ham folder
        spam_paths = ["%s/%s" % (trainingDataSpam, file) for file in os.listdir(trainingDataSpam)]
        ham_paths = ["%s/%s" % (trainingDataHam, file) for file in os.listdir(trainingDataHam)]
        for path in spam_paths:
            spam_contents.append(load_tokens(path))
        for path in ham_paths:
            ham_contents.append(load_tokens(path))

    # compare the possibility of spam and non-spam to get a True/False result
    def is_spam(self, email_path):
        pass

    # All the followings are optional in case that you finish it so fast
    # update the spam data, so your model can learn when it is working
    def add_spam(self, email_path):
        pass

    # update the ham data, so your model can learn when it is working
    def add_ham(self, email_path):
        pass