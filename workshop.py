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
# Spam Filter
############################################################

# Reserved for the unknown word, please do not change the value of unknown in your program
unknown = "<UNK>"
trainingDataSpam = "data/spam"
trainingDataHam = "data/ham"
smoothing = 1e-5


def load_tokens(email_path):
    """DO NOT EDIT THIS FUNCTION! Returns a list of all words in a file."""
    contents = []
    message = email.message_from_file(open(email_path, 'r'))
    for lines in email.iterators.body_line_iterator(message):
        for words in lines.split():
            contents.append(words)
    return contents


def get_contents(mail_path):
    """DO NOT EDIT THIS FUNCTION! Returns all words all files in the path."""
    paths = ["%s/%s" % (mail_path, file) for file in os.listdir(mail_path)]
    contents = []
    for path in paths:
        contents.append(load_tokens(path))

    return contents


def log_possibility(value, total, counter):
    """DO NOT EDIT THIS FUNCTION! Calculation of the log of possibility.
        Put zero for value if it is unknown."""
    return math.log(float(value + smoothing) / (total + smoothing * (len(counter) + 1)))


class SpamFilter(object):

    def __init__(self):
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
        spam_contents = get_contents(trainingDataSpam)  # List of all the file contents from spam folder
        ham_contents = get_contents(trainingDataHam)  # List of all the file contents from ham folder

#################################################################################################
#
# This is where you start to add codes
#
#       Three thing need to be done:
#           1. count through the contents, put the amount of each word in the counter
#           2. use the function log_possibility to calculate the log for each words
#           3. complete the is_spam() function by sum up all the log for spam and ham and then
#              get the result by comparing them
#
#
#################################################################################################
        
        # There are some examples of how to use log_possibility function, uncomment and change 'A word' to try it out
        # self.spam_log['A word'] = log_possibility(self.spam_counter['A word'], self.total_spam, self.spam_counter)
        
    # Compare the possibility of spam and non-spam to get a True/False result
    def is_spam(self, email_path):
        pass

    # All the following are optional, in case that you finish it so fast!
    # ==================================================================

    # Update the spam data, so your model can learn when it is working
    def add_spam(self, email_path):
        pass

    # Update the ham data, so your model can learn when it is working
    def add_ham(self, email_path):
        pass
        

#################################################################################################
#
# This is the test case (if you are using a python shell to test, you may want to comment it out)
#    
#################################################################################################

check_email = "test/dev190"
myfilter = SpamFilter()
print myfilter.is_spam(check_email)


