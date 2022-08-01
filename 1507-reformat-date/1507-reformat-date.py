class Solution:
    def reformatDate(self, date: str) -> str:
        
        # split the date by space
        # res = [], going to join it at the end "-"
        
        # year -> just split[-1]
        # month -> hashmap to map each Month to a number string
        # day -> strip the last chars of the day, if len() < 2, append a '0' to the front of it
        months = {
            'Jan' : '01',
            'Feb' : '02',
            'Mar' : '03',
            'Apr' : '04',
            'May' : '05',
            'Jun' : '06',
            'Jul' : '07',
            'Aug' : '08',
            'Sep' : '09',
            'Oct' : '10',
            'Nov' : '11',
            'Dec' : '12',
        } 
        res = []
        day, month, year = date.split(' ')
        res.append(year)
        res.append(months[month])
        
        # day
        string_date = day[:-2]
        if len(string_date) < 2:
            string_date = '0' + string_date
        
        res.append(string_date)
        return "-".join(res)
        
        