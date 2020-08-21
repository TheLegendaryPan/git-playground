from datetime import datetime, date, timedelta
import dateutil.parser

now = datetime.now()
current_date = now.strftime("%D")
current_date1 = "2020-07-28T14:56:22.343Z"

T_2_time = date.today() - timedelta(days = 2)
print("T_2_time is: ", T_2_time)

#return [item for item in self.done_items if datetime.datetime.date(parser.parse(item.update_time)) == self.current_date ]
#return [item for item in self.done_items if item.update_time == self.current_date1 ] ##works if current_date is hardcodes
#return [item for item in self.done_items if datetime.date(parser.parse(item.update_time)) == self.current_date #nothing returns
#return [item for item in self.done_items if datetime.datetime.date(parse.parse(item.update_time)) == self.current_date ] ## nothing comes back??
     
a=dateutil.parser.parse("2007-03-04T21:08:12")
print(a)

d1 = a.strftime("%Y-%m-%d")

print(d1)

d2 = datetime.strftime(dateutil.parser.parse("2007-03-04T21:08:12"), "%Y-%m-%d")

print(d2)

d3 = datetime.strftime(datetime.strptime('2020-07-28T14:56:22.343Z','%Y-%m-%dT%H:%M:%S.%fZ'), "%Y-%m-%d")

print(d3)

from datetime import date

today = date.today()
print("Today's date:", today)


list_of_items = [0,1,2,3,4,5]

def blah():
    count_of_list = len(list_of_items)
    print("List of list is: " + str(count_of_list))
#    if count_of_list == 6:
#       return list_of_items[0:4]
    if count_of_list <= 6:
        return list_of_items
   # return list_of_items[0:4]



print(list_of_items[0:4])
print(len(list_of_items))
a = blah()
print(a)
