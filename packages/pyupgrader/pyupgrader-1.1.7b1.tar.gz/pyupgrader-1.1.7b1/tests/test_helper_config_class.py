import unittest
import logging
import tempfile
import shutil
import os
import yaml
from tests.misc import mock_config_str, mock_config_dict
from pyupgrader.utilities.helper import Config

LOGGER = logging.getLogger(__name__)


class TestConfig(unittest.TestCase):
    
    def setUp(self):
        """
        Set up the test environment by creating a temporary directory and a temporary file.
        """
        # Create a temporary directory
        self.temp_dir_path = tempfile.mkdtemp()
        LOGGER.debug(f"Created temporary directory: {self.temp_dir_path}")
        # Create a temporary file inside the temporary directory
        self.yaml_file_path = os.path.join(self.temp_dir_path, "config.yaml")
        LOGGER.debug(f"Created temporary file: {self.yaml_file_path}")
        # create temp yaml file using mock_config
        with open(self.yaml_file_path, "w") as file:
            file.write(mock_config_str)

        self.config = Config()
    
    def tearDown(self):
        """
        Clean up method that is called after each test case.
        Removes the temporary directory and logs the removal.
        """
        shutil.rmtree(self.temp_dir_path)
        LOGGER.debug(f"Removed temporary directory: {self.temp_dir_path}")

    def test_load_yaml(self):
        """
        Test the load_yaml method of the Config class.
        """
        LOGGER.info("Testing test_load_yaml")
        data = self.config.load_yaml(self.yaml_file_path)
        LOGGER.debug(f"data: {data}")
        self.assertEqual(data, mock_config_dict)

    def test_loads_yaml(self):
        """
        Test case for loading YAML configuration.
        """
        LOGGER.info("Testing test_loads_yaml")
        data = self.config.loads_yaml(mock_config_str)
        self.assertEqual(data, mock_config_dict)

    def test_write_yaml(self):
        """
        Test the write_yaml method of the Config class.
        """
        LOGGER.info("Testing test_write_yaml")
        temp_file_path = os.path.join(self.temp_dir_path, "temp.yaml")
        self.config.write_yaml(temp_file_path, mock_config_dict)
        with open(temp_file_path, "r") as file:
            written_data = yaml.safe_load(file)
        self.assertEqual(written_data, mock_config_dict)

    def test_valid_config(self):
        """
        Test case to verify the validity of the configuration.
        """
        LOGGER.info("Testing test_valid_config")
        is_valid, error = self.config._valid_config(mock_config_dict)
        self.assertTrue(is_valid)
        self.assertEqual(error, "")

    def test_invalid_config(self):
        LOGGER.info("Testing test_invalid_config")
        invalid_config = {
            "version": "1.0",
            "description": "My config",
            "hash_db": "hash.db",
            "startup_path": "/path/to/startup",
            "required_only": True
        }

        is_valid, error = self.config._valid_config(invalid_config)
        self.assertFalse(is_valid)
        self.assertEqual(error, 'Missing "cleanup" attribute')

if __name__ == "__main__":
    unittest.main()
