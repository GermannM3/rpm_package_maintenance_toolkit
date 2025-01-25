import os
import subprocess
import argparse

def run_command(command):
    """Выполняет команду в подпроцессе."""
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды: {e}")
        exit(1)

def update_spec_version(spec_file, new_version):
    """Обновляет версию в SPEC файле."""
    with open(spec_file, 'r') as file:
        spec_content = file.read()
    
    # Обновляем версию
    spec_content = spec_content.replace("Version: ", f"Version: {new_version}\n")
    
    with open(spec_file, 'w') as file:
        file.write(spec_content)
    
    print(f"Версия в SPEC файле обновлена до {new_version}.")

def update_rpm(spec_file, new_version, output_dir):
    """Обновляет и пересобирает RPM пакет."""
    update_spec_version(spec_file, new_version)
    create_rpm(spec_file, output_dir)

def main():
    parser = argparse.ArgumentParser(description="Обновление RPM пакета")
    parser.add_argument("spec_file", help="Путь к SPEC файлу")
    parser.add_argument("new_version", help="Новая версия пакета")
    parser.add_argument("output_dir", help="Директория для выходных файлов")
    args = parser.parse_args()
    update_rpm(args.spec_file, args.new_version, args.output_dir)

if __name__ == "__main__":
    main()
