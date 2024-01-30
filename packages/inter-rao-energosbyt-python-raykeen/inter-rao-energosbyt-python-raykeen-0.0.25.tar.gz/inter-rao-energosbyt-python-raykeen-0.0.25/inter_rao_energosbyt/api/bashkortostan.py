__all__ = (
    "API",
    "TIMEZONE",
    "BashkortostanEnergosbytAPI",
    "UFAEletricityAccount",
    "UFAElectricityMeter",
)

import logging
from datetime import tzinfo
from typing import ClassVar

import pytz

from inter_rao_energosbyt.actions.sql.byt import Meters
from inter_rao_energosbyt.interfaces import BaseEnergosbytAPI
from inter_rao_energosbyt.presets.byt import (
    AbstractBytSubmittableMeter,
    AccountWithBytInfoFromSingle,
    AccountWithStaticBytProxy,
    BytAccountBase,
)
from inter_rao_energosbyt.enums import ProviderType, ServiceType


#################################################################################
# Программный интерфейс
#################################################################################


class BashkortostanEnergosbytAPI(BaseEnergosbytAPI):
    __slots__ = ()

    LOGGER = logging.getLogger(__name__)

    BASE_URL: ClassVar[str] = "https://lkk.bashesk.ru"
    AUTH_URL: ClassVar[str] = BASE_URL + "/auth"
    REQUEST_URL: ClassVar[str] = BASE_URL + "/gate_lkcomu_ufa"
    ACCOUNT_URL: ClassVar[str] = BASE_URL + "/accounts"
    APP_VERSION: ClassVar[str] = "1.29.0"


API = BashkortostanEnergosbytAPI
TIMEZONE = pytz.timezone("Asia/Yekaterinburg")


#################################################################################
# Энергосбытовая компания Респ. Башкортостан (ЭСКБ) (электричество)
#################################################################################


class UFAElectricityMeter(AbstractBytSubmittableMeter):
    __slots__ = ()

    @property
    def byt_plugin_submit_indications(self) -> str:
        return "propagateUfaInd"


@BashkortostanEnergosbytAPI.register_supported_account(
    provider_type=ProviderType.UFA,
    service_type=ServiceType.ELECTRICITY,
)
class UFAEletricityAccount(
    AccountWithStaticBytProxy,
    AccountWithBytInfoFromSingle,
    BytAccountBase,
):
    __slots__ = ()

    timezone: "tzinfo" = TIMEZONE

    def _create_meter_from_byt_data(self, meter_data: "Meters") -> UFAElectricityMeter:
        return UFAElectricityMeter.from_response(self, meter_data)

    @property
    def byt_plugin_proxy(self) -> str:
        return "ufaProxy"
