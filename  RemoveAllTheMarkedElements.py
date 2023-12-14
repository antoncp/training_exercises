class List:
    def remove_(self, integer_list, values_list):
        for i in values_list:
            while i in integer_list:
                integer_list.remove(i)
        return integer_list
