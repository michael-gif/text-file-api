class Crossfile():
    def __init__(self, filename=''):
        self.filename = filename

    def link(self, filename: str) -> str:
        '''
        Link the current instance to a 'database' file
        :param filename: full/relative path
        :return: status
        '''
        self.filename = filename
        return 'successfully linked to: ' + self.filename

    def get(self, identifier: str):
        '''
        | Gets resource associated with the given identifier.
        | If no identifier is specified, then the whole database is returned.
        :param identifier: unique string
        :return:  status
        '''
        identifier = str(identifier)
        with open(self.filename) as file:
            lines = file.readlines()
        if not identifier:
            return [tuple(line.strip('\n').split(',')) for line in lines]
        for line in lines:
            key, value = line.strip('\n').split(',')
            if key == identifier:
                return key, value
        return f"resource {identifier} doesn't exist"

    def post(self, identifier: str, resource) -> str:
        '''
        | Create a new resource in the database.
        | If the given identifier already exists, the resource isn't added.
        :param identifier: unique string
        :param resource: anything
        :return: status
        '''
        identifier = str(identifier)
        with open(self.filename) as file:
            lines = file.readlines()

        can_write = False
        if not lines:
            can_write = True
        else:
            # check to see if identifier is already in one of the lines
            for line in lines:
                key, value = line.strip('\n').split(',')
                if key == identifier:
                    can_write = False

        if can_write:
            with open(self.filename, 'a') as file:
                file.write(f"{identifier},{resource}\n")
            return 'resource added'
        else:
            return f"resource {identifier} already exists"

    def delete(self, identifier: str) -> str:
        '''
        | Deletes the resource associated with the given identifier.
        | If the given identifier doesn't exist, an error is returned
        :param identifier: unique string
        :return: status
        '''
        with open(self.filename) as file:
            lines = file.readlines()

        deleted_resource = False
        with open(self.filename, 'w') as file:
            file.seek(0)
            for line in lines:
                key, value = line.strip('\n').split(',')
                if key != identifier:
                    file.write(line)
                else:
                    deleted_resource = True
            file.truncate()

        return 'resource removed' if deleted_resource else f"resource {identifier} doesn't exist"
