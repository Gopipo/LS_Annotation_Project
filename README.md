# LS Annotation Project

Run dir2jsonl.py once to prepare images and text for prodigy:

```
python3 dir2jsonl.py
```
You may specify the image & text directories as well as the outfile as follows:
```
python3 dir2jsonl.py -i ./Corpora/images_webcorpus/ -t ./Corpora/tokenized_txt_files/tokenized_ -o imageTextPaired.jsonl
```

To use prodigy to start annotating call:
```
python3 -m prodigy image.caption-text-align my_database ./corpora/JSON/imageTextPaired.jsonl -F AnnotationInterface_ImageCaptionAndTextAlign.py
```
