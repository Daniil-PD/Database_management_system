import sqlite3

class DataManager():

    class Buyers():
        def __init__(self, id = None, email = None, address = None, name = None, phones = None, from_tuple = None):
            """Класс покупателя, может создоваться сразу из кортеджа, телефоны задаются отдельно"""
            if from_tuple == None:
                self.id = id
                self.email = email
                self.address = address
                self.name = name
                self.phones = list() if phones is None else phones
            else:
                self.id,  self.email, self.address, self.name = from_tuple[0:4]
                self.phones = list(from_tuple[4:])



    def __init__(self):
        self.conn = sqlite3.connect(r'SQLocal.db')


    def get_buyers(self, filter = None):

        cursor = self.conn.cursor()
        phones_list = list()
        if filter is None:
            cursor.execute("SELECT * FROM buyers;")
            phones_list = self.get_buyers_phone_numbers()
        else:
            if filter[0] == "phone":
                phones_list = self.get_buyers_phone_numbers(("phone_numbers",filter[1]))
            else:
                cursor.execute(f"SELECT * FROM buyers WHERE buyers.{filter[0]} LIKE '%{filter[1]}%' ")
                phones_list = self.get_buyers_phone_numbers()
        all_results = cursor.fetchall()
        buyers_list = list()

        for element in all_results:
            buyer = DataManager.Buyers(from_tuple=element)
            n = len(phones_list) - 1
            while n >= 0:
                if phones_list[n][0] == element[0]:
                    buyer.phones.append(phones_list[n][1])
                    del phones_list[n]
                n -= 1

            buyers_list.append(buyer)





        return buyers_list


    def get_buyers_phone_numbers(self, filter = None):
        cursor = self.conn.cursor()
        if filter is None:
            cursor.execute("SELECT * FROM buyers_phone_numbers")
        else:
            cursor.execute(f"SELECT * FROM buyers_phone_numbers WHERE buyers_phone_numbers.{filter[0]} LIKE '%{filter[1]}%'")
        all_results = cursor.fetchall()
        return all_results
