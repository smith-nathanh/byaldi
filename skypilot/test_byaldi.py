#!/usr/bin/env python3
"""
Test script to verify Byaldi installation and functionality on SkyPilot.
This script demonstrates basic usage of Byaldi's RAGMultiModalModel.
"""

import sys


def test_imports():
    """Test that all required packages can be imported."""
    print("Testing imports...")
    
    try:
        import torch
        print(f"✓ PyTorch {torch.__version__}")
        print(f"✓ CUDA available: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"✓ GPU: {torch.cuda.get_device_name(0)}")
            print(f"✓ CUDA version: {torch.version.cuda}")
    except ImportError as e:
        print(f"✗ PyTorch import failed: {e}")
        return False
    
    try:
        import byaldi
        print(f"✓ Byaldi {byaldi.__version__}")
    except ImportError as e:
        print(f"✗ Byaldi import failed: {e}")
        return False
    
    try:
        from byaldi import RAGMultiModalModel  # noqa: F401
        print("✓ RAGMultiModalModel imported")
    except ImportError as e:
        print(f"✗ RAGMultiModalModel import failed: {e}")
        return False
    
    return True

def test_model_loading():
    """Test loading a model."""
    print("\nTesting model loading...")
    
    try:
        from byaldi import RAGMultiModalModel
        
        # Try to load a model (this will download if not cached)
        print("Attempting to load ColPali model...")
        model = RAGMultiModalModel.from_pretrained("vidore/colpali")
        print("✓ Model loaded successfully")
        
        # Test basic functionality
        print("Testing model functionality...")
        # You would typically index documents and then search, but for this test
        # we'll just verify the model object exists and has expected methods
        assert hasattr(model, 'index'), "Model should have index method"
        assert hasattr(model, 'search'), "Model should have search method"
        print("✓ Model has expected methods")
        
        return True
        
    except Exception as e:
        print(f"✗ Model loading failed: {e}")
        return False

def main():
    """Main test function."""
    print("=== Byaldi Installation Test ===\n")
    
    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed")
        sys.exit(1)
    
    # Test model loading (optional - comment out if you don't want to download models)
    try:
        if not test_model_loading():
            print("\n⚠️  Model loading failed, but basic imports work")
            print("   This might be due to network issues or insufficient disk space")
        else:
            print("\n✅ All tests passed!")
    except KeyboardInterrupt:
        print("\n⚠️  Model loading interrupted by user")
    except Exception as e:
        print(f"\n⚠️  Model loading test encountered an error: {e}")
    
    print("\n=== Test completed ===")

if __name__ == "__main__":
    main()
