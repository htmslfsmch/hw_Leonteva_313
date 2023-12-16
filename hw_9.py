import os
import shutil


class FileManager:
    def __init__(self, current_directory='.'):
        self.current_directory = current_directory
        
#Просмотр содержимого текущей директории.
    def list_contents(self):
        print(f"Содержимое директории {self.current_directory}:")
        for item in os.listdir(self.current_directory):
            print(item)
            
# Создание новой директории.
    def create_directory(self, directory_name):
        path = os.path.join(self.current_directory, directory_name)
        os.mkdir(path)
        print(f"Создана новая директория: {path}")
        
# Удаление директории или файла.
    def delete(self, name):
        path = os.path.join(self.current_directory, name)
        if os.path.isfile(path):
            os.remove(path)
            print(f"Файл удален: {path}")
        elif os.path.isdir(path):
            os.rmdir(path)
            print(f"Директория удалена: {path}")
        else:
            print(f"Файл или директория не найдены: {path}")
            
# Копирование файла или директории.
    def copy(self, source, destination):
        source_path = os.path.join(self.current_directory, source)
        destination_path = os.path.join(self.current_directory, destination)
        if os.path.isfile(source_path):
            shutil.copy2(source_path, destination_path)
            print(f"Файл скопирован: {source_path} -> {destination_path}")
        elif os.path.isdir(source_path):
            shutil.copytree(source_path, destination_path)
            print(f"Директория скопирована: {source_path} -> {destination_path}")
        else:
            print(f"Файл или директория не найдены: {source_path}")
            
# Перемещение файла или директории.
    def move(self, source, destination):
        source_path = os.path.join(self.current_directory, source)
        destination_path = os.path.join(self.current_directory, destination)
        os.rename(source_path, destination_path)
        print(f"Файл или директория перемещены: {source_path} -> {destination_path}")

# Поиск файла по имени в текущей директории и всех поддиректориях.
    def search_file(self, filename):
        for root, dirs, files in os.walk(self.current_directory):
            if filename in files:
                print(f"Файл найден: {os.path.join(root, filename)}")
                return os.path.join(root, filename)
        print(f"Файл не найден: {filename}")
        
# Изменение прав доступа к файлу или директории.
    def change_permissions(self, name, mode):
        path = os.path.join(self.current_directory, name)
        os.chmod(path, mode)
        print(f"Изменены права доступа для {path} на {oct(mode)}")
