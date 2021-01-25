# Repository for the NLP-Planet postman workspace

## Simple NLP Collection
Example:
[![Screenshot-2021-01-25-at-23-02-16.png](https://i.postimg.cc/2ynPsxgp/Screenshot-2021-01-25-at-23-02-16.png)](https://postimg.cc/XB7HF9Vx)

### number of tokens
GET `https://nlpcol.herokuapp.com/api/v1/tokens/{mytext}`

### lemmatization
GET `https://nlpcol.herokuapp.com/api/v1/lemma/{mytext}`

### named entities
GET `https://nlpcol.herokuapp.com/api/v1/ner/{mytext}`

### sentiment
GET `https://nlpcol.herokuapp.com/api/v1/wiki_sentiment/{mytext}`

### word cloud
GET `https://nlpcol.herokuapp.com/api/v1/wordcloud/{mytext}`

## Wikipedia NLP Collection
Example:
[![Screenshot-2021-01-26-at-00-51-38.png](https://i.postimg.cc/sg7gPvy1/Screenshot-2021-01-26-at-00-51-38.png)](https://postimg.cc/HrWmdWrC)

### summary of wikipedia page
GET `https://nlpcol.herokuapp.com/api/v1/wiki_summary/{mytext}`

### returns the whole content of a wikipedia page
GET `https://nlpcol.herokuapp.com/api/v1/wiki_content/{mytext}`

### list the images urls of a wikipedia page
GET `https://nlpcol.herokuapp.com/api/v1/wiki_img/{mytext}`

### named entities of the content of a wikipedia page
GET `https://nlpcol.herokuapp.com/api/v1/wiki_ner/{mytext}`

### sentiment of the content of a wikipedia page
GET `https://nlpcol.herokuapp.com/api/v1/wiki_sentiment/{mytext}`

### wikipedia word cloud
GET `https://nlpcol.herokuapp.com/api/v1/wiki_wordcloud/{mytext}`



