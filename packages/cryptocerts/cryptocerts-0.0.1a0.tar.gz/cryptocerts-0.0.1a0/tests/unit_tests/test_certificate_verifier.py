from __future__ import annotations
import pytest
from cryptocerts.certificates import (
    TrustedCertificateStore,
    CertificateToken,
    CertificateVerifier,
    IntermediaryCertificateStore,
)
from cryptocerts.exceptions import InvalidChain, CertificateAlreadyStored

from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives import serialization
from ..utils import load_from_file


def test_certificate_verifier_initialize_empty():
    """
    Tests that a certificate verifier can be initialized with no arguments.
    """
    certificate_verifier = CertificateVerifier()

    assert isinstance(certificate_verifier, CertificateVerifier)


def test_certificate_verifier_initialize_with_trusted_store(
    root_certificate_token: CertificateToken,
):
    """
    Tests that a certificate verifier can be initialized with a trusted store.
    """
    trusted_store = TrustedCertificateStore()
    trusted_store.add_certificate(root_certificate_token)

    certificate_verifier = CertificateVerifier(trusted_store=trusted_store)

    assert len(certificate_verifier._trusted_store.certificates) == 1


def test_certificate_verifier_initialize_with_intermediary_store_valid(
    root_certificate_token: CertificateToken,
    intermediate_certificate_token: CertificateToken,
):
    """
    Tests that a certificate verifier can be initialized with an intermediary store that can be built to a trusted certificate.
    """
    trusted_store = TrustedCertificateStore()
    trusted_store.add_certificate(root_certificate_token)

    intermediary_store = IntermediaryCertificateStore()
    intermediary_store.add_certificate(intermediate_certificate_token)

    certificate_verifier = CertificateVerifier(
        trusted_store=trusted_store, intermediary_store=intermediary_store
    )

    assert len(certificate_verifier._intermediary_store.certificates) == 1


def test_certificate_verifier_initialize_with_intermediary_store_invalid_chain(
    intermediate_certificate_token: CertificateToken,
):
    """
    Tests that a certificate verifier throws an InvalidChain exception when the intermediary store can't be built to a trusted certificate.
    """

    def raises_invalid_chain():
        intermediary_store = IntermediaryCertificateStore()
        intermediary_store.add_certificate(intermediate_certificate_token)

        # This should raise an InvalidChain exception
        certificate_verifier = CertificateVerifier(
            intermediary_store=intermediary_store
        )

    pytest.raises(InvalidChain, raises_invalid_chain)


def test_certificate_verifier_initialize_with_same_certificates_in_trusted_and_intermediary_store(
    root_certificate_token: CertificateToken,
):
    """
    Tests that a certificate verifier throws an CertificateAlreadyStored exception when the intermediary store contains the same certificate as the trusted store.
    """

    def raises_certificate_already_stored():
        trusted_store = TrustedCertificateStore()
        trusted_store.add_certificate(root_certificate_token)

        intermediary_store = IntermediaryCertificateStore()
        intermediary_store.add_certificate(root_certificate_token)

        # This should raise an CertificateAlreadyStored exception
        certificate_verifier = CertificateVerifier(
            trusted_store=trusted_store, intermediary_store=intermediary_store
        )

    pytest.raises(CertificateAlreadyStored, raises_certificate_already_stored)


def test_certificate_verifier_verify_leaf_certificate(
    certificate_verifier: CertificateVerifier, leaf_certificate_token: CertificateToken
):
    """
    Tests that a certificate verifier can verify a leaf certificate.
    """
    result = certificate_verifier.verify_certificate(leaf_certificate_token)

    assert result.valid_to_trusted_root is True
    assert result.is_expired is False
    assert result.not_yet_valid is False
    assert result.signature_intact is True


def test_certificate_verifier_verify_intermediate_certificate(
    certificate_verifier: CertificateVerifier,
    intermediate_certificate_token: CertificateToken,
):
    """
    Tests that a certificate verifier can verify an intermediate certificate.
    """
    result = certificate_verifier.verify_certificate(intermediate_certificate_token)

    assert result.valid_to_trusted_root is True
    assert result.is_expired is False
    assert result.not_yet_valid is False
    assert result.signature_intact is True


def test_certificate_verifier_verify_root_certificate(
    certificate_verifier: CertificateVerifier, root_certificate_token: CertificateToken
):
    """
    Tests that a certificate verifier can verify a root certificate.
    """
    result = certificate_verifier.verify_certificate(root_certificate_token)

    assert result.valid_to_trusted_root is True
    assert result.is_expired is False
    assert result.not_yet_valid is False
    assert result.signature_intact is True


def test_certificate_verifier_pkcs7_verify_leaf_certificate(
    certificate_verifier: CertificateVerifier,
):
    """
    Tests that a certificate verifier can verify a leaf certificate using PKCS7.
    """
    certificate = CertificateToken(
        load_from_file("cloudflare/developers.cloudflare_pkcs7.p7b")
    )
    result = certificate_verifier.verify_certificate(certificate)

    assert result.valid_to_trusted_root is False
    assert result.is_expired is False
    assert result.not_yet_valid is False
    assert result.signature_intact is True
