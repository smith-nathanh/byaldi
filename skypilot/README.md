# SkyPilot Configuration for Byaldi

This directory contains SkyPilot configuration files to run Byaldi on cloud GPU instances.

## Prerequisites

1. Install SkyPilot: `pip install skypilot[gcp]` (or `[aws]` for AWS)
2. Configure your cloud credentials:
   - For GCP: `gcloud auth application-default login`
   - For AWS: Configure AWS CLI credentials

## Usage

### Launch Instance

**For production/heavy workloads (H100):**
```bash
sky launch skypilot/H100/config_accel_1gpu.yaml
```

**For development/testing (T4 - cheaper):**
```bash
sky launch skypilot/dev_config.yaml
```

Both configurations will:
- Install Byaldi and all dependencies
- Set up a Python virtual environment
- Start a Jupyter notebook server on port 8888

### Access Jupyter

After the instance is launched, you can access Jupyter at:
```
http://<instance-ip>:8888
```

The Jupyter server is configured without authentication for development purposes.

### Test Installation

A test script is provided to verify the installation:

```bash
sky exec <cluster-name> 'python ~/sky_workdir/skypilot/test_byaldi.py'
```

### SSH Access

You can SSH into the instance:

```bash
sky ssh <cluster-name>
```

The Python virtual environment is automatically activated in your shell.

### Stop/Terminate

- Stop the instance: `sky stop <cluster-name>`
- Terminate the instance: `sky down <cluster-name>`

## Configuration Details

### H100 Configuration (`H100/config_accel_1gpu.yaml`)
- **GPU**: H100 (1x)
- **Memory**: 32GB+
- **Disk**: 256GB
- **Spot instances**: Enabled

### Development Configuration (`dev_config.yaml`)
- **GPU**: T4 (1x) - More cost-effective for development
- **Memory**: 16GB+
- **Disk**: 128GB
- **Spot instances**: Enabled

### Common Features
Both configurations include:
- Byaldi package (with dev dependencies)
- Jupyter notebook with common ML packages
- All dependencies from `pyproject.toml`
- Automatic Python virtual environment setup

### Regions
Configured to use multiple GCP regions for availability:
- us-east4
- us-central1
- us-east5
- us-west1
- us-west4

## Customization

You can modify the configuration file to:
- Change GPU type or count
- Add additional dependencies
- Mount cloud storage buckets
- Configure different regions
- Add environment variables

See the [SkyPilot documentation](https://skypilot.readthedocs.io/) for more details.
