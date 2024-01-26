from pprint import pprint
from datetime import datetime, timedelta

def test_get_students(hh_client, test_data):
    response = hh_client.clients.get_students(term='9504432757', by_agents=False).students
    response1 = hh_client.ed_unit_students.get_students(student_client_id=response[-1].client_id, query_days=True)
    res = list(filter(lambda group: group.end_date >= datetime.now(), response1))
    res1 = hh_client.ed_unit_students.get_students(student_client_id=response[-1].client_id, ed_unit_id=res[-1].ed_unit_id, query_days=True, date_from=datetime.now() - timedelta(days=60), date_to=res[-1].end_date)[-1]
    days = res1.days
    days = list(filter(lambda day: day.date <= datetime.now() and day.pass_ and day.accepted , days))

    # eds = hh_client.ed_units.get_ed_units(id=res[-1].ed_unit_id, query_days=True)
    # print(days[-1].date.year)
    print(res1.ed_unit_name, res1.ed_unit_office_or_company_name)
    pprint(days[-1].date.strftime('%m–%d–%Y'))
