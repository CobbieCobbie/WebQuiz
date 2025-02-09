import json
import os


class Statement:
    def __init__(self, id, trueStatement, falseStatement, description):
        self.id = id
        self.trueStatement = trueStatement
        self.falseStatement = falseStatement
        self.description = description

    def __repr__(self):
        return f"Statement(id={self.id}, TrueStatement='{self.trueStatement}', FalseStatement='{self.falseStatement}', Description='{self.description}')"


    # class methods for (de-)serialization 

    def to_json(self):
        return json.dumps({
            'id': self.id, 
            'TrueStatement': self.trueStatement, # Bound by a number of chars, for readability of the Web App button on a tablet, e.g. 150 chars
            'FalseStatement': self.falseStatement, # Bound by a number of chars, for readability of the Web App button on a tablet, e.g. 150 chars
            'Description': self.description # Bound by a number of chars, for readability of the Web App button on a tablet, e.g. 400 chars
        })

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return Statement(data['id'], data['TrueStatement'], data['FalseStatement'], data['Description'])

    @staticmethod
    def load_from_file(filename="statements.json"):
        if not os.path.exists(filename):
            print(f"File {filename} does not exist.")
            return []

        with open(filename, "r") as file:
            statements_data = json.load(file)

        # Deserialize each statement from JSON string to Statement object
        return [Statement.from_json(json.dumps(item)) for item in statements_data]

    @staticmethod
    def save_to_file(statements, filename="statements.json"):
        # Method to save a list of Statement objects to a binary JSON file
        statements_data = [json.loads(statement.to_json()) for statement in statements]
        
        with open(filename, "w") as file:
            json.dump(statements_data, file, indent=4)


# test module and python call

def module_test():
    s1 = Statement(0, "True Statement 1", "False Statement 1", "Description 1")
    s2 = Statement(1, "True Statement 2", "False Statement 2", "Description 2")

    # Test serialization and deserialization
    s1_json = s1.to_json()
    s1_copy = Statement.from_json(s1_json)
    print(s1_copy)

    # Test save and load from file
    Statement.save_to_file([s1, s2], "statements.json")
    statements = Statement.load_from_file("statements.json")
    for statement in statements:
        print(statement)


if __name__ == "__main__":
    module_test()
