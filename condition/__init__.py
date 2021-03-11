class Condition():
    STATES = (
        'Address',
        'Protocol',
        'Ports',
        'Shell',
        'Privilege',
        'Binaries',
        'CWD',
        'Misudo',
        )

    def __init__(self):
        """
        Condition is used to validate whether a
        state can satisfy a specific goal.
        """
        self.conditions = []

    def __str__(self):
        msg = "===========\n"
        if len(self.conditions) == 0:
            msg += "None\n"
        else:
            for condition in self.conditions:
                msg += " ".join(condition) + "\n"
        msg += "===========\n"
        return msg

    def add(self, condition):
        """
        Add conditions.

        :param condition: condition is a set which has 2 elements.
        :type condition: tuple
        The first is a key of a state.
        the second is a value for checking condition.
        """
        self.conditions.append(condition)

    def is_satisfied(self, state):
        """
        Checks if a given state satisfies a condition
        that is defined in this instance.
        Every condition should be satisfied.

        :param state: A state to be checked.
        :type state: dict

        :returns: True if a given state satisfies a condition
            otherwise False.
        :rtype: bool
        """
        state_keys = list(state.keys())

        for condition in self.conditions:
            key, value = condition
            state_value = state[key]
            if key not in state_keys:
                return False
            if key not in Condition.STATES:
                raise RuntimeError(f'Not implemented ({key})')
            else:
                if value == "EXIST":
                    if key not in state_keys:
                        return False
                if value == "NOT EXIST":
                    if key in state_keys:
                        return False
                # validating NEQ, EQ and INCLUDE
                if len(value.split(' ')) == 2:
                    operator, value = value.split(' ')
                    if operator == 'NEQ':
                        if state_value == value:
                            return False
                    elif operator == 'EQ':
                        if not state_value == value:
                            return False
                    elif operator == 'INCLUDE':
                        if value in state_value:
                            return True
                        return False
                    else:
                        raise RuntimeError(
                            f'Not implemented ({operator})')
        return True

    def is_explorable(self, state):
        """
        Checks if a given state satisfies a condition that is
        defined in this instance considering the concept of ASSUMED,
        which means that this method is used to generate plan,
        not to perform plan.

        :param state: A state to be checked.
        :type state: dict

        :returns: True if a given state satisfies a condition otherwise False.
        :rtype: bool
        """
        state_keys = list(state.keys())
        for condition in self.conditions:
            key, value = condition
            if len(value.split(' ')) == 2:
                try:
                    operator, value = value.split(' ')
                except IndexError:
                    value = None
            if value == "NOT EXIST":
                if key in state_keys:
                    return False
            if key not in state_keys or \
                    value != state[key]:
                return False
            if value is None or \
                    state[key] == 'UNKNOWN':
                continue
        return True
