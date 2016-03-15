﻿#!/usr/bin/env python
#
# VMEncryption extension
#
# Copyright 2015 Microsoft Corporation
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
#
# Requires Python 2.7+
#
import os.path
from Common import CommonVariables

class ProcessLock(object):
    def __init__(self, logger, lock_file_path):
        self.logger = logger
        self.lock_file_path = lock_file_path
        self.fs = None

    def try_lock(self):
        try:
            self.fs = open(f,"a+")
            return True
        except Exception as e:
            self.logger.log("could not acquire a lock")
            return False

    def release_lock(self):
        self.fs.close()