import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_key = ""
news_key = ""

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_key,
}
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
r = requests.get(STOCK_ENDPOINT, params=parameters)
data = r.json()

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
closing_stock_list = [value['4. close'] for (key,value) in data['Time Series (Daily)'].items()]
yesterday_stock = float(closing_stock_list[0])
before_yesterday_stock = float(closing_stock_list[1])
print(yesterday_stock)
print(before_yesterday_stock)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = yesterday_stock - before_yesterday_stock
increase_decrease = None
if difference > 0:
    increase_decrease = "▲"
else:
    increase_decrease = "▼"

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / yesterday_stock) * 100)
print(diff_percent)

# If percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 5.0:
    print("Get News")

    # Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": news_key,
        "sortBy": "relevancy"
    }
    news_res = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_data = news_res.json()["articles"]

    top_3_news = news_data[:3]  # Use Python slice operator to create a list that contains the first 3 articles.
    news_list = [
        f"{STOCK_NAME}: {increase_decrease}{diff_percent}% \nHeadline: {article["title"]} \nBrief: {article["description"]}"
        for article in top_3_news]
    print(news_list)

else:
    print("Small percentage")

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 


#TODO 9. - Send each article as a separate message via Twilio. 


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

