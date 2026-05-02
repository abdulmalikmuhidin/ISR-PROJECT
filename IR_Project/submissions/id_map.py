class IdMap:
    def __init__(self):
        self.str_to_id = {}
        self.id_to_str = []

    def __len__(self):
        return len(self.id_to_str)

    def _get_str(self, i):
        return self.id_to_str[i]

    def _get_id(self, s):
        if s not in self.str_to_id:
            new_id = len(self.id_to_str)
            self.str_to_id[s] = new_id
            self.id_to_str.append(s)
        return self.str_to_id[s]

    def __getitem__(self, key):
        if type(key) is int:
            return self._get_str(key)
        elif type(key) is str:
            return self._get_id(key)
        else:
            raise TypeError