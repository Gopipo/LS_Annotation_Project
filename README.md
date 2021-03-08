# LS Annotation Project

Before running dir2jsonl.py once to prepare images and text for prodigy, make sure that your corpus directory structure is as follows:
Images:
e.g. .\Corpora\images_webcorpus\images_html\images_html_monolingual
Text:
e.g. .\Corpora\tokenized_txt_files\tokenized_monolingual
If not, adjust the for-loops following the #@CHECK_STRUCTURE marker.

You may specify the image & text directories as well as the outfile by either:
1. changing the paths within the code at positions following the #@CHECK_PATH marker
2. calling the function with the optional parameters: -i or --imgdir; -t or --txtdir; -o or --outfile
```
python3 dir2jsonl.py


python3 dir2jsonl.py -i ./Corpora/images_webcorpus/ -t ./Corpora/tokenized_txt_files/tokenized_ -o imageTextPaired.jsonl
```

To use prodigy to start annotating call:
```
python3 -m prodigy image.caption-text-align my_database ./corpora/JSON/imageTextPaired.jsonl -F AnnotationInterface_ImageCaptionAndTextAlign.py
```
If the image is a logo or another kind of boilerplate image, skip it by hitting *spacebar* or the grey prohibition symbol.

If the image is none of the above, enter the caption in the text input field below the image, mark the text section to which the image corresponds and finally press the green checkmark or the *a* key.

Due to conflicting "spans", the image interface in use provides additional tools to mark image spans; these are not needed.
