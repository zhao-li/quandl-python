import unittest
from quandl.operations.translator import Translator
import os 
import json

class TranslatorTestCase(unittest.TestCase):
  def setUp(self):
    path = os.path.dirname(__file__)
    with open(path + '/test.rsae.messages.json') as input_file:    
      data = json.load(input_file)
    with open(path + '/test.rsae.messages.translated.json') as desired_result_file:    
      self.desired_result = json.load(desired_result_file)
    self.translator = Translator(data)

  def test_translator_can_translate_data(self):
    self.assertTrue(
      set(self.translator.translate()['dataset_data']['data'][0]) ==
      set(self.desired_result['dataset_data']['data'][0])
    )

  def test_translator_can_keep_data_title_and_value_in_the_same_order(self):
    for attribute in [ 
      "supply-chain", "booking-no", "container-id", "gs-id", "msg-seq-no",
      "acq-dt", "msg-received-dt", "msg-received-age", "position-lat-long",
      "position-type", "locode", "msg-type", "raw"
    ]:
      with self.subTest(attribute=attribute):
        expected_index = self.translator.translate()['dataset_data']['column_names'].index(attribute)
        fixture_index = self.desired_result['dataset_data']['column_names'].index(attribute)
        self.assertEqual(
          self.translator.translate()['dataset_data']['data'][0][expected_index],
          self.desired_result['dataset_data']['data'][0][fixture_index]
        )

  def test_translator_can_translate_column_names(self):
    self.assertTrue(
      set(self.translator.translate()['dataset_data']['column_names']) ==
      set(self.desired_result['dataset_data']['column_names'])
    )
    self.assertCountEqual(
      self.translator.translate()['dataset_data']['column_names'],
      self.desired_result['dataset_data']['column_names']
    )

  def test_translator_can_translate_limit(self):
    self.assertEqual(
      self.translator.translate()['dataset_data']['limit'],
      self.desired_result['dataset_data']['limit']
    )

  def test_translator_can_translate_transform(self):
    self.assertEqual(
      self.translator.translate()['dataset_data']['transform'],
      self.desired_result['dataset_data']['transform']
    )

  def test_translator_can_translate_column_index(self):
    self.assertEqual(
      self.translator.translate()['dataset_data']['column_index'],
      self.desired_result['dataset_data']['column_index']
    )

  def test_translator_can_translate_start_date(self):
    self.assertEqual(
      self.translator.translate()['dataset_data']['start_date'],
      self.desired_result['dataset_data']['start_date']
    )

  def test_translator_can_translate_end_date(self):
    self.assertEqual(
      self.translator.translate()['dataset_data']['end_date'],
      self.desired_result['dataset_data']['end_date']
    )

  def test_translator_can_translate_frequency(self):
    self.assertEqual(
      self.translator.translate()['dataset_data']['frequency'],
      self.desired_result['dataset_data']['frequency']
    )

  def test_translator_can_translate_collapse(self):
    self.assertEqual(
      self.translator.translate()['dataset_data']['collapse'],
      self.desired_result['dataset_data']['collapse'],
    )

  def test_translator_can_translate_order(self):
    self.assertEqual(
      self.translator.translate()['dataset_data']['order'],
      self.desired_result['dataset_data']['order'],
    )

  def test_translator_puts_index_as_first_column(self):
    self.assertEqual(
      self.translator.translate()['dataset_data']['column_names'][0],
      self.desired_result['dataset_data']['column_names'][0],
    )
    self.assertEqual(
      self.translator.translate()['dataset_data']['data'][0][0],
      self.desired_result['dataset_data']['data'][0][0],
    )

