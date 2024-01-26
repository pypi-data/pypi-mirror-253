from typing import List, Literal, Optional, Union, overload

from weaviate.collections.aggregations.base import _Aggregate
from weaviate.collections.classes.aggregate import (
    PropertiesMetrics,
    _AggregateReturn,
    _AggregateGroupByReturn,
    _AggregateGroup,
)
from weaviate.collections.classes.filters import _Filters
from weaviate.warnings import _Warnings


class _NearVector(_Aggregate):
    @overload
    def near_vector(
        self,
        near_vector: List[float],
        *,
        certainty: Optional[Union[float, int]] = None,
        distance: Optional[Union[float, int]] = None,
        object_limit: Optional[int] = None,
        filters: Optional[_Filters] = None,
        group_by: Literal[None] = None,
        limit: Optional[int] = None,
        total_count: bool = True,
        return_metrics: Optional[PropertiesMetrics] = None,
    ) -> _AggregateReturn:
        ...

    @overload
    def near_vector(
        self,
        near_vector: List[float],
        *,
        certainty: Optional[Union[float, int]] = None,
        distance: Optional[Union[float, int]] = None,
        object_limit: Optional[int] = None,
        filters: Optional[_Filters] = None,
        group_by: str,
        limit: Optional[int] = None,
        total_count: bool = True,
        return_metrics: Optional[PropertiesMetrics] = None,
    ) -> _AggregateGroupByReturn:
        ...

    def near_vector(
        self,
        near_vector: List[float],
        *,
        certainty: Optional[Union[float, int]] = None,
        distance: Optional[Union[float, int]] = None,
        object_limit: Optional[int] = None,
        filters: Optional[_Filters] = None,
        group_by: Optional[str] = None,
        limit: Optional[int] = None,
        total_count: bool = True,
        return_metrics: Optional[PropertiesMetrics] = None,
    ) -> Union[_AggregateReturn, _AggregateGroupByReturn]:
        """Aggregate metrics over the objects returned by a near vector search on this collection.

        At least one of `certainty`, `distance`, or `object_limit` must be specified here for the vector search.

        This method requires that the objects in the collection have associated vectors.

        Arguments:
            `near_vector`
                The vector to search on.
            `certainty`
                The minimum certainty of the vector search.
            `distance`
                The maximum distance of the vector search.
            `object_limit`
                The maximum number of objects to return from the vector search prior to the aggregation.
            `filters`
                The filters to apply to the search.
            `group_by`
                The property name to group the aggregation by.
            `limit`
                The maximum number of aggregated objects to return.
            `total_count`
                Whether to include the total number of objects that match the query in the response.
            `return_metrics`
                A list of property metrics to aggregate together after the text search.

        Returns:
            Depending on the presence of the `group_by` argument, either a `_AggregateReturn` object or a `_AggregateGroupByReturn that includes the aggregation objects.

        Raises:
            `weaviate.exceptions.WeaviateGQLQueryError`:
                If an error occurs while performing the query against Weaviate.
        """
        return_metrics = (
            return_metrics
            if (return_metrics is None or isinstance(return_metrics, list))
            else [return_metrics]
        )
        builder = self._base(return_metrics, filters, limit, total_count)
        if group_by is not None:
            builder = builder.with_group_by_filter([group_by])
            builder = builder.with_fields(" groupedBy { path value } ")
        builder = self._add_near_vector(builder, near_vector, certainty, distance, object_limit)
        res = self._do(builder)
        return (
            self._to_aggregate_result(res, return_metrics)
            if group_by is None
            else self._to_group_by_result(res, return_metrics)
        )


class _NearVectorGroupBy(_Aggregate):
    def near_vector(
        self,
        near_vector: List[float],
        group_by: str,
        certainty: Optional[Union[float, int]] = None,
        distance: Optional[Union[float, int]] = None,
        object_limit: Optional[int] = None,
        filters: Optional[_Filters] = None,
        limit: Optional[int] = None,
        total_count: bool = True,
        return_metrics: Optional[PropertiesMetrics] = None,
    ) -> List[_AggregateGroup]:
        """Aggregate metrics over the objects returned by a near vector search on this collection and grouping the results grouping the results by a property.

        At least one of `certainty`, `distance`, or `object_limit` must be specified here for the vector search.

        This method requires that the objects in the collection have associated vectors.

        Arguments:
            `near_vector`
                The vector to search on.
            `group_by`
                The property name to group the aggregation by.
            `certainty`
                The minimum certainty of the vector search.
            `distance`
                The maximum distance of the vector search.
            `object_limit`
                The maximum number of objects to return from the vector search prior to the aggregation.
            `filters`
                The filters to apply to the search.
            `limit`
                The maximum number of aggregated objects to return.
            `total_count`
                Whether to include the total number of objects that match the query in the response.
            `return_metrics`
                A list of property metrics to aggregate together after the text search.

        Returns:
            A list of `_AggregateGroup` object that includes the aggregation objects.

        Raises:
            `weaviate.exceptions.WeaviateGQLQueryError`:
                If an error occurs while performing the query against Weaviate.
        """
        _Warnings.old_query_group_by_namespace("aggregate.near_text", "aggregate_group_by")
        return_metrics = (
            return_metrics
            if (return_metrics is None or isinstance(return_metrics, list))
            else [return_metrics]
        )
        builder = (
            self._base(return_metrics, filters, limit, total_count)
            .with_group_by_filter([group_by])
            .with_fields(" groupedBy { path value } ")
        )
        builder = self._add_near_vector(builder, near_vector, certainty, distance, object_limit)
        res = self._do(builder)
        return self._to_group_by_result(res, return_metrics).groups
