from typing import Dict, Any, List, Literal, Optional, Type, Tuple, Union, cast, overload

from requests.exceptions import ConnectionError as RequestsConnectionError

from weaviate.collections.classes.config import (
    _CollectionConfigUpdate,
    _InvertedIndexConfigUpdate,
    _ReplicationConfigUpdate,
    _VectorIndexConfigFlatUpdate,
    PropertyType,
    Property,
    ReferenceProperty,
    _ReferencePropertyMultiTarget,
    _VectorIndexConfigHNSWUpdate,
    _CollectionConfig,
    _CollectionConfigSimple,
    _Property,
    _ShardStatus,
    ShardTypes,
)
from weaviate.collections.classes.config_methods import (
    _collection_config_from_json,
    _collection_config_simple_from_json,
)
from weaviate.collections.classes.orm import Model
from weaviate.collections.validator import _raise_invalid_input
from weaviate.connect import ConnectionV4
from weaviate.exceptions import (
    UnexpectedStatusCodeError,
    ObjectAlreadyExistsError,
    WeaviateAddInvalidPropertyError,
)
from weaviate.util import _decode_json_response_dict, _decode_json_response_list


class _ConfigBase:
    def __init__(self, connection: ConnectionV4, name: str, tenant: Optional[str]) -> None:
        self.__connection = connection
        self._name = name
        self.__tenant = tenant

    def __get(self) -> Dict[str, Any]:
        try:
            response = self.__connection.get(path=f"/schema/{self._name}")
        except RequestsConnectionError as conn_err:
            raise RequestsConnectionError(
                "Collection configuration could not be retrieved."
            ) from conn_err
        if response.status_code != 200:
            raise UnexpectedStatusCodeError("Get collection configuration", response)
        return cast(Dict[str, Any], response.json())

    @overload
    def get(self, simple: Literal[False] = ...) -> _CollectionConfig:
        ...

    @overload
    def get(self, simple: Literal[True]) -> _CollectionConfigSimple:
        ...

    @overload
    def get(self, simple: bool = ...) -> Union[_CollectionConfig, _CollectionConfigSimple]:
        ...

    def get(self, simple: bool = False) -> Union[_CollectionConfig, _CollectionConfigSimple]:
        """Get the configuration for this collection from Weaviate.

        Arguments:
            simple : If True, return a simplified version of the configuration containing only name and properties.

        Raises:
            `requests.ConnectionError`
                If the network connection to Weaviate fails.
            `weaviate.UnexpectedStatusCodeError`
                If Weaviate reports a non-OK status.
        """
        if not isinstance(simple, bool):
            _raise_invalid_input("simple", simple, bool)
        schema = self.__get()
        if simple:
            return _collection_config_simple_from_json(schema)
        return _collection_config_from_json(schema)

    def update(
        self,
        *,
        description: Optional[str] = None,
        inverted_index_config: Optional[_InvertedIndexConfigUpdate] = None,
        replication_config: Optional[_ReplicationConfigUpdate] = None,
        vector_index_config: Optional[
            Union[_VectorIndexConfigHNSWUpdate, _VectorIndexConfigFlatUpdate]
        ] = None,
    ) -> None:
        """Update the configuration for this collection in Weaviate.

        Use the `weaviate.classes.Reconfigure` class to generate the necessary configuration objects for this method.

        Arguments:
            description: A description of the collection.
            inverted_index_config: Configuration for the inverted index. Use `Reconfigure.inverted_index` to generate one.
            replication_config: Configuration for the replication. Use `Reconfigure.replication` to generate one.
            vector_index_config: Configuration for the vector index. Use `Reconfigure.vector_index` to generate one.

        Raises:
            `requests.ConnectionError`:
                If the network connection to Weaviate fails.
            `weaviate.UnexpectedStatusCodeError`:
                If Weaviate reports a non-OK status.

        NOTE:
            - If you wish to update a specific option within the configuration and cannot find it in `CollectionConfigUpdate` then it is an immutable option.
            - To change it, you will have to delete the collection and recreate it with the desired options.
            - This is not the case of adding properties, which can be done with `collection.config.add_property()`.
        """
        config = _CollectionConfigUpdate(
            description=description,
            inverted_index_config=inverted_index_config,
            replication_config=replication_config,
            vector_index_config=vector_index_config,
        )
        schema = self.__get()
        schema = config.merge_with_existing(schema)
        try:
            response = self.__connection.put(path=f"/schema/{self._name}", weaviate_object=schema)
        except RequestsConnectionError as conn_err:
            raise RequestsConnectionError(
                "Collection configuration could not be updated."
            ) from conn_err
        if response.status_code != 200:
            raise UnexpectedStatusCodeError("Update collection configuration", response)

    def _add_property(self, additional_property: PropertyType) -> None:
        path = f"/schema/{self._name}/properties"
        obj = additional_property._to_dict()
        try:
            response = self.__connection.post(path=path, weaviate_object=obj)
        except RequestsConnectionError as conn_err:
            raise RequestsConnectionError("Property was not created properly.") from conn_err
        if response.status_code != 200:
            raise UnexpectedStatusCodeError("Add property to collection", response)

    def _get_property_by_name(self, property_name: str) -> Optional[_Property]:
        for prop in self.get().properties:
            if prop.name == property_name:
                return prop
        return None

    def get_shards(self) -> List[_ShardStatus]:
        """Get the statuses of the shards of this collection.

        If the collection is multi-tenancy and you did not call `.with_tenant` then you
        will receive the statuses of all the tenants within the collection. Otherwise, call
        `.with_tenant` on the collection first and you will receive only that single shard.

        Returns:
            `List[_ShardStatus]`:
                A list of objects containing the statuses of the shards.

        Raises:
            `requests.ConnectionError`:
                If the network connection to Weaviate fails.
            `weaviate.UnexpectedStatusCodeError`:
                If Weaviate reports a non-OK status.
        """
        try:
            response = self.__connection.get(
                path=f"/schema/{self._name}/shards{f'?tenant={self.__tenant}' if self.__tenant else ''}"
            )
            shards = _decode_json_response_list(response, "get shards")
            assert shards is not None
            return [
                _ShardStatus(
                    name=shard["name"],
                    status=shard["status"],
                    vector_queue_size=shard["vectorQueueSize"],
                )
                for shard in shards
            ]
        except RequestsConnectionError as conn_err:
            raise RequestsConnectionError("Shard statuses could not be retrieved.") from conn_err

    def update_shards(
        self,
        status: Literal["READY", "READONLY"],
        shard_names: Optional[Union[str, List[str]]] = None,
    ) -> Dict[str, ShardTypes]:
        """Update the status of one or all shards of this collection.

        Returns:
            `Dict[str, ShardTypes]`: All updated shards idexed by their name.

        Parameters
        ----------
            status: The new status of the shard. The available options are: 'READY' and 'READONLY'.
            shard_name: The shard name for which to update the status of the class of the shard. If None all shards are going to be updated.

        Raises:
            `requests.ConnectionError`:
                If the network connection to Weaviate fails.
            `weaviate.UnexpectedStatusCodeError`:
                If Weaviate reports a non-OK status.
        """
        if shard_names is None:
            shards_config = self.get_shards()
            shard_names = [shard_config.name for shard_config in shards_config]
        elif isinstance(shard_names, str):
            shard_names = [shard_names]

        data = {"status": status}

        to_return: Dict[str, ShardTypes] = {}

        for _shard_name in shard_names:
            path = f"/schema/{self._name}/shards/{_shard_name}"
            try:
                response = self.__connection.put(
                    path=path,
                    weaviate_object=data,
                )
            except RequestsConnectionError as conn_err:
                raise RequestsConnectionError(
                    f"Class shards' status could not be updated for shard '{_shard_name}' due to "
                    "connection error."
                ) from conn_err
            resp = _decode_json_response_dict(response, f"Update shard '{_shard_name}' status")
            assert resp is not None
            to_return[_shard_name] = resp["status"]

        return to_return


