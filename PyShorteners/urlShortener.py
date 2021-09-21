from pyshorteners import Shortener

# Do generate your own api key

api_key = ""
obj = Shortener(api_key = api_key)

# Url Shortening
def Url_Shortener(longUrl):
    shortUrl = obj.bitly.short(longUrl)
    return shortUrl

# Original url
def Og_url(shortUrl):
    longUrl = obj.bitly.expand(shortUrl)
    return longUrl

sample = input("Enter the url")
output = Url_Shortener(sample)
print(output)
print(Og_url(output))

