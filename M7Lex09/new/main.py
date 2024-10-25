from Date import Date
from AmericanDate import AmericanDate
from Calendar import Calendar

normal_date = Date(15, 11, 1897)
american_date = AmericanDate(15, 11, 1897)
calendar = Calendar()

calendar.showDate(normal_date)
calendar.showDate(american_date)