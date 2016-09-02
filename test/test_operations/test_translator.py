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
    self.assertEqual(
      self.translator.translate()['dataset_data']['data'],
      self.desired_result['dataset_data']['data']
    )

  def test_translator_can_translate_column_names(self):
    self.assertEqual(
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

