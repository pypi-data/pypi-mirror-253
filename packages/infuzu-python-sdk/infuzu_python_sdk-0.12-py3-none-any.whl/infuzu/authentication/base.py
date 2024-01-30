import base64
import json
import time
import uuid
from abc import (ABC, abstractmethod)
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import (serialization, hashes)
from cryptography.hazmat.primitives.asymmetric import ec


Curve: type[ec.EllipticCurve] = ec.SECP521R1


class InfuzuKey(ABC):
    def __init__(self, key: ec.EllipticCurvePublicKey | ec.EllipticCurvePrivateKey, key_pair_id: str) -> None:
        if not isinstance(key, self._key_type()):
            raise TypeError(f"key must be of type {self._key_type().__name__}")
        self._key: ec.EllipticCurvePublicKey | ec.EllipticCurvePrivateKey = key
        self._key_pair_id: str = key_pair_id

    @classmethod
    @abstractmethod
    def _key_type(cls) -> type[ec.EllipticCurvePrivateKey | ec.EllipticCurvePublicKey]:
        pass

    @abstractmethod
    def to_base64(self) -> str:
        pass

    @classmethod
    @abstractmethod
    def from_base64(cls, public_key_b64: str, key_pair_id: str) -> 'InfuzuPublicKey':
        pass

    def __eq__(self, other: any) -> bool:
        if isinstance(other, InfuzuKey):
            return self.to_base64() == other.to_base64()
        else:
            return False

    def __str__(self) -> str:
        return self.to_base64()


class InfuzuPublicKey(InfuzuKey):
    _CURVE: type[ec.EllipticCurve] = Curve

    @classmethod
    def _key_type(cls) -> type[ec.EllipticCurvePublicKey]:
        return ec.EllipticCurvePublicKey

    def to_base64(self) -> str:
        public_bytes: bytes = self._key.public_bytes(
            encoding=serialization.Encoding.X962, format=serialization.PublicFormat.CompressedPoint
        )
        return base64.urlsafe_b64encode(public_bytes).decode('utf-8')

    @classmethod
    def from_base64(cls, public_key_b64: str, key_pair_id: str) -> 'InfuzuPublicKey':
        public_key_bytes: bytes = base64.urlsafe_b64decode(public_key_b64)
        return cls(
            key=ec.EllipticCurvePublicKey.from_encoded_point(cls._CURVE(), public_key_bytes), key_pair_id=key_pair_id
        )

    def verify_signature(self, message: str, signature: str, allowed_time_difference: int = 300) -> bool:
        try:
            signature_data: dict[str, any] = json.loads(base64.urlsafe_b64decode(signature))
            sig_timestamp: int = signature_data["timestamp"]
            sig_signature: bytes = base64.urlsafe_b64decode(signature_data["signature"])
            sig_id: str = signature_data["id"]

            if sig_id != self._key_pair_id:
                return False

            if int(time.time()) - sig_timestamp > allowed_time_difference:
                return False

            message_with_metadata: dict[str, any] = {"message": message, "timestamp": sig_timestamp, "id": sig_id}
            message_str: str = json.dumps(message_with_metadata)
            message_bytes: bytes = message_str.encode('utf-8')

            self._key.verify(sig_signature, message_bytes, ec.ECDSA(hashes.SHA256()))
            return True
        except (InvalidSignature, json.JSONDecodeError, KeyError):
            return False


class InfuzuPrivateKey(InfuzuKey):
    _CURVE: type[ec.EllipticCurve] = Curve

    @classmethod
    def _key_type(cls) -> type[ec.EllipticCurvePrivateKey]:
        return ec.EllipticCurvePrivateKey

    @classmethod
    def generate(cls, key_pair_id: str) -> 'InfuzuPrivateKey':
        return cls(key=ec.generate_private_key(cls._CURVE(), default_backend()), key_pair_id=key_pair_id)

    def to_base64(self) -> str:
        private_num: int = self._key.private_numbers().private_value
        private_key_bytes: bytes = private_num.to_bytes((private_num.bit_length() + 7) // 8, 'big')
        return base64.urlsafe_b64encode(private_key_bytes).decode('utf-8')

    @classmethod
    def from_base64(cls, private_key_b64: str, key_pair_id: str) -> 'InfuzuPrivateKey':
        private_key_bytes: bytes = base64.urlsafe_b64decode(private_key_b64)
        private_numbers: int = int.from_bytes(private_key_bytes, 'big')
        return cls(
            key=ec.derive_private_key(private_numbers, curve=cls._CURVE(), backend=default_backend()),
            key_pair_id=key_pair_id
        )

    @property
    def public_key(self) -> InfuzuPublicKey:
        return InfuzuPublicKey(key=self._key.public_key(), key_pair_id=self._key_pair_id)

    def sign_message(self, message: str) -> str:
        timestamp: int = int(time.time())
        message_with_metadata: dict[str, any] = {"message": message, "timestamp": timestamp, "id": self._key_pair_id}
        message_str: str = json.dumps(message_with_metadata)
        message_bytes: bytes = message_str.encode('utf-8')
        signature_bytes: bytes = self._key.sign(message_bytes, ec.ECDSA(hashes.SHA256()))
        base_signature_str: str = base64.urlsafe_b64encode(signature_bytes).decode('utf-8')
        full_signature_dict: dict[str, any] = {
            "signature": base_signature_str, "id": self._key_pair_id, "timestamp": timestamp
        }
        print(full_signature_dict)
        full_signature_str: str = json.dumps(full_signature_dict)
        return base64.urlsafe_b64encode(full_signature_str.encode('utf-8')).decode('utf-8')


class InfuzuKeys:
    def __init__(self, private_key: InfuzuPrivateKey, pair_id: str) -> None:
        self.private_key: InfuzuPrivateKey = private_key
        self.public_key: InfuzuPublicKey = private_key.public_key
        self.id = pair_id

    @classmethod
    def generate(cls) -> 'InfuzuKeys':
        pair_id: str = str(uuid.uuid4()).replace("-",  "")
        private_key: InfuzuPrivateKey = InfuzuPrivateKey.generate(key_pair_id=pair_id)
        return cls(private_key=private_key, pair_id=pair_id)

    def __str__(self) -> str:
        return f"Key Pair ID: {self.id}\nPrivate Key: {self.private_key}\nPublic Key: {self.public_key}"

    @property
    def private_key_str(self) -> str:
        return self.private_key.to_base64()

    @property
    def public_key_str(self) -> str:
        return self.public_key.to_base64()
