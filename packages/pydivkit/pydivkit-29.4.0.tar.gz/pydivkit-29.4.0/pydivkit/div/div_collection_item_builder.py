# Generated code. Do not modify.
# flake8: noqa: F401, F405, F811

from __future__ import annotations

import enum
import typing

from pydivkit.core import BaseDiv, Expr, Field

from . import div


class DivCollectionItemBuilder(BaseDiv):

    def __init__(
        self, *,
        data: typing.Optional[typing.Sequence[typing.Any]] = None,
        data_element_name: typing.Optional[typing.Union[Expr, str]] = None,
        prototypes: typing.Optional[typing.Sequence[DivCollectionItemBuilderPrototype]] = None,
        **kwargs: typing.Any,
    ):
        super().__init__(
            data=data,
            data_element_name=data_element_name,
            prototypes=prototypes,
            **kwargs,
        )

    data: typing.Sequence[typing.Any] = Field(
        description="Data that will be used to create collection items.",
    )
    data_element_name: typing.Optional[typing.Union[Expr, str]] = Field(
        description=(
            "Name for accessing the next `data` element in the "
            "prototype. Working with thiselement is like working with "
            "DivKit dictionaries."
        ),
    )
    prototypes: typing.Sequence[DivCollectionItemBuilderPrototype] = Field(
        min_items=1, 
        description=(
            "Array of `div` from which the collection items will be "
            "created."
        ),
    )


class DivCollectionItemBuilderPrototype(BaseDiv):

    def __init__(
        self, *,
        div: typing.Optional[div.Div] = None,
        selector: typing.Optional[typing.Union[Expr, bool]] = None,
        **kwargs: typing.Any,
    ):
        super().__init__(
            div=div,
            selector=selector,
            **kwargs,
        )

    div: div.Div = Field(
        description=(
            "`Div` from which the collection items will be created. In "
            "`Div`, you can useexpressions using data from `data`, to "
            "access the next `data` element, you needto use the same "
            "prefix as in `data_element_prefix`."
        ),
    )
    selector: typing.Optional[typing.Union[Expr, bool]] = Field(
        description=(
            "A condition that is used to select a prototype for the next "
            "item in thecollection. If there is more than 1 true "
            "condition, the prototype that is earlierwill be selected. "
            "If none of the conditions are met, the data element will "
            "beskipped."
        ),
    )


DivCollectionItemBuilderPrototype.update_forward_refs()


DivCollectionItemBuilder.update_forward_refs()
