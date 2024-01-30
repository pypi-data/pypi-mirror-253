from transformers import AutoTokenizer

def get_tokenizer_for_model(model, cache_dir, debug=False):

  tokenizer = AutoTokenizer.from_pretrained(model, cache_dir)
  tokenizer.padding_side='right'

  # Add the pad token if missing the tokenizer vocabulary
  if '|<pad>|' not in tokenizer.get_vocab():
    tokenizer.add_tokens(['|<pad>|'])

  # Set the pad token
  tokenizer.pad_token = '|<pad>|'

  if debug == True:
    print("EOS token:", tokenizer.eos_token, ", id:", tokenizer.eos_token_id)
    print("Pad token: ", tokenizer.pad_token, ", ID: ", tokenizer.pad_token_id)

  return tokenizer 

def update_model_with_tokenizer(model, tokenizer, debug=False):

  # Resize token embeddings
  model.resize_token_embeddings(len(tokenizer))

  # Update pad token id in model and its config
  model.pad_token_id = tokenizer.pad_token_id
  model.config.pad_token_id = tokenizer.pad_token_id

  # Check if they are equal
  assert model.pad_token_id == tokenizer.pad_token_id, "The model's pad token ID does not match the tokenizer's pad token ID!"

  if debug == True:
    # Print the pad token ids
    print('Tokenizer pad token ID:', tokenizer.pad_token_id)
    print('Model pad token ID:', model.pad_token_id)
    print('Model config pad token ID:', model.config.pad_token_id)

    # model configuration
    print(model.config)

    # Sample string
    sample_string = ['[INST]']

    # Tokenize the stringified JSON object
    # encoded_sample = tokenizer(sample_string, truncation=True, padding=True, max_length=1024, return_tensors='pt', add_special_tokens=True)
    encoded_sample = tokenizer(sample_string, truncation=True, padding=True, max_length=1024, return_tensors='pt', add_special_tokens=False)

    # Count the number of tokens
    token_count = len(encoded_sample)

    BOS_token_id = tokenizer.bos_token_id
    EOS_token_id = tokenizer.eos_token_id
    BOS_token = tokenizer.decode([BOS_token_id])
    EOS_token = tokenizer.decode([EOS_token_id])

    print(f"Beginning of the sequence: {sample_string[0]} (BOS token: {BOS_token}, id: {BOS_token_id})")
    print(f"End of the sequence: {sample_string[-1]} (EOS token: {EOS_token}, id: {EOS_token_id})")

    print(f"The number of tokens in the string is: {token_count}")
    print(f"The ids are: {encoded_sample}")

    # Decode the input_ids
    decoded_sample = tokenizer.decode(encoded_sample['input_ids'][0], skip_special_tokens=False)

    print(f"The decoded string is: {decoded_sample}")
    print(f"The attention mask is: {encoded_sample['attention_mask']}")

  return model 