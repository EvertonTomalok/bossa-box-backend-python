# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_response_not_ok 1'] = GenericRepr('<src.utils.response.Response object at 0x100000000>')

snapshots['test_response_ok 1'] = GenericRepr('<src.utils.response.Response object at 0x100000000>')
