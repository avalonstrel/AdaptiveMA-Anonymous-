#!/usr/bin/env python
# coding=utf-8
"""Return a pipeline automatically based on its name.
"""

from lmflow.pipeline.evaluator import Evaluator
from lmflow.pipeline.finetuner import Finetuner
from lmflow.pipeline.inferencer import Inferencer
from lmflow.pipeline.raft_aligner import RaftAligner
from lmflow.pipeline.raft_aligner_eval import RaftAligner as RaftAlignerEval
from lmflow.pipeline.continual_finetuner import ContinualFinetuner
from lmflow.pipeline.mask_finetuner import MaskFinetuner

PIPELINE_MAPPING = {
    "evaluator": Evaluator,
    "continual_finetuner": ContinualFinetuner,
    "mask_finetuner":MaskFinetuner,
    "finetuner": Finetuner,
    "inferencer": Inferencer,
    "raft_aligner": RaftAligner,
    "raft_aligner_eval": RaftAlignerEval,
}


class AutoPipeline:
    """ 
    The class designed to return a pipeline automatically based on its name.
    """
    @classmethod
    def get_pipeline(self,
        pipeline_name,
        model_args,
        data_args,
        pipeline_args,
        *args,
        **kwargs
    ):
        if pipeline_name not in PIPELINE_MAPPING:
            raise NotImplementedError(
                f'Pipeline "{pipeline_name}" is not supported'
            )

        pipeline = PIPELINE_MAPPING[pipeline_name](
            model_args,
            data_args,
            pipeline_args,
            *args,
            **kwargs
        )
        return pipeline
