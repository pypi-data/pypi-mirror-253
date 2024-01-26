from inspect import currentframe
from typing import Generic, Mapping, Sequence, Type, TypeVar, Union, cast

T = TypeVar("T")
D = TypeVar("D", bound=Mapping)


class DictBuilder(Generic[D]):
    def __init__(self, mapping_type: Type[D] = dict):
        self.mapping_type = mapping_type

    def __getitem__(self, args: Union[slice, T, Sequence[Union[slice, T]]]) -> D:
        if not isinstance(args, tuple):
            args = (args,)  # type: ignore

        frame = currentframe()
        assert frame, "Unable to get the current frame."

        caller_frame = frame.f_back
        assert caller_frame, "Unable to get the caller's frame."

        obj = {}
        for arg in cast(Sequence[Union[slice, T]], args):
            if isinstance(arg, slice):
                assert isinstance(arg.start, str), "Key must be a string"
                obj[arg.start] = arg.stop
            else:
                for name, var in caller_frame.f_locals.items():
                    if var is arg:
                        obj[name] = arg
                        break

        return self.mapping_type(obj) if self.mapping_type is not dict else obj  # type: ignore
