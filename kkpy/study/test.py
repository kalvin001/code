import django
print(django.get_version())
import pandas as pd
import json

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
    
        return json.JSONEncoder.default(self, obj)


d = pd.DataFrame({
    'Smith': {'age': 10, 'sex': '1'},
    'Obama': {'age': 10, 'sex': '男'},  
    'Trump': {'age': 10, 'sex': '1'},
})

print(d)
print(d.to_json())