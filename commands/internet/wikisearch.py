from tkinter import E
import wikipedia

def main(query:str="The thing you want to search"):
    if(query == ""):
        return "Search something, not the void :joy:"
    output = ""
    results = wikipedia.search(query)
    count = 0
    for result in results:
        count += 1

    try:
        if count > 1:
            output += "\nMore than one result found, taking the first one..."
            page = wikipedia.page(title=results[0], auto_suggest=False)
            pageContent = (page.content[:500] + "...") if len(page.content) > 1500 else page.content
            output += ("\n\n    ***__" + page.title + "__***\n" + str(pageContent) + "\n<" + page.url + ">").replace("==","    **")
        else:
            page = wikipedia.page(title=query, auto_suggest=False)
            pageContent = (page.content[:500] + "...") if len(page.content) > 1500 else page.content
            output += ("\n\n    ***__" + page.title + "__***\n" + str(pageContent) + "\n<" + page.url + ">").replace("==","    **")
    except wikipedia.exceptions.PageError:
        return "Oops ! looks like i found nothing for " + query
    except wikipedia.exceptions.DisambiguationError as e:
        return e
    except KeyError:
        return "Oops! looks like i found nothing for " + query
        
    return output