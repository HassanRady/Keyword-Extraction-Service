import yake

kw_extractor = yake.KeywordExtractor()

# def preprocess(json_data):
#   text = json_data['text']
#   return " ".join(text)


def extract_keywords(text: str) -> list:
    return kw_extractor.extract_keywords(text)


def reform_output(keywords: list) -> list:
    return [keyword for keyword, score in keywords]


def pipeline(text: str) -> dict[str, list[str]]:
    keywords = extract_keywords(text)[:]
    keywords = reform_output(keywords)
    return {"output": keywords}


if __name__ == "__main__":
    docs = [
        """
  When it comes to evaluating the performance of keyword extractors, you can use some of the standard metrics in machine learning: accuracy, precision, recall, and F1 score. However, these metrics don’t reflect partial matches; they only consider the perfect match between an extracted segment and the correct prediction for that tag.
  Fortunately, there are some other metrics capable of capturing partial matches. An example of this is ROUGE.
  """
    ] * 1000

    keywords = pipeline(docs[0])

    print(keywords)
