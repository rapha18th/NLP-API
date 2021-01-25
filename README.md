# Repository for the NLP-Planet postman workspace

## Simple NLP Collection
Example:
[![Screenshot-2021-01-25-at-23-02-16.png](https://i.postimg.cc/2ynPsxgp/Screenshot-2021-01-25-at-23-02-16.png)](https://postimg.cc/XB7HF9Vx)

### Number of tokens
GET `https://nlpcol.herokuapp.com/api/v1/tokens/{mytext}`

### Lemmatization
GET `https://nlpcol.herokuapp.com/api/v1/lemma/{mytext}`

### Named entities
GET `https://nlpcol.herokuapp.com/api/v1/ner/{mytext}`

### Sentiment
GET `https://nlpcol.herokuapp.com/api/v1/wiki_sentiment/{mytext}`

## Wikipedia NLP Collection
Example:
[![Screenshot-2021-01-25-at-23-06-35.png](https://i.postimg.cc/SK53j5hF/Screenshot-2021-01-25-at-23-06-35.png)](https://postimg.cc/d724x534)

### summary of wikipedia page
GET `https://nlpcol.herokuapp.com/api/v1/wiki_summary/{mytext}`

### Return the whole content of a wikipedia page
GET `https://nlpcol.herokuapp.com/api/v1/wiki_content/{mytext}

### List the images urls of a wikipedia page
GET `https://nlpcol.herokuapp.com/api/v1/wiki_img/{mytext}`

### Named entities of the content of a wikipedia page
GET `https://nlpcol.herokuapp.com/api/v1/wiki_ner/{mytext}`

### Sentiment of the content of a wikipedia page
GET `https://nlpcol.herokuapp.com/api/v1/wiki_sentiment/{mytext}`



