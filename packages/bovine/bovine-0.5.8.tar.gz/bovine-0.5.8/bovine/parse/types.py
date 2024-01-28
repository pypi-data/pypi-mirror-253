# SPDX-FileCopyrightText: 2024 helge
#
# SPDX-License-Identifier: MIT

from dataclasses import dataclass, field
from typing import Set
from bovine.crypto.types import CryptographicIdentifier


@dataclass
class ReferencableCryptographicIdentifier(CryptographicIdentifier):
    id: str | None = None
    verification_relationships: Set[str] = field(default_factory=set)

    @classmethod
    def from_public_key(clz, data: dict):
        """Creates a ReferencableCryptographicIdentifier from a publicKey object, example:

        ```json
        {
            "id": "https://com.example/issuer/123#main-key",
            "owner": "https://com.example/issuer/123",
            "publicKeyPem": "-----BEGIN PUBLIC KEY-----\\n...\\n-----END PUBLIC KEY-----"
        }
        ```
        """
        result = super().from_public_key(data)
        result.id = data.get("id")
        return result

    @classmethod
    def from_multikey(clz, multikey: dict):
        result = super().from_multikey(multikey)
        result.id = multikey.get("id")
        return result

    def with_verification_relationships(self, **kwargs):
        for relation_ship_name, ids in kwargs.items():
            if self.id in ids:
                self.verification_relationships.add(relation_ship_name)
        return self
