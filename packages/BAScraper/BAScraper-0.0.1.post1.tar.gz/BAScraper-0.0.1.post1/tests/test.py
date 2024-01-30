from BAScraper.BAScraper import Pushpull

import json
from datetime import datetime

pp = Pushpull(sleepsec=2, threads=2)
result = pp.get_submissions(after=datetime(2023, 1, 1), before=datetime(2023, 1, 2),
                            subreddit='bluearchive', sort='asc', get_comments=False)

# [print(v['created_utc']) for _, v in result.items()]

# save result as JSON
with open("../example.json", "w", encoding='utf-8') as outfile:
    json.dump(result, outfile, indent=4)