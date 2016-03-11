class BaseConfig:
    def __init__(self):
        pass


class DevelopmentConfig(BaseConfig):
    def __init__(self):
        super().__init__()


class TestingConfig(BaseConfig):
    def __init__(self):
        super().__init__()


class ProductionConfig(BaseConfig):
    def __init__(self):
        super().__init__()
