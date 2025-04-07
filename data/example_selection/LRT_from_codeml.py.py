#!/usr/bin/env python3

import sys
import re
from scipy.stats import chi2

def extract_likelihood_and_params(file_path):
    logL = None
    nparams = None
    with open(file_path) as f:
        for line in f:
            if "lnL(ntime:" in line:
                match = re.search(r"lnL\(ntime:\s+\d+\s+np:\s+(\d+)\):\s+([-\d.]+)", line)
                if match:
                    nparams = int(match.group(1))
                    logL = float(match.group(2))
                    break
    if logL is None or nparams is None:
        raise ValueError(f"Could not extract likelihood and parameter count from {file_path}")
    return logL, nparams

def compute_lrt(logL1, logL2, k1, k2):
    if k1 == k2:
        raise ValueError("Models have the same number of parameters; LRT not applicable.")
    if k1 > k2:
        logL_complex, logL_simple = logL1, logL2
        df = k1 - k2
    else:
        logL_complex, logL_simple = logL2, logL1
        df = k2 - k1
    LR_stat = 2 * (logL_complex - logL_simple)
    p_value = chi2.sf(LR_stat, df)
    return LR_stat, df, p_value

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: lrt_from_codeml.py <codeml_output1> <codeml_output2>")
        sys.exit(1)

    file1, file2 = sys.argv[1], sys.argv[2]

    try:
        logL1, k1 = extract_likelihood_and_params(file1)
        logL2, k2 = extract_likelihood_and_params(file2)

        LR, df, p = compute_lrt(logL1, logL2, k1, k2)

        print(f"Model 1: logL = {logL1}, parameters = {k1}")
        print(f"Model 2: logL = {logL2}, parameters = {k2}")
        print(f"\nLRT statistic: {LR:.4f}")
        print(f"Degrees of freedom: {df}")
        print(f"P-value: {p:.4g}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

