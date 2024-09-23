

def extract_title(markdown: str) -> str:
    """pulls the h1 header from the markdown passed to the function.
    if there is no h1 header, an exception is raised.

    Args:
        markdown (str): markdown formated string
        
    Raises:
        ValueError: No title header found in passed arg.
        
    Returns:
        str: the h1 header text without the #  or leading white space.
    """
    lines = markdown.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            return line[2:]
    raise ValueError("Error: No title header found.")