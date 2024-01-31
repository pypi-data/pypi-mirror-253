from typing import Self

from pydantic import BaseModel, model_validator


class Label(BaseModel):
    """Represents a label for a given blockchain address.

    Attributes:
        address (str): The blockchain address.
        label (str): The label for the address. (e.g. "Binance")
        description (str): A description for the label. (e.g. "Binance 14)
    """

    address: str
    label: str
    description: str = ""
    is_address_case_sensitive: bool = False

    @model_validator(mode="after")
    def validate_address(self) -> Self:
        if not self.is_address_case_sensitive:
            self.address = self.address.lower()

        return self
