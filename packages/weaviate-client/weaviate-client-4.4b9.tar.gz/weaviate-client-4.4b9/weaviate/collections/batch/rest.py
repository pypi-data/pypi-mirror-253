from typing import Any, Dict, List, Optional, Union

from requests.exceptions import ConnectionError as RequestsConnectionError

from weaviate.collections.classes.batch import (
    DeleteManyReturn,
    ErrorReference,
    _BatchReference,
    BatchReferenceReturn,
    DeleteManyObject,
)
from weaviate.collections.classes.config import ConsistencyLevel
from weaviate.collections.classes.filters import _Filters
from weaviate.collections.filters import _FilterToREST
from weaviate.connect import ConnectionV4
from weaviate.exceptions import UnexpectedStatusCodeError
from weaviate.util import _decode_json_response_dict


class _BatchREST:
    def __init__(
        self, connection: ConnectionV4, consistency_level: Optional[ConsistencyLevel]
    ) -> None:
        self.__connection = connection
        self.__consistency_level = consistency_level

    def delete(
        self, collection: str, where: _Filters, verbose: bool, dry_run: bool, tenant: Optional[str]
    ) -> Union[DeleteManyReturn[List[DeleteManyObject]], DeleteManyReturn[None]]:
        payload: Dict[str, Any] = {
            "match": {
                "class": collection,
                "where": _FilterToREST.convert(where),
            }
        }
        if verbose:
            payload["output"] = "verbose"
        if dry_run:
            payload["dryRun"] = True

        params = {}
        if self.__consistency_level is not None:
            params["consistency"] = self.__consistency_level.value
        if tenant is not None:
            params["tenant"] = tenant

        try:
            response = self.__connection.delete(
                path="/batch/objects",
                weaviate_object=payload,
                params=params,
            )
        except RequestsConnectionError as conn_err:
            raise RequestsConnectionError("Batch delete was not successful.") from conn_err
        res = _decode_json_response_dict(response, "Delete in batch")
        assert res is not None
        if verbose:
            return DeleteManyReturn(
                failed=res["results"]["failed"],
                matches=res["results"]["matches"],
                objects=res["results"]["objects"],
                successful=res["results"]["successful"],
            )
        else:
            return DeleteManyReturn(
                failed=res["results"]["failed"],
                matches=res["results"]["matches"],
                successful=res["results"]["successful"],
                objects=None,
            )

    def references(self, references: List[_BatchReference]) -> BatchReferenceReturn:
        params: Dict[str, str] = {}
        if self.__consistency_level is not None:
            params["consistency_level"] = self.__consistency_level

        refs = [
            {"from": ref.from_, "to": ref.to}
            if ref.tenant is None
            else {"from": ref.from_, "to": ref.to, "tenant": ref.tenant}
            for ref in references
        ]

        response = self.__connection.post(
            path="/batch/references", weaviate_object=refs, params=params
        )
        if response.status_code == 200:
            payload = response.json()
            errors = {
                idx: ErrorReference(
                    message=entry["result"]["errors"]["error"][0]["message"],
                    reference=references[idx],
                )
                for idx, entry in enumerate(payload)
                if entry["result"]["status"] == "FAILED"
            }
            return BatchReferenceReturn(
                elapsed_seconds=response.elapsed.total_seconds(),
                errors=errors,
                has_errors=len(errors) > 0,
            )
        raise UnexpectedStatusCodeError("Send ref batch", response)


class _BatchRESTAsync:
    def __init__(
        self, connection: ConnectionV4, consistency_level: Optional[ConsistencyLevel]
    ) -> None:
        self.__consistency_level = consistency_level
        self.__connection = connection

    async def references(self, references: List[_BatchReference]) -> BatchReferenceReturn:
        params: Dict[str, str] = {}
        if self.__consistency_level is not None:
            params["consistency_level"] = self.__consistency_level

        refs = [
            {"from": ref.from_, "to": ref.to}
            if ref.tenant is None
            else {"from": ref.from_, "to": ref.to, "tenant": ref.tenant}
            for ref in references
        ]

        response = await self.__connection.apost(
            path="/batch/references", weaviate_object=refs, params=params
        )
        if response.status_code == 200:
            payload = response.json()
            errors = {
                idx: ErrorReference(
                    message=entry["result"]["errors"]["error"][0]["message"],
                    reference=references[idx],
                )
                for idx, entry in enumerate(payload)
                if entry["result"]["status"] == "FAILED"
            }
            return BatchReferenceReturn(
                elapsed_seconds=response.elapsed.total_seconds(),
                errors=errors,
                has_errors=len(errors) > 0,
            )
        raise UnexpectedStatusCodeError("Send ref batch", response)
