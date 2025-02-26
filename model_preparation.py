import spacy
from spacy.tokens import DocBin
from tqdm import tqdm

nlp=spacy.blank("en")
db=DocBin()
import json
f=open("annotations.json")
Train_Data=json.load(f)
for text,annot in tqdm(Train_Data['annotations']):
    doc=nlp.make_doc(text)
    ents=[]
    for start, end, label in annot['entities']:
        span=doc.char_span(start, end, label=label,alignment_mode='contract')
        if span is None:
            print('skipping entity')
        else:
            ents.append(span)
    doc.ents=ents
    db.add(doc)
db.to_disk("supervised_learning.spacy")
