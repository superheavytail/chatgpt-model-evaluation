# kullm v2
#CUDA_VISIBLE_DEVICES=3 python step1_generate_answers.py \
#--model_name nlpai-lab/kullm-polyglot-12.8b-v2 \
#--save_name kullm_v2 \
#--eval_set_path res/user_oriented_instructions_eval.jsonl \
#--output_dir ./generated/ \
#--model_type kullm \
#--debug False

# kullm v3
#CUDA_VISIBLE_DEVICES=2 python step1_generate_answers.py \
#--model_name nlpai-lab/kullm_v3 \
#--save_name kullm_v3 \
#--eval_set_path res/user_oriented_instructions_eval.jsonl \
#--output_dir.//generated/ \
#--model_type solar \
#--debug False

# solar instruct
#CUDA_VISIBLE_DEVICES=1 python step1_generate_answers.py \
#--model_name upstage/SOLAR-10.7B-Instruct-v1.0 \
#--save_name upstage-solar \
#--eval_set_path res/user_oriented_instructions_eval.jsonl \
#--output_dir ./generated/ \
#--model_type solar \
#--debug False

# mistral 7B (excluded since it often say English, though Korean context.)
#CUDA_VISIBLE_DEVICES=0 python step1_generate_answers.py \
#--model_name mistralai/Mistral-7B-Instruct-v0.2 \
#--save_name mistral \
#--eval_set_path res/user_oriented_instructions_eval.jsonl \
#--output_d./generated/ \
#--model_type mistral \
#--debug False

# beomi/koalpaca_v1.1b
#CUDA_VISIBLE_DEVICES=4 python step1_generate_answers.py \
#--model_name beomi/KoAlpaca-Polyglot-12.8B \
#--save_name koalpaca_v1_1b \
#--eval_set_path res/user_oriented_instructions_eval.jsonl \
#--output_dir ./generated/ \
#--model_type koalpaca_v1_1b \
#--debug False


# gpt-3.5 turbo
#python step1_generate_answers.py \
#--model_name gpt-3.5-turbo-0125 \
#--save_name gpt_3_5_turbo_0125 \
#--eval_set_path res/user_oriented_instructions_eval.jsonl \
#--output_dir ./generated/ \
#--model_type openai \
#--debug False

# gpt-4 turbo
#python step1_generate_answers.py \
#--model_name gpt-4-0125-preview \
#--save_name gpt_4_0125_preview \
#--eval_set_path res/user_oriented_instructions_eval.jsonl \
#--output_dir ./generated/ \
#--model_type openai \
#--debug False

# kullm3 (templated) (local)
#CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python step1_generate_answers.py \
#--model_name /mnt/raid6/potatowook/KULLM3-ckpt/solar-instruct-ko-en-noxP3x-templated/checkpoint-6909 \
#--save_name kullm3_prompted_bsz16 \
#--eval_set_path res/user_oriented_instructions_eval.jsonl \
#--output_dir ./generated/ \
#--model_type kullm3 \
#--debug False

# kullm3 (templated) (bsz16) (multi-GPU)
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 torchrun --nproc_per_node=8 step1_generate_answers.py \
--model_name /mnt/raid6/potatowook/KULLM3-ckpt/solar-instruct-ko-en-noxP3x-templated/checkpoint-6909 \
--save_name kullm3_prompted_bsz16 \
--eval_set_path res/user_oriented_instructions_eval.jsonl \
--output_dir ./generated/ \
--model_type kullm3 \
--debug False

# kullm3 (templated) (bsz8) (multi-GPU)
#CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 torchrun --nproc_per_node=8 step1_generate_answers.py \
#--model_name /mnt/raid6/potatowook/KULLM3-ckpt/solar-instruct-ko-en-noxP3x-templated/checkpoint-13817 \
#--save_name kullm3_prompted_bsz8 \
#--eval_set_path res/user_oriented_instructions_eval.jsonl \
#--output_dir ./generated/ \
#--model_type kullm3 \
#--debug False