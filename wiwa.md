```python

class Network:
    """
    Class to represent a computer network.
    """
    network_count = 0

    def __init__(self, name, ip_address):
        if not self.validate_ip(ip_address):
            raise InvalidIPAddressError(ip_address)
        
        self.name = name
        self.ip_address = ip_address
        self.devices = []
        Network.network_count += 1

    def add_device(self, device):
        self.devices.append(device)
        print(f"Added {device} to network {self.name}")

    @classmethod
    def count_networks(cls):
        print(f"Total networks created: {cls.network_count}")

    @staticmethod
    def validate_ip(ip):
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        try:
            for part in parts:
                if not 0 <= int(part) <= 255:
                    return False
        except ValueError:
            return False
        return True

    @classmethod
    def generate_random_ip(cls):
        return '.'.join(str(random.randint(0, 255)) for _ in range(4))

    @classmethod
    def create_random_network(cls):
        name = input("Enter network name: ")
        ip = cls.generate_random_ip()
        return cls(name, ip)

    def __repr__(self):
        return f"Network(name='{self.name}', ip_address='{self.ip_address}', devices={self.devices})"

    def __str__(self):
        return f"Network: {self.name}, IP: {self.ip_address}, Devices: {self.devices}"

    def __len__(self):
        return len(self.devices)

    def __contains__(self, item):
        return item in self.devices

    def __getitem__(self, index):
        return self.devices[index]

class InvalidIPAddressError(Exception):
    """
    Exception raised for invalid IP addresses.
    """
    def __init__(self, ip, message="Invalid IP address format"):
        self.ip = ip
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.ip} -> {self.message}"
```


```python

class Network:
    """
    Class to represent a computer network.
    """
    network_count = 0

    def __init__(self, name, ip_address, subnet_mask):
        if not self.validate_ip(ip_address):
            raise InvalidIPAddressError(ip_address)
        if not self.validate_subnet_mask(subnet_mask):
            raise InvalidSubnetMaskError(subnet_mask)
        
        self.name = name
        self.ip_address = ip_address
        self.subnet_mask = subnet_mask
        self.devices = []
        Network.network_count += 1

    def add_device(self, device):
        self.devices.append(device)
        print(f"Added {device} to network {self.name}")

    @classmethod
    def count_networks(cls):
        print(f"Total networks created: {cls.network_count}")

    @staticmethod
    def validate_ip(ip):
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        try:
            for part in parts:
                if not 0 <= int(part) <= 255:
                    return False
        except ValueError:
            return False
        return True

    @staticmethod
    def validate_subnet_mask(subnet_mask):
        parts = subnet_mask.split('.')
        if len(parts) != 4:
            return False
        try:
            binary_subnet = ''.join(format(int(part), '08b') for part in parts)
            if '01' in binary_subnet:
                return False
        except ValueError:
            return False
        return True

    @classmethod
    def generate_random_ip(cls):
        return '.'.join(str(random.randint(0, 255)) for _ in range(4))

    @classmethod
    def generate_random_subnet_mask(cls):
        return '.'.join(['255', '255', '255', str(random.choice([0, 128, 192, 224, 240, 248, 252, 254]))])

    @classmethod
    def create_random_network(cls):
        name = input("Enter network name: ")
        ip = cls.generate_random_ip()
        subnet_mask = cls.generate_random_subnet_mask()
        return cls(name, ip, subnet_mask)

    def __repr__(self):
        return f"Network(name='{self.name}', ip_address='{self.ip_address}', subnet_mask='{self.subnet_mask}', devices={self.devices})"

    def __str__(self):
        return f"Network: {self.name}, IP: {self.ip_address}, Subnet Mask: {self.subnet_mask}, Devices: {self.devices}"

    def __len__(self):
        return len(self.devices)

    def __contains__(self, item):
        return item in self.devices

    def __getitem__(self, index):
        return self.devices[index]

class InvalidIPAddressError(Exception):
    """
    Exception raised for invalid IP addresses.
    """
    def __init__(self, ip, message="Invalid IP address format"):
        self.ip = ip
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.ip} -> {self.message}"

class InvalidSubnetMaskError(Exception):
    """
    Exception raised for invalid subnet masks.
    """
    def __init__(self, subnet_mask, message="Invalid subnet mask format"):
        self.subnet_mask = subnet_mask
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.subnet_mask} -> {self.message}"
```



```python

class Network:
    """
    Class to represent a computer network.
    """
    network_count = 0

    def __init__(self, name, ip_address, subnet_mask):
        if not self.validate_ip(ip_address):
            raise InvalidIPAddressError(ip_address)
        if not self.validate_subnet_mask(subnet_mask):
            raise InvalidSubnetMaskError(subnet_mask)
        
        self.name = name
        self.ip_address = ip_address
        self.subnet_mask = subnet_mask
        self.devices = []
        Network.network_count += 1

    def add_device(self, device):
        self.devices.append(device)

    @classmethod
    def count_networks(cls):
        return cls.network_count

    @staticmethod
    def validate_ip(ip):
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        try:
            for part in parts:
                if not 0 <= int(part) <= 255:
                    return False
        except ValueError:
            return False
        return True

    @staticmethod
    def validate_subnet_mask(subnet_mask):
        parts = subnet_mask.split('.')
        if len(parts) != 4:
            return False
        try:
            binary_subnet = ''.join(format(int(part), '08b') for part in parts)
            if '01' in binary_subnet:
                return False
        except ValueError:
            return False
        return True

    @classmethod
    def generate_random_ip(cls):
        return '.'.join(str(random.randint(0, 255)) for _ in range(4))

    @classmethod
    def generate_random_subnet_mask(cls):
        return '.'.join(['255', '255', '255', str(random.choice([0, 128, 192, 224, 240, 248, 252, 254]))])

    @classmethod
    def create_random_network(cls):
        name = input("Enter network name: ")
        ip = cls.generate_random_ip()
        subnet_mask = cls.generate_random_subnet_mask()
        return cls(name, ip, subnet_mask)

    def __repr__(self):
        return f"Network(name='{self.name}', ip_address='{self.ip_address}', subnet_mask='{self.subnet_mask}', devices={self.devices})"

    def __str__(self):
        return f"Network: {self.name}, IP: {self.ip_address}, Subnet Mask: {self.subnet_mask}, Devices: {self.devices}"

    def __len__(self):
        return len(self.devices)

    def __contains__(self, item):
        return item in self.devices

    def __getitem__(self, index):
        return self.devices[index]

class InvalidIPAddressError(Exception):
    """
    Exception raised for invalid IP addresses.
    """
    def __init__(self, ip, message="Invalid IP address format"):
        self.ip = ip
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.ip} -> {self.message}"

class InvalidSubnetMaskError(Exception):
    """
    Exception raised for invalid subnet masks.
    """
    def __init__(self, subnet_mask, message="Invalid subnet mask format"):
        self.subnet_mask = subnet_mask
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.subnet_mask} -> {self.message}"
```