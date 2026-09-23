from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec


def generate_key_pair():
    private_key = ec.generate_private_key(ec.SECP256K1())
    public_key = private_key.public_key()
    return private_key, public_key


def key_to_hex(private_key, public_key):
    private_value = private_key.private_numbers().private_value
    private_bytes = private_value.to_bytes(32, byteorder="big")

    public_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.UncompressedPoint,
    )

    return private_bytes, public_bytes


def compress_public_key(public_key):
    return public_key.public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.CompressedPoint,
    )


def decompress_public_key(compressed_public_key):
    return ec.EllipticCurvePublicKey.from_encoded_point(
        ec.SECP256K1(), compressed_public_key
    )


def save_hex_keys(private_bytes, public_bytes):

    base_directory = Path(__file__).resolve().parent
    keys_directory = base_directory / "keys"
    keys_directory.mkdir(exist_ok=True)

    private_key_path = keys_directory / "private_key.hex"
    public_key_path = keys_directory / "public_key.hex"

    private_key_path.write_text(private_bytes.hex(), encoding="utf-8")
    public_key_path.write_text(public_bytes.hex(), encoding="utf-8")

    return private_key_path, public_key_path


def main():
    private_key, public_key = generate_key_pair()
    private_bytes, public_bytes = key_to_hex(private_key, public_key)
    compressed_public_key = compress_public_key(public_key)

    private_hex = private_bytes.hex()
    public_hex = public_bytes.hex()
    compressed_hex = compressed_public_key.hex()

    reduction = (
        (len(public_bytes) - len(compressed_public_key)) / len(public_bytes)
    ) * 100

    print("ECDSA KEY GENERATION USING SECP256K1")
    print("=" * 72)
    print(f"Private key (hex): {private_hex}")
    print(f"Private key size: {len(private_bytes)} bytes")
    print(f"Private key length: {len(private_hex)} hexadecimal characters")

    print(f"\nOriginal public key (hex): {public_hex}")
    print(f"Original public key size: {len(public_bytes)} bytes")
    print(f"Original public key length: {len(public_hex)} hexadecimal characters")

    print(f"\nCompressed public key (hex): {compressed_hex}")
    print(f"Compressed public key size: {len(compressed_public_key)} bytes")
    print(
        "Compressed public key length: "
        f"{len(compressed_hex)} hexadecimal characters"
    )
    print(f"Storage reduction: {reduction:.2f}%")

    private_key_path, public_key_path = save_hex_keys(
        private_bytes,
        public_bytes,
    )

    print(f"\nPrivate key saved to: {private_key_path}")
    print(f"Public key saved to: {public_key_path}")

    message = b"COMP726 ECDSA signature verification test"
    signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

    reconstructed_public_key = decompress_public_key(compressed_public_key)
    reconstructed_bytes = reconstructed_public_key.public_bytes(
        encoding=serialization.Encoding.X962,
        format=serialization.PublicFormat.UncompressedPoint,
    )

    keys_match = reconstructed_bytes == public_bytes
    print(f"Decompressed key matches original key: {keys_match}")

    try:
        reconstructed_public_key.verify(
            signature, message, ec.ECDSA(hashes.SHA256())
        )
        print("Signature verification: SUCCESS")
    except InvalidSignature:
        print("Signature verification: FAILED")


if __name__ == "__main__":
    main()
