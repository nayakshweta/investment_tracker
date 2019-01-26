import urllib, re
from django.core.management import BaseCommand
from investapp.models import Scheme, DailyNAV, TotalInvestment, HoldingInvestment
from datetime import datetime

class Command(BaseCommand):

    def handle(self, *args, **option):
        todays_nav = urllib.urlopen("https://www.amfiindia.com/spages/NAVAll.txt")
        print "nav saved!!!"
        #self.parse_nav(todays_nav)
        self.calc_total_inv() 

    def parse_nav(self, todays_nav):
        for line in todays_nav:
            try:
                regex_str = ('(?P<scheme_code>[0-9]+)\;'
                '(?P<isin_div_payout>[A-Z0-9-]+)\;'
                '(?P<isin_div_reinvestment>[A-Z0-9-]+)\;'
                '(?P<scheme_name>[^;]+)\;'
                '(?P<navalue>[0-9.]+)\;'
                '(?P<repurchase_price>[0-9.]+)\;'
                '(?P<sale_price>[0-9.]+)\;'
                '(?P<date_of_nav>[0-9\-A-Za-z]+)')
                
                entry = re.match(pattern=regex_str, string=line.strip())

                if entry:
                    # print entry.group('scheme_code', 'scheme_name', 'navalue', 'date_of_nav')
                    self.add_to_db(entry)
            except:
                pass

    def add_to_db(self, entry):

        entry_scheme_code = int(entry.group('scheme_code'))
        entry_scheme_name = entry.group('scheme_name')
        entry_date_str = entry.group('date_of_nav')
        entry_date = datetime.strptime(entry_date_str, "%d-%b-%Y")
        
        entry_nav = float(entry.group('navalue'))

        fund, created = Scheme.objects.get_or_create(
            scheme_code=entry_scheme_code, 
            defaults={'scheme_name':entry_scheme_name},
            )

        daily_nav_object, created2 = DailyNAV.objects.get_or_create(
            scheme=fund,
            date=entry_date,
            defaults={'asset_value':entry_nav},
            )
        print daily_nav_object, created2
    

    def calc_total_inv(self):
        # For each scheme that I am holding:
        #     Step 1: Get the latest NAV for the holding.   
        #     Step 2; Get the total number of units for the holding
        #     Step 3: today's value = latest_nav * total no of units
        

        Step 1: 



DailyNAV.objects.filter(scheme=h.scheme).latest('date')
