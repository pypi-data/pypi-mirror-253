from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from huggingface_hub import InferenceClient

def invoice_to_chatgpt3_5(content: str, template: str, data_points):
  llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

  if template == "":
    template = """
    You are an expert admin who will extract core information from documents 

    {content}

    Above is the content; please try to extract all data points from the content above
    and export in a JSON array format for each invoice line item:
    {data_points}

    Now please extract details from the content and export in a JSON array format,
    return ONLY the JSON array:
    """

  prompt = PromptTemplate(
    input_variables=["content", "data_points"],
    template=template,
  )

  chain = LLMChain(llm=llm, prompt=prompt)

  results = chain.run(content=content, data_points=data_points)

  return results

def invoice_to_hf_llama(content: str, template: str, data_points, hf_token, endpoint_url):

  client = InferenceClient(token=hf_token, model=endpoint_url)

  # generation parameter
  gen_kwargs = dict(
    max_new_tokens=748,
    top_k=30,
    top_p=0.9,
    temperature=0.2,
    repetition_penalty=1.02,
    stream=False,
    details=True,
  )

  if template == "":
    template = """
    You are an expert admin who will extract core information from documents 

    {content}

    Above is the content; please try to extract all data points from the content above
    and export in a JSON array format:
    {data_points}

    """

  prompt = PromptTemplate.from_template(template)
  prompt_str = prompt.format(content=content, data_points=data_points)

  print(prompt)
  print("================================")
  print(prompt_str)
  print("================================")
  # prompt = "What killed the dinosaurs?"
  response = client.text_generation(prompt_str, **gen_kwargs)
  print(response.generated_text)

  return response.generated_text 