class _ConfigCollection(_ConfigBase):
    def add_property(self, prop: Property) -> None:
        """Add a property to the collection in Weaviate.

        Arguments:
            prop : The property to add to the collection.

        Raises:
            `requests.ConnectionError`:
                If the network connection to Weaviate fails.
            `weaviate.UnexpectedStatusCodeError`:
                If Weaviate reports a non-OK status.
            `weaviate.ObjectAlreadyExistsError`:
                If the property already exists in the collection.
        """
        if not isinstance(prop, Property):
            _raise_invalid_input(
                "prop",
                prop,
                Property,
            )
        if self._get_property_by_name(prop.name) is not None:
            raise ObjectAlreadyExistsError(
                f"Property with name '{prop.name}' already exists in collection '{self._name}'."
            )
        self._add_property(prop)

    def add_reference(self, ref: Union[ReferenceProperty, _ReferencePropertyMultiTarget]) -> None:
        """Add a reference to the collection in Weaviate.

        Arguments:
            ref : The reference to add to the collection.

        Raises:
            `requests.ConnectionError`:
                If the network connection to Weaviate fails.
            `weaviate.UnexpectedStatusCodeError`:
                If Weaviate reports a non-OK status.
            `weaviate.ObjectAlreadyExistsError`:
                If the reference already exists in the collection.
        """
        if not isinstance(ref, ReferenceProperty) and not isinstance(
            ref, _ReferencePropertyMultiTarget
        ):
            _raise_invalid_input(
                "ref",
                ref,
                Union[ReferenceProperty, _ReferencePropertyMultiTarget],
            )
        if self._get_property_by_name(ref.name) is not None:
            raise ObjectAlreadyExistsError(
                f"Reference with name '{ref.name}' already exists in collection '{self._name}'."
            )
        self._add_property(ref)


