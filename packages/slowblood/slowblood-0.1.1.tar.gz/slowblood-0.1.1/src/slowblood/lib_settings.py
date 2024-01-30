## Project Level Constants 

VERSION = 1 

# Used for prompt/request data 
class BasicInferenceRequest:
  def __init__(self, token="", inference_url="", system_prompt="", content_prompt="", output_prompt=""):
    self.token = token
    self.inference_url = inference_url
    self.system_prompt = system_prompt
    self.content_prompt = content_prompt
    self.output_prompt = output_prompt

  def __str__(self):
    return f"BIR [ token: {self.token}, inference_url: {self.inference_url}, system_prompt: {self.system_prompt}, content_prompt: {self.content_prompt}, output_prompt: {self.output_prompt} ]"

  def __repr__(self):
    return f"BasicInferenceRequest(\'{self.token}\', \'{self.inference_url}\', \'{self.system_prompt}\', \'{self.content_prompt}\', \'{self.output_prompt}\')"


# Used for metadata for Fine Tuning 
class ArtifactNames:
  def __init__(self, base_model, new_model_name, repo_name, dataset):
    self.base_model = base_model
    base_model_name = base_model.split("/")[-1]
    self.adapter_model = repo_name + "/" + base_model_name + "_" + new_model_name
    self.new_model = repo_name + "/" + new_model_name 
    self.dataset = dataset 
  
  def __str__(self):  
    return f"ArtifactNames [ base_model: {self.base_model}, adapter_model: {self.adapter_model}, new_model: {self.new_model}, dataset: {self.dataset} ]"

  def __repr__(self):  
    return f"ArtifactNames(\'{self.base_model}\', \'{self.adapter_model}\', \'{self.new_model}\', \'{self.dataset}\')"


class FineTuningSettings:
  def __init__(self, base_model, new_model_name, repo_name, dataset, cache_dir="/cache"):
    self.base_model = base_model
    base_model_name = base_model.split("/")[-1]
    self.adapter_model = repo_name + "/" + base_model_name + "_" + new_model_name
    self.new_model = repo_name + "/" + new_model_name
    self.dataset = dataset
    self.cache_dir = cache_dir