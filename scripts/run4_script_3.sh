screen -L -d -m python3 src/sample_model_set.py --model_set_path bma-models/uninformative_crown_limited_bidirs/crown_EDP_GOX --samples_output_dir bma-models/uninformative_crown_limited_bidirs/distributed_bma_samples4 --num_threads 16 --num_procs 1 --max_num_levels 120 --new_level_interval 50000 --save_interval 2500 --step_size 0.025 --starting_point_method chebyshev --thread_steps=200

screen -L -d -m python3 src/sample_model_set.py --model_set_path bma-models/uninformative_crown_limited_bidirs/crown_EDP_GOX_MGOX --samples_output_dir bma-models/uninformative_crown_limited_bidirs/distributed_bma_samples4 --num_threads 16 --num_procs 1 --max_num_levels 120 --new_level_interval 50000 --save_interval 2500 --step_size 0.025 --starting_point_method chebyshev --thread_steps=200

screen -L -d -m python3 src/sample_model_set.py --model_set_path bma-models/uninformative_crown_limited_bidirs/crown_EDP --samples_output_dir bma-models/uninformative_crown_limited_bidirs/distributed_bma_samples4 --num_threads 16 --num_procs 1 --max_num_levels 120 --new_level_interval 50000 --save_interval 2500 --step_size 0.025 --starting_point_method chebyshev --thread_steps=200

screen -L -d -m python3 src/sample_model_set.py --model_set_path bma-models/uninformative_crown_limited_bidirs/crown_EDP_MGOX --samples_output_dir bma-models/uninformative_crown_limited_bidirs/distributed_bma_samples4 --num_threads 16 --num_procs 1 --max_num_levels 120 --new_level_interval 50000 --save_interval 2500 --step_size 0.025 --starting_point_method chebyshev --thread_steps=200

