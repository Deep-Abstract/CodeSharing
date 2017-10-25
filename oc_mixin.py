# Configuration
src = "/home/hz/Desktop/lem/mode5100l.w2c"

# Import
import numpy as np
import sys
from gensim.models import Word2Vec

try:
    eval("Model")
except:
    Model = Word2Vec.load(src)


def W2CGetter(model):
    def _f(str):
        if str in model:
            return model[str]
        elif f"DBPEDIA_ID/{str}" in model:
            return model[f"DBPEDIA_ID/{str}"]
        else:
            return np.zeros((model.vector_size,))

    return _f


W2C = W2CGetter(Model)


def stream2dict(stream):
    dic = dict()
    for srcs in stream:
        ontologies = [filename[:-len(".csv")] for filename in stream.now]
        for ontology, src in zip(ontologies, srcs):
            dic[ontology] = src
    return dic


def get_neg(dic: dict):
    def getter(ontologies, N):
        sources = np.hstack([list(src.entity) for ontology, src in dic.items() if ontology not in ontologies])
        rndIndices = np.random.permutation(N)
        return np.take(sources, rndIndices)

    return getter
