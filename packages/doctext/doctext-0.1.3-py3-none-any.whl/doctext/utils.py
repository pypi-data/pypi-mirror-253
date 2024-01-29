#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

def run_checked(command) -> bool:
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)    
    if result.returncode != 0:
        return False
    return True