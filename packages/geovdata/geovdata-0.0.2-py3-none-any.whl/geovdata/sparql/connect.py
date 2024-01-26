from . import globals


def connect_external(url: str, verbose: bool = True) -> None:
    """Connect to an external SPARQL endpoint."""
    globals.url = url
    if verbose:
        print(f">> External SPARQL URL set to <{url}>")
    
    # Temp
    print('SPARQL URL:', url)


def connect_geovistory(pk_project: int = -1) -> None:
    """Connect to Geovistory correct SPARQL endpoint."""

    if  pk_project == -1:
        path = "https://sparql.geovistory.org/api_v1_community_data"
    else:
        path = f"https://sparql.geovistory.org/api_v1_project_{pk_project}"

    globals.url = path
    print(f">> SPARQL endpoint of Geovistory project {'COMMUNITY' if pk_project == -1 else pk_project} set.")
