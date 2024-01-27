from typing import Any, Callable, Dict

import pytorch_lightning as pl
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim.lr_scheduler import LambdaLR


class LitSourceSeparation(pl.LightningModule):
    def __init__(
        self,
        batch_data_preprocessor,
        model: nn.Module,
        loss_function: Callable,
        optimizer_type: str,
        learning_rate: float,
        lr_lambda: Callable,
    ):
        r"""Pytorch Lightning wrapper of PyTorch model, including forward,
        optimization of model, etc.

        Args:
            batch_data_preprocessor: object, used for preparing inputs and
                targets for training. E.g., BasicBatchDataPreprocessor is used
                for preparing data in dictionary into tensor.
            model: nn.Module
            loss_function: function
            learning_rate: float
            lr_lambda: function
        """
        super().__init__()

        self.batch_data_preprocessor = batch_data_preprocessor
        self.model = model
        self.optimizer_type = optimizer_type
        self.loss_function = loss_function
        self.learning_rate = learning_rate
        self.lr_lambda = lr_lambda

    def training_step(self, batch_data_dict: Dict, batch_idx: int) -> torch.float:
        r"""Forward a mini-batch data to model, calculate loss function, and
        train for one step. A mini-batch data is evenly distributed to multiple
        devices (if there are) for parallel training.

        Args:
            batch_data_dict: e.g. {
                'vocals': (batch_size, channels_num, segment_samples),
                'accompaniment': (batch_size, channels_num, segment_samples),
                'mixture': (batch_size, channels_num, segment_samples)
            }
            batch_idx: int

        Returns:
            loss: float, loss function of this mini-batch
        """
        input_dict, target_dict = self.batch_data_preprocessor(batch_data_dict)
        # input_dict: {
        #     'waveform': (batch_size, channels_num, segment_samples),
        #     (if_exist) 'condition': (batch_size, channels_num),
        # }
        # target_dict: {
        #     'waveform': (batch_size, target_sources_num * channels_num, segment_samples),
        # }

        # Forward.
        self.model.train()

        output_dict = self.model(input_dict)
        # output_dict: {
        #     'waveform': (batch_size, target_sources_num * channels_num, segment_samples),
        # }

        outputs = output_dict['waveform']
        # outputs:, e.g, (batch_size, target_sources_num * channels_num, segment_samples)

        # Calculate loss.
        loss = self.loss_function(
            output=outputs,
            target=target_dict['waveform'],
            mixture=input_dict['waveform'],
        )

        return loss

    def configure_optimizers(self) -> Any:
        r"""Configure optimizer."""

        if self.optimizer_type == "Adam":
            optimizer = optim.Adam(
                self.model.parameters(),
                lr=self.learning_rate,
                betas=(0.9, 0.999),
                eps=1e-08,
                weight_decay=0.0,
                amsgrad=True,
            )

        elif self.optimizer_type == "AdamW":
            optimizer = optim.AdamW(
                self.model.parameters(),
                lr=self.learning_rate,
                betas=(0.9, 0.999),
                eps=1e-08,
                weight_decay=0.0,
                amsgrad=True,
            )

        else:
            raise NotImplementedError

        scheduler = {
            'scheduler': LambdaLR(optimizer, self.lr_lambda),
            'interval': 'step',
            'frequency': 1,
        }

        return [optimizer], [scheduler]


def get_model_class(model_type):
    r"""Get model.

    Args:
        model_type: str, e.g., 'ResUNet143_DecouplePlusInplaceABN'

    Returns:
        nn.Module
    """
    if model_type == 'ResUNet143_DecouplePlusInplaceABN_ISMIR2021':
        from bytesep.models.resunet_ismir2021 import (
            ResUNet143_DecouplePlusInplaceABN_ISMIR2021,
        )

        return ResUNet143_DecouplePlusInplaceABN_ISMIR2021

    elif model_type == 'UNet':
        from bytesep.models.unet import UNet

        return UNet

    elif model_type == 'UNetSubbandTime':
        from bytesep.models.unet_subbandtime import UNetSubbandTime

        return UNetSubbandTime

    elif model_type == 'ResUNet143_Subbandtime':
        from bytesep.models.resunet_subbandtime import ResUNet143_Subbandtime

        return ResUNet143_Subbandtime

    elif model_type == 'ResUNet143_DecouplePlus':
        from bytesep.models.resunet import ResUNet143_DecouplePlus

        return ResUNet143_DecouplePlus

    elif model_type == 'ConditionalUNet':
        from bytesep.models.conditional_unet import ConditionalUNet

        return ConditionalUNet

    elif model_type == 'LevelRNN':
        from bytesep.models.levelrnn import LevelRNN

        return LevelRNN

    elif model_type == 'WavUNet':
        from bytesep.models.wavunet import WavUNet

        return WavUNet

    elif model_type == 'WavUNetLevelRNN':
        from bytesep.models.wavunet_levelrnn import WavUNetLevelRNN

        return WavUNetLevelRNN

    elif model_type == 'TTnet':
        from bytesep.models.ttnet import TTnet

        return TTnet

    elif model_type == 'TTnetNoTransformer':
        from bytesep.models.ttnet_no_transformer import TTnetNoTransformer

        return TTnetNoTransformer

    elif model_type == 'JiafengCNN':
        from bytesep.models.ttnet_jiafeng import JiafengCNN

        return JiafengCNN

    else:
        raise NotImplementedError
