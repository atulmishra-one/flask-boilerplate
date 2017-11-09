class BaseConfig:
    DEBUG = TRUE
    SECRET_KEY = r"PUT YOUR SECRET KEY HERE"
    SQLALCHEMY_DATABASE_URI = None
                

class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(DevelopmentConfig):
    DEBUG = False
                

app_config = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig
}