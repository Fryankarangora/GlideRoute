# test_glideroute.py
"""
Tests for GlideRoute module.
"""

import unittest
from glideroute import GlideRoute

class TestGlideRoute(unittest.TestCase):
    """Test cases for GlideRoute class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GlideRoute()
        self.assertIsInstance(instance, GlideRoute)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GlideRoute()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
