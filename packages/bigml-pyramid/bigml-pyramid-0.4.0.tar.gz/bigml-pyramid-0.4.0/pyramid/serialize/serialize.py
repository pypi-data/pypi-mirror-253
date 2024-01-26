"""Serialization primitives for Laminar models and data

These functions define serialization primiatives used to write Laminar
models and data to temporary storage on disk.

"""

import math
import struct
import json
import multiprocessing

import numpy as np

from sensenet.constants import NUMERIC, CATEGORICAL, IMAGE
from sensenet.constants import MEAN, STANDARD_DEVIATION
from sensenet.constants import ZERO, ONE

CAT_CODE = 0
NUM_CODE = 1
BIN_CODE = 2
IMG_CODE = 3

BYTE = struct.Struct("B")
SIGNED_INT = struct.Struct("i")
UNSIGNED_INT = struct.Struct("I")
FLOAT = struct.Struct("f")
DOUBLE = struct.Struct("d")
TWO_INTS = struct.Struct("II")
TWO_FLOATS = struct.Struct("ff")
TWO_DOUBLES = struct.Struct("dd")
INT_FLOAT = struct.Struct("If")
NODE = struct.Struct("BIf")

# Make sure we don't start allocating like crazy if there's a bug;
# List sizes always come after this byte
LIST_HEADER_BYTE = 76  # ASCII 'L'


def serialize_boolean(abool):
    if abool:
        return BYTE.pack(1)
    else:
        return BYTE.pack(0)


def deserialize_boolean(abytes, offset):
    b = BYTE.unpack_from(abytes, offset=offset)[0]
    return True if b else False, 1


def serialize_int(anint):
    if anint is None:
        return serialize_boolean(False) + SIGNED_INT.pack(0)
    else:
        return serialize_boolean(True) + SIGNED_INT.pack(anint)


def deserialize_int(abytes, offset):
    is_int = deserialize_boolean(abytes, offset)[0]
    anint = SIGNED_INT.unpack_from(abytes, offset=offset + 1)[0]

    if is_int:
        return anint, 5
    else:
        return None, 5


def serialize_double(adouble):
    return DOUBLE.pack(adouble)


def deserialize_double(abytes, offset):
    adouble = DOUBLE.unpack_from(abytes, offset=offset)[0]
    return adouble, 8


def serialize_string(astr):
    if astr is not None and len(astr) > 0:
        strbytes = astr.encode("utf-8")
    else:
        strbytes = b""

    return UNSIGNED_INT.pack(len(strbytes)) + strbytes


def deserialize_string(abytes, offset):
    start = offset + 4
    slen = UNSIGNED_INT.unpack_from(abytes, offset=offset)[0]
    sbytes = abytes[start : start + slen]

    if slen > 0:
        return str(sbytes, "utf-8"), 4 + len(sbytes)
    else:
        return None, 4


def serialize_json(adict):
    try:
        return serialize_string(json.dumps(adict))
    except:
        print({k: type(adict[k]) for k in adict.keys()})
        raise ValueError()


def deserialize_json(abytes, offset):
    value, vlen = deserialize_string(abytes, offset)
    return json.loads(value), vlen


def serialize_list(alist, serializer):
    header = BYTE.pack(LIST_HEADER_BYTE)

    if alist:
        size = UNSIGNED_INT.pack(len(alist))
        return header + size + b"".join(serializer(x) for x in alist)
    else:
        return header + UNSIGNED_INT.pack(0)


def deserialize_list(abytes, offset, deserializer):
    output = []
    header = BYTE.unpack_from(abytes, offset=offset)[0]

    if header != LIST_HEADER_BYTE:
        raise ValueError("Header byte not encountered in deserialize_list")

    list_len = UNSIGNED_INT.unpack_from(abytes, offset=offset + 1)[0]
    total_bytes = 5

    for _ in range(list_len):
        value, vlen = deserializer(abytes, offset + total_bytes)
        output.append(value)
        total_bytes += vlen

    return output, total_bytes


def structure_or_none(atuple):
    if atuple[0]:
        return atuple
    else:
        return None, atuple[1]


def deserialize_list_or_none(abytes, offset, ser_fns):
    return structure_or_none(deserialize_list(abytes, offset, ser_fns))


def serialize_int_list(alist):
    return serialize_list(alist, serialize_int)


def deserialize_int_list(abytes, offset):
    return deserialize_list(abytes, offset, deserialize_int)


def serialize_double_list(alist):
    return serialize_list(alist, serialize_double)


def deserialize_double_list(abytes, offset):
    return deserialize_list(abytes, offset, deserialize_double)


def serialize_string_list(alist):
    return serialize_list(alist, serialize_string)


def deserialize_string_list(abytes, offset):
    return deserialize_list(abytes, offset, deserialize_string)


def serialize_tensor(atensor):
    if not atensor:
        return serialize_list([], serialize_int)
    else:
        atensor = np.array(atensor)

        dims = atensor.shape
        fvec = atensor.flatten()

        ser_dims = serialize_list(dims, serialize_int)
        ser_vals = struct.pack("%sf" % len(fvec), *fvec)

        return ser_dims + ser_vals


