# Copyright 2023 BMW AG
# SPDX-License-Identifier: MPL-2.0

import xmlschema
import pathlib

list(pathlib.Path('../../../').glob('*.srmd'))

xs = xmlschema.XMLSchema11('SSPTraceability/SRMD.xsd')

for srmd_file in pathlib.Path('../../../').glob('*.srmd'):
    print("Validating " + str(srmd_file))
    xs.validate(srmd_file)
