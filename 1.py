import logging
logging.basicConfig(filename="string.log", level=logging.DEBUG)
s = "this is my first programming class and iam learning string"


class String:

    def extract(self, s):
        try:
            logging.info("the string for this code is ", s)
            s1 = s[1:300:3]
            logging.info("output is:", s1)
            return s1
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def reverse_st(self, s):
        try:
            s2 = s[::-1]
            logging.info("output is:", s2)
            return s2
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def lower_strin(self, s):
        try:
            s3 = s.lower()
            logging.info("output is", s3)
            return s3
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def capitalize_stri(self, s):
        try:
            s4 = s.capitalize()
            logging.info("output is:", s4)
            return s4
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def expand(self, s):
        try:
            logging.info("The given string for this operation is %s", s)
            s5 = s.expandtabs()
            logging.info("The output is", s5)
            return s5
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def strip_str(self, s):
        try:
            s6 = s.strip()
            logging.info("output is :", s6)
            return s6
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def lstrip_str(self, s):
        try:
            s7 = s.lstrip()
            logging.info("output is :", s7)
            return s7
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def rstrip_str(self, s):
        try:
            s8 = s.rstrip()
            logging.info("output is :", s8)
            return s8
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def replace_string(self, s):
        try:
            s9 = s.replace()
            logging.info("output is :", s9)
            return s9
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def center(self, s):
        try:
            s10 = s.center(20, '*')
            logging.info("output is :", s10)
            return s10
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
