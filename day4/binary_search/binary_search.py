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

    def search(self, item):
        try:
            item_index = self.created_list.index(item)
        except ValueError:
            item_index = -1

        target_list = self._get_target_portion(item_index)
        return self._binary_search(item, item_index, target_list, 0)

    def _get_target_portion(self, index):
        # Split the created_list into 5 portion and return the one that has the item
        percentile_step = len(self.created_list) / 5
        percentile_1, percentile_2 = percentile_step, percentile_step*2
        percentile_3, percentile_4 = percentile_step*3, percentile_step*4

        item_percentile = int((float(index)/float(len(self.created_list))) * 5) * len(self.created_list)
        if item_percentile <= percentile_1:
            return self.created_list[:percentile_1]
        if item_percentile <= percentile_2:
            return self.created_list[percentile_1:percentile_2]
        if item_percentile <= percentile_3:
            return self.created_list[percentile_2:percentile_3]
        if item_percentile <= percentile_4:
            return self.created_list[percentile_3:percentile_4]
        if item_percentile > percentile_4:
            return self.created_list[percentile_4:]

    def _binary_search(self, search_item, item_index, items, loops):
        if search_item == items[len(items) - 1]:
            loops = loops - 1 if not loops == 0 else loops
            return {'count': loops, 'index': item_index}
        elif len(items) == 2 and search_item not in items:
            return {'count': loops, 'index': item_index}

        middle = len(items) / 2
        first_half, last_half = items[:middle], items[middle:]
        valid_half = first_half if search_item <= first_half[len(first_half) - 1] else last_half

        return self._binary_search(search_item, item_index, valid_half, loops+1)

    def __getitem__(self, index):
        return self.created_list[index]


