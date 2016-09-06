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
    self._check_data_attribute_order("supply-chain")
    self._check_data_attribute_order("booking-no")
    self._check_data_attribute_order("container-id")
    self._check_data_attribute_order("gs-id")
    self._check_data_attribute_order("msg-seq-no")
    self._check_data_attribute_order("acq-dt")
    self._check_data_attribute_order("msg-received-dt")
    self._check_data_attribute_order("msg-received-age")
    self._check_data_attribute_order("position-lat-long")
    self._check_data_attribute_order("position-type")
    self._check_data_attribute_order("locode")
    self._check_data_attribute_order("msg-type")
    self._check_data_attribute_order("raw")

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

  def _check_data_attribute_order(self, attribute):
    expected_index = self.translator.translate()['dataset_data']['column_names'].index(attribute)
    fixture_index = self.desired_result['dataset_data']['column_names'].index(attribute)
    self.assertEqual(
      self.translator.translate()['dataset_data']['data'][0][expected_index],
      self.desired_result['dataset_data']['data'][0][fixture_index]
    )

