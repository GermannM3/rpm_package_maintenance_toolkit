import unittest
import subprocess
import os

class TestCreateRpm(unittest.TestCase):
    def setUp(self):
        # Устанавливаем пути к тестовым файлам
        self.spec_file = os.path.join(os.path.dirname(__file__), "..", "examples", "example_package", "example.spec")
        self.output_dir = os.path.join(os.path.dirname(__file__), "..", "output")
        os.makedirs(self.output_dir, exist_ok=True)
    
    def test_create_rpm(self):
        # Выполняем скрипт создания RPM пакета
        subprocess.run(["python3", "../scripts/create_rpm.py", self.spec_file, self.output_dir], check=True)
        
        # Проверяем, что пакет создан
        self.assertTrue(os.path.isfile(os.path.join(self.output_dir, "example_package-1.0-1.noarch.rpm")))
    
    def test_update_rpm(self):
        # Обновляем версию
        new_version = "1.1"
        subprocess.run(["python3", "../scripts/update_rpm.py", self.spec_file, new_version, self.output_dir], check=True)
        
        # Проверяем, что пакет с новой версией создан
        self.assertTrue(os.path.isfile(os.path.join(self.output_dir, f"example_package-{new_version}-1.noarch.rpm")))
    
    def tearDown(self):
        # Удаляем созданные пакеты
        for file in os.listdir(self.output_dir):
            if file.endswith(".rpm"):
                os.remove(os.path.join(self.output_dir, file))

if __name__ == "__main__":
    unittest.main()
