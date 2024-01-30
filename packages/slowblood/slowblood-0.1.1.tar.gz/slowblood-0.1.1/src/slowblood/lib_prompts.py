# Library of Prompt related functions for various types of models

def debugPrintMessage(prompt, message = ""):
  print(f" == debug {message} ====================")
  print(prompt)
  print(" ========================================")


def createLlama2Prompt(system_prompt: str, content_prompt: str, output_prompt: str, debug = False) -> str:
  return create_llama2_prompt(system_prompt, content_prompt, output_prompt, debug = False) 

def create_llama2_prompt(system_prompt: str, content_prompt: str, output_prompt: str, debug = False) -> str:
  prompt = f"""
  <s>[INST] <<SYS>>
  {system_prompt}
  <</SYS>>

  {content_prompt} {output_prompt}[/INST]
  """.strip()

  if debug == True:
    debugPrintMessage(prompt, "prompt")

  return prompt


def create_openai_prompt(system_prompt: str, content_prompt: str, debug = False) -> str:
  prompt = f"""
  {system_prompt} 

  {content_prompt}
  """.strip()

  if debug == True:
    debugPrintMessage(prompt, "prompt")

  return prompt

