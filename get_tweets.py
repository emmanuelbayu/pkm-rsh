import twint
import nest_asyncio
import threading
nest_asyncio.apply()

def get_tweet(start_date, end_date, search, output_file):
    c = twint.config()
    c.Search = search
    c.Since = start_date
    c.Until = end_date
    c.Store_csv = True
    c.Output = output_file
    twint.run.Search(c)

start_date = ["2021-1-1", "2021-1-1"]
end_date = ["2021-3-31", "2021-3-31"]
search = ["@jokowi", "@dpr_ri"]
output = ["tweet_jokowi.csv", "tweet_dpr.csv"]
threads = []

for i in range(2):
    t = threading.Thread(target=get_tweet, args=[start_date[i], end_date[i], search[i], output[i]])
    t.start()
    threads.append(t)

for t in threads:
    t.join()