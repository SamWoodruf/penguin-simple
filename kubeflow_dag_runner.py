import os
from absl import logging
from tfx import v1 as tfx
from pipeline import _create_pipeline
from tfx.orchestration.kubeflow import kubeflow_dag_runner
from tfx.utils import telemetry_utils
import tempfile
import tensorflow as tf
import tensorflow_io as tfio

S3_BUCKET_NAME = 'kubeflow001'

PIPELINE_NAME = 'penguin-simple'

PIPELINE_ROOT = 's3://{}/pipeline_root/{}'.format(S3_BUCKET_NAME, PIPELINE_NAME)

MODULE_ROOT = 's3://{}/pipeline_module/{}'.format(S3_BUCKET_NAME, PIPELINE_NAME)

DATA_ROOT = 's3://{}/data/{}'.format(S3_BUCKET_NAME, PIPELINE_NAME)

SERVING_MODEL_DIR = 's3://{}/serving_module/{}'.format(S3_BUCKET_NAME, PIPELINE_NAME)

TRAINER_MODULE_FILE = 'penguin_trainer.py'

PIPELINE_DEFINITION_FILE = PIPELINE_NAME + '_pipeline.json'

TFX_IMAGE = 'public.ecr.aws/t5a1x0i0/tfx-image'

PIPELINE_DEFINITION_FILE = PIPELINE_NAME + '_pipeline.json'

logging.set_verbosity(logging.DEBUG)

metadata_config = kubeflow_dag_runner.get_default_kubeflow_metadata_config()
runner_config = kubeflow_dag_runner.KubeflowDagRunnerConfig(
        kubeflow_metadata_config=metadata_config,
        tfx_image=TFX_IMAGE)
     
kubeflow_dag_runner.KubeflowDagRunner(config=runner_config).run(
                                          _create_pipeline(
                                              pipeline_name=PIPELINE_NAME,
                                              pipeline_root=PIPELINE_ROOT,
                                              data_root=DATA_ROOT,
                                              module_file=os.path.join(MODULE_ROOT, TRAINER_MODULE_FILE),
                                              serving_model_dir=SERVING_MODEL_DIR))
