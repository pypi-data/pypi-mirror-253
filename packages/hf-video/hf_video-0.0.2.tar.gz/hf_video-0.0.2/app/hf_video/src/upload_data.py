import os
import argparse
import datasets
import numpy as np
import pandas as pd
from glob import glob
import multiprocessing as mp
from datasets import Dataset, Features, Value
from datasets import disable_caching


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path_to_data", type=str)
    parser.add_argument("--writer_batch_size", type=int, default=100)
    parser.add_argument("--repo_id", type=str, default="obrookes/more_testing")
    parser.add_argument("--max_shard_size", type=str, default="10MB")
    parser.add_argument("--cache_dir", type=str, default=None)
    return parser.parse_args()


def data_generator(path_to_data):
    video_paths = glob(f"{path_to_data}/*.mp4")
    for video_path in video_paths:
        with open(video_path, "rb") as f:
            assert os.path.exists(
                video_path
            ), f"video_path: {video_path} does not exist!"
            item = {"video": f.read(), "filename": video_path.split("/")[-1]}
            yield item


if __name__ == "__main__":
    # "/home/dl18206/Desktop/phd/data/panaf/PanAf500/videos/raw/all"
    args = parse_args()

    all_generator = lambda: data_generator(path_to_data=args.path_to_data)

    data = datasets.Dataset.from_generator(
        all_generator,
        num_proc=mp.cpu_count(),
        writer_batch_size=args.writer_batch_size,
        cache_dir=args.cache_dir,
    )

    dataset = datasets.DatasetDict(
        {
            "train": data,
        }
    )
    succesful_competion = False
    while not succesful_competion:
        try:
            dataset.push_to_hub(
                repo_id=args.repo_id, max_shard_size=args.max_shard_size
            )
            succesful_competion = True
        except Exception as e:
            print(e)
