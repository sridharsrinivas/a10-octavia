# Copyright 2019 A10 Networks
# All Rights Reserved.
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

from octavia.common import exceptions
from octavia.i18n import _
from octavia.network import base


class NoDatabaseURL(exceptions.OctaviaException):
    message = _("Must set db connection url in configuration file.")


class PortCreationFailedException(base.NetworkException):
    pass


class DeallocateTrunkException(base.NetworkException):
    pass


class AllocateTrunkException(base.NetworkException):
    pass


class VRIDIPNotInSubentRangeError(base.NetworkException):
    pass
