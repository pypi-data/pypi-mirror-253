
**ConfigMate** streamlines heavyweight config parsing into a sleek, zero-boilerplate experience that lets you configure with confidence.

Key Features
---------------
- *Extensible file format support*: - Automatic detection & parsing of all standard config file formats.
- *Environment variable interpolation*: - Parse environment variables while keeping defaults in your configuration file.
- *Override files*: Segregate base configuration management and DEV/STAG/PROD overrides in separate files.
- *CLI support*: Override configuration values with files or values dirctly from an automatically generated command line interface.
- *Type validation*: - Custom validation support, and seamless extension for Pydantic's fantastic validation capabilities.

Get Started with ConfigMate
-------------------------------

ConfigMate simplifies your configuration management. Get started with these easy steps:

**Installation**

Install ConfigMate with all standard features:

.. code-block:: bash

    pip install "configmate[standard]"

Alternatively, install with specific features (e.g., Pydantic):

.. code-block:: bash

    pip install "configmate[pydantic]"

**Set Up Configuration**

1. **Create a Configuration File:**

   Define your database configuration in `config.yaml`:

   .. code-block:: yaml

        # config.yaml
        Database configuration:
            host: localhost
            port: ${DB_PORT:8000}

2. **Integrate with Your Script:**

   Use ConfigMate to load and validate configuration in your script:

   .. code-block:: python

        # example.py
        import configmate
        import dataclasses

        @dataclasses.dataclass
        class DatabaseConfig:
            host: str
            port: int

        config = configmate.get_config(
            "config.yaml", 
            section='Database configuration', 
            validation=DatabaseConfig
        )
        print(config)

**Run Your Script with Different Configurations**

Execute your script, and override configurations using environment variables or command-line arguments:

.. code-block:: bash

    # Default configuration
    python example.py 
    >> DatabaseConfig(host='localhost', port=8000)

    # Override port using an environment variable
    DB_PORT=9000 python example.py
    >> DatabaseConfig(host='localhost', port=9000)

    # Override host using a command-line argument
    python example.py ++host foreignhost
    >> DatabaseConfig(host='foreignhost', port=8000)


.. Quick comparison
.. ----------------

.. .. role:: centered
..    :class: centered

.. .. role:: centered
..    :class: centered

.. .. list-table::
..    :widths: 25 10 10 10 10 10 10 10 10
..    :header-rows: 1

..    * - Feature / package
..      - configmate
..      - configparser
..      - fileparsers (toml/yaml...)
..      - argparse
..      - pallets/click
..      - google/fire
..      - omegaconf
..      - hydra
..    * - No Boilerplate
..      - :centered:`✅`
..      - :centered:`❌`
..      - :centered:`✅`
..      - :centered:`❌`
..      - :centered:`❌`
..      - :centered:`✅`
..      - :centered:`❌`
..      - :centered:`✅`
..    * - Support for Multiple File Formats
..      - :centered:`✅`
..      - :centered:`❌`
..      - :centered:`✅`
..      - :centered:`❌`
..      - :centered:`❌`
..      - :centered:`❌`
..      - :centered:`❌`
..      - :centered:`❌`
..    * - Hierarchical Configuration
..      - :centered:`✅`
..      - :centered:`✅`
..      - :centered:`✅`
..      - :centered:`❌`
..      - :centered:`❌`
..      - :centered:`✅`
..      - :centered:`✅`
..      - :centered:`✅`
..    * - Command-line Interface (CLI) Support
..      - :centered:`✅`
..      - :centered:`❌`
..      - :centered:`❌`
..      - :centered:`✅`
..      - :centered:`✅`
..      - :centered:`✅`
..      - :centered:`❌`
..      - :centered:`✅`
..    * - Type Validation
..      - :centered:`✅`
..      - :centered:`❌`
..      - :centered:`Partial`
..      - :centered:`❌`
..      - :centered:`✅`
..      - :centered:`❌`
..      - :centered:`Partial`
..      - :centered:`Partial`
..    * - Environment Variable Interpolation
..      - :centered:`✅`
..      - :centered:`✅`
..      - :centered:`❌`
..      - :centered:`❌`
..      - :centered:`❌`
..      - :centered:`❌`
..      - :centered:`✅`
..      - :centered:`✅`
..    * - Dependency Count
..      - :centered:`Low`
..      - :centered:`Low`
..      - :centered:`Low`
..      - :centered:`Low`
..      - :centered:`Low`
..      - :centered:`Low`
..      - :centered:`Low`
..      - :centered:`Moderate`
 