def deserialize_tensor(abytes, offset):
    dims, dsize = deserialize_list(abytes, offset, deserialize_int)

    if dims:
        total_size = np.prod(dims)
        foffset = offset + dsize
        fvec = struct.unpack_from("%sf" % total_size, abytes, offset=foffset)

        atensor = np.array(fvec).reshape(tuple(dims))
        return atensor.tolist(), dsize + total_size * 4
    else:
        return None, dsize


def serialize_map(adict, ser_fns):
    if adict:
        key_list = sorted(set(adict.keys()) & set(ser_fns.keys()))
    else:
        key_list = []

    ser_keys = serialize_string_list(key_list)

    ser_values = b""
    for key in key_list:
        ser_fn = ser_fns[key][0]
        ser_values += ser_fn(adict[key])

    return ser_keys + ser_values


def deserialize_map(abytes, offset, ser_fns):
    key_list, key_len = deserialize_string_list(abytes, offset)

    total_size = key_len
    outmap = {}

    for key in key_list:
        deser_fn = ser_fns[key][1]
        try:
            value, size = deser_fn(abytes, offset + total_size)
        except:
            raise ValueError(str((key, deser_fn)))

        outmap[key] = value
        total_size += size

    return outmap, total_size


def deserialize_map_or_none(abytes, offset, ser_fns):
    return structure_or_none(deserialize_map(abytes, offset, ser_fns))


FUNCTION_PAIRS = {
    "boolean": (serialize_boolean, deserialize_boolean),
    "int": (serialize_int, deserialize_int),
    "double": (serialize_double, deserialize_double),
    "string": (serialize_string, deserialize_string),
    "tensor": (serialize_tensor, deserialize_tensor),
    "list": (serialize_list, deserialize_list),
    "int_list": (serialize_int_list, deserialize_int_list),
    "double_list": (serialize_double_list, deserialize_double_list),
    "string_list": (serialize_string_list, deserialize_string_list),
    "map": (serialize_map, deserialize_map),
    "json": (serialize_json, deserialize_json),
}

IMAGE_FNS = {
    "outputs": FUNCTION_PAIRS["int"],
    "loading_method": FUNCTION_PAIRS["string"],
    "mean_image": FUNCTION_PAIRS["tensor"],
    "version": FUNCTION_PAIRS["string"],
    "input_image_shape": FUNCTION_PAIRS["int_list"],
    "output_indices": FUNCTION_PAIRS["int_list"],
    "base_image_network": FUNCTION_PAIRS["string"],
}


def serialize_preprocessor(adict):
    if "type" in adict:
        ftype = adict["type"]

        if ftype == CATEGORICAL:
            ptype = CAT_CODE
            ser_vals = serialize_string_list(adict.get("values", []))
        elif ftype == IMAGE:
            ptype = IMG_CODE
            ser_vals = b""
        elif ftype == NUMERIC:
            if ONE in adict:
                ptype = BIN_CODE
                v1, v2 = adict["zero_value"], adict["one_value"]
            else:
                ptype = NUM_CODE
                v1, v2 = adict.get(MEAN, -1), adict.get(STANDARD_DEVIATION, -1)

            ser_vals = TWO_DOUBLES.pack(v1, v2)
        else:
            raise ValueError('type of "%s" unknown!' % ftype)
    else:
        raise ValueError(
            "No type in adict with keys: %s" % str(sorted(adict.keys()))
        )

    if "index" in adict:
        return BYTE.pack(ptype) + UNSIGNED_INT.pack(adict["index"]) + ser_vals
    else:
        return BYTE.pack(ptype) + UNSIGNED_INT.pack(0) + ser_vals


def deserialize_preprocessor(abytes, offset, ignore_index=False):
    ptype = BYTE.unpack_from(abytes, offset=offset)[0]
    idx = UNSIGNED_INT.unpack_from(abytes, offset=offset + 1)[0]

    if ignore_index:
        output = {}
    else:
        output = {"index": idx}

    if ptype == CAT_CODE:
        values, vlen = deserialize_string_list(abytes, offset + 5)
        output["type"] = CATEGORICAL
        output["values"] = values
    elif ptype == IMG_CODE:
        # output, vlen = deserialize_map(abytes, offset + 5, IMAGE_FNS)
        vlen = 0
        output["index"] = idx
        output["type"] = IMAGE
    elif ptype == NUM_CODE or ptype == BIN_CODE:
        v1, v2 = TWO_DOUBLES.unpack_from(abytes, offset=offset + 5)
        output["type"] = NUMERIC
        vlen = 16

        if ptype == NUM_CODE:
            output[MEAN] = v1
            output[STANDARD_DEVIATION] = v2
        else:
            output[ZERO] = v1
            output[ONE] = v2
    else:
        raise ValueError("'%d' is not a preprocessor type!" % ptype)

    return output, vlen + 5


def serialize_preprocessors(alist):
    return serialize_list(alist, serialize_preprocessor)


def deserialize_preprocessors(abytes, offset):
    return deserialize_list(abytes, offset, deserialize_preprocessor)
