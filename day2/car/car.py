class Car(object):
    def __init__(self, name='General', model='GM', kind='saloon'):
        self.name = name
        self.model = model
        self.kind = kind
        self.num_of_doors = self._get_num_of_doors()
        self.num_of_wheels = self._get_num_of_wheels()
        self.speed = 0

    def is_saloon(self):
        return True if self.kind == 'saloon' else False

    def drive(self, acceleration):
        if self.kind == 'trailer':
            self.speed = 77
        else:
            self.speed = 1000
        return self

    def _get_num_of_doors(self):
        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            return 2
        return 4

    def _get_num_of_wheels(self):
        if self.kind == 'trailer':
            return 8
        return 4
