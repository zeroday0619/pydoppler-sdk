class Endpoints:
    ROOT_URL = "https://api.doppler.com/v3"

    @classmethod
    def workspace(cls) -> str: ...
    @classmethod
    def activity_logs(cls) -> str: ...
    @classmethod
    def activity_log(cls) -> str: ...
    @classmethod
    def projects(cls) -> str: ...
    @classmethod
    def project(cls) -> str: ...
    @classmethod
    def environments(cls) -> str: ...
    @classmethod
    def environment(cls) -> str: ...
    @classmethod
    def configs(cls) -> str: ...
    @classmethod
    def config(cls) -> str: ...
    @classmethod
    def config_clone(cls) -> str: ...
    @classmethod
    def config_lock(cls) -> str: ...
    @classmethod
    def config_unlock(cls) -> str: ...
    @classmethod
    def config_logs(cls) -> str: ...
    @classmethod
    def configs_log_rollback(cls) -> str: ...
