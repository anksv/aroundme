import json

class commonData:
    db_name = 'aroundmedb'
    db_collection = 'location_data'

    def convert_to_json(self,obj):
        return json.dumps(obj)

    def map_json(self, data):
        return json.loads(data.decode('utf-8'))

