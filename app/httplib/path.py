PathParam = dict[str, str]

class Path:
    @staticmethod
    def params(endpoint: str, target: str) -> PathParam:
        paths = endpoint.split('/')
        targets = target.split('/')

        if len(paths) != len(targets):
            return {}

        path_params = {}

        for idx, path in enumerate(paths):
            if path.startswith('{') and path.endswith('}'):
                path_var = path.replace('{', '').replace('}', '')
                path_params[path_var] = targets[idx]
            elif path != targets[idx]:
                return {}

        return path_params

    @staticmethod
    def matches(endpoint: str, target: str) -> bool:
        paths = Path.parse(endpoint)
        targets = Path.parse(target)

        if len(paths) != len(targets):
            return False

        for idx, path in enumerate(paths):
            if not path.startswith('{') and path != targets[idx]:
                return False

        return True

    @staticmethod
    def parse(path: str, sep='/'):
        return path.split(sep)
