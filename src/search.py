from duckduckgo_search import DDGS


def search_web(sport, max_results=3):
    """Search the web for recent information about the selected sport."""
    query = f"{sport} latest news recent matches tournament updates"

    try:
        results = DDGS().text(query, max_results=max_results)

        snippets = []

        for result in results:
            title = result.get("title", "")
            body = result.get("body", "")
            snippets.append(f"{title}: {body}")

        return "\n".join(snippets)

    except Exception as e:
        return f"Web search unavailable: {e}"


if __name__ == "__main__":
    print(search_web("Cricket"))