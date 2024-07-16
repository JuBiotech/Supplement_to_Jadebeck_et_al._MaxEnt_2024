import random

import click
import x3c2fluxpy
from mfa_toolbox import BMASampler, NestedSamplingOptions, FMLOptions
from pathlib import Path
from os import listdir
from os.path import isfile, join
from time import time
import hopsy
import numpy as np
import sys


@click.command()
@click.option("--model_set_path", help="path to directory containing fml models", required=True, type=str)
@click.option("--samples_output_dir", help="directory for storing samples",
              default="bma_samples", type=str)
@click.option("--num_threads", default=1, type=int)
@click.option("--num_procs", default=1, type=int)
@click.option("--num_particles_per_thread", default=1, type=int)
@click.option("--new_level_interval", default=20000, type=int)
@click.option("--save_interval", default=20000, type=int)
@click.option("--step_size", default=1., type=float)
@click.option("--max_num_levels", default=30, type=int)
@click.option("--max_num_saves", default=0, type=int)
@click.option("--rng_seed", default=random.randint(0, int(1e6)), type=int)
@click.option("--prior_seed", default=random.randint(0, int(1e6)), type=int)
@click.option("--prior_thinning", default=1000, type=int)
@click.option("--thread_steps", default=1000, type=int)
@click.option("--eps", help="move starting point away from border by eps", default=0, type=float)
@click.option("--starting_point_method", help="use fit from fml or chebyshev", default="fit", type=str)
def sample_model_set(model_set_path: str, samples_output_dir: str,
                     num_threads: int,
                     num_procs: int,
                     num_particles_per_thread: int,
                     new_level_interval: int,
                     save_interval: int,
                     step_size: float,
                     max_num_levels: int,
                     max_num_saves: int,
                     rng_seed: int,
                     prior_seed: int,
                     prior_thinning: int,
                     thread_steps: int,
                     eps: float,
                     starting_point_method: str):
    fml_files = [f for f in listdir(model_set_path) if isfile(join(model_set_path, f)) and Path(f).suffix == ".fml"]
    print(fml_files)

    nested_sampling_options_list = []
    fml_options_list = []

    for i, fml_file in enumerate(fml_files):
        nested_sampling_options = NestedSamplingOptions()
        nested_sampling_options.num_threads = num_threads
        nested_sampling_options.num_particles_per_thread = num_particles_per_thread
        nested_sampling_options.new_level_interval = new_level_interval
        nested_sampling_options.save_interval = save_interval
        nested_sampling_options.max_num_levels = max_num_levels
        nested_sampling_options.max_num_saves = max_num_saves
        nested_sampling_options.rng_seed = rng_seed * i
        nested_sampling_options.prior_seed = prior_seed * i
        nested_sampling_options.prior_thinning = prior_thinning
        nested_sampling_options.proposal_step_size = step_size
        nested_sampling_options.thread_steps = thread_steps
        nested_sampling_options.beta = 100

        nested_sampling_options_list.append(nested_sampling_options)

        fml_options = FMLOptions()
        fml_options.fml_path = str(Path(model_set_path) / fml_file)
        fml_options.output_directory = str(Path(samples_output_dir) / Path(fml_file).stem)

        # Round & preprocess polytope in the next steps
        x3c2model = x3c2fluxpy.X3CModel(fml_options.fml_path, fml_options.config)
        A2 = x3c2model.A
        b2 = x3c2model.b
        bounded_problem = hopsy.add_box_constraints(
            hopsy.Problem(A2, b2),
            lower_bound=-1000,
            upper_bound=1000,
            simplify=True
        )
        starting_point = x3c2model.initial_point if starting_point_method == 'fit' else hopsy.compute_chebyshev_center(bounded_problem)
        bounded_problem.starting_point = starting_point + eps * np.ones(starting_point.shape)
        fml_options.starting_point = bounded_problem.starting_point

        assert np.all(bounded_problem.b - bounded_problem.A @ bounded_problem.starting_point > 0)
        rounded_problem = hopsy.round(bounded_problem)

        fml_options.rounding_matrix = rounded_problem.transformation
        fml_options.rounding_shift = rounded_problem.shift

        fml_options.rounded_polytope_matrix = rounded_problem.A
        fml_options.rounded_polytope_bounds = rounded_problem.b

        fml_options.polytope_matrix = bounded_problem.A
        fml_options.polytope_bounds = bounded_problem.b

        fml_options_list.append(fml_options)

    sampler = BMASampler(nested_sampling_options_list=nested_sampling_options_list, fml_options_list=fml_options_list)
    start = time()
    print('start sampling')
    sampler.sample(num_procs=num_procs, terminal_output=False)
    end = time()
    print('finished sampling after', end - start, 'seconds')


if __name__ == "__main__":
    sample_model_set()
