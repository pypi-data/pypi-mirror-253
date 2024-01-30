from typing import Any, ClassVar, Mapping, Optional, TYPE_CHECKING

import attr

from inter_rao_energosbyt.actions.sql import ACTION_SQL
from inter_rao_energosbyt.actions.sql.prepay_params import PrepayParamsBase
from inter_rao_energosbyt.actions.sql.subscription import GetPdSubscrStatusBase

if TYPE_CHECKING:
    from inter_rao_energosbyt.interfaces import BaseEnergosbytAPI


@attr.s(kw_only=True, frozen=True, slots=True)
class GetKsgPdSubscrStatus(GetPdSubscrStatusBase):
    returns_single: ClassVar[bool] = False

    @classmethod
    async def async_request(
        cls,
        api: "BaseEnergosbytAPI",
        data: Optional[Mapping[str, Any]] = None,
        query: str = "GetKsgPdSubscrStatus",
    ):
        """Query request: GetKsgPdSubscrStatus

        :param api: API object to perform request with
        :param data: Additional request data
        :param query: Query name (default: query name associated with query class)
        """
        data = {} if data is None else dict(data)

        return await api.async_action_map(cls, ACTION_SQL, query, data)


@attr.s(kw_only=True, frozen=True, slots=True)
class KsgPrepayParams(PrepayParamsBase):
    returns_single: ClassVar[bool] = True

    @classmethod
    async def async_request(
        cls,
        api: "BaseEnergosbytAPI",
        data: Optional[Mapping[str, Any]] = None,
        query: str = "KsgPrepayParams",
    ):
        """Query request: KsgPrepayParams

        :param api: API object to perform request with
        :param data: Additional request data
        :param query: Query name (default: query name associated with query class)
        """
        data = {} if data is None else dict(data)

        return await api.async_action_map(cls, ACTION_SQL, query, data)
