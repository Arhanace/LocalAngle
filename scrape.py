import newspaper
import json
import datetime
import jsonpickle
import nltk
from newspaper import news_pool
from newspaper import Source
from newspaper import Config
from time import sleep
from tqdm import tqdm
from json import JSONEncoder


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent

config.request_timeout = 10

begin_time = datetime.datetime.now()

sources = {
#National Outlets
'ABC News': 'https://abcnews.go.com',
'CBS News': 'https://cbsnews.com',
'NBC News': 'https://nbcnews.com',
'NPR': 'https://npr.org',
'The Hill': 'https://thehill.com',
'The Atlantic': 'https://theatlantic.com',
'Bloomberg': 'https://bloomberg.com',
'The Guardian': 'https://theguardian.com',
'Newsweek': 'https://newsweek.com',
'Associated Press': 'https://ap.org',
'CNN': 'https://cnn.com',
'USA Today': 'https://usatoday.com',
'New York Times': 'https://nytimes.com',
'Washington Post': 'https://washingtonpost.com',
'Wall Street Journal': 'https://wsj.com',
'Huffington Post': 'https://huffpost.com',
'Fox News': 'https://foxnews.com',
'Forbes': 'https://forbes.com',
'Politico': 'https://politico.com',
'Today': 'https://today.com',
'Vox': 'https://vox.com',
'Time': 'https://time.com',
'Slate': 'https://slate.com',
'MSNBC': 'https://msnbc.com',
'The New Yorker': 'https://newyorker.com',
'Salon': 'https://salon.com',


# #Large Local Outlets
'LA Times': 'https://latimes.com',
'Chicago Tribune':'https://chicagotribune.com',
'Tampa Bay Times': 'https://tampabay.com',
'Star Tribune': 'https://startribune.com',
'Houston Chronicle': 'https://houstonchronicle.com',
'Arizona Republic': 'https://azcentral.com',
'San Francisco Chronicle': 'https://www.sfchronicle.com',
'Boston Globe': 'https://www.bostonglobe.com',

# #Sports
'ESPN': 'https://espn.com',
'Bleacher Report': 'https://bleacherreport.com',
'Sports Illustrated': 'https://si.com',
'The Ringer': 'https://theringer.com'
}

papers = []
print()
print()
print()
print('Building Source Set....')
for site in tqdm(sources):
	papers.append(newspaper.build(sources[site], memoize_articles=False))



#Create Sources
print()
print("Gathering and Downloading Articles....")
news_pool.set(papers, threads_per_source=10)
news_pool.join()

num_articles = 0
indx = 0

for p in papers:
	num_articles += p.size()
	print(list(sources.keys())[indx] + ": " + str(p.size()))
	indx += 1

print()
print ('Total Articles: ' + str(num_articles))
print(' ')
print('Time to Scrape: ' + str(datetime.datetime.now() - begin_time))
print()


begin_time2 = datetime.datetime.now()
print()
print("Parsing Articles....")



ALL_STORIES = {}
source_indx = 0

for source in papers:

	source_articles = []
	print(list(sources.keys())[source_indx] + " Articles:")
	
	for article in tqdm(source.articles):
		try:	
			article.download()
			article.parse()
			article.nlp()

			s = {
			'Title': str(article.title),
			'Authors': list(article.authors),
			'Date': str(article.publish_date),
			'Text': str(article.text),
			'Summary': str(article.summary),
			'URL': str(article.url),
			'Keywords': list(article.keywords)
			}


			source_articles.append(s)
		except:
			pass

	ALL_STORIES[list(sources.keys())[source_indx]] = source_articles
	source_indx += 1

	json_data = json.dumps(ALL_STORIES, indent = 4, ensure_ascii=False)

	with open("articles.json", "w") as outfile:
		outfile.write(json_data)





print('Time to Parse: ' + str(datetime.datetime.now() - begin_time2))
