# Slowblood Python Module

> This python package will have a collection of structures, functions and tools for interacting with LLMs and Datasets.

<br>

## Project and PyPI Package 
- https://pypi.org/project/slowblood/
- https://github.com/kyledinh/slowblood
- https://huggingface.co/Slowblood

<br>

## Usage Examples

> Get RunPod Available GPUs with price
```python
import slowblood
slowblood.lib_runpod.runpod_info(RUNPOD_API_KEY)

# or if you have the RUNPOD_API_KEY set in .env file
slowblood.runpod_get_available_gpus()
```

output:
```
GPUs: 
{'maxGpuCount': 8, 'id': 'NVIDIA A100 80GB PCIe', 'displayName': 'A100 80GB', 'manufacturer': 'Nvidia', 'memoryInGb': 80, 'cudaCores': 0, 'secureCloud': True, 'communityCloud': True, 'securePrice': 1.89, 'communityPrice': 1.59, 'oneMonthPrice': None, 'threeMonthPrice': None, 'oneWeekPrice': None, 'communitySpotPrice': 0.89, 'secureSpotPrice': None, 'lowestPrice': {'minimumBidPrice': 0.89, 'uninterruptablePrice': 1.59}} ...
```

### Copy Save HuggingFace Model
> Copy a Hugging Face model to a new Hugging Face Org


<br>

## Required Dependencies

```
pip install -qU git+https://github.com/huggingface/transformers.git
pip install -qU git+https://github.com/huggingface/peft.git
pip install -qU git+https://github.com/huggingface/accelerate.git
```

<br>

## Package Structs, Methods and Consts 

### Datasets 

- `TextDataset`
- `prepare_dataset_llama2()`
- `generate_from_dataset_llama2()`

### Model

- `BITS_AND_BYTES_CONFIG_4BIT`
- `load_peft_model_with_adapters()` 
- `print_trainable_parameters()`

### PDF Manipulation 

- `convert_pdf_to_images()`
- `extract_text_from_pdf()` 
- `extract_text_from_imgs()`

### Settings

- `BasicInferenceRequest`
- `ArtifactNames`
- `FineTuningSettings`

### Tokenizer

- `get_tokenizer_for_model()`
- `update_model_with_tokenizer()`


