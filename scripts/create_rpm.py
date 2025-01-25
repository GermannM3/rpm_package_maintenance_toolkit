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

def create_rpm(spec_file, output_dir):
    """Создает RPM пакет из SPEC файла."""
    # Проверяем, существует ли SPEC файл
    if not os.path.isfile(spec_file):
        print(f"SPEC файл {spec_file} не найден.")
        exit(1)
    
    # Создаем директории для сборки, если они не существуют
    build_dir = os.path.join(os.path.dirname(spec_file), "BUILD")
    rpm_dir = os.path.join(os.path.dirname(spec_file), "RPMS")
    for directory in [build_dir, rpm_dir]:
        os.makedirs(directory, exist_ok=True)
    
    # Устанавливаем переменные окружения для rpmbuild
    env = os.environ.copy()
    env["HOME"] = os.path.dirname(spec_file)
    env["RPM_BUILD_DIR"] = build_dir
    env["RPM_RPMDIR"] = rpm_dir
    
    # Выполняем сборку RPM пакета
    run_command(["rpmbuild", "-bb", spec_file, "--target", "noarch"])
    
    # Перемещаем готовый пакет в output_dir
    for package in os.listdir(rpm_dir):
        if package.endswith(".rpm"):
            package_path = os.path.join(rpm_dir, package)
            os.rename(package_path, os.path.join(output_dir, package))
    
    print(f"RPM пакет успешно создан и сохранен в {output_dir}.")

def main():
    parser = argparse.ArgumentParser(description="Создание RPM пакета")
    parser.add_argument("spec_file", help="Путь к SPEC файлу")
    parser.add_argument("output_dir", help="Директория для выходных файлов")
    args = parser.parse_args()
    create_rpm(args.spec_file, args.output_dir)

if __name__ == "__main__":
    main()
