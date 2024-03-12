# kullm v2
CUDA_VISIBLE_DEVICES=0 python step1_generate_answers.py \
--model_name nlpai-lab/kullm-polyglot-12.8b-v2 \
--save_name kullm_v2 \
--eval_set_path res/user_oriented_instructions_eval.jsonl \
--output_dir my-output-dir \
--model_type kullm \
--debug False