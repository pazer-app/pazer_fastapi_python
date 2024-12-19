from pazer_core_python import CoreConfig


def config() -> CoreConfig:
    return CoreConfig(
        TITLE="Pazer Core - Python",
        VERSION="0.1.0",
        CROSS_ALLOW_CROSS=False,
        CROSS_ALLOW_ORIGINS=[],
        CROSS_ALLOW_CREDENTIALS=False,
        CROSS_ALLOW_METHODS=[],
        CROSS_ALLOW_HEADERS=[],
        SESSION_HOST={
            "main_read": {
                "hostname": "127.0.0.1",
                "port": 6379,
                "namespace": "test",
                "scheme": "http",
            },
            "main_write": {
                "hostname": "127.0.0.1",
                "port": 6379,
                "namespace": "test",
                "scheme": "http",
            }
        },
        DATABASE_HOST={
            "main_read": {
                "hostname": "localhost",
                "username": "test",
                "password": "test",
                "database": "test",
                "port": 3306,
                "charset": "utf8mb4",
            },
            "main_write": {
                "hostname": "localhost",
                "username": "test",
                "password": "test",
                "database": "test",
                "port": 3306,
                "charset": "utf8mb4",
            },
        },
    )
