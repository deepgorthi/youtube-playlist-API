#!/usr/bin/env python3

import re

class TimePattern:

    def __init__(self):
        self.hour_pattern = re.compile(r'(\d+)H')
        self.minute_pattern = re.compile(r'(\d+)M')
        self.second_pattern = re.compile(r'(\d+)S')
