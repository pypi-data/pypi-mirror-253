"""
Helper functions for encoding python types into eth-abi format
"""
from typing import Union

import numpy as np
from eth_abi import encode, is_encodable  # type: ignore


def convert_sd59x18(num: float) -> int:
    """Converts floating point number to sd59x18 number

    Args:
        num (float): input floating point

    Returns:
        int: output sd59x18 number
    """

    # Convert to string
    num_str: str = np.format_float_positional(num)

    # Split at decimal
    split: list[str] = num_str.split(".")

    # Collect leading number
    leading: str = split[0]
    # Collect trailing decimals
    decimals: str = split[1]

    # Parse leading number
    leading_first_char_negative: bool = leading[0] == "-"
    if leading_first_char_negative:
        # Strip negative
        leading = leading[1:]
    # Parse for 0-case
    if int(leading) == 0:
        leading = ""

    # Parse trailing decimals
    if len(decimals) > 18:
        # Trim to 18 decimal precision
        decimals = decimals[:18]
    # Pad ending decimals
    zeroes = (18 - len(decimals)) * "0"
    decimals = f"{decimals}{zeroes}"
    # Remove leading zeroes
    decimals = decimals.lstrip("0")

    return int(f"{'-' if leading_first_char_negative else ''}{leading}{decimals}")


def encode_multidim_array(arr: list[Union[int, float]], flatten: bool = True) -> bytes:
    """encodes multi dimensional (including single dim) array,
     optionally flattening if needed.
    For floats, we encode to sd59x18 representation. We keep int as is.

    Args:
        arr (list[Union[int, float]]): array to encode
        flatten (bool, optional): whether or not to flatten the array. Defaults to True.

    Raises:
        ValueError: if non int or float array passed in
        ValueError: if there is error in encoding

    Returns:
        bytes: raw bytes encoded values
    """
    np_arr = np.array(arr)
    if flatten:
        np_arr = np_arr.reshape([-1])
    shape = np.shape(np_arr)

    converted = None
    if np.issubdtype(np_arr.dtype.type, np.floating):
        # encode float array
        vectorized = np.vectorize(convert_sd59x18)
        converted = vectorized(np_arr).tolist()
    elif np.issubdtype(np_arr.dtype.type, np.integer):
        # already int type, no need to encode
        converted = np_arr.tolist()
    else:
        raise ValueError(
            f"Only int or float arrays supported, but found {np_arr.dtype}"
        )

    if flatten:
        solidity_type_str = "int256[]"
    else:
        arr_str = ["int256"]
        arr_str = arr_str + ["[]" for x in shape]
        solidity_type_str = "".join(arr_str)

    if is_encodable(solidity_type_str, converted):
        return encode([solidity_type_str], [converted])  # type: ignore
    else:
        raise ValueError(
            f"Cannot encode {converted} into {solidity_type_str}. flatten = {flatten}"
        )


def encode_vector(vector: list[float]) -> bytes:
    """Parses vector to int256[] sd59x18 bytes

    Args:
        vector (list[float]): input vector

    Returns:
        bytes: output int256[] sd59x18 bytes representation
    """

    # Convert all floats to sd59x18
    converted: list[int] = []
    for vec in vector:
        converted.append(convert_sd59x18(vec))

    # Encode to int256[]
    return encode(["int256[]"], [converted])  # type: ignore
