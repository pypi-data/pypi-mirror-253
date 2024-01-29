export CUDA_VISIBLE_DEVICES=3
python generate.py --model "codegen2-3b" --bs 4 --construct_prompt "output_v_mutation" --dataset "humaneval" --n_samples 100 | tee -a log/codegen2-3b_output_v_mutation_humaneval.txt
python generate.py --model "incoder-6b" --bs 1 --construct_prompt "output_v_mutation" --dataset "humaneval" --n_samples 100 | tee -a log/incoder-6b_output_v_mutation_humaneval.txt
python generate.py --model "incoder-1b" --bs 1 --construct_prompt "output_v_mutation" --dataset "humaneval" --n_samples 100 | tee -a log/incoder-1b_output_v_mutation_humaneval.txt
