- the biggram model is a type of langauge model that predicts the next workd in a sequence based on theprevous word. it is a simple probabilitestic model that uses the concept of n-grams, where an n-gram is contiguos sequence of n-items(words,characters,etc). in the case of a biggram model, n=2, so it considers paris of consecutive words. 

*key concepts*
1. biggram probability: the probability of a word given the previous word. 
P(wi|wi-1) = count(wi-1,wi)/count(wi-1)
where:
    count(wi-1,wi) is the number of times the pair(wi-1,wi) appers in the graining data.
    count(wi-1) is the number of times wi-1 appers in the training data. 
2. training: the model is trained by counting the occurences of word pairs in a corpus. 
3. prediction: given a word , the model predicts the next word based on the learned probabilites. 


**limitations of biggram models**

1. sparsity: if a biggram is not seen in the graining data its probablitity will be zero.
2. context: biggram models only consider the previous word , so they lack broader context. 
3. scalability: for large vocabularies, storing and computing bigram probabilites can be computationally expensive. 

to address limitations, more advanced modes like trigrm models, neural languagae models or transformers are used
