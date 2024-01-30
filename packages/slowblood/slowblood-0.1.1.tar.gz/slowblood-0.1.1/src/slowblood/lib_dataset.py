from datasets import load_dataset
import re
import torch
from torch.utils.data import Dataset

class TextDataset(Dataset):
    def __init__(self, encodings, response_lengths, input_lengths):
        self.encodings = encodings
        self.response_lengths = response_lengths
        self.input_lengths = input_lengths

    def __getitem__(self, idx):
        item = {key: val[idx].clone().detach() for key, val in self.encodings.items()}

        # Set labels to be the same as input_ids
        item["labels"] = item["input_ids"].clone()

        # Calculate the start and end positions of the response
        response_start_position = self.input_lengths[idx]
        response_end_position = self.input_lengths[idx] + self.response_lengths[idx]

        # Create a loss mask that covers only the response tokens
        item["loss_mask"] = torch.zeros_like(item["input_ids"])
        item["loss_mask"][response_start_position:response_end_position] = 1

        # Shift the loss mask to the left by one position
        shifted_loss_mask = torch.cat([item["loss_mask"][1:], torch.tensor([0])])
        item["loss_mask"] = shifted_loss_mask

        # Shift the labels to the left by one position
        item["labels"][:-1] = item["input_ids"][1:]

        # Replace the token after the response with an EOS token
        item["labels"][response_end_position - 1] = 2

        # Replace the token after the response with an 1 in the loss mask
        item["loss_mask"][response_end_position - 1] = 1

        return item

    def __len__(self):
        return len(self.encodings["input_ids"])


def prepare_dataset_llama2(dataset, tokenizer):
    # Define the roles and markers
    B_FUNC, E_FUNC = "<FUNCTIONS>", "</FUNCTIONS>"
    B_USER, E_USER = "<USER>", "</USER>"
    B_SYS, E_SYS = "<SYS>", "</SYS>"
    B_INST, E_INST = "[INST]", "[/INST]"

    # Create the formatted text with the correct roles for each part of the dialogue
    formatted_dataset = dataset.map(
        lambda x: {
            "input_text": "".join([
                f"{B_SYS}{x['systemPrompt'].strip()}{E_SYS}",
                f"{B_INST} {x['userPrompt'].strip()} {E_INST}\n\n",
                f"{x['assistantResponse'].strip()}",  # appending the EOS token in TextData...
            ]),
            "response_text": "".join([
                f"{x['assistantResponse'].strip()}",  # appending the EOS token in TextData...
            ]),
        }
    )

    # Tokenize the datasets
    encodings = tokenizer([dialogue["input_text"] for dialogue in formatted_dataset], truncation=True, padding=True, max_length=1024, return_tensors='pt', add_special_tokens=True)

    # Tokenize the response one by one without padding and special tokens for the purpose of calculating length
    response_lengths = [len(tokenizer.encode(dialogue["response_text"], truncation=True, max_length=1024, padding=False, add_special_tokens=False)) for dialogue in formatted_dataset]

    # Tokenize the input one by one without padding and with the initial special token for the purpose of calculating length
    total_lengths = [len(tokenizer.encode(dialogue["input_text"], truncation=True, max_length=1024, padding=False, add_special_tokens=True)) for dialogue in formatted_dataset]
    input_lengths = [total_length - response_length for total_length, response_length in zip(total_lengths, response_lengths)]

    # Create TextDataset
    text_dataset = TextDataset(encodings, response_lengths, input_lengths)

    return text_dataset

def generate_from_dataset_llama2(index, data, model, tokenizer):
    # Define the roles and markers
    B_INST, E_INST = "[INST]", "[/INST]"
    B_SYS, E_SYS = "<SYS>", "</SYS>\n\n"

    # Format your prompt template
    system_prompt = data['train'][index]['systemPrompt']
    user_prompt = data['train'][index]['userPrompt']
    correct_answer = data['train'][index]['assistantResponse']

    # Format your prompt template
    prompt = f"{B_SYS}{system_prompt.strip()}{E_SYS}{B_INST} {user_prompt.strip()} {E_INST}\n\n"
    print(f"Prompt: {prompt}")

    encoding = tokenizer(prompt, return_tensors="pt").to("cuda:0")
    output = model.generate(input_ids=encoding.input_ids,
                            attention_mask=encoding.attention_mask,
                            max_new_tokens=2000,
                            do_sample=True,
                            temperature=0.01,
                            eos_token_id=tokenizer.eos_token_id,
                            top_k=0)

    print()

    # Subtract the length of input_ids from output to get only the model's response
    output_text = tokenizer.decode(output[0, len(encoding.input_ids[0]):], skip_special_tokens=False)
    output_text = re.sub('\n+', '\n', output_text)  # remove excessive newline characters

    print("Generated Assistant Response: ", output_text, "\n")
    print("Correct Assistant Response:", correct_answer, "\n")

def get_info_for_dataset():
    print("dataset: info")