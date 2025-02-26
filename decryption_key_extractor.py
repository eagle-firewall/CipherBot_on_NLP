import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
nlp=spacy.blank("en")
db=DocBin()
import json
f=open('annotations.json')
train_data=json.load(f)
for text, annot in tqdm(train_data['annotations']):
    doc=nlp.make_doc(text)
    ents=[]
    for start, end, label in annot['entities']:
        span=doc.char_span(start, end, label=label, alignment_mode='contract')
        if span is None:
            print('skipping entity')
        else:
            ents.append(span)
        doc.ents=ents
        db.add(doc)
    db.to_disk('./training_data.spacy')
    