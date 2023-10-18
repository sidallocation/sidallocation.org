#! /usr/bin/env python
#
# SPDX-License-Identifier: MIT

import sys
import yaml


def yaml_construct_mapping(loader, node):
    """A custom YAML loader for mappings so we can error out on
    duplicate keys."""
    loader.flatten_mapping(node)
    duplicates = set()
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in duplicates:
            raise ValueError(f"Duplicate key found: {key}")
        duplicates.add(key)
        value = loader.construct_object(value_node)
        mapping[key] = value
    return mapping


yaml.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    yaml_construct_mapping,
    Loader=yaml.SafeLoader,
)


def load_allocations(file_path):
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
        return data


def flatten(allocations):
    flattened = []

    for id, allocation in allocations.items():
        ranges = allocation["ranges"]
        del allocation["ranges"]
        for range in ranges:
            allocation = allocation.copy()
            allocation["id"] = id
            allocation["range"] = range
            flattened.append(allocation)

    return flattened


def check_overlap(allocations):
    for idx, entry in enumerate(allocations):
        if idx > 0:
            prev = allocations[idx - 1]
            prev_end = prev["range"]["start"] + prev["range"]["size"]
            if entry["range"]["start"] < prev_end:
                print(
                    "ERROR: {} overlaps {}".format(entry["id"], prev["id"]),
                    file=sys.stderr,
                )


def main():
    allocations = load_allocations("allocations.yml")
    meta = allocations["meta"]

    # First we expand all the entries so each SID range is its own
    # entry. For example, if one organization has multiple ranges
    # listed, this will expand that entry into multiple entries.
    allocations = flatten(allocations["allocations"])

    # Now that each range is its own entry, sort by the start of the
    # range.
    allocations = sorted(allocations, key=lambda e: e["range"]["start"])
    check_overlap(allocations)

    formatted = []

    for allocation in allocations:
        start = allocation["range"]["start"]
        size = allocation["range"]["size"]
        last = start + size - 1
        formatted.append(
            ["{}-{}".format(start, last), allocation["org"], allocation["note"]]
        )

    # Make all cells have the same width per column.
    col_lens = []
    for i in range(len(formatted[0])):
        max_len = max([len(formatted[i]) for formatted in formatted])
        for entry in formatted:
            entry[i] = entry[i].ljust(max_len)
        col_lens.append(max_len)

    print("# {}\n\n{}\n\n".format(meta["title"], meta["preamble"]), end="")

    print(
        "| {} | {} | {} |".format(
            "SID Range".ljust(col_lens[0]),
            "Organization".ljust(col_lens[1]),
            "Note".ljust(col_lens[2]),
        )
    )
    print(
        "| {} | {} | {} |".format(
            ":-".ljust(col_lens[0]), ":-".ljust(col_lens[1]), ":-".ljust(col_lens[2])
        )
    )
    for allocation in formatted:
        print("| {} |".format(" | ".join(allocation)))


if __name__ == "__main__":
    sys.exit(main())
