#    Copyright 2020, A10 Networks
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import acos_client
import mock
from unittest.mock import patch

from octavia.tests.unit import base

from a10_octavia.controller.worker.tasks.handler_virtual_server import CreateVirtualServerTask
from octavia.common import data_models as o_data_models
from octavia.tests.common import constants as t_constants
from a10_octavia.common.data_models import VThunder

AMPHORA = o_data_models.Amphora(id=t_constants.MOCK_AMP_ID1)
VTHUNDER = VThunder()
LB = o_data_models.LoadBalancer(id=123, amphorae=[AMPHORA])

class TestCreateVirtualServerTask(base.TestCase):

    def setUp(self):
        patcher = patch(
            'a10_octavia.controller.worker.tasks.common.BaseVThunderTask.client_factory')
        self.client_factory_mock = patcher.start()
        self.client_factory_mock.return_value = mock.Mock()
        super(TestCreateVirtualServerTask, self).setUp()

    def test_revert_create_virtual_server_task(self):
        net = CreateVirtualServerTask()
        net.revert(LB, VTHUNDER)
        self.client_factory_mock.return_value.slb.virtual_server.delete.assert_called_with(LB.id) 
