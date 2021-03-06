# django-model-auditor

django-model-auditor is a Python library for maintaining versions of your django model instances.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install django-model-auditor
```

## Usage
1. Add audits in INSTALLED_APPS inside settings.py of your django project 
```python
INSTALLED_APPS = [
    'audits.apps.AuditsConfig',
]
```
2. run migration to create auditlog model
```python
python manage.py migrate
```

3. Change metaclass of model(for which audit logs are needed) to ModelHistoryMeta
```python
from audits.models import ModelHistoryMeta
from django.db import models

class ExampleModel(models.Model, metaclass=ModelHistoryMeta):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
```

4. Example
```python
import ExampleModel
object = ExampleModel(field1="foo", field2="bar")
object.save() #will create an entry in auditlog model

object.field1 = "Foo"
object.field2 = "Bar"
object.save() #will create another entry in auditlog model

object.field1 = "FOO"
object.field2 = "BAR"
object.save() #will create another entry in auditlog model

#To get previous versions of the object 
previous_versions = AuditLog.get_prev_versions(object, limit=2)

#By default get_prev_versions return only last_prev_version to 
#get more versions we need to specify limit

latest_prev_version = previous_versions[0]
print("%s %s"%(latest_prev_version.field1, latest_prev_version.field2)) # "Foo","Bar"


prev_to_prev_version = previous_versions[1]
print("%s %s"%(prev_to_prev_version.field1, prev_to_prev_version.field2)) # "foo","bar"

```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
