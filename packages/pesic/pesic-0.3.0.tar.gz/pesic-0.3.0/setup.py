import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="pesic",
    version="0.3.0",
    author="Stanislav Bolshakov",
    author_email="st.bolshakov@gmail.com",
    url="https://github.com/StanislavBolshakov/pesic",
    description="PetroElectroSbyt API Wrapper",
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
    install_requires=["aiohttp", "asyncio"]
)
