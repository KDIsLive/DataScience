# from langchain_community.document_loaders import TextLoader
# loader = TextLoader("sample.txt", encoding="utf-8")
# txt = loader.load()
# print(txt)


from langchain_community.document_loaders import WebBaseLoader

def writeTxtLoader():
    """Load a web page and extract text content."""
    loader = WebBaseLoader(web_path = "https://www.linkedin.com/in/devendra-kushwaha-4a681937/",
                       bs_kwargs = '{"parse_only":bs4.SoupStrainer(class_="t-14")}')
    txt = loader.load()
    print(txt)
