def calc_readtime(response):

    texts = response.xpath("//div[@id='docs-content']//text()").extract()
    clean_texts =" ".join(texts).strip().split("\n")
    words = " ".join(clean_texts).strip()
    words = words.replace("|", "").replace("  ","")
    new_words = words.split(" ")
    words_per_minute = 200
    readtime = len(new_words)/ words_per_minute

    return readtime