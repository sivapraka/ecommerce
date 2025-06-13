import unittest
import tempfile
import os
from pathlib import Path

from ecommerce.config_managerImpl import FileBasedConfigurationManagerImpl


class TestFileBasedConfigurationManager(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_config_file = None

        FileBasedConfigurationManagerImpl.reset_instance()
        self.temp_config_file = Path(
            os.path.join(self.temp_dir.name, "config.properties")
        )
        with open(self.temp_config_file, "w") as file:
            file.write("stringKey=stringValue\nintKey=42")

    def test_get_instance_method(self):
        instance = FileBasedConfigurationManagerImpl.get_instance()
        self.assertIsNotNone(
            instance, "If getInstance() is called, it should return a non-null instance"
        )

    def test_singleton_behavior(self):
        instance1 = FileBasedConfigurationManagerImpl.get_instance()
        self.assertIsNotNone(
            instance1,
            "If getInstance() is called, it should return a non-null instance",
        )
        instance2 = FileBasedConfigurationManagerImpl.get_instance()
        self.assertIs(
            instance1,
            instance2,
            "If getInstance() is called multiple times, it should return the same instance",
        )

    def test_reset_instance_method(self):
        instance1 = FileBasedConfigurationManagerImpl.get_instance()
        self.assertIsNotNone(
            instance1,
            "If getInstance() is called, it should return a non-null instance",
        )
        FileBasedConfigurationManagerImpl.reset_instance()
        instance2 = FileBasedConfigurationManagerImpl.get_instance()
        self.assertIsNot(
            instance1,
            instance2,
            "If resetInstance() is called, getInstance() should return a new instance",
        )

    def test_get_configuration(self):

        instance = FileBasedConfigurationManagerImpl.get_instance()
        self.assertIsNotNone(
            instance, "If getInstance() is called, it should return a non-null instance"
        )
        instance.load(self.temp_config_file)
        value = instance.get_configuration("stringKey")
        self.assertEqual(
            "stringValue",
            value,
            "If a configuration value exists, it should be returned",
        )

    def test_get_configuration_with_type_conversion(self):
        instance = FileBasedConfigurationManagerImpl.get_instance()
        self.assertIsNotNone(
            instance,
            "If getInstance() is called, it should return a non-null instance",
        )
        instance.load(self.temp_config_file)
        int_value = instance.get_configuration_with_type("intKey", int)
        self.assertEqual(
            42,
            int_value,
            "If a configuration value exists, it should be returned after type conversion",
        )

    def test_set_configuration(self):
        instance = FileBasedConfigurationManagerImpl.get_instance()
        self.assertIsNotNone(
            instance, "If getInstance() is called, it should return a non-null instance"
        )
        instance.load(self.temp_config_file)
        instance.set_configuration("newKey", "newValue")
        value = instance.get_configuration("newKey")
        self.assertEqual(
            "newValue",
            value,
            "If a configuration value is set, it should be returned by getConfiguration()",
        )

    def test_remove_configuration(self):
        instance = FileBasedConfigurationManagerImpl.get_instance()
        self.assertIsNotNone(
            instance, "If getInstance() is called, it should return a non-null instance"
        )
        instance.load(self.temp_config_file)
        instance.remove_configuration("stringKey")
        value = instance.get_configuration("stringKey")
        self.assertIsNone(
            value,
            "If a configuration value is removed, it should return None when getConfiguration() is called",
        )

    def test_clear(self):

        instance = FileBasedConfigurationManagerImpl.get_instance()
        self.assertIsNotNone(
            instance, "If getInstance() is called, it should return a non-null instance"
        )

        instance.load(self.temp_config_file)

        instance.clear()
        string_value = instance.get_configuration("stringKey")
        int_value = instance.get_configuration_with_type("intKey", int)
        self.assertIsNone(
            string_value,
            "If the configuration is cleared, getConfiguration() should return None",
        )
        self.assertIsNone(
            int_value,
            "If the configuration is cleared, getConfiguration() should return None",
        )


if __name__ == "__main__":
    unittest.main()
