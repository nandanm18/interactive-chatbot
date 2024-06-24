
from clarifai.client.workflow import Workflow

# Your PAT (Personal Access Token) can be found in the Account's Security section

# Initialize the workflow_url
workflow_url = "https://clarifai.com/nandanm/lammatutorial/workflows/workflow-666733"
text_classfication_workflow = Workflow(
    url= workflow_url , pat="639c28d7d93f4a38a2be4b5ee496cfb2"
)
result = text_classfication_workflow.predict_by_bytes(b"I hate you", input_type="text")
print(result.results[0].outputs[0].data)
