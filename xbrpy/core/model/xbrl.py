class Context:
    def __init__(self, id, entity, period, scenario):
        pass


class ContextEntity:
    def __init__(self, identifier, segment=None):
        pass


class ContextEntitySegment:
    def __init__(self):
        pass


class ContextPeriod:
    def __init__(self):
        pass


class ContextScenario:
    def __init__(self):
        pass


class Unit:
    def __init__(self, id):
        pass


class Fact:
    def __init__(self, idx, context_ref, tag, value, unit_ref=None, precision=None):
        """

        Args:
            idx: (string) ID of the Fact element
            context_ref: (string) ID of the context ref attribute
            tag: (string) tag of the Fact element
            value: (string) text value of the Fact element
            unit_ref: (string) ID of the unit ref attribute
            precision: (string) value representing precision or decimals of the significance/accuracy of the element

        Returns: Nothing

        """
        self.idx = idx
        self.context_ref = context_ref
        self.tag = tag
        self.value = value
        self.unit_ref = unit_ref
        self.precision = precision  # Can be called either "decimals" or "precision"

    def get_context(self):
        pass

    def get_unit(self):
        pass


class Footnote:
    def __init__(self):
        pass
