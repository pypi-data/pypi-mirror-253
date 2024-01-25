from pprint import pprint

def test_get_students(hh_client, test_data):
    response = hh_client.clients.get_students(term='79226036452', by_agents=False)
    pprint(response)
