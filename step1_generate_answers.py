from pathlib import Path
import fire
import jsonlines
import json

from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm
from batched_chatgpt import call_chatgpt


def main(
    model_name,
    save_name,
    eval_set_path,
    output_dir,
    model_type,
    debug: bool = False
):
    # check if save path is safe
    save_path = Path(output_dir) / save_name
    save_path = save_path.with_suffix(".jsonl")
    if save_path.exists():
        raise FileExistsError(f"{save_path} exists!")

    print("=== model name ===")
    print(model_name)
    print("===    ====    ===")

    # prepare evaluation set
    eval_set = [e for e in jsonlines.open(eval_set_path).iter()]
    eval_set = eval_set[:5] if debug else eval_set

    generated_answers = []

    if model_type == 'openai':
        input_texts = [f"{e['instruction']}\n\n{e['instances'][0]['input']}" for e in eval_set]
        generated_answers = call_chatgpt(input_texts, chunk_size=20, model_name=model_name)
    else:
        # model, tokenizer load
        try:
            model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype='auto',
                attn_implementation='sdpa').to('cuda')
        except ValueError:
            model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype='auto').to('cuda')
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # building input text
        # solar uses apply_chat_template but kullm doesn't
        if model_type == 'solar' or model_type == 'mistral':
            input_texts = [f"{e['instruction']}\n\n{e['instances'][0]['input']}" for e in eval_set]
            input_template_texts = [tokenizer.apply_chat_template(
                [{"role": "user", "content": t}], tokenize=False, add_generation_prompt=True) for t in input_texts]
            if model_type == 'solar':
                split_criterion = "### Assistant:\n"
            elif model_type == 'mistral':
                split_criterion = "[/INST]"
            else:
                raise NotImplementedError

        elif model_type in ['kullm', 'koalpaca_v1_1b']:
            # for generate
            model.config.pad_token_id = model.config.eos_token_id

            with open(f"templates/{model_type}.json", 'rt') as f:
                template = json.load(f)

            input_template_texts = []
            for e in eval_set:
                if e['instances'][0]['input']:
                    input_text = template['prompt_input'].format_map({
                        'instruction': e['instruction'],
                        'input': e['instances'][0]['input']
                    })
                else:
                    input_text = template['prompt_no_input'].format_map({
                        'instruction': e['instruction'],
                    })
                input_template_texts.append(input_text)
            split_criterion = template['response_split']
        else:
            raise NotImplementedError

        input_ids = [tokenizer(e, return_tensors='pt')["input_ids"].to(model.device) for e in input_template_texts]

        # do generation
        if not tokenizer.pad_token_id and tokenizer.eos_token_id:
            tokenizer.pad_token_id = tokenizer.eos_token_id
        for item in tqdm(input_ids):
            res = model.generate(
                item,
                use_cache=True,
                max_new_tokens=2048-len(item[0]),
                eos_token_id=tokenizer.eos_token_id,
                pad_token_id=tokenizer.pad_token_id
            )
            answer = tokenizer.decode(res[0], skip_special_tokens=True)

            try:
                if model_type in ['kullm', 'koalpaca_v1_1b', 'solar']:
                    model_answer = answer.split(split_criterion, 1)[1]
                elif model_type in ['mistral']:
                    model_answer = answer.rsplit(split_criterion, 1)[1]
                else:
                    raise NotImplementedError
            except IndexError:
                print("model generate nothing!! Full model answer:")
                print(answer)
                model_answer = "(no answer from model)"  # Some models rarely generate nothing.

            generated_answers.append(model_answer)
            if debug:
                print(model_answer)

    # saving results
    # zip instruction, input, answer
    results = []
    for eval_item, answer in zip(eval_set, generated_answers):
        results.append({
            'instruction': eval_item['instruction'],
            'input': eval_item['instances'][0]['input'],
            'answer': answer
        })

    with open(save_path, "wt", encoding="utf-8") as f:
        for result in results:
            json.dump(result, f, ensure_ascii=False)  # set ensure_ascii False for Korean language
            f.write("\n")  # since it's jsonl

    if debug:
        for result in results:
            print(f"{result['instruction']=}")
            print(f"{result['input']=}")
            print(f"{result['answer']=}")


if __name__ == '__main__':
    fire.Fire(main)
