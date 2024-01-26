class Host:
    name: str
    data: dict

    def __init__(self, name, **data) -> None:
        self.name = name
        self.data = data


class Group:
    hosts: list[Host]
    data: dict

    def __init__(self, *hosts: Host, **data) -> None:
        self.hosts = list(hosts)
        self.data = data

    def __iter__(self):
        for host in self.hosts:
            yield host

    def append(self, *hosts: Host) -> None:
        self.hosts.extend(hosts)
