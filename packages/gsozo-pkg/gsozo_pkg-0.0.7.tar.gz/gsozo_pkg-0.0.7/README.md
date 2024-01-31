# Grupo sozo Package

Set of python modules to implements or extend interfaces, like: extend pipedrive or mailchimp (third party module)


# gsozo_pkg
![](https://img.shields.io/badge/version-0.7.1-success) ![](https://img.shields.io/badge/Python-%203.8%20|%203.9%20|%203.10%20-4B8BBE?logo=python&logoColor=white)
<br />*gsozo_pkg* is an API wrapper for [Pipedrive](https://www.pipedrive.com/) written in Python.

## Installing
```
pip install gsozo-pkg
```

## Usage

### Using this library with API Token

#### Client instantiation
```python
from gsozo_pkg.pipedrive import Client

client = Client("CLIENT_ID", "CLIENT_TOKEN")
```

### Activities 

API docs: https://developers.pipedrive.com/docs/api/v1/Activities

#### Get all activity types
```python
response = client.activities.get_activity_types()
```

### Deals

API docs: https://developers.pipedrive.com/docs/api/v1/Deals <br />
API docs: https://developers.pipedrive.com/docs/api/v1/DealFields

#### Get one deal field
```python
response = client.deals.get_deal_one_field('FIELD_ID')
```

#### Update a deal field
```python
data = {
    'id': ''
}
response = client.deals.update_deal_field('FIELD_ID', data)
```

#### Delete a participant from a deal
```python
response = client.deals.delete_participant_to_deal_by_person_id('DEAL_ID', 'PERSON_ID')
```

### Organizations

API docs: https://developers.pipedrive.com/docs/api/v1/Organizations

#### Add a follower to an organization
```python
response = client.organizations.add_follower_to_organization('ORGANIZATION_ID', 'USER_ID')
```

### Persons 

API docs: https://developers.pipedrive.com/docs/api/v1/Persons

#### Get all persons
```python
response = client.persons.get_all_persons('*ARGS', 'PAGINATION_ON' = TRUE)
```

#### List activities associated with a person
```python
response = client.persons.get_person_activities('PERSON_ID')
```

#### List files attached to a person
```python
response = client.persons.get_person_attaches('PERSON_ID')
```

#### List mail messages associated with a person
```python
response = client.persons.get_person_emails('PERSON_ID')
```

#### List followers of a person
```python
response = client.persons.get_person_followers('PERSON_ID', 'PAGINATION_ON' = TRUE)
```

#### Add a follower to a person
```python
response = client.persons.add_follower_to_person('PERSON_ID', 'USER_ID')
```

#### Delete a follower from a person
```python
response = client.persons.delete_follower_to_person('PERSON_ID', 'USER_ID')
```

#### Merge two persons
```python
response = client.persons.merge_two_persons('PERSON_TO_KEEP', 'PERSON_TO_OVERWRITE')
```

### PersonFields 

API docs: https://developers.pipedrive.com/docs/api/v1/PersonFields

#### Get one person field
```python
response = client.persons.get_person_one_field('FIELD_ID')
```

#### Update a person field
```python
data = {
    'id': ''
}
response = client.persons.update_person_field('FIELD_ID', data)
```

For additional information or access to other endpoints within the same API structure, refer to the library used as a template for building this one [pipedrive-python-lib](https://github.com/GearPlug/pipedrive-python).
