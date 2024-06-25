
from clarifai.client.workflow import Workflow

# Your PAT (Personal Access Token) can be found in the Account's Security section

# Initialize the workflow_url
workflow_url = "https://clarifai.com/dr8yqqxtfdod/llama2/workflows/workflow-49e976"
text_classfication_workflow = Workflow(
    url= workflow_url , pat="922503104f3942c3bbe45d2e50311c15"
)
result = text_classfication_workflow.predict_by_bytes(b"I hate you", input_type="text")
print(result.results[0].outputs[0].data)
