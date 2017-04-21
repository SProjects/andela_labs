class BinarySearch:
    def __init__(self, a, b):
        self.list_size = a
        self.step = b
        self.generated_list = self._generate_list()
        self.length = len(self.generated_list)

    def _generate_list(self):
        result = []
        value = self.step
        while len(result) < self.list_size:
            result.append(value)
            value += self.step
        return result

    def search(self, search_item):
        target_list = self._get_target_list(search_item)
        return self._binary_search(search_item, target_list, 0)

    def _get_target_list(self, search_item):
        """
        This method divides the self.generated_list into 5 portions/percentiles. Then uses the search_item to calculate
         the portion/percentile the it belongs to. The calculated portion/percentile is then used to determine which
         slice of self.generated_list to return for search.

        :param search_item:
        :return: slice of self.generated_list that contains the search_item
        """
        percentiles = 5
        percentile_step = len(self.generated_list) / percentiles
        percentile_limit_1, percentile_limit_2 = percentile_step, percentile_step * 2
        percentile_limit_3, percentile_limit_4 = percentile_step * 3, percentile_step * 4

        last_element = self.generated_list[len(self.generated_list) - 1]
        search_item_percentile = float(search_item) / float(last_element) * percentiles
        if search_item_percentile <= 1:
            return self.generated_list[:percentile_limit_1]
        if 1 < search_item_percentile <= 2:
            return self.generated_list[percentile_limit_1:percentile_limit_2]
        if 2 < search_item_percentile <= 3:
            return self.generated_list[percentile_limit_2:percentile_limit_3]
        if 3 < search_item_percentile <= 4:
            return self.generated_list[percentile_limit_3:percentile_limit_4]
        if search_item_percentile > 4:
            return self.generated_list[percentile_limit_4:]

    def _binary_search(self, search_item, items, loops):
        if search_item == items[len(items) - 1]:
            loops = loops - 1 if not loops == 0 else loops
            return {'count': loops, 'index': self.generated_list.index(search_item)}
        elif len(items) == 2 and search_item not in items:
            return {'count': loops - 1, 'index': -1}

        middle = len(items) / 2
        first_half, last_half = items[:middle], items[middle:]
        valid_half = first_half if search_item <= first_half[len(first_half) - 1] else last_half

        return self._binary_search(search_item, valid_half, loops + 1)

    def __getitem__(self, index):
        return self.generated_list[index]
