from schedule import Schedule
from contact_actions import *

schedule = Schedule()
schedule.perform_action(AddContact(name="Guilherme", phone_number="12345"))
schedule.perform_action(AddContact(name="Gu", phone_number="67890"))
schedule.perform_action(AddContact(name="Kendy", phone_number="54321"))
schedule.perform_action(DisplaySchedule())
schedule.perform_action(RemoveContact(name="Kendy"))
schedule.perform_action(DisplaySchedule())
print(schedule.perform_action(SearchByInitial(initial="G")))