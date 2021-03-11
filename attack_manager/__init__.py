# TODO To be implemented as a real DB on the non-volatile system.
# (sqlite is suitable here).

# TODO change super class to Singleton after adding threading
# from utils.singleton import Singleton
from attack_record import AttackRecord
from condition import Condition


class AttackManager():
    """
    A manager of attack records.
    Every attack record can be accessed through this class.
    This class should be considered as CRUD operator on database.
    """

    def __init__(self, database_records):
        """
        Constructor AttackManager instance.

        :param: database_records
        """
        self.__records = []
        self.records_from_db = database_records

    def get(self):
        """
        Provides all AttackRecords.

        :return list: AttackRecord instances.
        """
        return self.__records

    def __str__(self):
        msg = "AttackDB ===========\n"
        if len(self.__records) == 0:
            msg += "None\n"
        else:
            for i in range(len(self.__records)):
                msg += "[" + str(i + 1) + "] " + str(self.__records[i]) + "\n"
        msg += "===================\n"
        return msg

    def update(self):
        """
        Storing each attack record into __records as an instance of this class.
        An attack record is stored in there as an
        instance of AttackRecord class.
        """
        for record in self.records_from_db:
            keys = list(record.keys())
            if not ("Name" in keys) or \
                    not ("Preconditions" in keys) or \
                    not ("Postconditions" in keys) or \
                    not ("Command" in keys):
                print("INVALID RECORD :\n" + str(record) + "\n")
                continue

            name = record["Name"]
            pre_conditions = Condition()
            for pre_condition in record["Preconditions"]:
                pre_conditions.add(pre_condition)
            post_conditions = record["Postconditions"]
            command = record["Command"]
            self.__records.append(
                AttackRecord(name,
                             pre_conditions,
                             post_conditions,
                             command))
