# LS Annotation Project

## Preprocessing
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
## Annotating
To use prodigy to start annotating call:
```
python3 -m prodigy image.caption-text-align my_database ./corpora/JSON/imageTextPaired.jsonl -F AnnotationInterface_ImageCaptionAndTextAlign.py
```
(prodigy recipe_name database_name path_to_preprocessing_output_file)

If the image is a logo or another kind of boilerplate image, skip it by hitting *spacebar* or the grey &#128711; button.

If the image is none of the above, enter the caption in the text input field below the image, mark the text section to which the image corresponds and finally press the &#9989; button or the *a* key.

### Error correction
To correct a text span, hover over the yellow highlighting and then hit the x at its top left corner.
If you erroneously commited something, hit *backspace*, *del*, or the grey &#8629; button.

### Saving your progress
On the left you see the Prodigy progress element. 
To save your annotations hit the &#128190; in its top right corner.

