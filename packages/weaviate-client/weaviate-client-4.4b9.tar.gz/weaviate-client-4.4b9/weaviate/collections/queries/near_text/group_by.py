from typing import Generic, List, Literal, Optional, Type, Union, overload

from weaviate.collections.classes.filters import (
    _Filters,
)
from weaviate.collections.classes.grpc import (
    METADATA,
    PROPERTIES,
    REFERENCES,
    Move,
)
from weaviate.collections.classes.internal import (
    _GroupBy,
    GroupByReturn,
    ReturnProperties,
    ReturnReferences,
    _QueryOptions,
    References,
    TReferences,
    CrossReferences,
)
from weaviate.collections.classes.types import Properties, TProperties
from weaviate.collections.queries.base import _BaseQuery
from weaviate.warnings import _Warnings
from weaviate.types import NUMBER


class _NearTextGroupBy(Generic[Properties, References], _BaseQuery[Properties, References]):
    @overload
    def near_text(
        self,
        query: Union[List[str], str],
        group_by_property: str,
        number_of_groups: int,
        objects_per_group: int,
        certainty: Optional[NUMBER] = None,
        distance: Optional[NUMBER] = None,
        move_to: Optional[Move] = None,
        move_away: Optional[Move] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        auto_limit: Optional[int] = None,
        filters: Optional[_Filters] = None,
        include_vector: bool = False,
        return_metadata: Optional[METADATA] = None,
        *,
        return_properties: Optional[PROPERTIES] = None,
        return_references: Literal[None] = None,
    ) -> GroupByReturn[Properties, References]:
        ...

    @overload
    def near_text(
        self,
        query: Union[List[str], str],
        group_by_property: str,
        number_of_groups: int,
        objects_per_group: int,
        certainty: Optional[NUMBER] = None,
        distance: Optional[NUMBER] = None,
        move_to: Optional[Move] = None,
        move_away: Optional[Move] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        auto_limit: Optional[int] = None,
        filters: Optional[_Filters] = None,
        include_vector: bool = False,
        return_metadata: Optional[METADATA] = None,
        *,
        return_properties: Optional[PROPERTIES] = None,
        return_references: REFERENCES,
    ) -> GroupByReturn[Properties, CrossReferences]:
        ...

    @overload
    def near_text(
        self,
        query: Union[List[str], str],
        group_by_property: str,
        number_of_groups: int,
        objects_per_group: int,
        certainty: Optional[NUMBER] = None,
        distance: Optional[NUMBER] = None,
        move_to: Optional[Move] = None,
        move_away: Optional[Move] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        auto_limit: Optional[int] = None,
        filters: Optional[_Filters] = None,
        include_vector: bool = False,
        return_metadata: Optional[METADATA] = None,
        *,
        return_properties: Optional[PROPERTIES] = None,
        return_references: Type[TReferences],
    ) -> GroupByReturn[Properties, TReferences]:
        ...

    @overload
    def near_text(
        self,
        query: Union[List[str], str],
        group_by_property: str,
        number_of_groups: int,
        objects_per_group: int,
        certainty: Optional[NUMBER] = None,
        distance: Optional[NUMBER] = None,
        move_to: Optional[Move] = None,
        move_away: Optional[Move] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        auto_limit: Optional[int] = None,
        filters: Optional[_Filters] = None,
        include_vector: bool = False,
        return_metadata: Optional[METADATA] = None,
        *,
        return_properties: Type[TProperties],
        return_references: Literal[None] = None,
    ) -> GroupByReturn[TProperties, References]:
        ...

    @overload
    def near_text(
        self,
        query: Union[List[str], str],
        group_by_property: str,
        number_of_groups: int,
        objects_per_group: int,
        certainty: Optional[NUMBER] = None,
        distance: Optional[NUMBER] = None,
        move_to: Optional[Move] = None,
        move_away: Optional[Move] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        auto_limit: Optional[int] = None,
        filters: Optional[_Filters] = None,
        include_vector: bool = False,
        return_metadata: Optional[METADATA] = None,
        *,
        return_properties: Type[TProperties],
        return_references: REFERENCES,
    ) -> GroupByReturn[TProperties, CrossReferences]:
        ...

    @overload
    def near_text(
        self,
        query: Union[List[str], str],
        group_by_property: str,
        number_of_groups: int,
        objects_per_group: int,
        certainty: Optional[NUMBER] = None,
        distance: Optional[NUMBER] = None,
        move_to: Optional[Move] = None,
        move_away: Optional[Move] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        auto_limit: Optional[int] = None,
        filters: Optional[_Filters] = None,
        include_vector: bool = False,
        return_metadata: Optional[METADATA] = None,
        *,
        return_properties: Type[TProperties],
        return_references: Type[TReferences],
    ) -> GroupByReturn[TProperties, TReferences]:
        ...

    def near_text(
        self,
        query: Union[List[str], str],
        group_by_property: str,
        number_of_groups: int,
        objects_per_group: int,
        certainty: Optional[NUMBER] = None,
        distance: Optional[NUMBER] = None,
        move_to: Optional[Move] = None,
        move_away: Optional[Move] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        auto_limit: Optional[int] = None,
        filters: Optional[_Filters] = None,
        include_vector: bool = False,
        return_metadata: Optional[METADATA] = None,
        *,
        return_properties: Optional[ReturnProperties[TProperties]] = None,
        return_references: Optional[ReturnReferences[TReferences]] = None,
    ) -> Union[
        GroupByReturn[Properties, References],
        GroupByReturn[Properties, CrossReferences],
        GroupByReturn[Properties, TReferences],
        GroupByReturn[TProperties, References],
        GroupByReturn[TProperties, CrossReferences],
        GroupByReturn[TProperties, TReferences],
    ]:
        """Group the results of a by-text object search in this collection using an text-capable vectorisation module and vector-based similarity search.

        See the [docs](https://weaviate.io/developers/weaviate/api/graphql/search-operators#neartext) for a more detailed explanation.

        NOTE:
            You must have a text-capable vectorisation module installed in order to use this method, e.g. any of the `text2vec-` and `multi2vec-` modules.

        Arguments:
            `query`
                The text or texts to search on, REQUIRED.
            `group_by_property`
                The property to group by, REQUIRED.
            `number_of_groups`
                The number of groups to return, REQUIRED.
            `objects_per_group`
                The number of objects to return per group, REQUIRED.
            `certainty`
                The minimum similarity score to return. If not specified, the default certainty specified by the server is used.
            `distance`
                The maximum distance to search. If not specified, the default distance specified by the server is used.
            `limit`
                The maximum number of results to return. If not specified, the default limit specified by the server is returned.
            `offset`
                The offset to start from. If not specified, the retrieval begins from the first object in the server.
            `auto_limit`
                The maximum number of [autocut](https://weaviate.io/developers/weaviate/api/graphql/additional-operators#autocut) results to return. If not specified, no limit is applied.
            `filters`
                The filters to apply to the search.
            `include_vector`
                Whether to include the vector in the results. If not specified, this is set to False.
            `return_metadata`
                The metadata to return for each object, defaults to `None`.
            `return_properties`
                The properties to return for each object.
            `return_references`
                The references to return for each object.

        NOTE:
            - If `return_properties` is not provided then all properties are returned except for blob properties.
            - If `return_metadata` is not provided then no metadata is provided.
            - If `return_references` is not provided then no references are provided.

        Returns:
            A `GroupByReturn` object that includes the searched objects grouped by the specified property.

        Raises:
            `weaviate.exceptions.WeaviateGRPCQueryError`:
                If the request to the Weaviate server fails.
        """
        _Warnings.old_query_group_by_namespace("query.near_text", "query_group_by")
        res = self._query().near_text(
            near_text=query,
            certainty=certainty,
            distance=distance,
            move_to=move_to,
            move_away=move_away,
            limit=limit,
            offset=offset,
            autocut=auto_limit,
            filters=filters,
            group_by=_GroupBy(
                prop=group_by_property,
                number_of_groups=number_of_groups,
                objects_per_group=objects_per_group,
            ),
            return_metadata=self._parse_return_metadata(return_metadata, include_vector),
            return_properties=self._parse_return_properties(return_properties),
            return_references=self._parse_return_references(return_references),
        )
        return self._result_to_groupby_return(
            res,
            _QueryOptions.from_input(
                return_metadata,
                return_properties,
                include_vector,
                self._references,
                return_references,
            ),
            return_properties,
            return_references,
        )
