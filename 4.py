class Block:
    def __init__(self, name, m, s):
        self.name = name
        self.m = m
        self.s = s

    def

    def __lt__(self, other):
        if self.gruz == other.gruz:
            if self.dal == other.dal:
                if len(self.name) == len(other.name):
                    return self.name < other.name
                 return len(self.name) < len(other.name)
            return self.dal < other.dal
        return self.gruz < other.gruz

    def __le__(self, other):
        if self.gruz == other.gruz:
            if self.dal == other.dal:
                if len(self.name) == len(other.name):
                    return self.name <= other.name
                return len(self.name) <= len(other.name)
            return self.dal <= other.dal
        return self.gruz <= other.gruz

    def __eq__(self, other):
        if self.gruz == other.gruz:
            if self.dal == other.dal:
                if len(self.name) == len(other.name):
                    return self.name == other.name
        return False

    def __ne__(self, other):
        if self.gruz == other.gruz:
            if self.dal == other.dal:
                if len(self.name) == len(other.name):
                    return self.name != other.name
        return True

    def __ge__(self, other):
        if self.gruz == other.gruz:
            if self.dal == other.dal:
                if len(self.name) == len(other.name):
                    return self.name >= other.name
                return len(self.name) >= len(other.name)
            return self.dal >= other.dal
        return self.gruz >= other.gruz

    def __gt__(self, other):
        if self.gruz == other.gruz:
            if self.dal == other.dal:
                if len(self.name) == len(other.name):
                    return self.name > other.name
                return len(self.name) > len(other.name)
            return self.dal > other.dal
        return self.gruz > other.gruz