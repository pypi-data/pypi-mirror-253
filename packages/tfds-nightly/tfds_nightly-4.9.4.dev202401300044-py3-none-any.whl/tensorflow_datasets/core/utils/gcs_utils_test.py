# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""GCS utils test."""

from tensorflow_datasets import testing
from tensorflow_datasets.core.utils import gcs_utils
from tensorflow_datasets.testing import test_utils


class GcsUtilsDisabledTest(testing.TestCase):

  DO_NOT_APPLY_FIXTURES = [test_utils.disable_gcs_access]

  def test_is_dataset_accessible(self):
    is_ds_on_gcs = gcs_utils.is_dataset_on_gcs('mnist/1.0.0')
    self.assertTrue(is_ds_on_gcs)


if __name__ == '__main__':
  testing.test_main()
