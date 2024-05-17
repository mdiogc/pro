
```python
class FileSystem:
    """
    Class to represent a file system.
    """
    fs_count = 0

    def __init__(self, name, root_path):
        if not self.validate_path(root_path):
            raise InvalidPathError(root_path)
        
        self.name = name
        self.root_path = root_path
        self.folders = []
        self.files = []
        FileSystem.fs_count += 1

    def add_folder(self, folder):
        self.folders.append(folder)
        return f"Added {folder} to file system {self.name}"

    def remove_folder(self, folder_name):
        for folder in self.folders:
            if folder.name == folder_name:
                self.folders.remove(folder)
                return f"Removed {folder_name} from file system {self.name}"
        return f"Folder '{folder_name}' not found in file system {self.name}"

    def search_files(self, query):
        results = []
        for folder in self.folders:
            for file in folder.files:
                if query in file.name:
                    results.append(file)
        return results

    def copy_file(self, source_path, dest_path):
        try:
            shutil.copy2(source_path, dest_path)
            return f"File copied from {source_path} to {dest_path}"
        except FileNotFoundError:
            return "Source file not found"
        except PermissionError:
            return "Permission denied"

    def move_file(self, source_path, dest_path):
        try:
            shutil.move(source_path, dest_path)
            return f"File moved from {source_path} to {dest_path}"
        except FileNotFoundError:
            return "Source file not found"
        except PermissionError:
            return "Permission denied"

    @classmethod
    def count_filesystems(cls):
        return f"Total file systems created: {cls.fs_count}"

    @staticmethod
    def validate_path(path):
        return os.path.isabs(path)

    @classmethod
    def generate_random_path(cls):
        return os.path.join("/", "".join(random.choices(string.ascii_lowercase + string.digits, k=10)))

    @classmethod
    def create_random_filesystem(cls):
        name = input("Enter file system name: ")
        path = cls.generate_random_path()
        return cls(name, path)

    def __repr__(self):
        return f"FileSystem(name='{self.name}', root_path='{self.root_path}', folders={self.folders})"

    def __str__(self):
        return f"File System: {self.name}, Root Path: {self.root_path}, Folders: {self.folders}"

    def __len__(self):
        return len(self.folders)

    def __contains__(self, item):
        return item in self.folders

    def __getitem__(self, index):
        return self.folders[index]

class Folder:
    """
    Class to represent a folder.
    """
    def __init__(self, name, path):
        if not FileSystem.validate_path(path):
            raise InvalidPathError(path)
        
        self.name = name
        self.path = path
        self.files = []

    def add_file(self, file):
        self.files.append(file)
        return f"Added {file} to folder {self.name}"

    def remove_file(self, file_name):
        for file in self.files:
            if file.name == file_name:
                self.files.remove(file)
                return f"Removed {file_name} from folder {self.name}"
        return f"File '{file_name}' not found in folder {self.name}"

    def __repr__(self):
        return f"Folder(name='{self.name}', path='{self.path}', files={self.files})"

    def __str__(self):
        return f"Folder: {self.name}, Path: {self.path}, Files: {self.files}"

    def __len__(self):
        return len(self.files)

    def __contains__(self, item):
        return item in self.files

    def __getitem__(self, index):
        return self.files[index]

class File:
    """
    Class to represent a file.
    """
    def __init__(self, name, size, path):
        if not FileSystem.validate_path(path):
            raise InvalidPathError(path)

        self.name = name
        self.size = size  # Size in bytes
        self.path = path

    def __repr__(self):
        return f"File(name='{self.name}', size={self.size}, path='{self.path}')"

    @property
    def info(self):
        return f"{self.name} ({self.size} bytes) at {self.path}"

    @info.setter
    def info(self, new_info):
        self.size, self.path = new_info

class InvalidPathError(Exception):
    """
    Exception raised for invalid file paths.
    """
    def __init__(self, path, message="Invalid file path"):
        self.path = path
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.path} -> {self.message}"
```















```python
class FileSystem:
    """
    Class to represent a file system.
    """
    fs_count = 0

    def __init__(self, name, root_path):
        if not self.validate_path(root_path):
            raise InvalidPathError(root_path)
        
        self.name = name
        self.root_path = root_path
        self.folders = []
        FileSystem.fs_count += 1

    def add_folder(self, folder):
        self.folders.append(folder)
        print(f"Added {folder} to file system {self.name}")

    @classmethod
    def count_filesystems(cls):
        print(f"Total file systems created: {cls.fs_count}")

    @staticmethod
    def validate_path(path):
        return os.path.isabs(path)

    @classmethod
    def generate_random_path(cls):
        return os.path.join("/", "".join(random.choices(string.ascii_lowercase + string.digits, k=10)))

    @classmethod
    def create_random_filesystem(cls):
        name = input("Enter file system name: ")
        path = cls.generate_random_path()
        return cls(name, path)

    def __repr__(self):
        return f"FileSystem(name='{self.name}', root_path='{self.root_path}', folders={self.folders})"

    def __str__(self):
        return f"File System: {self.name}, Root Path: {self.root_path}, Folders: {self.folders}"

    def __len__(self):
        return len(self.folders)

    def __contains__(self, item):
        return item in self.folders

    def __getitem__(self, index):
        return self.folders[index]

class Folder:
    """
    Class to represent a folder.
    """
    def __init__(self, name, path):
        if not FileSystem.validate_path(path):
            raise InvalidPathError(path)
        
        self.name = name
        self.path = path
        self.files = []

    def add_file(self, file):
        self.files.append(file)
        print(f"Added {file} to folder {self.name}")

    def __repr__(self):
        return f"Folder(name='{self.name}', path='{self.path}', files={self.files})"

    def __str__(self):
        return f"Folder: {self.name}, Path: {self.path}, Files: {self.files}"

    def __len__(self):
        return len(self.files)

    def __contains__(self, item):
        return item in self.files

    def __getitem__(self, index):
        return self.files[index]

class File:
    """
    Class to represent a file.
    """
    def __init__(self, name, size, path):
        if not FileSystem.validate_path(path):
            raise InvalidPathError(path)

        self.name = name
        self.size = size  # Size in bytes
        self.path = path

    def __repr__(self):
        return f"File(name='{self.name}', size={self.size}, path='{self.path}')"

    @property
    def info(self):
        return f"{self.name} ({self.size} bytes) at {self.path}"

    @info.setter
    def info(self, new_info):
        self.size, self.path = new_info

class InvalidPathError(Exception):
    """
    Exception raised for invalid file paths.
    """
    def __init__(self, path, message="Invalid file path"):
        self.path = path
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.path} -> {self.message}"

```