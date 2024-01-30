from peft import PeftModel, prepare_model_for_kbit_training
from transformers import BitsAndBytesConfig
import torch

BITS_AND_BYTES_CONFIG_4BIT = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

def load_peft_model_with_adpaters(model, adapters):
  model = PeftModel.from_pretrained(
      model, 
      adapters
  )
  model.gradient_checkouting_enabled()
  model = prepare_model_for_kbit_training(model)

  return model 


def print_trainable_parameters(model):
    """
    Prints the number of trainable parameters in the model.
    """
    trainable_params = 0
    all_param = 0
    for _, param in model.named_parameters():
        all_param += param.numel()
        if param.requires_grad:
            trainable_params += param.numel()
    print(
        f"trainable params: {trainable_params} || all params: {all_param} || trainable%: {100 * trainable_params / all_param}"
    )