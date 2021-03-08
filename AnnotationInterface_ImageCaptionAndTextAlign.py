#!/usr/bin/python3
# -*- coding: utf-8 -*-

import prodigy
import spacy
from prodigy.components.loaders import JSONL, Images
from prodigy.components.preprocess import fetch_images, add_tokens

@prodigy.recipe(
    "image.caption-text-align",
    dataset=("The dataset to use", "positional", None, str),
    sourcefile=("The file containing text and image paths", "positional", None, str)
    )

def image_caption_text_align(dataset: str, sourcefile: str):
    """Stream in images and corresponding text.
    """
    nlp = spacy.load("de_core_news_sm")

    stream = JSONL(sourcefile)
    stream = fetch_images(stream)
    stream = add_tokens(nlp, stream)


    blocks = [
        {"view_id": "image_manual"},
        {"view_id": "text_input",
            "field_id": "caption",
            "field_rows": 4,
            "field-autofocus": True},
        {"view_id": "ner_manual"}
    ]
    return {
        "dataset": dataset,
        "stream": stream,
        "view_id": "blocks",
        "config": {"blocks": blocks,
            "lang": nlp.lang,
            "labels": ["current image"],
            "image_manual_spans_key": "image_spans"
        }
    }
