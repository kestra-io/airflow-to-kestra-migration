def _get_astronauts(ti=None):
    import requests

    r = requests.get("http://api.open-notify.org/astros.json")
    r.raise_for_status()
    number_of_people_in_space = r.json()["number"]
    list_of_people_in_space = r.json()["people"]

    ti.xcom_push(key="number_of_people_in_space", value=number_of_people_in_space)

    return [[item] for item in list_of_people_in_space]
