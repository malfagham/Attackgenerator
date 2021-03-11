class AttackRecord():
    """
    AttackRecord class is an instance of each attack.
    Information of attack and resources for performing attack are defined here.
    """
    def __init__(self, name, pre_condition, post_condition, command):
        """
        Constructor

        :param name:The name of attack.
        :param pre_condition:Precondition of attack.
        :param post_condition:Postcondition of atack.
        :param command:Path of command file for this attack.
        """
        self.name = name
        self.condition = pre_condition
        self.post_condition = post_condition
        self.command = command

    def __str__(self):
        msg = "name : " + self.name + "\n"
        msg += "command : " + self.command + "\n"
        msg += "preconditions :\n"
        msg += str(self.condition) + "\n"
        msg += "postconditions :\n"
        if len(self.post_condition) == 0:
            msg += "\tnone\n"
        else:
            for condition in self.post_condition:
                msg += "\t" + " ".join(condition) + "\n"
        return msg

    # TODO complete the methods for AttackRecord
    def is_explorable(self, state):
        """
        Checks conditions are explorable based on the current state.
        Exploration is to collect possible attack scenarios.
        'ASSUMED' keyword is used to denotes a state can be updated
        with unknown values because attack scenarios don't know
        the result of runtime.

        :param state:A given state to be checked.
        :type state: dict

        :returns: True is explorable, otherwise False.
        :rtype: bool
        """
        return self.condition.is_explorable(state)

    def mark_explored(self, state):
        """
        Update a state as if this attack is performed well.
        If a result of an attack scenario is not determined,
        "UNKNOWN" value is assigned as "UNKNOWN" value makes
        possible to connect attacks before attacks are performed actually.

        :param state:A given state to be marked.
        :type state: dict

        :returns: A marked state.
        :rtype: dict
        """
        for condition in self.post_condition:
            key, value = condition
            if condition[1] == "UNKNOWN":
                state[key] = "UNKNOWN"
            else:
                state[key] = value
        return state

    def is_satisfied(self, state):
        """
        Checks this AttackRecord can be trigerred on a given state.

        :param state: A given state
        :type state: dict

        :returns: True if an attack can be triggered, otherwise False.
        :rtype: bool
        """
        return self.condition.is_satisfied(state)
