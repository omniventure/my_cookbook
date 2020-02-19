try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

query = input("What do you want to search for? ")

search_results = []

for i in search(query,      # Your Query
                tld='com',  # Top Level Domain
                lang='en',  # Language
                num=10,     # Number of results per page
                start=0,    # First results to retrieve
                stop=None,  # Last result to retrieve
                pause=2.0   # Lapse between HTTP requests
                ):
    search_results.append(i)
    print(i)
