from jokeapi import Jokes

async def GetJoke(filters, user):

    j = await Jokes()

    if filters:
        filters = filters.replace(" ", "")
        try:
            jk = await j.get_joke(category=[filters])
        except Exception as e:
            try:
                jk = await j.get_joke(search_string=filters)
            except Exception:
                return "Something went wrong !"
    else:
        jk = await j.get_joke()

    try:
        
        if jk["type"] == "single":
            return jk["joke"]
        else:
            return jk["setup"] + "\n" + jk["delivery"]

    except Exception:
        return "Found nothing :(, sorry !"