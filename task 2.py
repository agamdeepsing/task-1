import logging
logging.basicConfig(filename="lists.log", level=logging.DEBUG)
l = [3, 4, 5, 6, 7, [23, 456, 67, 87, 94], [345, 56, 87, 8, 98, 9], (234, 6657, 6), {"key1": "sudh, 234:[23,45,656]"}]


class list:
    def reverse(self, l):
        try:
            logging.info("the list for the given number %s", l)
            l1 = l.reverse()
            logging.info("output is %s", l1)
            return l1
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def extract(self, l):
        try:
            l2 = []
            logging.info("the list for the given number %s", l)
            for i in range(len(l)):
                if(type(l[i]) == int and l[i] == 234):
                  l2.append(i)
                elif(type(l[i]) == list or type(l[i]) == set or type(l[i]) == tuple):

                    l2.append(i)
            logging.info("output is %s",l2)
            return l2
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def extract_456(self, l):
        try:
            logging.info("the list for the given number %s", l)
            l3 = l[5][1]
            logging.info("output is %s", l3)
            return l3
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def extract_list(self,l):
        try:
            l4 = []
            for i in l:
                if type(i) == list:
                    l4.append(i)
            logging.info("the output is %s", l4)
            return l4
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def extract_sudh(self, l):
        try:
            l5 = l[8]['key1']
            logging.info("output is %s", l5)
            return l5
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def extract_keys(self, l):
        try:
            l8 = []
            for i in l:
                if type(i) == dict:
                   l8.append(i.keys())

            logging.info("output is %s", l8)
            return l8
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def extract_values(self, l):
        try:
            l7 = []
            for i in l:
                if type(i) == dict:
                    l7.append(i.values())
            logging.info("output is %s", l7)
            return l7
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
b = list()
b.reverse(l)
b.extract(l)
b.extract_456(l)
b.extract_list(l)
b.extract_sudh(l)
b.extract_keys(l)
b.extract_values(l)
