import wikipedia
from bs4 import BeautifulSoup
from utils import consoledebug_return as Debug

def main(query:str="The thing you want to search", username="Unknown"):

    if(not query):
        return "Search something, not the void :joy:"
    
    print(Debug.Info("User " + username + " used wiki command, input: " + query))

    output = ""
    results = wikipedia.search(query)
    count = 0

    print("    " + Debug.DuringOperation("Searching pages"))

    for result in results:
        count += 1

    try:
        if count > 1:
            print("    " + Debug.Warn("More than one result found"))
            print("        " + Debug.DuringOperation("Taking the first one"))
            output += "\nMore than one result found, taking the first one..."
            print(Debug.DuringOperation("Fetching the page content..."))
            page = wikipedia.page(title=results[0], auto_suggest=False)
            pageContent = (page.content[:500] + "...") if len(page.content) > 500 else page.content
            print(Debug.DuringOperation("Formatting output"))
            output += ("\n\n    ***__" + page.title + "__***\n" + str(pageContent) + "\n<" + page.url + ">").replace("==","    **")
            output += "\n\nFrom Wikipedia, the free encyclopedia"
        else:
            print("    " + Debug.DuringOperation("Fetching the page content..."))
            page = wikipedia.page(title=query, auto_suggest=False)
            pageContent = (page.content[:500] + "...") if len(page.content) > 500 else page.content
            print("    " + Debug.DuringOperation("Formatting output"))
            output += ("\n\n    ***__" + page.title + "__***\n" + str(pageContent) + "\n<" + page.url + ">").replace("==","    **")
            output += "\n\nFrom Wikipedia, the free encyclopedia"

    except wikipedia.exceptions.PageError:
        return "Oops ! looks like i found nothing for " + query
    except wikipedia.exceptions.DisambiguationError as e:
        return e
    except KeyError:
        return "Oops! looks like i found nothing for " + query
    
    print(Debug.Success("Wikipedia page found and returned successfully !"))
    return output