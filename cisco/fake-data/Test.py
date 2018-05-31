import unittest
from JsonParser import file_reader, path_extractor

class test_json(unittest.TestCase):
    def test_check_file_read(self):
        reader = file_reader("log.json")
        result = reader.parse_file()
        ph_extractor =path_extractor(result)
        ph_extractor.find_path_field()
        ph_extractor.find_most_k_frequent_path(3)
                
if __name__ == '__main__':
    unittest.main()