import unittest
from JsonParser import file_reader, path_extractor

class test_json(unittest.TestCase):
    def test_check_file_read(self):
        with self.assertRaises(ValueError):
            reader = file_reader("log2.json")
            result = reader.parse_file()

    def test_json_path_extractor(self):
        reader = file_reader("test_log.json")
        result = reader.parse_file()
        ph_extractor =path_extractor(result)
        ph_extractor.find_path_field()
        self.assertEqual(ph_extractor.find_most_k_frequent_path(2), {1: ('soccer', 4), 2: ('sheep', 2)})
                
if __name__ == '__main__':
    unittest.main()