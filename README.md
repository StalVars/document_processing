#


# First convert pdf to images

mkdir images # this folder is required for putting the converted pdf pages into images 
python examples/pdf_to_image.py <pdf_file_path>


# Create OCR text from images
Solo
~ tesseract has to be installed for the following, already. To use this in the cluster, use the right image here: bash run_docker_nikjou.sh  python ...

python preprocess/image_processing_layoutlmv3.py --input_file <image> 
python preprocess/image_processing_layoutlmv3.py --input_file <image> --output_file <outputjson>



# To use LAyoutLMv3 Model
you can find the example here: https://huggingface.co/docs/transformers/model_doc/layoutlmv3 
LayoutLMv3FeatureExtractor is a huggingface class, uses pytesseract

