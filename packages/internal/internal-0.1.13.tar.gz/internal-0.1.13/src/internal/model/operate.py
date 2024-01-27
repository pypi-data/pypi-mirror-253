from typing import Optional

from .base_model import InternalBaseModel
from deepdiff import DeepDiff


class Operate:
    add: Optional[dict] = None
    remove: Optional[dict] = None
    change: Optional[dict] = None

    @classmethod
    async def compare_diff(cls, original: dict, compare: dict):
        original = cls.remove_ignore_field(original)
        compare = cls.remove_ignore_field(compare)

        diff_result = DeepDiff(original, compare, ignore_order=True)
        if not diff_result:
            return None

        operate = Operate(
            add=diff_result.get("iterable_items_added", None),
            remove=diff_result.get("iterable_items_removed", None),
            change=diff_result.get("values_changed", None)
        )
        return operate

    @classmethod
    async def remove_ignore_field(cls, model_dict: dict):
        return {k: v for k, v in model_dict.items() if k not in ['create_time', 'update_time']}
