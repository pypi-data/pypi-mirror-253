from .lib_dataset import (
    TextDataset,
    prepare_dataset_llama2,
    generate_from_dataset_llama2,
)

from .lib_llm_inference import (
    invoice_to_chatgpt3_5,
    invoice_to_hf_llama,
)

from .lib_model import (
    load_peft_model_with_adpaters,
    print_trainable_parameters,
)

from .lib_pdf import (
    convert_pdf_to_images,
    extract_text_from_pdf, 
    extract_text_from_imgs, 
)

from .lib_prompts import (
    create_llama2_prompt,
    create_openai_prompt,
)

from .lib_settings import (
    BasicInferenceRequest,
    ArtifactNames,
    FineTuningSettings,
)

from .lib_tokenizer import (
    get_tokenizer_for_model, 
    update_model_with_tokenizer,
)

from .lib_runpod import (
    load_runpod_token,
    runpod_info,
)

def runpod_get_available_gpus():
    rp_api_key = load_runpod_token()
    return runpod_info(rp_api_key)

def help():
    print("Help!", " version 0.1.1", " Jan 29, 2024")
    print("Go to https://pypi.org/project/slowblood/ for more information.")