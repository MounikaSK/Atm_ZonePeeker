import sys

# Get the search query from command-line arguments
search_query = sys.argv[1:]
print(search_query)

# Your Python function here
def process_search_query(search_query):
    # Your processing logic here
    print("URL from python file: ",search_query)
    return f"Processed URL: {search_query}"

result = process_search_query(search_query)
print("Generated Captions: ",result)
