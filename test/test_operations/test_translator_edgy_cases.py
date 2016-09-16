import unittest
from quandl.operations.translator import Translator
import os 
import json

class TranslatorTestEdgeCase(unittest.TestCase):
  def setUp(self):
    path = os.path.dirname(__file__)
    with open(path + '/test.rsae.messages.no_data.json') as input_file:    
      data = json.load(input_file)
    with open(path + '/test.rsae.messages.no_data.translated.json') as desired_result_file:    
      self.desired_result = json.load(desired_result_file)
    self.translator = Translator(data)

  def test_translator_translates_no_data_to_empty_lists(self):
    for property in ['data', 'column_names']:
      with self.subTest(property=property):
        self.assertTrue(
          set(self.translator.translate()['dataset_data'][property]) ==
          set(self.desired_result['dataset_data'][property])
        )

