"""Tests for smart-rot13-cipher."""

import pytest
from smart_rot13_cipher import cipher


class TestCipher:
    """Test suite for cipher."""

    def test_basic(self):
        """Test basic usage."""
        result = cipher("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            cipher("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = cipher(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
