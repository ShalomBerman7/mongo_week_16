from connection import collection, serialize_docs


def get_engineering_high_salary_employees():
    query = {'salary': {"$gt": 65000},
             'job_role.department': 'Engineering'}
    projection = {'_id': 0,
                  'employee_id': 1,
                  'name': 1,
                  'salary': 1}
    documents = collection.find(query, projection)
    return serialize_docs(documents)


def get_employees_by_age_and_role():
    query = {'age':
                 {"$gte": 30, "$lte": 45},
             'job_role.title':
                 {"$in": ["Engineer", "Specialist"]}}
    projection = {'_id': 0}
    documents = collection.find(query, projection)
    return serialize_docs(documents)


def get_top_seniority_employees_excluding_hr():
    query = {'job_role.department': {"$ne": "HR"}}
    projection = {'_id': 0}
    documents = collection.find(query, projection).sort({"years_at_company": -1}).limit(7)
    return serialize_docs(documents)


def get_employees_by_age_or_seniority():
    query = {"$or": [
        {"age": {"$gte": 50}},
        {"years_at_company": {"lte": 3}}
    ]}
    projection = {'_id': 0,
                  'employee_id': 1,
                  'name': 1,
                  'age': 1,
                  'years_at_company': 1}
    documents = collection.find(query, projection)
    return serialize_docs(documents)


def get_managers_excluding_departments():
    query = {'job_role.title': 'Manager',
             'job_role.department': {"$nin": ['Sales', 'Marketing']}}
    projection = {'_id': 0}
    documents = collection.find(query, projection)
    return serialize_docs(documents)


def get_employees_by_lastname_and_age():
    query = {"$and": [
        {"name": {"$regex": "Nelson|Wright"}},
        {"age": {"$lte": 35}}
    ]}
    projection = {'_id': 0,
                  'name': 1,
                  'age': 1,
                  'job_role.department': 1}
    documents = collection.find(query, projection)
    return serialize_docs(documents)
