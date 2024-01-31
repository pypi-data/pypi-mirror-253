import torch
import contextlib
import functools
import torchvision
import numpy as np
from typing import Union
from einops import rearrange
from torch.utils.data.dataloader import DataLoader
from torchvision.transforms import Compose, Resize
from pytorchvideo.transforms import ApplyTransformToKey
from .byte_decoder import extract_frames_pyav, FrameSelectionMethod


class PanAfTransform:
    def __init__(
        self,
        num_frames: int = 32,
        image_size: int = 224,
        rng: np.random.Generator = np.random.default_rng(),
        frame_selection_method: FrameSelectionMethod = FrameSelectionMethod.RANDOM,
        video_transform: torchvision.transforms.Compose = None,
        starting_second: int = 0,
        ending_second: int = 15,
    ):
        self.num_frames = num_frames
        self.image_size = image_size
        self.rng = rng
        self.frame_selection_method = frame_selection_method
        self.video_transform = video_transform

    def get_video_from_bytes(
        self,
        video_bytes: Union[str, bytes],
    ):
        frames = extract_frames_pyav(
            video_data=video_bytes,
            modality="video",
            starting_second=0,  # TODO: auto-calculate this
            ending_second=15,  # TODO: auto-calculate this too...
            num_frames=self.num_frames,
            rng=self.rng,
            frame_selection_method=self.frame_selection_method,
        )
        return frames

    def get_video_tensors(self, frames):
        """Converts video frames into tensor format and applies transforms.

        Args:
            video_frames: Frames extracted from a video.
            image_size (int): The size for each video frame.

        Returns:
            Transformed video frames in tensor format.
        """
        video_frames = rearrange(frames, "t h w c -> c t h w")  # .to(torch.float32)
        video_transform = self.video_transform or Compose(
            [
                Resize((self.image_size, self.image_size)),
            ]
        )
        output_dict = ApplyTransformToKey("video", video_transform)(
            {"video": video_frames}
        )
        return rearrange(
            output_dict["video"], "c t h w -> t c h w"
        )  # if normalising then / 255.0

    def transform_batch(self, input_dict: dict):
        """
        Converts a dict of video bytes into a dict of video tensors and applies transform.
        Args:
            input_dict: Dict of video bytes i.e., {"video": video_bytes, "filename": filename}
        Returns:
            Dict of video tensors i.e., {"video": video_tensors, "filename": filename}
        """
        assert "video" in input_dict.keys()
        for idx in range(len(input_dict["video"])):
            frames = self.get_video_from_bytes(input_dict["video"][idx])
            input_dict["video"][idx] = self.get_video_tensors(frames)
        return input_dict

    def __call__(self, input_dict: dict):
        return self.transform_batch(input_dict)
