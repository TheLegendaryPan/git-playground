from datetime import datetime, date
import dateutil.parser
class ViewModel:

    current_date = str(date.today())
    #current_date = '2020-07-28'
    current_date1 = "2020-07-28T14:56:22.343Z"

    print("curr date:", current_date)
    print("utc date:", current_date1)

    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def to_do_items(self):
        return [item for item in self._items if item.status == "To Do"]
        
    @property
    def doing_items(self):
        return [item for item in self._items if item.status == "Pending"]

    @property
    def done_items(self):
        return [item for item in self._items if item.status == "Done"]

    @property
    def show_recent_done(self):
       #return [item for item in self.done_items if item.update_time == self.current_date1 ] ##works if current_date is hardcodes
       #return [item for item in self.done_items if datetime.date(parser.parse(item.update_time)) == self.current_date #nothing returns
       #return [item for item in self.done_items if datetime.datetime.date(parse.parse(item.update_time)) == self.current_date ] ## nothing comes back??
       #d2 = datetime.strftime(dateutil.parser.parse("2007-03-04T21:08:12"), "%Y-%m-%d") this converts fine to just date
       #d3 = datetime.strftime(datetime.strptime('2012-03-01T10:00:00Z','%Y-%m-%dT%H:%M:%SZ'), "%Y-%m-%d") -- WORKS but need to convert
       #return [item for item in self.doing_items if datetime.strftime(datetime.strptime(item.update_time,'%Y-%m-%dT%H:%M:%S.%fZ'), "%Y-%m-%d") == self.current_date ] ## THIS ALSO WORKS!
       return [item for item in self.done_items if datetime.strftime(datetime.strptime(item.update_time,'%Y-%m-%dT%H:%M:%S.%fZ'), "%Y-%m-%d") == self.current_date ] ## THIS WORKS!
           

