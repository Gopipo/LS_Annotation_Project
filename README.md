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
2. calling the function with the optional parameters: -i or --imgdir; -t or --txtdir; -o or --outfile; -p or --keeppaths
```
python3 dir2jsonl.py


python3 dir2jsonl.py -i ./Corpora/images_webcorpus/ -t ./Corpora/tokenized_txt_files/tokenized_ -o imageTextPaired.jsonl -p
```
## Annotating
This requires [Explosion's](https://explosion.ai/) [prodigy with an active license](https://prodi.gy/buy).

To use prodigy to start annotating call:
```
python3 -m prodigy image.caption-text-align my_database ./corpora/JSON/imageTextPaired.jsonl -F AnnotationInterface_ImageCaptionAndTextAlign.py
```
(prodigy recipe_name database_name path_to_preprocessing_output_file)
[Official prodigy documentation](https://prodi.gy/docs/#first-steps1)

If the image is a logo or another kind of boilerplate image, skip it by hitting *spacebar* or the grey &#128711; button.

If the image is none of the above, enter the caption in the text input field below the image, mark the text section to which the image corresponds and finally press the &#9989; button or the *a* key.

### Error correction
To correct a text span, hover over the yellow highlighting and then hit the x at its top left corner.
If you erroneously commited something, hit *backspace*, *del*, or the grey &#8629; button.

### Saving your progress
On the left you see the Prodigy progress element. 
To save your annotations hit the &#x1F4BE; in its top right corner. If all is saved, it shows a &#128504; instead.

Prodigy can now be terminated from the console upon which it displays your session summary indicating how many annotations were saved successfully. 

### Practical Tipps
If you forgot the name of your database:
```
python3 -m prodigy stats -ls
```
Most images repeat often; save your annotations in a separate text file and copy-paste them from there. (Remember a key word or expression so you can easily find them again using Ctrl+f.) 
For text alignment, use your browser's find function (Ctrl+f) and select "Highlight all" in order to quickly scan a text for words and expressions.
Single words may be doubleclicked. If the word is highlighted directly by the search function, 1 click suffices.
You cannot mark segments past a newline-character. However, as long as you do not move down to the next line, you can move your cursor past them and the selection still works.

## Getting the data
Export your annotations to a JSONL-file with this command:
```
python3 -m prodigy db-out my_database > ./annotations.jsonl
```
[Click here to check the official prodigy documentation](https://prodi.gy/docs/#first-steps2)
