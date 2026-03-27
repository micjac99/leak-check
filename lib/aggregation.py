from typing import Sequence, Optional, Iterable


def clean_str_set(values: Iterable[Optional[str]]) -> list[str]:
    return list({
        v.strip()
        for v in values
        if v and str(v).strip()
    })


def clean_int_set(values: Iterable) -> list[int]:
    result = set()
    for v in values:
        try:
            if v is not None and str(v).strip():
                result.add(int(v))
        except (TypeError, ValueError):
            continue
    return list(result)


def clean_id_set(values: Iterable) -> list[str]:
    return list({
        str(v)
        for v in values
        if v is not None
    })