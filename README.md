# Korean LLM Auto-evaluation with OpenAI API


## How to use
Edit the arguments, and run the ```.sh``` file!
```sh example.sh```

### Supported Models
- nlpai-lab/kullm-v3
- nlpai-lab/kullm-polyglot-12.8b-v2
- upstage/SOLAR-10.7B-Instruct-v1.0
- mistralai/Mistral-7B-Instruct-v0.2 (excluded since it generates english even though given Korean prompt)
- beomi/KoAlpaca-Polyglot-12.8B
- OpenAI Models (gpt-3.5-turbo, gpt-4-turbo)

## Default Evaluation Template
### System Prompt
```
You're a helpful assistant and a Korean language expert.
```
### User Prompt
```
You will be given evaluation instruction, input and AI-generated response.
Your task is to rate the response on given metric.
Please make sure you read and understand these instructions carefully. Please keep this document open while reviewing, and refer to it as needed.

Evaluation Criteria:
- Fluency (1-5): The quality of the language used in the translation. A high-quality response should be grammatically correct, idiomatic, and free from spelling and punctuation errors.
- Coherence (1-5): A high score indicates that the response maintains consistent context. A low score is given if the response shifts context or language inappropriately from instruction(e.g. instruction's language is Korean, but response is English).
- Accuracy (1-5) - The correctness of the answer. The answer should be factually correct and directly answer the question asked
- Completeness (1-5) - The extent to which the response covers all aspects of the question. The response should not just address one part of the question, but should provide a comprehensive response.
- Overall Quality (1-5) - The overall effectiveness and excellence of the response, integrating considerations of all above criteria.

Evaluation Steps:
1. Read the instruction and input carefully and understand what it is asking.
2. Read the AI-generated response and Evaluation Criteria.
3. Assign a score for each criterion on a scale of 1 to 5, where 1 is the lowest and 5 is the highest.

Instruction:
{instruction}

Input:
{input}

Response:
{response}

Evaluation Form (scores ONLY):
- Fluency (1-5):
- Coherence (1-5):
- Accuracy (1-5):
- Completeness (1-5):
- Overall Quality (1-5):
```

# Requirements
- [batched-chatgpt](https://github.com/superheavytail/batched-chatgpt)
```bash
pip install batched-chatgpt
```