# LLM Auto-evaluation with OpenAI API


## How to use
Edit the arguments, and run the ```.sh``` file!
```sh example.sh```

### Supported Models
- nlpai-lab/kullm-polyglot-12.8b-v2
- upstage/SOLAR-10.7B-Instruct-v1.0
- mistralai/Mistral-7B-Instruct-v0.2
- beomi/KoAlpaca-Polyglot-12.8B
- OpenAI APIs (comming soon!)

## Default Template (editable)
```
두 사람 간의 대화가 주어집니다. 다음의 지시문(Instruction), 입력(Input)을 받게 될 것입니다. 그리고 지시문과 입력에 대한 응답(Response)이 제시됩니다.
당신의 작업은 응답을 평가 기준에 따라 응답을 평가하는 것입니다.
이 평가 기준을 꼼꼼히 읽고 이해하는 것이 중요합니다. 평가하는 동안 이 문서를 계속 열어두고 필요할 때 참조해 주세요.

평가 기준:
- 이해 가능성 (0 - 1): Instruction에 기반하여 Response를 이해 할 수 있나요? 이해할 수 있으면 1, 없으면 0입니다. 
- 자연스러움 (1 - 3): 자연스러운 문장이란 유창하고 문법 오류가 없는 글을 말합니다. 점수가 높을수록 자연스러운 문장입니다.
- 맥락 유지 (1 - 3): Instruction을 고려했을 때 Response가 맥락을 유지하나요? 점수가 높을수록 문맥에 맞는 응답입니다. Instruction에 알맞은 Response일수록 점수가 높습니다.
- 정확성 (1 - 3): Response가 정확한 사실에 기반하면 3, 중립이면 2, 거짓일 경우 1점을 부여합니다.
- 전반적인 품질 (1 - 5): 위의 답변을 바탕으로 이 발언의 전반적인 품질을 평가하세요. 점수가 높을수록 품질이 좋은 응답입니다.

평가 단계:
1. Instruction, Input, 그리고 Response을 주의깊게 읽습니다.
2. 위의 평가 기준에 따라 Response을 평가합니다.

Instruction:
{{instruction}}

Input:
{{input}}

Response:
{{response}}
```
