'''
the api is a class so make a new instance of it before use so it doesn't throw errors.
for example: a = crossfile.api()

a.get(<identifier>)  --> gets a resource from the database using an integer identifier
a.post(<identifier>,<string data>) --> creates a new resource in the database
a.delete(<identifier>) --> deletes a resource using an integer identifier
'''
class api(object):
    def __init__(self):
        self.dataname = ''
    def link(self,databasename):
        self.dataname = databasename
        return 'linked to: ' + self.dataname
    #gets a resource from the database
    def get(self,identifier):
        identifier = str(identifier)
        if identifier == '':
            f = open(self.dataname,'r')
            lines = f.readlines()
            for x in range(len(lines)):
                lines[x] = lines[x].strip('\n')
                lines[x] = lines[x].split(',')
            return lines
            f.close()
        else:
            identifier = str(identifier)
            #gets all of the identifiers
            with open(self.dataname,'r') as f:
                lines = f.readlines()
                identifiers = []
                for line in lines:
                    line = line.split(',')
                    identifiers.append(line[0])
            #finds the resource with the identifier, if it exists
            if identifier in identifiers:
                for line in lines:
                    line = line.strip('\n')
                    line = line.split(',')
                    if line[0] == identifier:
                        return line
            else:
                return '404 not found'
    #creates a new resource and puts it in the database
    def post(self,identifier,resource):
        oktowrite = True
        with open(self.dataname, "r") as f:
            lines = f.readlines()
            #check to see if databse is empty
            if lines == []:
                oktowrite = True
            #if databse not empty then check to see if resource already exists
            else:
                for line in lines:
                    line = line.strip('\n')
                    line = line.split(',')
                    if line[0] == str(identifier):
                        oktowrite = False
        if oktowrite == True:
            with open(self.dataname, "a") as f:
                f.write(str(identifier) + ',' + resource + '\n')
            return 'resource added'
        else:
            response = ['resource ' + str(identifier) + ' already exists']
            return ''.join(response)
    #deletes a resource
    def delete(self,identifier):
        with open(self.dataname, "r") as f:
            lines = f.readlines()
        with open(self.dataname, "w") as f:
            for line in lines:
                line = line.strip('\n')
                line = line.split(',')
                if lines != []:
                    if line[0] != str(identifier):
                        f.write(','.join(line) + '\n')
                else:
                    return '404 not found'
            return 'resource removed'
