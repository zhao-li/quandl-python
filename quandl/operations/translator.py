class Translator():
  def __init__(self, data):
    self.data = data

  def translate(self):
    return {
      "dataset_data": {
        "data": self._get_data(),
        "column_names": self._get_column_names(),
        "limit": self._get_limit(),
        "transform": self._get_transform(),
        "column_index": self._get_column_index(),
        "start_date": self._get_start_date(),
        "end_date": self._get_end_date(),
        "frequency": self._get_frequency(),
        "collapse": self._get_collapse(),
        "order": self._get_order()
      }
    }

  def _get_data(self):
    data_entries = []
    if self.data['data'] is not None:
      for data_entry in self.data['data']:
        data_entries.append(self._flatten(data_entry))
    return data_entries

  def _flatten(self, entry):
    flattened_entry = []
    for column_title in self._get_column_names():
      flattened_entry.append(
        entry['attributes'][column_title]
      )
    return flattened_entry

  def _get_column_names(self):
    column_names = []
    if self.data['data'] is not None and len(self.data['data']) >= 1:
      for column_title, cell_value in self.data['data'][0]['attributes'].items():
        column_names.append(column_title)
      column_name_for_indexing = self.data['data'][0]['index']
      column_names.remove(column_name_for_indexing)
      column_names.insert(0, column_name_for_indexing)
    return column_names

  def _get_limit(self):
    return None

  def _get_transform(self):
    return None

  def _get_column_index(self):
    return None

  def _get_start_date(self):
    return None

  def _get_end_date(self):
    return None

  def _get_frequency(self):
    return None

  def _get_collapse(self):
    return None

  def _get_order(self):
    return None