class _ConfigCollectionModel(_ConfigBase):
    def __compare_properties_with_model(
        self, schema_props: List[_Property], model_props: List[PropertyType]
    ) -> Tuple[List[_Property], List[PropertyType]]:
        only_in_model: List[PropertyType] = []
        only_in_schema: List[_Property] = list(schema_props)

        schema_props_simple = [
            {
                "name": prop.name,
                "dataType": prop._to_dict().get("dataType"),
            }
            for prop in schema_props
        ]

        for prop in model_props:
            try:
                idx = schema_props_simple.index(
                    {"name": prop.name, "dataType": prop._to_dict().get("dataType")}
                )
                schema_props_simple.pop(idx)
                only_in_schema.pop(idx)
            except ValueError:
                only_in_model.append(prop)
        return only_in_schema, only_in_model

    def update_model(self, model: Type[Model]) -> None:
        only_in_schema, only_in_model = self.__compare_properties_with_model(
            self.get().properties, model.type_to_properties(model)
        )
        if len(only_in_schema) > 0:
            raise TypeError("Schema has extra properties")

        # we can only allow new optional types unless the default is None
        for prop in only_in_model:
            new_field = model.model_fields[prop.name]
            if new_field.annotation is None:
                continue  # if user did not annotate with type then ignore field
            non_optional_type = model.remove_optional_type(new_field.annotation)
            if new_field.default is not None and non_optional_type == new_field.annotation:
                raise WeaviateAddInvalidPropertyError(prop.name)

        for prop in only_in_model:
            self._add_property(prop)

    def is_invalid(self, model: Type[Model]) -> bool:
        only_in_schema, only_in_model = self.__compare_properties_with_model(
            self.get().properties, model.type_to_properties(model)
        )
        return len(only_in_schema) > 0 or len(only_in_model) > 0
