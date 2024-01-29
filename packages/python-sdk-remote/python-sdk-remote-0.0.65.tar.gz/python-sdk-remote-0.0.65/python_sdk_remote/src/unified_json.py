from .valid_json_versions import valid_json_versions


class UnifiedJson:
    def __init__(self, data: dict, version: str):
        if version not in valid_json_versions:
            raise Exception(
                f"version {version} is not in valid_json_versions {valid_json_versions}"
            )
        self.version = version
        self.data = data

    def get_unified_json(self):
        return {"version": self.version, "data": self.data}

    def __str__(self):
        return self.get_unified_json()

    def __repr__(self):
        return self.__str__()
