class BinarySearch:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.created_list = self._generate_list()
        self.length = len(self.created_list)

    def _generate_list(self):
        result = []
        value = self.b
        while len(result) < self.a:
            result.append(value)
            value += self.b
        return result

    def search(self, search_item):
        target_list = self._get_target_list(search_item)
        return self._binary_search(search_item, target_list, 0)

    def _get_target_list(self, search_item):
        # Split the created_list into 5 portions and return the one that has the item
        percentiles = 5
        percentile_step = len(self.created_list) / percentiles
        percentile_limit_1, percentile_limit_2 = percentile_step, percentile_step * 2
        percentile_limit_3, percentile_limit_4 = percentile_step * 3, percentile_step * 4

        last_element = self.created_list[len(self.created_list) - 1]
        item_percentile = float(search_item) / float(last_element) * percentiles
        if item_percentile <= 1:
            return self.created_list[:percentile_limit_1]
        if 1 < item_percentile <= 2:
            return self.created_list[percentile_limit_1:percentile_limit_2]
        if 2 < item_percentile <= 3:
            return self.created_list[percentile_limit_2:percentile_limit_3]
        if 3 < item_percentile <= 4:
            return self.created_list[percentile_limit_3:percentile_limit_4]
        if item_percentile > 4:
            return self.created_list[percentile_limit_4:]

    def _binary_search(self, search_item, items, loops):
        if search_item == items[len(items) - 1]:
            loops = loops - 1 if not loops == 0 else loops
            return {'count': loops, 'index': self.created_list.index(search_item)}
        elif len(items) == 2 and search_item not in items:
            return {'count': loops - 1, 'index': -1}

        middle = len(items) / 2
        first_half, last_half = items[:middle], items[middle:]
        valid_half = first_half if search_item <= first_half[len(first_half) - 1] else last_half

        return self._binary_search(search_item, valid_half, loops + 1)

    def __getitem__(self, index):
        return self.created_list[index]


