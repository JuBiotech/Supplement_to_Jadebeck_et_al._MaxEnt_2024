screen -L -d -m python3 src/sample_model_set.py --model_set_path bma-models/informative_crown_limited_bidirs/crown_GOX --samples_output_dir bma-models/informative_crown_limited_bidirs/distributed_bma_samples4 --num_threads 16 --num_procs 1 --max_num_levels 150 --new_level_interval 50000 --save_interval 2500 --step_size 0.025 --starting_point_method chebyshev --thread_steps=200

screen -L -d -m python3 src/sample_model_set.py --model_set_path bma-models/informative_crown_limited_bidirs/crown_GOX_MGOX --samples_output_dir bma-models/informative_crown_limited_bidirs/distributed_bma_samples4 --num_threads 16 --num_procs 1 --max_num_levels 150 --new_level_interval 50000 --save_interval 2500 --step_size 0.025 --starting_point_method chebyshev --thread_steps=200

screen -L -d -m python3 src/sample_model_set.py --model_set_path bma-models/informative_crown_limited_bidirs/crown --samples_output_dir bma-models/informative_crown_limited_bidirs/distributed_bma_samples4 --num_threads 16 --num_procs 1 --max_num_levels 150 --new_level_interval 50000 --save_interval 2500 --step_size 0.025 --starting_point_method chebyshev --thread_steps=200

screen -L -d -m python3 src/sample_model_set.py --model_set_path bma-models/informative_crown_limited_bidirs/crown_MGOX --samples_output_dir bma-models/informative_crown_limited_bidirs/distributed_bma_samples4 --num_threads 16 --num_procs 1 --max_num_levels 150 --new_level_interval 50000 --save_interval 2500 --step_size 0.025 --starting_point_method chebyshev --thread_steps=200

