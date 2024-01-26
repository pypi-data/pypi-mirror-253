"""Functions for data serialization

These functions are used to read and write training data to a standard
format for quick reading from disk when needed.

"""

import math
import struct

from sensenet.constants import NUMERIC, CATEGORICAL, IMAGE

import pyramid.serialize.serialize as ser

DATA_HEADER_BYTE = 68  # ASCII 'D'
MAX_ROW_MEMORY = 32 * 1024 * 1024
MAX_FILE_NAME_LENGTH = 32


def row_max(row_length):
    """Return a maximum number of rows to read into memory

    Given a byte length for a row, return a sensible number of rows to
    return that will not overwhelm the memory of any reasonable system.

    """
    return max(1, int(math.floor(MAX_ROW_MEMORY / float(row_length))))


def add_format_values(current_fmt, n_float, current_is_image):
    next_fmt = current_fmt

    if n_float > 0:
        if n_float > 1:
            next_fmt += str(n_float)

        next_fmt += "d"

    if current_is_image:
        return next_fmt + ("%dp" % MAX_FILE_NAME_LENGTH)
    else:
        return next_fmt


def serialization_format(info_list):
    ser_fmt = "<"
    n_float = 0

    for info in info_list:
        if info["type"] in [NUMERIC, CATEGORICAL]:
            n_float += 1
        elif info["type"] == IMAGE:
            ser_fmt = add_format_values(ser_fmt, n_float, True)
            n_float = 0

    ser_fmt = add_format_values(ser_fmt, n_float, False)

    return ser_fmt


def read_header_info(fin):
    head_bytes = fin.read(1)
    sentry_byte = ser.BYTE.unpack_from(head_bytes, 0)[0]

    if sentry_byte != DATA_HEADER_BYTE:
        raise ValueError(
            "First byte is %d != %d" % (sentry_byte, DATA_HEADER_BYTE)
        )


def lazy_rows(fin, info_list, index_set):
    """Lazily read a sequence of data rows from an input stream

    Given an open input stream, generate data rows from the stream,
    according to the header information present at the start of the
    stream.  Reads MAX_ROW_MEMORY bytes into memory at a time and
    yields the rows present in that chunk before reading again.

    """
    read_header_info(fin)

    fmt = serialization_format(info_list)
    unpacker = struct.Struct(fmt)

    max_rows = row_max(unpacker.size)
    bytes_per_read = max_rows * unpacker.size

    data = fin.read(bytes_per_read)
    row_idx = 0

    while data:
        start = 0

        while start < len(data):
            if index_set is None or row_idx in index_set:
                yield list(unpacker.unpack_from(data, start))

            start += unpacker.size
            row_idx += 1

        data = fin.read(bytes_per_read)
